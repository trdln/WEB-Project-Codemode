from rest_framework import serializers

from .models import Tutor, TutorPhoneNumbers, Course, CourseTutor, Student, StudentPhoneNumbers, StudentCourseTutor, \
    Money


class TutorSerializer(serializers.ModelSerializer):
    phones = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tutor
        fields = '__all__'


class TutorPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorPhoneNumbers
        fields = '__all__'


class CourseSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    price = serializers.IntegerField()
    info = serializers.TextField()

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.info = validated_data.get('info', instance.info)
        instance.save()
        return instance

class CourseTutor(serializers.ModelSerializer):
    class Meta:
        model = CourseTutor
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    phones = serializers.StringRelatedField(many=True)

    class Meta:
        model = Student
        fields = '__all__'


class StudentPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPhoneNumbers
        fields = '__all__'


class StudentCourseTutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourseTutor
        fields = '__all__'


class MoneySerializer(serializers.Serializer):
    student_id = serializers.PrimaryKeyRelatedField(queryset=Money.objects.all())
    time = serializers.DateTimeField()
    type = serializers.BooleanField()
    message = serializers.CharField()
    status = serializers.CharField()

    def create(self, validated_data):
        return Money.objects.create(**validated_data)