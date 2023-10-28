from django.shortcuts import render, redirect
from account.models import KYC, Account
from account.forms import KYCForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required # ensures that user cannot access page if not logged in
from core.forms import CreditCardForm, LoanForm
from core.models import CreditCard, Transaction, Notification, Loan



# @login_required #user must be logged in before they can access page. Have commended this because i have the "..user.is.authenticated"
def account(request):
    if request.user.is_authenticated:
        try:
                kyc = KYC.objects.get(user=request.user)
        except:
                messages.warning(request, "You need to submit your kyc")
                return redirect("account:kyc-reg") 
            
        account = Account.objects.get(user=request.user)
    else:
        messages.warning(request, "You need to login to access the dashboard")
        return redirect("userauths:sign-in")
    
    context = {
        "kyc":kyc,
        "account":account,
    }

    return render(request, "account/account.html", context)


@login_required
def kyc_registration(request):
    user = request.user
    account = Account.objects.get(user=user)

    try:
        kyc = KYC.objects.get(user=user)
    except:
        kyc = None
    
    if request.method == "POST":
        form = KYCForm(request.POST, request.FILES, instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(request, "KYC Form submitted successfully, In review now.")
            return redirect("core:index")
    else:
        form = KYCForm(instance=kyc)
    context = {
        "account": account,
        "form": form,
        "kyc": kyc,
    }
    return render(request, "account/kyc-form.html", context)

# @login_required
# def loan_registration(request):
#     user = request.user
#     account = Account.objects.get(user=user)

#     try:
#         kyc = KYC.objects.get(user=user)
#     except:
#         kyc = None
    
#     if request.method == "POST":
#         form = KYCForm(request.POST, request.FILES, instance=kyc)
#         if form.is_valid():
#             new_form = form.save(commit=False)
#             new_form.user = user
#             new_form.account = account
#             new_form.save()
#             messages.success(request, "KYC Form submitted successfully, In review now.")
#             return redirect("core:index")
#     else:
#         form = KYCForm(instance=kyc)
#     context = {
#         "account": account,
#         "form": form,
#         "kyc": kyc,
#     }
#     return render(request, "account/kyc-form.html", context)

def dashboard(request):
    if request.user.is_authenticated:
        try:
            kyc = KYC.objects.get(user=request.user)
        except:
            messages.warning(request, "You need to submit your kyc")
            return redirect("account:kyc-reg")
        
        recent_transfer = Transaction.objects.filter(sender=request.user, transaction_type="transfer", status="completed").order_by("-id")[:1]
        recent_recieved_transfer = Transaction.objects.filter(reciever=request.user, transaction_type="transfer").order_by("-id")[:1]


        sender_transaction = Transaction.objects.filter(sender=request.user, transaction_type="transfer").order_by("-id")
        reciever_transaction = Transaction.objects.filter(reciever=request.user, transaction_type="transfer").order_by("-id")

        request_sender_transaction = Transaction.objects.filter(sender=request.user, transaction_type="request")
        request_reciever_transaction = Transaction.objects.filter(reciever=request.user, transaction_type="request")
        
        
        account = Account.objects.get(user=request.user)
        loans = Loan.objects.filter(user=request.user).order_by("-id")
        # loans = Loan.objects.get(user=request.user)
        credit_card = CreditCard.objects.filter(user=request.user).order_by("-id")
        notifications = Notification.objects.filter(user=request.user)
        # try:
        #     loans = PersonalLoan.objects.get(user=request.user)
        # except:
        #     loans = None

        if request.method == "POST":
            form = LoanForm(request.POST, request.FILES)
            # form = LoanForm(request.POST, request.FILES, instance=loans)
            # form = KYCForm(request.POST, request.FILES, instance=kyc)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.user = request.user 
                new_form.save()
                
                Notification.objects.create(
                    user=request.user,
                    notification_type="Applied for a Loan"
                )
                
                loan_id = new_form.loan_id
                messages.success(request, "Loan Application added successfully.")
                return redirect("account:dashboard")
        else:
            form = LoanForm()
            
        
    else:
        messages.warning(request, "You need to login to access the dashboard")
        return redirect("userauths:sign-in")

    #notifications = Notification(user=request.user)
    # loans = Loan.objects.filter(user=request.user).order_by("-id")
    context = {
        "kyc":kyc,
        "account":account,
        "form":form,
        "loans": loans,
        "credit_card":credit_card,
         "notifications": notifications,
        "sender_transaction":sender_transaction,
        "reciever_transaction":reciever_transaction,

        'request_sender_transaction':request_sender_transaction,
        'request_reciever_transaction':request_reciever_transaction,
        'recent_transfer':recent_transfer,
        'recent_recieved_transfer':recent_recieved_transfer,
       
    }
    return render(request, "account/dashboard.html", context)
    
