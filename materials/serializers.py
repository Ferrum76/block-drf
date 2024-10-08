from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson, Subscription
from materials.validators import YoutubeValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [YoutubeValidator(field='link_to_video')]


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    def get_status_subscribed(self, course):
        request = self.context.get('request')
        return Subscription.objects.filter(course=course, user=request.user).exists()

    class Meta:
        model = Course
        fields = '__all__'



class CourseCountSerializer(ModelSerializer):
    quantity_lesson = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_quantity_lesson(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_status_subscribed(self, course):
        request = self.context.get('request')
        return Subscription.objects.filter(course=course, user=request.user).exists()

    class Meta:
        model = Course
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
