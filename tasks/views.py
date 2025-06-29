from rest_framework import viewsets, permissions, filters, status, generics, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task
from .serializers import TaskSerializer
from .filters import TaskFilter

from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer to handle user registration."""
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user


class RegisterView(generics.CreateAPIView):
    """API view to register a new user."""
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage authenticated user tasks.
    Includes filtering, ordering, pagination, and marking complete.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = TaskFilter
    ordering_fields = ['due_date', 'created_at']

    def get_queryset(self):
        """Limit tasks to those owned by the current authenticated user."""
        user = self.request.user
        if not user or user.is_anonymous:
            return Task.objects.none()
        return Task.objects.filter(owner=user)

    def perform_create(self, serializer):
        """Attach the logged-in user as the owner when creating a task."""
        serializer.save(owner=self.request.user)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('priority', openapi.IN_QUERY, type=openapi.TYPE_STRING, enum=['low', 'medium', 'high']),
        openapi.Parameter('completed', openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN),
        openapi.Parameter('due_date_after', openapi.IN_QUERY, type=openapi.TYPE_STRING, format='date'),
        openapi.Parameter('due_date_before', openapi.IN_QUERY, type=openapi.TYPE_STRING, format='date'),
        openapi.Parameter('ordering', openapi.IN_QUERY, type=openapi.TYPE_STRING, description='Order by: due_date or created_at'),
        openapi.Parameter('page', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='Page number')
    ])
    def list(self, request, *args, **kwargs):
        """List tasks with filter, search, pagination, and ordering support."""
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['patch'])
    def mark_complete(self, request, pk=None):
        """Custom endpoint to mark a task as completed."""
        task = self.get_object()
        task.completed = True
        task.save()
        return Response({'status': 'Task marked as completed'}, status=status.HTTP_200_OK)