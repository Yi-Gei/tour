#!encoding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):

    def create_user(self, email, password):
        user = self.model(email=MyUserManager.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Visitor(AbstractBaseUser):
    GENDER = (
        (1, '男'),
        (2, '女'),
    )
    email = models.EmailField(
        max_length=254, unique=True, db_index=True)
    name = models.CharField(max_length=20, blank=False, null=False)
    gender = models.IntegerField(choices=GENDER, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    regdate = models.DateTimeField(auto_now=True)
    headimg = models.URLField(null=True, blank=True)
    desc = models.CharField(max_length=512, null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = MyUserManager()
    def __unicode__(self):
        return self.name

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __unicode__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"  # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
            "Does the user have permissions to view the app ‘app_label‘?"  # Simplest possible answer: Yes, always
            return True

    @property
    def is_staff(self):
        # Simplest possible answer: All admins are staff
        return self.is_admin
