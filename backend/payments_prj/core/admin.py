from django.contrib import admin
from core.models import Transaction, CreditCard, Notification, Loan
from import_export.admin import ImportExportModelAdmin

class TransactionAdmin(admin.ModelAdmin):
    list_editable = ['amount', 'status', 'transaction_type']
    list_display = ['user', 'amount', 'status', 'transaction_type', 'reciever', 'sender']
    
class CreditCardAdmin(admin.ModelAdmin):
    list_editable = ['amount', 'card_type']
    list_display = ['user', 'amount', 'card_type']
    
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'notification_type', 'amount' ,'date']
    

class LoanAdminModel(ImportExportModelAdmin):
    list_editable = [ 'loan_balance', 'loan_term', 'admin_fee', 'penalty_fee', 'interest_rate_percent', 'loan_status', 'repayment_per_month'] #, 'kyc_submitted', 'kyc_confirmed'] 
    list_display = [ 'user','loan_balance', 'loan_term', 'admin_fee', 'penalty_fee', 'interest_rate_percent', 'loan_status', 'repayment_per_month', 'loan_type'] #, 'kyc_submitted', 'kyc_confirmed'] 
    list_filter = ['loan_status', 'loan_type']
    search_fields = ["loan_status", "user", 'loan_type']
    
    # def percentage(self, obj):
    #     # return f"{obj.interest_rate:.2%}"
    #     return str(format(float(obj.interest_rate * 100), '.2f') + ' %')
    


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(CreditCard, CreditCardAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Loan, LoanAdminModel)