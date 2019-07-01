from django.db import models
from django.utils import timezone
from django.utils.timezone import datetime

app_name = 'PDI'

# Create your models here.

class ActivityType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 20)

    class Meta():
        verbose_name_plural = 'Activity Types'

    def __str__(self):
        return self.name
class DataSubject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200, null=True)
    
    class Meta():
        verbose_name_plural = 'Data Subjects'
        
    def __str__(self):
        return self.name
    
class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    act_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    data_subject = models.ForeignKey(DataSubject, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(timezone.now)
    date_modified = models.DateTimeField(timezone.now)

    class Meta():
        verbose_name_plural = 'Activities'
    
    def __str__(self):
        return self.name

class Office(models.Model):
    id = models.AutoField(primary_key=True)
    abbr = models.CharField(max_length = 100)
    name = models.CharField(max_length = 250)
    activity = models.ForeignKey(Activity, on_delete = 'CASCADE', null = True)
    description = models.CharField(max_length = 250, null = True)

    class Meta():
        verbose_name_plural = 'Offices'

    def __str__(self):
        return self.name
    
class Classification(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200, null = True)

    class Meta():
        verbose_name_plural = 'Classifications'
    
    def __str__(self):
        return self.name, self.description
    
class Basis(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200, null = True)

    class Meta():
        verbose_name_plural = 'Bases'
    
    def __str__(self):
        return self.name
    
class Data(models.Model):
    id = models.AutoField(primary_key=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    name =  models.CharField(max_length = 100)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE,
    blank = True, null = True)
    source = models.CharField(max_length = 100)
    purpose = models.CharField(max_length = 250)
    basis = models.ForeignKey(Basis, on_delete=models.CASCADE, blank = True, null = True)
    locations = models.CharField(max_length = 250)
    user_internal = models.CharField(max_length = 250)
    user_pip = models.CharField(max_length = 250)
    user_pic = models.CharField(max_length = 250)
    policy_use = models.CharField(max_length = 500)
    policy_protection = models.CharField(max_length = 500)
    policy_backup = models.CharField(max_length = 500)
    policy_disposal = models.CharField(max_length = 500)
    date_created = models.DateTimeField(timezone.now)
    date_modified = models.DateTimeField(timezone.now)

    class Meta():
        verbose_name_plural = 'Data'
    
    def __str__(self):
        return self.name