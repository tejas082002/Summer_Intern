from django.db import models
from datetime import date
# Create your models here.
standard=(
    ('None','None'),
    ('I','I'),
    ('II','II'),
    ('III','III'),
    ('IV','IV'),
    ('V','V'),
    ('VI','VI'),
    ('VII','VII'),
    ('VIII','VIII'),
    ('IX','IX'),
    ('X','X'),
    ('XI','XI'),
    ('XII','XII')
)
Gender=(
    ('Male','Male')
    ,('Female','Female'),('Others','others'))
Country=(('INDIA','INDIA'),('OTHERS','OTHERS'))

class Student_records(models.Model):
    Fname = models.CharField(max_length=50)
    Lname =  models.CharField(max_length=50)
    email =  models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    standard=models.CharField(
        max_length = 20,
        choices = standard,
        default = 'VII'
        )
    state =  models.CharField(max_length=50)
    postalpcode =  models.CharField(max_length=20)
    country =  models.CharField(max_length=50,choices=Country,default ='INDIA')
    DOB = models.DateTimeField()
    gender=models.CharField(max_length=30,choices=Gender,default='others')
    phone = models.CharField(max_length=15)
    


    def __str__(self):
        return(f"{self.Fname} {self.Lname}")
    
    
