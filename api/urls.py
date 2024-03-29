from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.get_route),
    path('projects/', views.get_projects),
    path('projects/<str:pk>/', views.get_project),
    path('projects/<str:pk>/vote/', views.view_vote),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
