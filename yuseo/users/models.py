from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations: True

    def create_user(self, login_id, password, email, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

       
        user = self.model(
            login_id = login_id,
            email = email,
    
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, login_id, password, **extra_fields):
    
        superuser = self.create_user(
            login_id = login_id,
            email = email,
            password = password,
        )

        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser

class User(AbstractBaseUser, PermissionsMixin):
    login_id = models.CharField(unique=True, blank=False, null=False, max_length=15, default='')
    email = models.CharField(unique=True, blank=False, null=False, max_length=255)
    #last_login = models.DateField(auto_now=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user_id

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 user id로 설정
    USERNAME_FIELD = 'login_id'
    # 필수 작성 field
    REQUIRED_FIELDS = ['email']
    
    
    
    class Meta:
        db_table = 'user'


 