from django.db import models
from .managers import UserManager

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Register your models here.

#  This is the core Django User, but recreated and upgraded to use email instead
# of username
class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True,  null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # Three types of users:
    # 1. superuser (usual Django user)
    # 2. AJ Lakes administrators (is_staff = True)
    # 3. Company Managers, who manage staff who will use the VR App
    #           (company relationship set here)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"{self.email}"
