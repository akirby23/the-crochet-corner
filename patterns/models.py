from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

DIFFICULTY_LEVEL_CHOICES = [
    ("B", "Beginner"),
    ("I", "Intermediate"),
    ("A", "Advanced"),
]


class Pattern(models.Model):
    title = models.CharField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    difficulty_level = models.CharField(
        choices=DIFFICULTY_LEVEL_CHOICES, max_length=20)
    yarn_type = models.CharField(max_length=50)
    hook_size = models.CharField(max_length=10)
    gauge = models.CharField(max_length=50)
    instructions = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
