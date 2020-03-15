from django.contrib import admin
from shop_app.models import student

# Register your models here.
#admin.site.register(student)

class studentAdmin(admin.ModelAdmin):
    list_display = ('id','cName','cSex','cBirthday','cEmail','cPhone','cAddr')

admin.site.register(student,studentAdmin)    
