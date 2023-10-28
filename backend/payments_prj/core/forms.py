from django import forms
from core.models import CreditCard, Loan
from django.forms import ImageField, FileInput, DateInput

class CreditCardForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Card Holder Name"}))
    number = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Card Number"}))
    month = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"MM"}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"YY"}))
    cvv = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"CVV"}))

    class Meta:
        model = CreditCard
        fields = ['name', 'number', 'month', 'year', 'cvv', 'card_type']

# class AmountForm(forms.ModelForm):
#     amount = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"$30"}))
    
#     class Meta:
#         model = CreditCard
#         fields = ['amount']

class LoanForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Loan Holder Name"}))
    payslip = ImageField(widget=FileInput)
    credit_report = ImageField(widget=FileInput)
        
    class Meta:
        model = Loan
        fields = ['full_name','loan_amount', 'loan_term', 'payslip', 'credit_report', 'loan_type']
        widgets = {
            "loan_amount" :  forms.NumberInput(attrs={"placeholder":"Loan Amount"}),
            "loan_term" : forms.NumberInput(attrs={"placeholder":"No of months to pay"})
        }
