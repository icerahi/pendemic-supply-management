from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .views import user_login,user_logout


urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include('dashboard.urls')),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),

]


urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
