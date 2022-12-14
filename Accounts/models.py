from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    size_used = models.PositiveIntegerField(default=0)

    def computing_size(self, size):
        if self.size_used + size <= 100000000:
            self.size_used += size
            self.save(update_fields=['size_used'])
            return True
        else:
            return False

    # 100 mg
    def __str__(self):
        return f'{self.user.username} >> {self.size_used}'
