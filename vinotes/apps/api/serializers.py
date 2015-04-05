from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note, Trait, Wine, Winery


class WinerySerializer(serializers.ModelSerializer):
    wines = serializers.PrimaryKeyRelatedField(many=True, queryset=Wine.objects.all())


    class Meta:
        model = Winery
        fields = ('id', 'name', 'wines')


class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = ('id', 'winery', 'name', 'vintage')


class TraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trait
        fields = ('id', 'name')


class NoteSerializer(serializers.ModelSerializer):
    taster = serializers.ReadOnlyField(source='taster.username')


    class Meta:
        model = Note
        fields = ('id', 'taster', 'tasted', 'wine', 'color_traits', 
                  'nose_traits', 'taste_traits', 'finish_traits', 'rating')


class UserSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())


    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'notes')