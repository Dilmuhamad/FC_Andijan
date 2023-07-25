from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Header(models.Model):
    photo = models.FileField()
    name = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.name


class Video(models.Model):
    photo = models.FileField()
    name = models.CharField(max_length=255)
    video_fail = models.FileField(null=True, blank=True)
    video_url = models.CharField(max_length=255, null=True, blank=True)


class Position(models.Model):
    name = models.CharField(max_length=255)


class Player(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    game = models.IntegerField()
    time_played = models.IntegerField()
    start = models.IntegerField()
    sub_off = models.IntegerField()



class ArenasInformation(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    volume = models.IntegerField()
    places = models.IntegerField()
    sector = models.IntegerField()
    map = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


class Partner(models.Model):
    img = models.FileField()


class Tournament(models.Model):
    data = models.DateTimeField()
    match = models.IntegerField()


class New(models.Model):
    news = models.TextField()
    photo = models.ImageField()
    is_file = models.BooleanField()
    video_file = models.FileField()
    video_url = models.CharField(max_length=255)
    tournament = models.ManyToManyField(Tournament)


class Team(models.Model):
    title = models.CharField(max_length=255)
    players = models.ManyToManyField(Player)


class Leadership(models.Model):
    photo = models.FileField()


class Level(models.Model):
    name = models.CharField(max_length=255)


class Leader(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)
    text = models.TextField()
    level = models.ForeignKey(Level, on_delete=models.CASCADE)


class Coach(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)
    text = models.TextField()
    level = models.ForeignKey(Level, on_delete=models.CASCADE)


class Club(models.Model):
    content = RichTextUploadingField()


class Shop(models.Model):
    text = models.TextField()
    photo = models.ImageField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Academy(models.Model):
    content = RichTextUploadingField()


class Arena(models.Model):
    content = RichTextUploadingField()

