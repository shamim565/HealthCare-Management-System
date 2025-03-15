from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class GenderTypes(models.TextChoices):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHERS = 'OTHERS'
    
class Roles(models.IntegerChoices):
    ADMIN = '0', 'Admin'
    DOCTOR = '1', 'Doctor'
    NURSE = '2', 'Nurse'
    PATIENT = '3', 'Patient'
    RECEPTIONIST = '4', 'Receptionist'
    
    
    @classmethod
    def get_role(cls, value):
        for choice in cls.choices:
            if choice[0] == value:
                return choice[1]
            
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email: str, password: str, **kwargs):
        if not email:
            raise ValueError('User must have email')

        email = self.normalize_email(email.lower())
        kwargs.setdefault('username', self.__get_uniq_username())
        user = self.model(email=email, **kwargs)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('role', Roles.ADMIN)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self.create_user(email, password, **kwargs)

    def __get_uniq_username(self):
        username = get_random_string(10)
        if self.model.objects.filter(username=username).exists():
            return self.__get_uniq_username()
        return username
    
            
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    email_confirmed_at = models.DateTimeField(null=True)
    phone_number = models.CharField(max_length=20, unique=True, null=True)
    phone_number_confirmed_at = models.DateTimeField(null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=20, choices=GenderTypes, null=True)
    picture = models.ImageField(upload_to='profile_pictures/', null=True)
    address = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.SmallIntegerField(choices=Roles, default=Roles.PATIENT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    
    @property
    def is_admin(self):
        return self.role == Roles.ADMIN

    @property
    def is_doctor(self):
        return self.role == Roles.DOCTOR

    @property
    def is_nurse(self):
        return self.role == Roles.NURSE

    @property
    def is_patient(self):
        return self.role == Roles.PATIENT

    @property
    def is_receptionist(self):
        return self.role == Roles.RECEPTIONIST

    objects = UserManager()
    
    class Meta:
        ordering = ('-id',)
    

