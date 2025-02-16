from django.db import models

SIZE_CHOICES = [
    ("T", "1-10"),
    ("S", "10-100"),
    ("M","100-1000"),
    ("L","1000-10000"),
    ("XL","10000-100000"),
    ("2XL","100000+"),


]
class Partner(models.Model):
    name= models.CharField(max_length=100)
    CompanySize= models.CharField(max_length=100,choices=SIZE_CHOICES)
    url= models.URLField(max_length=100)
    #image=models.ImageField(upload_to='PartnerImages')
    def __str__(self):
        return self.name