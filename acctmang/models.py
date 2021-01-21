from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserAccountManager(BaseUserManager):
    use_in_migrations = True 

    def _create_user(self, phone_number, email, password, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number can not be empty")

        if not email:
            raise ValueError("email number can not be empty")

        if not password:
            raise ValueError("password number can not be empty")


        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password) 
        user.save(using=self.db)

        return user

    def create_user(self, phone_number=None, email=None, password=None, **extra_fields):
        return self._create_user(phone_number, email, password, **extra_fields)


    def create_superuser(self, phone_number=None, email=None, password=None, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser']=True

        return self._create_user(phone_number, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    REQUIRED_FIELDS = ['email',]
    USERNAME_FIELD = 'phone_number'

    PROVINCES = (
        ('01', 'Greater manchester'),
        ('02',  'Cheshire'),
        ('03', 'Lancashire'),
    )

    phone_number = models.CharField('Phone Number', max_length=20, unique=True)
    email = models.EmailField('Email', unique=True)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=7)
    province = models.CharField(choices=PROVINCES, max_length=2)
    is_staff = models.BooleanField(default=False)
    is_superuser =  models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserAccountManager()

    def __str__(self):
        return str(self.email)