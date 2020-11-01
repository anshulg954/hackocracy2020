from django.contrib import admin

from .models import Company_CEO, Funder,StartUpProduct, Company_Funder_Mapping, AI_filtered_Company_Funder_Mapping, usrOTP

# register model to admin. 
admin.site.register(Company_CEO) 
admin.site.register(Funder)
admin.site.register(StartUpProduct)
admin.site.register(Company_Funder_Mapping)
admin.site.register(AI_filtered_Company_Funder_Mapping)
admin.site.register(usrOTP)