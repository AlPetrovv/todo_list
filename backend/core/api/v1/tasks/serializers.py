from rest_framework import serializers

from apps.tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ('id', 'created_at', 'updated_at')


class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']