from django.db import models
from userauths.models import User 
from account.models import Account
from shortuuid.django_fields import ShortUUIDField

LOAN_STATUS = (
    ("Active", "Active"),
    ("Pending", "Pending"),
    ("In-active", "In-active"),
    ("In-arrears", "In-arrears"),
    ("Paid-off", "Paid-off"),
    ("Written-off", "Written-off")
)

LOAN_TYPE = (
    ("Personal", "Personal"),
    ("Business", "Business")
)

TRANSACTION_TYPE = (
    ("transfer", "Transfer"),
    ("recieved", "Recieved"),
    ("withdraw", "withdraw"),
    ("refund", "Refund"),
    ("request", "Payment Request"),
    ("none", "None")
)

TRANSACTION_STATUS = (
    ("failed", "failed"),
    ("completed", "completed"),
    ("pending", "pending"),
    ("processing", "processing"),
    ("request_sent", "request_sent"),
    ("request_settled", "request settled"),
    ("request_processing", "request processing"),

)


CARD_TYPE = (
    ("master", "master"),
    ("visa", "visa"),
    ("verve", "verve"),

)


NOTIFICATION_TYPE = (
    ("None", "None"),
    ("Transfer", "Transfer"),
    ("Credit Alert", "Credit Alert"),
    ("Debit Alert", "Debit Alert"),
    ("Sent Payment Request", "Sent Payment Request"),
    ("Recieved Payment Request", "Recieved Payment Request"),
    ("Funded Credit Card", "Funded Credit Card"),
    ("Withdrew Credit Card Funds", "Withdrew Credit Card Funds"),
    ("Deleted Credit Card", "Deleted Credit Card"),
    ("Added Credit Card", "Added Credit Card"),
    ("Loan Repayment", "Loan Repayment"),

)

# LOAN_STATUS = (
#     ("Pending", "Pending"),
#     ("Approved", "Approved"),
#     ("Active", "Active"),
#     ("In Arrears", "In Arrears"),
#     ("Locked", "Locked"),
#     ("Closed", "Closed"),
#     ("Written-Off", "Written-Off"),
#     ("Refinanced", "Refinanced"),
    

# )


class Transaction(models.Model):
    transaction_id = ShortUUIDField(unique=True, length=15, max_length=20, prefix="TRN")
   
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="user") #'on_delete=...' means that even if user is deleted we are keeping teh transaction
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    description = models.CharField(max_length=1000, null=True, blank=True)
   
    reciever = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="reciever")
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="sender")
   
    reciever_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name="reciever_account")
    sender_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name="sender_account")

    status = models.CharField(choices=TRANSACTION_STATUS, max_length=100, default="pending")
    transaction_type = models.CharField(choices=TRANSACTION_TYPE, max_length=100, default="none")

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    #below is to return a string representation
    def __str__(self):
        try:
            return f"{self.user}"
        except:
            return f"Transaction"
        

class Loan(models.Model):
    # user =  models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_id = ShortUUIDField(unique=True, length=5, max_length=20, prefix="LOAN", alphabet="1234567890")
    full_name = models.CharField(max_length=100)
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    loan_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00) #1'max_dgitis' is '12' means that maximum is in billions
    loan_term = models.IntegerField()
    repayment_per_month = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    admin_fee = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    penalty_fee = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    interest_rate_percent = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    loan_account_no = ShortUUIDField(unique=True,length=10, max_length=25, prefix="217", alphabet="1234567890") #"alphabet" teh way it is means that account number will only be numbers. prefix means every account will start with 217
    loan_status = models.CharField(max_length=100, choices=LOAN_STATUS, default="In-active")
    payslip = models.ImageField(upload_to="payslip", null=True, blank=True)
    credit_report = models.ImageField(upload_to="credit_report", null=True, blank=True)
    # date_of_birth = models.DateTimeField(auto_now_add=False)
    loan_start = models.DateTimeField(blank=True, null=True)
    # loan_start = models.DateTimeField(auto_now_add=True)
    loan_type = models.CharField(choices=LOAN_TYPE, max_length=20, default="Personal")
    date = models.DateTimeField(auto_now_add=True)
    
    @property
    def interest_rate_in_percentage(self):
        return f"{self.interest_rate} %"
    
    def __str__(self):
        return f"{self.user}"


class CreditCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 'CASCADE' is to ensure that if the user gets deleted we delete their credit card also
    card_id = ShortUUIDField(unique=True, length=5, max_length=20, prefix="CARD", alphabet="1234567890")
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    cvv = models.IntegerField()

    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    card_type = models.CharField(choices=CARD_TYPE, max_length=20, default="master")
    card_status = models.BooleanField(default=True)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"

#Loan Model
# class Loan(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE) # 'CASCADE' is to ensure that if the user gets deleted we delete their credit card also
#     loan_id = ShortUUIDField(unique=True, length=5, max_length=20,  alphabet="1234567890")

#     loan_name = models.CharField(max_length=100)
#     number = models.IntegerField()
#     month = models.IntegerField()
#     year = models.IntegerField()
#     cvv = models.IntegerField()

#     loan_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
#     loan_interest = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
#     loan_admin = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
#     loan_penalty = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    

#     card_type = models.CharField(choices=CARD_TYPE, max_length=20, default="master")
#     loan_status = models.BooleanField(default=True)

#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    notification_type = models.CharField(max_length=100, choices=NOTIFICATION_TYPE, default="none")
    amount = models.IntegerField(default=0)
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    nid = ShortUUIDField(length=10, max_length=25, alphabet="abcdefghijklmnopqrstuvxyz")
    
    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Notification"

    def __str__(self):
        return f"{self.user} - {self.notification_type}"
