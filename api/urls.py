from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Ecommerce API",
        default_version='v1',
        description="Ecommerce API",
    ),
    
    public=True,
    
)
urlpatterns = [
    # Swagger
    path('', include('product.urls'), name="Product"),
    path('swagger/schema/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('auth/', include('Auth.urls'), name="User_auth"),
    path('webutils/', include('webutils.urls'), name="Webutils"),

]
