from django.contrib import admin
from django.urls import path,include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView
)

urlpatterns = [
    path('api/',include('api.urls')),
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/verify/', TokenVerifyView.as_view(), name='token_verify')
]