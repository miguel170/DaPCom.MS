from django.db import models

# Create your models here.
class Office(models.Model):
    abbr = models.CharField(max_length = 100)
    name = models.CharField(max_length = 250)
    description = models.CharField(max_length = 250)

    def __str__(self):
        return self.name + " ("+ self.abbr + ")"

class ActivityType(models.Model):
    id = models.AutoField(primary_key=True)
    ACTIVITY_TYPE = [
        'Program',
        'Project',
        'Process',
        'Measure',
        'System',
        'Technology'
        ]

    name = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.id, self.name
    
class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    act_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    owner = models.ForeignKey(Office, on_delete=models.CASCADE)
    datasubject = models.CharField(max_length = 20)
    date_created = models.DateTimeField(auto_now = True)
    date_modified = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.id, self.name,
        self.act_type, owner, datasubject, date_created,
        date_modified
    
class Classification(models.Model):
    DATA_CLASS = [
        ('PI', 'Personal Information', 1),
        ('SPI', 'Sensitive Personal Information', 3),
        ('Priv', 'Privileged Information', 4),
    ]

    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    rating = models.IntegerField()
    
    def __str__(self):
        return self.name, self.description
    
class Basis(models.Model):
    BASIS = [
        ('Consent', 'Requires legal consent and authorization of the Data Subject'),
        ('Others', ''),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)

    class Meta():
        verbose_name_plural = 'Bases'
    
    def __str__(self):
        return [self.id, self.name, self.description]
    
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
    date_created = models.DateTimeField(auto_now = True)
    date_modified = models.DateTimeField(auto_now = True)

    
    def __str__(self):
        return self.id, self.name,
        self.activity_set.name, self.purpose
        
    