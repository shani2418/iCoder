from django.db import models

# Create your models here.
#Database ---->Excel workbook
#Models In Django ----> Table ---> Sheet

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)#automatoc thai jai atle n khabar pade search kari levu google

    def __str__(self):
        return 'message from' + self.name + ' - ' + self.email
