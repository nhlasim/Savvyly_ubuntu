from django.db import models
import uuid
from shortuuid.django_fields import ShortUUIDField
from userauths.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_mailbox.signals import message_received
import re

ACCOUNT_STATUS = (
    ("active", "Active"),
    ("pending", "Pending"),
    ("in-active", "In-active")
)



MARITAL_STATUS = (
    ("married", "Married"),
    ("single", "Single"),
    ("other", "Other")
)

GENDER = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other")
)


IDENTITY_TYPE = (
    ("national_id_card", "National ID Card"),
    ("drivers_licence", "Drivers Licence"),
    ("international_passport", "International Passport")
)



# NATIONALITY = (
#     ("south africa", "Soth Africa"),
#     ("zimbabwe", "Zimbabwe"),
#     ("eswatini", "Eswatini"),
#     ("botswana", "Botswana"),
#     ("lesotho", "Lesotho"),
#     ("nigeria", "Nigeria"),
# )

@receiver(message_received)
def dance_jig(sender, message, **args):
    # print ("massage received")
    # print ("I just recieved a message titled %s from a mailbox named %s with body %s " % (message.subject, message.mailbox.name, message.text, ))
    text = message.text
  
    #Check if this is incoming payment
    string_list = re.split("\s", text)
    print(string_list)
    i = 0
    while i < len(string_list):
        if (string_list[i-1] == 'Incoming' and string_list[i] == 'payment'):
            print("Incoming payment")
            break
        i += 1
    
    #Reference nunber code    
    # string_list = re.split("\s", text)
    # print(string_list)
    # i = 0
    # while i < len(string_list):
    #     if string_list[i] == 'Reference:':
    #         reference_number = string_list[i+1] 
    #         print(reference_number)
    #         break
    #     i += 1
        
        
    # Reading the amount trasnferred code
    # numbers = [float(num) for num in re.findall(r'[\d.]+', text)]
    # print("Amount deposited %s " % (numbers[0],))
    # print("Reference number %s " % (int(numbers[2]),))
    



def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]  #"." mean that we are taking the file extension like png jpg etc
    filename = "%s_%s" % (instance.id, ext)
    return "user_{0}/{1}".format(instance.user.id, filename)

def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]  #"." mean that we are taking the file extension like png jpg etc
    filename = "%s_%s" % (instance.id, ext)
    return "user_{0}/{1}".format(instance.user.id, filename)

class Account(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    # user =  models.ForeignKey(User, on_delete=models.CASCADE)
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00) #1'max_dgitis' is '12' means that maximum is in billions
    account_number = ShortUUIDField(unique=True,length=10, max_length=25, prefix="217", alphabet="1234567890") #"alphabet" teh way it is means that account number will only be numbers. prefix means every account will start with 217
    account_id = ShortUUIDField(unique=True,length=7, max_length=25, prefix="DEX", alphabet="1234567890") #2175893745837
    pin_number = ShortUUIDField(unique=True,length=4, max_length=7, alphabet="1234567890") #2737
    red_code = ShortUUIDField(unique=True,length=10, max_length=20, alphabet="abcdefgh1234567890") #2737
    account_status = models.CharField(max_length=100, choices=ACCOUNT_STATUS, default="in-active")
    date = models.DateTimeField(auto_now_add=True)
    kyc_submitted = models.BooleanField(default=False)
    kyc_confirmed = models.BooleanField(default=False)
    recommended_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="recommended_by")
    review = models.CharField(max_length=100, null=True, blank=True, default="Review")
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.user}"
    
    
class KYC(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    account =  models.OneToOneField(Account, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="kyc", default="default.jpg")
    marrital_status = models.CharField(choices=MARITAL_STATUS, max_length=40)
    gender = models.CharField(choices=GENDER, max_length=40)
    identity_type = models.CharField(choices=IDENTITY_TYPE, max_length=140)
    identity_image = models.ImageField(upload_to="kyc", null=True, blank=True)
    date_of_birth = models.DateTimeField(auto_now_add=False)
    signature = models.ImageField(upload_to="kyc")

    # Address
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    # Contact Detail
    mobile = models.CharField(max_length=1000)
    fax = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
        


    def __str__(self):
        return f"{self.user}"    

        
    class Meta:
        ordering = ['-date']

    
def create_account(sender, instance, created, **kwargs):
    #**kwargs allows us to pass a variable number of keyword arguments 
    # to a Python function. In the function, we use the double-asterisk 
    # (**) before the parameter name to denote this type of argument
    # EXAMPLE
    # def total_fruits(**kwargs):
    #     print(kwargs, type(kwargs))

    # total_fruits(banana=5, mango=7, apple=8)
    if created:
        Account.objects.create(user=instance)
            
def save_account(sender, instance,**kwargs):
    instance.account.save()
    
#post_save helps to save a user acount object whenevr a user signs up on our platform
post_save.connect(create_account, sender=User)
post_save.connect(save_account, sender=User)