
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth
from django.urls import path, include
from app import views as user_view
from app import views

admin.site.site_header = 'OneHealth'
admin.site.index_title = 'OneHealth'
admin.site.site_title = 'OneHealth Website'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('login/', user_view.Login, name='login'),
    path("logout", views.logout_request, name= "logout"),
    # path('signup/', views.signup, name='signup'),
    # path('register/', user_view.register, name='register'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
