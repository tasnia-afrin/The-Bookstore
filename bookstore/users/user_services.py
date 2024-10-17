from django.db.models import QuerySet
from mainapp.models import CustomUser

class UserServices:
    def create_superuser(
        self,
        email: str,
        password: str,
        first_name: str = "",
        last_name: str = "",       
    ) -> CustomUser:
        return CustomUser.objects.create_user(
            first_name=first_name,
            last_name=last_name,            
            password=password,
            email=email,            
            status=CustomUser.ACTIVE,
            is_active=True,
            is_staff=True,
            is_verified=True,
            is_superuser=True,
        )
    
    
    def create_user(
        self,
        email: str,
        username:str,
        password: str,
        first_name: str = "",
        last_name: str = "",
        user_type: str = "",
    ) -> CustomUser:
        return CustomUser.objects.create_user(
            username=username,
            email=email,   
            password=password, 
            first_name=first_name,
            last_name=last_name,                    
            user_type=user_type,
            is_active=True,
        )
    
    
    