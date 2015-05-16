from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Note, Trait, Wine, Winery


class WinerySerializer(serializers.HyperlinkedModelSerializer):
    wines = serializers.HyperlinkedIdentityField(
        many=True, read_only=True, view_name='wine-detail')


    class Meta:
        model = Winery
        fields = ('url', 'name', 'wines')


class WineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wine
        fields = ('url', 'winery', 'name', 'vintage')


class TraitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trait
        fields = ('url', 'name')


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    taster = serializers.ReadOnlyField(source='taster.username')


    class Meta:
        model = Note
        fields = ('url', 'taster', 'tasted', 'wine', 'color_traits', 
                  'nose_traits', 'taste_traits', 'finish_traits', 'rating')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    notes = serializers.HyperlinkedIdentityField(
        many=True, read_only=True, view_name='note-detail')


    class Meta:
        model = get_user_model()
        fields = ('url', 'email', 'password', 'notes')
        write_only_fields = ('password',)


    def create(self, validated_data):
        """
        Make sure user's password is hashed before storing.
        """
        user = get_user_model()(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user