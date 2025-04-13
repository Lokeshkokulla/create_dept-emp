from django.shortcuts import render
from django.http import HttpResponse
from app.models import *



def EmpToDeptJoin(request):
    QLEDO=EMP.objects.all().select_related('dept_no')
    d={'QLEDO':QLEDO}
    return render(request,'EmpToDeptJoin.html',d)

def EmpToMgrJoin(request):
    QLEMO=EMP.objects.all().select_related('MGR')




    QLEMO=EMP.objects.all().select_related('MGR').filter(sal__gt=5000)
    QLEMO=EMP.objects.all().select_related('MGR').filter(ename__startswith='v')
    QLEMO=EMP.objects.all().select_related('MGR').filter(ename__endswith='d')
    QLEMO=EMP.objects.all().select_related('MGR').filter(MGR__job='sales')
    QLEMO=EMP.objects.all().select_related('MGR').filter(MGR__hiredate__year__gt='2024')
    QLEMO=EMP.objects.all().select_related('MGR').filter(job='accounting')
    QLEMO=EMP.objects.all().select_related('MGR').filter(job='accounting')
    QLEMO=EMP.objects.all().select_related('MGR')
    QLEMO=EMP.objects.all().select_related('MGR').filter(MGR__ename='hardhik')
    	




    d1={'QLEMO':QLEMO}
    return render(request,'EmpToMgrJoin.html',d1) 




def EmpToDEPTMGRJoin(request):
    QLEDMO=EMP.objects.all().select_related('dept_no','MGR')
    QLEDMO=EMP.objects.all().select_related('dept_no','MGR').filter(ename='virat')
    QLEDMO=EMP.objects.all()
    d={'QLEDMO':QLEDMO}
    return render(request,'EmpToDEPTMGRJoin.html',d)




























def insert_DEPT(request):
    dno=int(input('enter dept number'))
    dn=input('enter dname')
    l=input('enter dloc')
    DTO=DEPT.objects.get_or_create(dept_no=dno,dname=dn,dloc=l)
    if DTO[1]:
        return HttpResponse(f'{dno} is created')
    else:
        return HttpResponse(f'{dno} is already exists')

def insert_EMP(request):
    eno = int(input('enter empno'))
    en = input('enter ename')
    job = input('enter job')
    sal = float(input('enter the sal'))
    hd = input('enter date')
    comm = input('enter commission')
    
    if comm:
        comm = float(comm)
    else:
        comm = None
    
    dept_no = int(input('enter deptno'))
    DO = DEPT.objects.get(dept_no=dept_no)  

    MGR = input('enter mgr')
    MO = EMP.objects.filter(empno=int(MGR)).first() if MGR else None  

    TEO = EMP.objects.get_or_create(
        empno=eno, ename=en, job=job, sal=sal, comm=comm, dept_no=DO, MGR=MO, hiredate=hd
    )

    if TEO[1]:
        return HttpResponse(f'{eno} is created')
    else:
        return HttpResponse(f'{eno} already exists')
