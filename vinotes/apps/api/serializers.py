from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note, Trait, Wine, Winery


class WinerySerializer(serializers.ModelSerializer):
    wines = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Winery
        fields = ('id', 'name', 'wines')


class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = ('id', 'winery', 'name', 'vintage')


class TraitSerializer(serializers.ModelSerializer):
    color_notes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    nose_notes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    taste_notes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    finish_notes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Trait
        fields = ('id', 'name', 'color_notes', 
                  'nose_notes', 'taste_notes', 'finish_notes')


class NoteSerializer(serializers.ModelSerializer):
    taster = serializers.ReadOnlyField(source='taster.username')


    class Meta:
        model = Note
        fields = ('id', 'taster', 'tasted', 'wine', 'color_traits', 
                  'nose_traits', 'taste_traits', 'finish_traits', 'rating')


class UserSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'notes')