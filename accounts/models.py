from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    # @classmethod
    # def create_social_user(strategy, details, backend, user=None, *args, **kwargs):
    #     if user is None:
    #         user_model = get_user_model()
    #         user = user_model.objects.create(email=details['email'])
    #         user.first_name = details.get('first_name', '')
    #         user.last_name = details.get('last_name', '')
    #         user.is_active = True
    #     else:
    #         user.is_active = True
    #     user.save()
    #     return {'user': user}

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Adres email",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        ordering = ("-id",)
        verbose_name = "Użytkownik"
        verbose_name_plural = "Użytkownik"

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        # Ta metoda jest wymagana, ale możesz ją dostosować do swoich potrzeb
        return self.is_admin

    def has_perm(self, perm, obj=None):
        # Ta metoda jest wymagana, ale możesz ją dostosować do swoich potrzeb
        return self.is_admin