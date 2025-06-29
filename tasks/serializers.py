from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the task model with validation."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = [
            'id',
            'owner',
            'title',
            'description',
            'due_date',
            'completed',
            'priority',
            'created_at',
            'updated_at',
        ]

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_due_date(self, value):
        from datetime import date
        if value < date.today():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

    def validate_priority(self, value):
        valid_choices = ['low', 'medium', 'high']
        if value not in valid_choices:
            raise serializers.ValidationError(f"Priority must be one of {valid_choices}.")
        return value
