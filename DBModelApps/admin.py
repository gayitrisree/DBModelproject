from django.contrib import admin
from DBModelApp.models import Employee

#Register _disply=['eno','name','salary','company',];
admin.site.register(Employee,EmployeeAdmin)

