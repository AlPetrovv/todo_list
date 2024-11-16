from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey('auth_users.AuthUser', on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f'{self.user.email} - {self.title}'

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-updated_at']
