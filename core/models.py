from django.db import models

# Create your models here.

class GoogleBotVisit(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    path_accessed = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    verified_google_ip = models.BooleanField(default=False)

    def __str__(self):
        return f"GoogleBot visit from {self.ip_address} at {self.timestamp}"