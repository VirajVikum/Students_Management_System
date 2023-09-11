from django.db import models

# Create your models here.
class Department(models.Model):
    d_name = models.CharField(max_length=50)
    d_code = models.CharField(max_length=5)
    hod = models.CharField(max_length=50)

    def __str__(self):
        return self.d_name



class Students(models.Model):
    index = models.CharField(max_length=5)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.EmailField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.f_name + ' ' + self.l_name