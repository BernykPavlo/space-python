from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=20)
    min_distance_from_star = models.FloatField(help_text="In million kilometers")
    max_distance_from_star = models.FloatField(help_text="In million kilometers")
    radius = models.IntegerField(help_text="In kilometers")
    orbital_period = models.IntegerField(help_text="In Earth days")

    def __str__(self):
        return self.name

    @property
    def average_distance_from_star(self):
        return (self.min_distance_from_star + self.max_distance_from_star) / 2