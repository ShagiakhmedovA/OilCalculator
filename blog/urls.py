from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/<int:pk>/', views.get_user_profile, name='user_profile'),
    path('accounts/<int:pk>/edit/', views.edit_user_profile, name='edit_user_profile'),
    path('theory/', views.theory, name='theory'),
    path('about_program/', views.about_program, name='about_program'),
    path('calculation', views.calculation_new, name='calculation_new'),
    path('calculation/<int:pk>/detail', views.calculation_detail, name='calculation_detail'),
    path('calculation/<int:pk>/delete', views.calculation_delete, name='calculation_delete'),
    path('history/', views.history_show, name='history_show'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

