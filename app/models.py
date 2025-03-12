from django.db import models

# Create your models here.

class DEPT(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    dloc=models.CharField(max_length=100)

class EMP(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.DecimalField(max_digits=10,decimal_places=3)
    comm=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    hiredate=models.DateField(auto_now=True)
    dept_no=models.ForeignKey(DEPT,on_delete=models.CASCADE)
    MGR=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)

class SALGRADE(models.Model):
    high_sal=models.DecimalField(max_digits=10,decimal_places=3)
    low_sal=models.DecimalField(max_digits=10,decimal_places=3)

