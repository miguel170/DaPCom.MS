from django.db import models

# Create your models here.
class ActivityType(models.Model):
    name = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.name
    
class Activity(models.Model):
    name = models.CharField(max_length = 100)
    act_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    datasubject = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.name
        
class Office(models.Model):
    abbr = models.CharField(max_length = 100)
    name = models.CharField(max_length = 250)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    description = models.CharField(max_length = 250)

    def __str__(self):
        return "[" + self.abbr + "] " + self.name
    
class Classification(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    rating = models.IntegerField()
    
    def __str__(self):
        return self.description
    
class Basis(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
    
class Data(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    name =  models.CharField(max_length = 100)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    source = models.CharField(max_length = 100)
    purpose = models.CharField(max_length = 250)
    basis = models.ForeignKey(Basis, on_delete=models.CASCADE)
    locations = models.CharField(max_length = 250)
    user_internal = models.CharField(max_length = 250)
    user_pip = models.CharField(max_length = 250)
    user_pic = models.CharField(max_length = 250)
    policy_use = models.CharField(max_length = 500)
    policy_protection = models.CharField(max_length = 500)
    policy_backup = models.CharField(max_length = 500)
    policy_disposal = models.CharField(max_length = 500)
    
    def __str__(self):
        return self.name + " - " + self.purpose
        
    