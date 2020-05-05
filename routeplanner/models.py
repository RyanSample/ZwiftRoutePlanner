from django.db import models

class World(models.Model):
    world_name = models.CharField(max_length=200)

    def __str__(self):
        return self.world_name

class Route(models.Model):
    world = models.ForeignKey(World, on_delete=models.CASCADE)
    route_name = models.CharField(max_length=200)
    route_length = models.FloatField(default=0.0)
    elevation_gain = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.route_name
