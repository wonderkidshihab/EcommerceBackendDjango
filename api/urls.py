from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
urlpatterns = [
    # Swagger
    path('', get_swagger_view(title='Ecommerce API')),
    path('auth/', include('Auth.urls'), name="User_auth"),
    
    
]
