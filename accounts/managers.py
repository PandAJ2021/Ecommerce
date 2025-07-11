from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, name, email, phone, password=None):

        if not name:
            raise ValueError('Users must have a name')
        if not email:
            raise ValueError('Users must have email')
        if not phone:
            raise ValueError('Users must have phone')
        
        user = self.model(
            name = name,
            email = self.normalize_email(email),
            phone = phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, phone, password=None):
        user = self.create_user(name, email, phone, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
