"""
Contains models for API app.
"""
from django.conf import settings
from django.db import models


class Winery(models.Model):
    """A winery.

    :param name: Name of winery.
    """
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'wineries'


class Wine(models.Model):
    """A wine.

    :param winery: Wine's assigned :class:`Winery` object.
    :param name: Name of wine.
    :param vintage: Year wine was produced.
    """
    winery = models.ForeignKey(Winery, related_name='wines')
    name = models.CharField(max_length=150)
    vintage = models.IntegerField()

    def __str__(self):
        return '{winery} {wine} {vintage}'.format(
            winery=self.winery, wine=self.name, vintage=self.vintage)

    class Meta:
        unique_together = ('winery', 'name', 'vintage',)


class Trait(models.Model):
    """A wine trait.

    :param name: Name of trait.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    """A wine tasting note.

    :param taster: Note's assigned user model object.
    :param tasted: Date of wine tasting.
    :param wine: Note's assigned :class:`Wine` object.
    :param color_traits: Note's assigned :class:`Trait` objects for its
        color characteristics.
    :param nose_traits: Note's assigned :class:`Trait` objects for its
        nose characteristics.
    :param taste_traits: Note's assigned :class:`Trait` objects for its
        taste characteristics.
    :param finish_traits: Note's assigned :class:`Trait` objects for its
        finish characteristics.
    :param rating: Rating of wine (1 to 5 stars).
    """
    taster = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notes')
    tasted = models.DateTimeField(null=True, blank=True)
    wine = models.ForeignKey(Wine)
    color_traits = models.ManyToManyField(
        Trait, related_name='color_notes', blank=True)
    nose_traits = models.ManyToManyField(
        Trait, related_name='nose_notes', blank=True)
    taste_traits = models.ManyToManyField(
        Trait, related_name='taste_notes', blank=True)
    finish_traits = models.ManyToManyField(
        Trait, related_name='finish_notes', blank=True)
    RATING_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5),)
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES, null=True, blank=True)

    def __str__(self):
        return 'Tasting note for: {wine}'.format(wine=self.wine)
