from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        """
        Creates and saves a User with the given  first_name, last_name, email, and password.
        """
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, first_name, last_name, email, password=None):
        """
        Creates and saves a superuser with the given first_name, last_name, email, and password.
        """
        user = self.create_user( 
            first_name,
            last_name,
            email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

