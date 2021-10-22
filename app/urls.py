from django.urls import include
from django.urls import path, re_path
from rest_framework import routers
from . import views
from .views import SignUpView, validate_username
from .views import contact_form

router = routers.DefaultRouter()

router.register('home-section', views.HomeSectionViewSet, basename='home_section')
router.register('health-center', views.HealthCenterViewSet, basename='health_center')
router.register('footer-section', views.FooterBannerViewSet, basename='footer_section')
router.register('doctor-section', views.DoctorsViewSet, basename='doctor_section')
router.register('blog-section', views.BlogViewSet, basename='blog_section')
router.register('appointment-section', views.AppointmentViewSet, basename='appointment_section')
router.register('contact-section', views.ContactViewSet, basename='contact_section')
router.register('comment-section', views.CommentViewSet, basename='comment_section')


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('doctor/', views.DoctorView.as_view(), name='doctors'),
    path('about/', views.AboutUsView.as_view(), name='about_us'),
    path('news/', views.BlogView.as_view(), name='news'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    re_path('detail/(?P<pk>\d+)/', views.DetailView.as_view(), name='detail'),
    path('contact-us/', views.ContactusView.as_view(), name="contact_us"),
    path('appointment/', views.AppointmentView.as_view(), name='appointment'),
    path('leave-comment/', views.CommentView.as_view(), name='leave_comment'),
    path('test/', views.index, name='index_use'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('validate_username', validate_username, name='validate_username'),
    # path('page/', views.FileExamListView.as_view(), name='file-exam-view'),
    path('contact-form/', contact_form, name='contact_form'),
    # path('search/', views.search, name="search"),
    path('results/', views.SearchView.as_view(), name='search'),
    path('blog-search/', views.BlogSearchView.as_view(), name='blog_search'),
    # rest_framework
    path('all_api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

urlpatterns += router.urls