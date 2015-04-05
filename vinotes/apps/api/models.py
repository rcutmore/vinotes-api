from django.db import models

class Winery(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'wineries'

class Wine(models.Model):
    winery = models.ForeignKey(Winery, related_name='wines')
    name = models.CharField(max_length=150)
    vintage = models.IntegerField()

    def __str__(self):
        return '{winery} {wine} {vintage}'.format(
            winery=self.winery, wine=self.name, vintage=self.vintage)

    class Meta:
        unique_together = ('winery', 'name', 'vintage',)

class Trait(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Note(models.Model):
    RATING_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5),)

    taster = models.ForeignKey('auth.User', related_name='notes')
    tasted = models.DateTimeField(null=True, blank=True)
    wine = models.ForeignKey(Wine)
    color_traits = models.ManyToManyField(
        Trait, related_name='color_traits', null=True, blank=True)
    nose_traits = models.ManyToManyField(
        Trait, related_name='nose_traits', null=True, blank=True)
    taste_traits = models.ManyToManyField(
        Trait, related_name='taste_traits', null=True, blank=True)
    finish_traits = models.ManyToManyField(
        Trait, related_name='finish_traits', null=True, blank=True)
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES, null=True, blank=True)

    def __str__(self):
        return 'Tasting note for: {wine}'.format(wine=self.wine)