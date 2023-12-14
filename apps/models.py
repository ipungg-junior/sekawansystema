from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UsersManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        # Buat user baru dengan menggunakan phone_number sebagai identitas unik
        if not phone_number:
            raise ValueError('The phone number field must be set')
        
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        # Buat superuser dengan menggunakan phone_number sebagai identitas unik
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, password, **extra_fields)

# Create your models here.
class Users(AbstractUser):
    phone_number = models.CharField(null=False, blank=False, unique=True, max_length=14)
    profile_picture = models.ImageField(upload_to='profile_pic/', null=True, blank=True)
    username = models.CharField(max_length=30, unique=True, null=True, blank=True)

    USERNAME_FIELD = 'phone_number'
    objects = UsersManager()

    def __str__(self):
        return self.phone_number
    

class SupportForm(models.Model):
    name = models.CharField(max_length=22)
    email = models.CharField(max_length=60)
    topic = models.CharField(max_length=90)
    phone = models.CharField(max_length=13)
    message = models.TextField()
