from django.contrib import admin
from Session_Auth_app.models import Emp

# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','email'] #eno act as link
    search_fields = ['ename']   #we'll get searchbox
    list_display_links = ['email']  #now email act as link
    readonly_fields = ['eno']
    list_editable = ['esal']
    exclude = ['esal'] #or fields=['email','esal']
    list_filter = ['ename']

admin.site.register(Emp,EmpAdmin)