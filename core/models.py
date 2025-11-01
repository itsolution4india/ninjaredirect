from django.db import models
from datetime import datetime
# Create your models here.

class GoogleBotVisit(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    path_accessed = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    verified_google_ip = models.BooleanField(default=False)

    def __str__(self):
        return f"GoogleBot visit from {self.ip_address} at {self.timestamp}"
    
class NormalVisit(models.Model):
    ip_address = models.CharField(max_length=255)
    user_agent = models.TextField(blank=True, null=True)
    path_accessed = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.path_accessed}"    
    
    
class GotBaited(models.Model):
    have_clicked =  models.BooleanField( default= False)
    date_time = models.DateTimeField(auto_now_add=True )
    visitor = models.ForeignKey(NormalVisit  , on_delete=models.CASCADE  ,  related_name="GotBaited")
    