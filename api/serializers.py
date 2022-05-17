from rest_framework import serializers
from yourturnapp.models import Project, Tag, Profile
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class YourTurnAppSerializer(serializers.ModelSerializer):
    project_owner = ProfileSerializer(many=False)

    class Meta:
        model = Project
        fields = '__all__'
