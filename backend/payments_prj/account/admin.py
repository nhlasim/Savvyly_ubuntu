from django.contrib import admin
from account.models import Account, KYC
from userauths.models import User
from import_export.admin import ImportExportModelAdmin

#The Django admin application can use your models to automatically build a site area 
# that you can use to create, view, update, and delete records. 
# This can save you a lot of time during development, 
# making it very easy to test your models and get a feel for whether you have the right data.

class AccountAdminModel(ImportExportModelAdmin):
    list_editable = ['account_status', 'account_balance'] #, 'kyc_submitted', 'kyc_confirmed'] 
    list_display = ['user', 'account_number' ,'account_status', 'account_balance'] #, 'kyc_submitted', 'kyc_confirmed'] 
    list_filter = ['account_status']
    


class KYCAdmin(ImportExportModelAdmin):
    search_fields = ["full_name"]
    list_display = ['user', 'full_name', 'gender', 'identity_type', 'date_of_birth'] 


admin.site.register(Account, AccountAdminModel)
admin.site.register(KYC, KYCAdmin)