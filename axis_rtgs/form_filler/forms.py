"""# form_filler/forms.py

from django import forms

class AxisBankForm(forms.Form):
    """
    #Form for collecting data to fill the Axis Bank RTGS/NEFT/IMPS form.
    #Each field corresponds to a placeholder in the Word document.
"""
    date = forms.CharField(
        label="Date (e.g., 27 June 2025)",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})
    )
    branch = forms.CharField(
        label="branch",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})
    )
    pan_no = forms.CharField(
        label="PAN Number",
        max_length=10,
        required=False, # PAN might not always be mandatory for all transactions
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})
    )
    remitter_account_number = forms.CharField(
        label="Remitter's Account Number",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})
    )
    remitter_name = forms.CharField(
        label="remitter_name",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})
    )
    remitter_LEI_code = forms.CharField(
        label="remitter_LEI_code",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})
    )
    beneficiary_LEI_code = forms.CharField(
        label="Beneficiary LEI Code",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})
    )
    remiter_address = forms.CharField(
        label="remiter_address",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})
    )
    beneficiary_bank_address = forms.CharField(
    label="Beneficiary Bank Address",
    max_length=255,
    required=True,  # or False if optional
    widget=forms.TextInput(attrs={
        'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
    })
)

    cheque_number = forms.CharField(
        label="Cheque Number",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})
    )
    cheque_date = forms.CharField(
    label="Cheque Date (e.g., 27 June 2025)",
    max_length=100,
    required=False,
    widget=forms.TextInput(attrs={
        'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
        'placeholder': 'e.g., 27 June 2025'
    })
)


    mobile_number = forms.CharField(
        label="Mobile/Other Number",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})
    )
    other_number = forms.CharField(
        label="Other Number",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})
    )
    beneficiary_name = forms.CharField(
        label="Beneficiary's Name",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})
    )
    beneficiary_account_number = forms.CharField(
        label="Beneficiary Account Number",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})
    )
    beneficiary_bank_name = forms.CharField(
        label="Beneficiary Bank Name",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})
    )
    beneficiary_bank_ifsc_code = forms.CharField(
        label="Beneficiary Bank IFSC Code",
        max_length=11,
        required=True,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})
    )
    transaction_amount = forms.DecimalField(
        label="Transaction Amount (e.g., 1000.00)",
        max_digits=15,
        decimal_places=2,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})
    )
    
    sender_to_receiver_information = forms.CharField(
        label="Sender to Receiver Information (Optional)",
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'rows': 3})
    )

    def clean_beneficiary_account_number(self):
        # Basic validation: ensure it's digits only. More complex validation can be added.
        account_number = self.cleaned_data['beneficiary_account_number']
        if not account_number.isdigit():
            raise forms.ValidationError("Beneficiary Account Number must contain only digits.")
        return account_number

    def clean_beneficiary_bank_ifsc_code(self):
        # Basic IFSC code validation: 11 alphanumeric characters.
        ifsc_code = self.cleaned_data['beneficiary_bank_ifsc_code']
        if len(ifsc_code) != 11 or not ifsc_code.isalnum():
            raise forms.ValidationError("IFSC Code must be 11 alphanumeric characters.")
        return ifsc_code"""




# import datetime
# from django import forms
# from django.forms.widgets import DateInput

# class AxisBankForm(forms.Form):
#     """
#     Form for collecting data to fill the Axis Bank RTGS/NEFT/IMPS form.
#     Each field corresponds to a placeholder in the Word document.
#     """

#     date = forms.DateField(
#         label="Date",
#         required=True,
#         initial=datetime.date.today,
#         widget=DateInput(attrs={
#             'type': 'date',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

    

#     remitter_account_number = forms.CharField(
#         label="Remitter's Account Number",
#         max_length=50,
#         required=True,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
#     remitter_name = forms.CharField(
#         label="Remitter Name",
#         max_length=255,
#         required=True,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )


#     branch = forms.CharField(
#         label="Branch",
#         max_length=255,
#         required=True,
#         widget=forms.TextInput(attrs={ 
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     pan_no = forms.CharField(
#         label="PAN Number",
#         max_length=10,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     remitter_LEI_code = forms.CharField(
#         label="Remitter LEI Code",
#         max_length=255,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

    

#     remitter_address = forms.CharField(
#         label="Remitter Address",
#         max_length=255,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

    

#     cheque_number = forms.CharField(
#         label="Cheque Number",
#         max_length=20,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     cheque_date = forms.DateField(
#         label="Cheque Date",
#         required=False,
#         widget=DateInput(attrs={
#             'type': 'date',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     mobile_number = forms.CharField(
#         label="Mobile/Other Number",
#         max_length=20,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     other_number = forms.CharField(
#         label="Other Number",
#         max_length=20,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
#     beneficiary_account_number = forms.CharField(
#         label="Beneficiary Account Number",
#         max_length=50,
#         required=True,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
#     beneficiary_name = forms.CharField(
#         label="Beneficiary's Name",
#         max_length=255,
#         required=True,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
    
#     beneficiary_LEI_code = forms.CharField(
#         label="Beneficiary LEI Code",
#         max_length=255,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

    
#     beneficiary_bank_address = forms.CharField(
#         label="Beneficiary Bank Address",
#         max_length=255,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     beneficiary_bank_name = forms.CharField(
#         label="Beneficiary Bank Name",
#         max_length=255,
#         required=True,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     beneficiary_bank_ifsc_code = forms.CharField(
#         label="Beneficiary Bank IFSC Code",
#         max_length=11,
#         required=True,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     transaction_amount = forms.DecimalField(
#         label="Transaction Amount (e.g., 1000.00)",
#         max_digits=15,
#         decimal_places=2,
#         required=True,
#         widget=forms.NumberInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     sender_to_receiver_information = forms.CharField(
#         label="Sender to Receiver Information (Optional)",
#         max_length=500,
#         required=False,
#         widget=forms.Textarea(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
#             'rows': 3
#         })
#     )

#     def clean_beneficiary_account_number(self):
#         account_number = self.cleaned_data['beneficiary_account_number']
#         if not account_number.isdigit():
#             raise forms.ValidationError("Beneficiary Account Number must contain only digits.")
#         return account_number

#     def clean_beneficiary_bank_ifsc_code(self):
#         ifsc_code = self.cleaned_data['beneficiary_bank_ifsc_code']
#         if len(ifsc_code) != 11 or not ifsc_code.isalnum():
#             raise forms.ValidationError("IFSC Code must be 11 alphanumeric characters.")
#         return ifsc_code




import datetime
import re
from django import forms
from django.forms.widgets import DateInput


class AxisBankForm(forms.Form):
    """
    Form for collecting data to fill the Axis Bank RTGS/NEFT/IMPS form.
    Each field corresponds to a placeholder in the Word document.
    """

    # -------------------- Date --------------------
    date = forms.DateField(
        label="Date",
        required=True,
        initial=datetime.date.today(),  # ✅ Fixed: added ()
        widget=DateInput(attrs={
            'type': 'date',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    # -------------------- Remitter Details --------------------
    remitter_account_number = forms.CharField(
        label="Remitter's Account Number",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter remitter account number',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    remitter_name = forms.CharField(
        label="Remitter Name",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter remitter name',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    branch = forms.CharField(
        label="Branch",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter branch name',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    pan_no = forms.CharField(
        label="PAN Number",
        max_length=10,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'ABCDE1234F',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 uppercase'
        })
    )

    remitter_LEI_code = forms.CharField(
        label="Remitter LEI Code",
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter LEI code (if applicable)',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    remitter_address = forms.CharField(
        label="Remitter Address",
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter remitter address',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    # -------------------- Cheque Details --------------------
    cheque_number = forms.CharField(
        label="Cheque Number",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter cheque number (if applicable)',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    cheque_date = forms.DateField(
        label="Cheque Date",
        required=False,
        widget=DateInput(attrs={
            'type': 'date',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    # -------------------- Contact Details --------------------
    mobile_number = forms.CharField(
        label="Mobile Number",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter mobile number',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    alternate_contact_number = forms.CharField(
        label="Alternate Contact Number",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter alternate number (optional)',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    # -------------------- Beneficiary Details --------------------
    beneficiary_account_number = forms.CharField(
        label="Beneficiary Account Number",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter beneficiary account number',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    beneficiary_name = forms.CharField(
        label="Beneficiary Name",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter beneficiary name',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    beneficiary_LEI_code = forms.CharField(
        label="Beneficiary LEI Code",
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter LEI code (if applicable)',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    beneficiary_bank_address = forms.CharField(
        label="Beneficiary Bank Address",
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter bank address (optional)',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    beneficiary_bank_name = forms.CharField(
        label="Beneficiary Bank Name",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter bank name',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    beneficiary_bank_ifsc_code = forms.CharField(
        label="Beneficiary Bank IFSC Code",
        max_length=11,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter IFSC code (11 chars)',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 uppercase'
        })
    )

    # -------------------- Transaction Details --------------------
    transaction_amount = forms.DecimalField(
        label="Transaction Amount (e.g., 1000.00)",
        max_digits=15,
        decimal_places=2,
        required=True,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter transaction amount',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    sender_to_receiver_information = forms.CharField(
        label="Sender to Receiver Information (Optional)",
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter any notes or instructions',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
            'rows': 3
        })
    )

    # -------------------- Custom Validations --------------------
    def clean_beneficiary_account_number(self):
        account_number = self.cleaned_data['beneficiary_account_number']
        if not account_number.isdigit():
            raise forms.ValidationError("Beneficiary Account Number must contain only digits.")
        return account_number

    def clean_beneficiary_bank_ifsc_code(self):
        ifsc_code = self.cleaned_data['beneficiary_bank_ifsc_code'].upper()
        if len(ifsc_code) != 11 or not ifsc_code.isalnum():
            raise forms.ValidationError("IFSC Code must be 11 alphanumeric characters.")
        return ifsc_code

    def clean_transaction_amount(self):
        amount = self.cleaned_data['transaction_amount']
        if amount <= 0:
            raise forms.ValidationError("Transaction amount must be greater than zero.")
        return amount

    # def clean_pan_no(self):
    #     pan = self.cleaned_data.get('pan_no')
    #     if pan and not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', pan.upper()):
    #         raise forms.ValidationError("Invalid PAN format (e.g., ABCDE1234F).")
    #     return pan
    




# from django import forms
# from django import forms

# class UnionBankForm(forms.Form):
#     branch = forms.CharField(
#         label="Branch",
#         max_length=255,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
#     transaction_reference_no = forms.CharField(
#         label="Transaction Reference No.",
#         max_length=100,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
#     account_number = forms.CharField(
#         label="Account Number",
#         max_length=50,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
#     beneficiary_name = forms.CharField(
#         label="Beneficiary Name",
#         max_length=255,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
    
#     beneficiary_branch_name = forms.CharField(
#         label="Beneficiary Branch Name",
#         max_length=255,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
#     beneficiary_branch_address = forms.CharField(
#         label="Beneficiary Branch Address",
#         max_length=500,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
#     beneficiary_ifsc = forms.CharField(
#         label="IFSC Code",
#         max_length=11,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     date_of_remittance = forms.CharField(
#         label="Date of Remittance (e.g., 27 June 2025)",
#         max_length=50,
#         widget=DateInput(attrs={
#             'type': 'date',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
#     account_type = forms.CharField(
#         label="Account Type",
#         max_length=50,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
    
#     beneficiary_address = forms.CharField(
#         label="Beneficiary Address",
#         max_length=500,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
#     remitter_account_number = forms.CharField(
#         label="Remitter Account Number",
#         max_length=50,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
#     remitter_name = forms.CharField(
#         label="Remitter Name",
#         max_length=50,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
    
#     pan_number = forms.CharField(
#         label="PAN Number",
#         max_length=10,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
#     mobile_number = forms.CharField(
#         label="Mobile Number",
#         max_length=20,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
#     amount = forms.DecimalField(
#         label="Amount (e.g., 1000.00)",
#         max_digits=15,
#         decimal_places=2,
#         widget=forms.NumberInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
#     payment_mode = forms.CharField(
#         label="Mode of Payment",
#         max_length=100,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
#     cheque_number = forms.CharField(
#         label="Cheque Number",
#         max_length=20,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
#     cheque_date = forms.CharField(
#         label="Cheque Date (e.g., 27 June 2025)",
#         max_length=50,
#         required=False,
#         widget=DateInput(attrs={
#             'type': 'date',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )
#     remitter_address = forms.CharField(
#         label="Remitter Address",
#         max_length=500,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     def clean_account_number(self):
#         acc = self.cleaned_data.get('account_number')
#         if not acc.isdigit():
#             raise forms.ValidationError("Account number must contain only digits.")
#         return acc

#     def clean_beneficiary_ifsc(self):
#         code = self.cleaned_data.get('beneficiary_ifsc')
#         if len(code) != 11 or not code.isalnum():
#             raise forms.ValidationError("IFSC Code must be exactly 11 alphanumeric characters.")
#         return code



# import datetime
# import re
# from django import forms
# from django.forms.widgets import DateInput


# class UnionBankForm(forms.Form):
#     # -------------------- Date --------------------
#     date_of_remittance = forms.DateField(
#         label="Date of Remittance",
#         required=True,
#         initial=datetime.date.today(),
#         widget=DateInput(attrs={
#             'type': 'date',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     # -------------------- Remitter Details --------------------
#     remitter_account_number = forms.CharField(
#         label="Remitter Account Number",
#         max_length=50,
#         required=True,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Enter remitter account number',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     remitter_name = forms.CharField(
#         label="Remitter Name",
#         max_length=255,
#         required=True,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Enter remitter name',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     remitter_address = forms.CharField(
#         label="Remitter Address",
#         max_length=500,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Enter remitter address',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     pan_number = forms.CharField(
#         label="PAN Number",
#         max_length=10,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'ABCDE1234F',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 uppercase'
#         })
#     )

#     mobile_number = forms.CharField(
#         label="Mobile Number",
#         max_length=20,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Enter mobile number',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     cheque_number = forms.CharField(
#         label="Cheque Number",
#         max_length=20,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Enter cheque number (if applicable)',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     cheque_date = forms.DateField(
#         label="Cheque Date",
#         required=False,
#         widget=DateInput(attrs={
#             'type': 'date',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     # -------------------- Beneficiary Details --------------------
#     beneficiary_account_number = forms.CharField(
#         label="Beneficiary Account Number",
#         max_length=50,
#         required=True,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Enter beneficiary account number',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     beneficiary_name = forms.CharField(
#         label="Beneficiary Name",
#         max_length=255,
#         required=True,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Enter beneficiary name',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     beneficiary_branch_name = forms.CharField(
#         label="Beneficiary Branch Name",
#         max_length=255,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Enter branch name',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     beneficiary_branch_address = forms.CharField(
#         label="Beneficiary Branch Address",
#         max_length=500,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Enter branch address',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     beneficiary_ifsc = forms.CharField(
#         label="IFSC Code",
#         max_length=11,
#         required=True,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Enter IFSC code (11 chars)',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 uppercase'
#         })
#     )

#     # -------------------- Transaction Details --------------------
#     amount = forms.DecimalField(
#         label="Transaction Amount",
#         max_digits=15,
#         decimal_places=2,
#         required=True,
#         widget=forms.NumberInput(attrs={
#             'placeholder': 'Enter transaction amount',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     payment_mode = forms.CharField(
#         label="Mode of Payment",
#         max_length=100,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Enter payment mode',
#             'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
#         })
#     )

#     # -------------------- Custom Validations --------------------
#     def clean_remitter_account_number(self):
#         acc = self.cleaned_data.get('remitter_account_number')
#         if not acc.isdigit():
#             raise forms.ValidationError("Remitter account number must contain only digits.")
#         return acc

#     def clean_beneficiary_account_number(self):
#         acc = self.cleaned_data.get('beneficiary_account_number')
#         if not acc.isdigit():
#             raise forms.ValidationError("Beneficiary account number must contain only digits.")
#         return acc

#     def clean_pan_number(self):
#         pan = self.cleaned_data.get('pan_number')
#         if pan and not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', pan.upper()):
#             raise forms.ValidationError("Invalid PAN format (e.g., ABCDE1234F).")
#         return pan

#     def clean_beneficiary_ifsc(self):
#         code = self.cleaned_data.get('beneficiary_ifsc')
#         if len(code) != 11 or not code.isalnum():
#             raise forms.ValidationError("IFSC Code must be exactly 11 alphanumeric characters.")
#         return code

#     def clean_amount(self):
#         amt = self.cleaned_data.get('amount')
#         if amt <= 0:
#             raise forms.ValidationError("Transaction amount must be greater than zero.")
#         return amt





import datetime
import re
from django import forms
from django.forms.widgets import DateInput


class UnionBankForm(forms.Form):
    # -------------------- General Details --------------------
    date_of_remittance = forms.DateField(
        label="Date of Remittance",
        required=True,
        initial=datetime.date.today,
        widget=DateInput(attrs={
            'type': 'date',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    # -------------------- Remitter Details --------------------
    remitter_account_number = forms.CharField(
        label="Remitter Account Number",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter remitter account number',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    remitter_name = forms.CharField(
        label="Remitter Name",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter remitter name',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    remitter_address = forms.CharField(
        label="Remitter Address",
        max_length=500,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter remitter address',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    pan_number = forms.CharField(
        label="PAN Number",
        max_length=10,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'ABCDE1234F',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 uppercase'
        })
    )

    mobile_number = forms.CharField(
        label="Mobile Number",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter mobile number',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    cheque_number = forms.CharField(
        label="Cheque Number",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter cheque number (if applicable)',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    cheque_date = forms.DateField(
        label="Cheque Date",
        required=False,
        widget=DateInput(attrs={
            'type': 'date',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    # -------------------- Beneficiary Details --------------------
    beneficiary_account_number = forms.CharField(
        label="Beneficiary Account Number",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter beneficiary account number',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    beneficiary_name = forms.CharField(
        label="Beneficiary Name",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter beneficiary name',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    beneficiary_branch_name = forms.CharField(
        label="Beneficiary Branch Name",
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter branch name',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    beneficiary_branch_address = forms.CharField(
        label="Beneficiary Branch Address",
        max_length=500,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter branch address',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    beneficiary_ifsc = forms.CharField(
        label="IFSC Code",
        max_length=11,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter IFSC code (11 chars)',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 uppercase'
        })
    )

    # -------------------- Transaction Details --------------------
    amount = forms.DecimalField(
        label="Transaction Amount",
        max_digits=15,
        decimal_places=2,
        required=True,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter transaction amount',
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    # payment_mode = forms.CharField(
    #     label="Mode of Payment",
    #     max_length=100,
    #     required=False,
    #     widget=forms.TextInput(attrs={
    #         'placeholder': 'Enter payment mode',
    #         'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
    #     })
    # )

    # -------------------- Custom Validations --------------------
    def clean_remitter_account_number(self):
        acc = self.cleaned_data.get('remitter_account_number')
        if not acc.isdigit():
            raise forms.ValidationError("Remitter account number must contain only digits.")
        return acc

    def clean_beneficiary_account_number(self):
        acc = self.cleaned_data.get('beneficiary_account_number')
        if not acc.isdigit():
            raise forms.ValidationError("Beneficiary account number must contain only digits.")
        return acc

    # def clean_pan_number(self):
    #     pan = self.cleaned_data.get('pan_number')
    #     if pan and not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', pan.upper()):
    #         raise forms.ValidationError("Invalid PAN format (e.g., ABCDE1234F).")
    #     return pan

    def clean_beneficiary_ifsc(self):
        code = self.cleaned_data.get('beneficiary_ifsc')
        if len(code) != 11 or not code.isalnum():
            raise forms.ValidationError("IFSC Code must be exactly 11 alphanumeric characters.")
        return code

    def clean_amount(self):
        amt = self.cleaned_data.get('amount')
        if amt <= 0:
            raise forms.ValidationError("Transaction amount must be greater than zero.")
        return amt
