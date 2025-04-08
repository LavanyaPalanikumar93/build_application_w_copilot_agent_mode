from djongo import models

class User(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

class Team(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    members = models.JSONField()

class Activity(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    user_id = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    team_id = models.CharField(max_length=255)
    points = models.IntegerField()

class Workout(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()