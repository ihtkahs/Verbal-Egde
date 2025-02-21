from django.urls import path
from .views import (
    signup_view, login_view, logout_view, dashboard_view, practice_view, 
    save_audio, dashboard_home, practice, responses, performance, settings_home
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard/home/', dashboard_home, name='dashboard_home'),
    path('dashboard/practice/', practice, name='practice'),
    path('dashboard/responses/', responses, name='responses'),
    path('dashboard/performance/', performance, name='performance'),
    path('dashboard/settings/', settings_home, name='settings_home'),
    path('practice_home/', practice_view, name='practice_home'),
    path('save_audio/', save_audio, name='save_audio'),
]

# Serve media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
