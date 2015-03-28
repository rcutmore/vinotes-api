from django.db import models

class Winery(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Wine(models.Model):
    title = models.CharField(max_length=150)
    vintage = models.IntegerField()
    description = models.TextField(blank=True)
    winery = models.ForeignKey(Winery)

    def __str__(self):
        return '{winery} {wine} {vintage}'.format(
            winery=self.winery, wine=self.title, vintage=self.vintage)

class Trait(models.Model):
    description = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.description

class Note(models.Model):
    RATING_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5),)

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