from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("insert_DEPT/", insert_DEPT, name="insert_DEPT"),
    path("insert_EMP/", insert_EMP, name="insert_EMP"),
    path('EmpToDeptJoin/',EmpToDeptJoin,name="EmpToDeptJoin"),
    path('EmpToMgrJoin/',EmpToMgrJoin,name='EmpToMgrJoin.html'),
    path('EmpToDEPTMGRJoin/',EmpToDEPTMGRJoin,name='EmpToDEPTMGRJoin.html'),
]
