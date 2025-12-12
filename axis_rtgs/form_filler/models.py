"""from django.db import models

class Remitter(models.Model):
    account_number = models.CharField(max_length=50)  # Remitter's Account Number
    name = models.CharField(max_length=100)  # Remitter Name
    lei_code = models.CharField(max_length=30, blank=True, null=True)  # Remitter LEI Code
    address = models.TextField()  # Remitter Address
    cheque_number = models.CharField(max_length=30)  # Cheque Number
    mobile_number = models.CharField(max_length=15)  # Mobile/Other Number
    other_number = models.CharField(max_length=15, blank=True, null=True)  # Other Number
    branch = models.CharField(max_length=255)  
    pan_no = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return f"{self.name} - {self.account_number}"
"""
from django.db import models

class AxisBankRemitter(models.Model):
    account_number = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=11)
    address = models.TextField()
    cheque_number = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=15)
    other_number = models.CharField(max_length=15, blank=True, null=True)
    branch = models.CharField(max_length=255)
    pan_no = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.account_number}"
    

from django.db import models

class AxisBankBeneficiary(models.Model):
    unique_code = models.CharField(max_length=6, blank=True, null=True)
    name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=255)
    bank_address = models.TextField(blank=True, null=True)
    # lei_code = models.CharField(max_length=50, blank=True, null=True)
    ifsc_code = models.CharField(max_length=20)
    # transaction_amount = models.DecimalField(
    #     max_digits=15,
    #     decimal_places=2,
    #     null=True,      # allow blank for existing records
    #     blank=True
    # )
    def __str__(self):
        return f"{self.name} ({self.account_number})"


class UnionBankRemitter(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    pan_number = models.CharField(max_length=10, blank=True, null=True)
    cheque_number = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    other_number = models.CharField(max_length=15, blank=True, null=True)
    # Add any other Union Bank specific fields here if needed

    def __str__(self):
        return f"{self.name} - {self.account_number or 'No Account'}"



class RemitterAccount(models.Model):
    unique_code = models.CharField(max_length=6)  # ✅ add this line
    bank_name = models.CharField(max_length=100)
    remitter_account_number = models.CharField(max_length=50)
    remitter_name = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    pan_no = models.CharField(max_length=10, blank=True, null=True)
    ifsc_code = models.CharField(max_length=25)
    remitter_address = models.TextField(blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    other_number = models.CharField(max_length=20, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.remitter_name} - {self.bank_name}"



from django.db import models
import uuid
from django.contrib.auth.hashers import make_password

from django.db import models
import uuid

class SignUp(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=255)  # Plain text (⚠️ for testing only)
    unique_code = models.CharField(max_length=6, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk and not self.unique_code:
            self.unique_code = uuid.uuid4().hex[:6].upper()

        # No password hashing!
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


