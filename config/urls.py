from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
urlpatterns = [
    path('changeme/', admin.site.urls),
    # API JWT Token Auth
    path("api/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    # the rest to go to greenhouse
    path("api/", include("greenhouse.urls")),
    path("accounts/", include("allauth.urls")),
    path("", include("greenhouse.urls")),
]
