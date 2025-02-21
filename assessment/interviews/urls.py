from django.urls import path
from .views import signup_view, login_view, logout_view, dashboard_view, practice_view, save_audio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('practice/', practice_view, name='practice'),
    path('save_audio/', save_audio, name='save_audio'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
