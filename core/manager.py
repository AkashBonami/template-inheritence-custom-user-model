from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
 
class customUserManager(BaseUserManager):
    def create_user(self,email,name,password,**extra_feilds):
        if not email:
            raise ValueError(_("Email is Required"))
        user=self.model(email=email,
        name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,email,name,password,**extra_feilds):
        user=self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_admin=True 
        user.save(using=self._db)
        return user
        