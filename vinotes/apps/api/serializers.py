"""
Contains serializers for API app.
"""
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Note, Trait, Wine, Winery


class WinerySerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for :class:`Winery` objects."""
    wines = serializers.HyperlinkedIdentityField(
        many=True, read_only=True, view_name='wine-detail')

    class Meta:
        model = Winery
        fields = ('pk', 'url', 'name', 'wines',)


class WineSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for :class:`Wine` objects."""

    class Meta:
        model = Wine
        fields = ('pk', 'url', 'winery', 'name', 'vintage',)


class TraitSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for :class:`Trait` objects."""

    class Meta:
        model = Trait
        fields = ('pk', 'url', 'name',)


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for :class:`Note` objects."""
    taster = serializers.ReadOnlyField(source='taster.email')

    class Meta:
        model = Note
        fields = (
            'pk', 'url', 'taster', 'tasted', 'wine', 'color_traits',
            'nose_traits', 'taste_traits', 'finish_traits', 'rating',
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for user model."""
    notes = serializers.HyperlinkedIdentityField(
        many=True, read_only=True, view_name='note-detail')

    class Meta:
        model = get_user_model()
        fields = ('url', 'email', 'password', 'notes',)
        write_only_fields = ('password',)

    def create(self, validated_data):
        """Hash user's password and create token.

        :param validated_data: Validated incoming data.
        :returns: New user model object.
        """
        user = get_user_model()(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
