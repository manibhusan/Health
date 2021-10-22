from rest_framework import serializers

from .models import *


class HomeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSection
        fields = '__all__'


class HealthCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthCenter
        fields = '__all__'


class FooterBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterBanner
        fields = '__all__'


class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
