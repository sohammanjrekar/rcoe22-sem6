from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Complaint(models.Model):
    STATUS =((1,'Solved'),(2, 'InProgress'),(3,'Pending'))
    TYPE=(('ClassRoom',"ClassRoom"),('Teacher',"Teacher"),('Management',"Management"),('College',"College"),('Other',"Other"))

    Subject=models.CharField(max_length=200,blank=False,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    Type_of_complaint=models.CharField(choices=TYPE,null=True,max_length=200)
    Description=models.TextField(max_length=4000,blank=False,null=True)
    Time = models.DateField(auto_now=True)
    status=models.IntegerField(choices=STATUS,default=3)
    def __init__(self, *args, **kwargs):
        super(Complaint, self).__init__(*args, **kwargs)
        self.__status = self.status

    def save(self, *args, **kwargs):
        if self.status and not self.__status:
            self.active_from = datetime.datetime.now()
        super(Complaint, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.get_Type_of_complaint_display()
    def __str__(self):
 	    return str(self.user)

class Grievance(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.guser