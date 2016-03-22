from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User,BaseUserManager,AbstractBaseUser
from django.conf import settings

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, city, user_status,password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            city=city,
            user_status=user_status
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email, city, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user_status=1
        user = self.create_user(email,
            password=password,
            city = city,
            user_status=1,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=255,verbose_name='username')
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    USER_STATUS = ((1, 'volunteer'), (2, 'recipant'))
    city = models.CharField(max_length=60)
    user_status = models.PositiveSmallIntegerField(choices=USER_STATUS)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['city']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def get_city(self):
        return self.city

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def ustatus(self):
        return self.user_status

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    message = models.TextField()
    release_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    unpublishing_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_accomplished = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class PostConfirmation(Post):
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='post_added')
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='post_approved')

    def approve(self):
        self.is_accomplished = True
        self.save()

    def __unicode__(self):
        return self.user.name

    def __str__(self):
        return self.user.name

class Material(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    material_name = models.CharField(max_length=120)
    material_message = models.TextField()
    material_image = models.ImageField()
    reserved_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='material_reserved_by')
    ORDER_STATUS = ((0, 'not_rezerved'), (1, 'rezerved'), (2, 'given'))
    status = models.PositiveSmallIntegerField(choices=ORDER_STATUS)

