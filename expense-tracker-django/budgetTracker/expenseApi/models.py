from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id}: {self.name}"

class UserAccounts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    mobile = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.user.username}"
    
class Profile(models.Model):
   user = models.OneToOneField(UserAccounts, on_delete=models.CASCADE, related_name='user_profile')
   email = models.EmailField(max_length=100)
   image = models.ImageField(default='default.jpg', upload_to='user_profile')