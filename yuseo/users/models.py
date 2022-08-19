from tkinter import N
from tkinter import TRUE

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

cleanup_data = TRUE

class UserManager(BaseUserManager):
    use_in_migrations: True

    def create_user(self, login_id, password, nickname, **kwargs):
       
        user = self.model(
            login_id = login_id,

            nickname = nickname,
    
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, login_id, password, **extra_fields):

        superuser = self.create_user(
            nickname = nickname,
            login_id = login_id,
            password = password,

            )

        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser

class User(AbstractBaseUser, PermissionsMixin):
    login_id = models.CharField(unique=True, blank=False, null=False, max_length=15, default='')
    nickname = models.CharField(unique=True, blank=False, null=False, max_length=15)
    #email = models.CharField(unique=True, blank=False, null=False, max_length=255)
    #last_login = models.DateField(auto_now=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['nickname', 'password']      # superuser 만들 때 필수 !!

    def __str__(self):
        return self.login_id

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 user id로 설정
    USERNAME_FIELD = 'login_id'
    # 필수 작성 field
    
    
    
    class Meta:
        db_table = 'user'