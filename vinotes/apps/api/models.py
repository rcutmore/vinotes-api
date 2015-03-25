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

class Note(models.Model):
    wine = models.ForeignKey(Wine)

    def __str__(self):
        return 'Tasting note for: {wine}'.format(wine=self.wine)