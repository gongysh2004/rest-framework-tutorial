from django.urls import include, re_path
from rest_framework.schemas import get_schema_view
from knox import views as knox_views
from snippets.views import LoginView

urlpatterns = [
    re_path(r'^', include('snippets.urls')),
    re_path(r'^api-auth/login/', LoginView.as_view(), name='knox_login'),
    re_path(r'^api-auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    re_path(r'^api-auth/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]
