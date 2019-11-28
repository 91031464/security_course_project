from django.db import models

class Tour(models.Model):
    tour_name = models.CharField(max_length=150)
    duration = models.ForeignKey('Duration', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    available = models.BooleanField()
    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True)

    class Meta:
        permissions = (("can_change_availability", "Set tour as available"),)

    def __str__(self):
        return self.tour_name + ' - ' + self.duration.duration


class Duration(models.Model):
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.duration

class Agent(models.Model):

    PROVIDER_CHOICES =(
        ('NZ Best', 'NZ Best Tour Company'),
        ('NZ First', 'New Zealand First Bus Tours'),
        ('Little Black Bus', 'Little Black Bus Individual Tours')
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    agent_username = models.CharField(max_length=30)
    email_address = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    provider = models.CharField(choices=PROVIDER_CHOICES, max_length=30)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' - ' + self.provider