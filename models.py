from django.db import models
from django.utils import timezone
from resume import choices


class Person(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='resumepr/images', blank=True)
    b_date = models.DateTimeField(default=timezone.now(), blank=True)
    bio = models.CharField(max_length=100, blank=True,null=True)
    city = models.CharField(max_length=15, blank=True,null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Interest(models.Model):
    sport = models.CharField(max_length=10, choices=choices.MUSIC, blank=True, null=True)
    music = models.CharField(max_length=10, choices=choices.SPORT, blank=True, null=True)
    food = models.CharField(max_length=10, choices=choices.FOOD, blank=True, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True, related_query_name='interests',
                               related_name='interest')

    def __str__(self):
        return self.sport + ' ' + self.music + ' ' + self.food


class Job(models.Model):
    start_date = models.IntegerField(default=timezone.now(), blank=True,null=True,)
    finish_date = models.IntegerField(default=timezone.now(), blank=True,null=True,)
    place = models.CharField(max_length=30, blank=True,null=True)
    position = models.CharField(max_length=30, blank=True,null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True, related_name='jobs',
                               related_query_name='job')

    def __str__(self):
        return self.place


class Education(models.Model):
    start_date = models.IntegerField(default=timezone.now(), blank=True,null=True,)
    finish_date = models.IntegerField(default=timezone.now(), blank=True,null=True,)
    place = models.CharField(max_length=30, blank=True,null=True,)
    speciality = models.CharField(max_length=30, blank=True,null=True, )
    type = models.CharField(max_length=10, choices=choices.TYPE, blank=True, null=True,)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True, related_name='education',
                               related_query_name='educations',)




class Contact(models.Model):
    phone = models.CharField(max_length=30, blank=True,null=True)
    email = models.EmailField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True, related_name='contact',
                               related_query_name='contacts')

    def __str__(self):
        return self.email


class Social(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True)
    twitter = models.CharField(max_length=30, blank=True)
    facebook = models.CharField(max_length=30, blank=True)
    instagram = models.CharField(max_length=30, blank=True)
    telegram = models.CharField(max_length=30, blank=True)
    skype = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.telegram + self.facebook
