from django.forms import ModelForm
from .models import *
from django.utils.translation import gettext_lazy as _
from django import forms


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields=['customer','status']
         
class UserUpdate(ModelForm):
    class Meta:
        model = Customer
        fields=['fname','lname','email','u_phone','profile']
        labels = {
            'fname':_('First Name',),
            'lname':_('Last Name',),
            'email':_('Email ID',),
            'u_phone':_('Mobile Number',),
            'profile':_('Profile Picture',),
        }
        help_texts = {
            'fname': _('Cannot contain Numbers or Special Characters'),
            'lname': _('Cannot contain Numbers or Special Characters'),
            'email': _('Enter valid personal email address'),
            'u_phone': _('10 digit Mobile Number'),
        }

class Shipping(ModelForm):
    class Meta:
        model = Delivery
        fields=['dno','street','locality','pincode']
        labels = {
            'dno':_('Flat/Door Number',),
            'street':_('Street',),
            'locality':_('Locality',),
            'pincode':_('Pincode',),
        }
        help_texts = {
            'locality': _('Adding a landmark would be Helpful'),
        }

class SellerUpdate(ModelForm):
    class Meta:
        model = Seller
        fields=['fname','lname','company','email','s_phone','description','image', 'pswd', 'conf_pswd']
        labels = {
            'fname':_('First Name',),
            'lname':_('Last Name',),
            'company':_('Company',),
            'email':_('Email ID',),
            's_phone':_('Mobile Number',),
            'description':_('Description',),
            'image':_('Business Logo',),
            'pswd': _('Password'),
            'conf_pswd': _('Confirm Password')
        }
        help_texts = {
            'fname': _('Cannot contain Numbers or Special Characters'),
            'lname': _('Cannot contain Numbers or Special Characters'),
            'email': _('Enter valid personal email address'),
            's_phone': _('10 digit Mobile Number'),
            'description': _('Enter a short description of your business'),
            'pswd': _('A strong password is at least 6 characters long & has uppercase, lowercase, numbers and special characters'),
            'conf_pswd': _('Ensure that the same password is entered')
        }
        widgets = {
            'pswd': forms.PasswordInput(),
            'conf_pswd': forms.PasswordInput()
        }

class CustLogin(ModelForm):
    class Meta:
        model = Customer
        fields = ['email', 'pswd']
        widgets = {
            'pswd': forms.PasswordInput()
        }
        labels = {
            'email': _('Email ID'),
            'pswd': _('Password'),
        }

class SellerLogin(ModelForm):
    class Meta:
        model = Seller
        fields = ['email', 'pswd']
        widgets = {
            'pswd': forms.PasswordInput()
        }
        labels = {
            'email': _('Email ID'),
            'pswd': _('Password'),
        }

class CustRegister(ModelForm):
    # User.is_customer = True
    class Meta:
        model = Customer
        fields = ['fname', 'lname', 'email', 'u_phone', 'pswd', 'conf_pswd']
        labels = {
            'fname': _('First Name'),
            'lname': _('Last Name'),
            'email': _('Email'),
            'u_phone': _('Mobile'),
            'pswd': _('Password'),
            'conf_pswd': _('Confirm Password')
        }
        help_texts = {
            'fname': _('Cannot contain Numbers or Special Characters'),
            'lname': _('Cannot contain Numbers or Special Characters'),
            'email': _('Enter valid personal email address'),
            'u_phone': _('10 digit Mobile Number'),
            'pswd': _('A strong password is at least 6 characters long & has uppercase, lowercase, numbers and special characters'),
            'conf_pswd': _('Ensure that the same password is entered')
        }
        widgets = {
            'pswd': forms.PasswordInput(),
            'conf_pswd': forms.PasswordInput()
        }

class SellRegister(ModelForm):
    # User.is_seller = True
    class Meta:
        model = Seller
        fields = ['fname', 'lname', 'company', 'address', 'locality', 'email', 's_phone', 'description', 'pswd', 'conf_pswd']
        labels ={
            'fname': _('First Name'),
            'lname': _('Last Name'),
            'email': _('Email'),
            's_phone': _('Mobile'),
            'company': _('Company Name'),
            'address': _('Address'),
            'locality': _('Locality'),
            'description': _('Description'),
            'pswd': _('Password'),
            'conf_pswd': _('Confirm Password')
        }
        help_texts = {
            'fname': _('Cannot contain Numbers or Special Characters'),
            'lname': _('Cannot contain Numbers or Special Characters'),
            'email': _('Enter valid personal email address'),
            's_phone': _('10 digit Mobile Number'),
            'company': _('Company Name'),
            'address': _('Location of Business'),
            'locality': _('Locality of Business'),
            'description': _('Short Description of Business'),
            'pswd': _('A strong password is at least 6 characters long & has uppercase, lowercase, numbers and special characters'),
            'conf_pswd': _('A strong password is at least 6 characters long & has uppercase, lowercase, numbers and special characters')
        }
        widgets = {
            'pswd': forms.PasswordInput(),
            'conf_pswd': forms.PasswordInput()
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description']
        labels = {
            'name': _('Product Name'),
            'price': _('Price per item'),
            'category': _('Category'),
            'description': _('Description')
        }


class ProductUpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description']
        labels = {
            'name': _('Product Name'),
            'price': _('Price per item'),
            'category': _('Category'),
            'description': _('Description')
        }

class StatusUpdate(ModelForm):
    class Meta:
        model = Order
        fields = ['status']
        labels = {
            'status': _('Status')
        }
