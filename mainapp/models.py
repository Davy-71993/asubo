from django.db import models

class Solution(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name


