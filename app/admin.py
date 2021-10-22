from django.contrib import admin

# Register your models here.
from app.models import HomeSection, HealthCenter, Doctors, Blog, Appointment, Contact, Comment, FooterBanner

admin.site.register(HomeSection)
admin.site.register(HealthCenter)
admin.site.register(Doctors)
admin.site.register(Blog)
admin.site.register(Appointment)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(FooterBanner)

