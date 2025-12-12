# form_filler/forms.py

from django import forms

class AxisBankForm(forms.Form):
    """
    Form for collecting data to fill the Axis Bank RTGS/NEFT/IMPS form.
    Each field corresponds to a placeholder in the Word document.
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
        label="Date (e.g., 27 June 2025)",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})
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
        return ifsc_code
