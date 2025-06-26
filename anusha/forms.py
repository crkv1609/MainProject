from django import forms
from .models import *

from django.utils import timezone
from datetime import timedelta


class InsuranceForm(forms.ModelForm):
    class Meta:
        model = AllInsurance
        fields = '__all__'
class genInsuranceForm(forms.ModelForm):
    class Meta:
        model = GeneralInsurance
        fields = '__all__'
class lifeInsuranceForm(forms.ModelForm):
    class Meta:
        model = LifeInsurance
        fields = '__all__'
class healthInsuranceForm(forms.ModelForm):
    class Meta:
        model = healthInsurance
        fields = '__all__'

class goldBasicDetailForm(forms.ModelForm):
    terms_accepted = forms.BooleanField(required=True, error_messages={'required': 'You must accept the terms and conditions to proceed.'})

    class Meta:
        model = goldbasicdetailform
        fields = ['fname', 'lname', 'Dob', 'phone_number', 'pan_num', 
                  'Aadhar_number', 'gender', 'email', 
                  'marital_status', 'required_loan_amount','terms_accepted']
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'pan_num': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'maxlength': '10',
                'onkeypress': 'return event.charCode >= 48 && event.charCode <= 57',
                'min': '0',
                
            }),               'Aadhar_number':forms.TextInput(attrs={'class':'form-control'}),
            'Dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'marital_status': forms.Select(attrs={'class': 'form-control'}),

            'required_loan_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'created_at':forms.DateInput(attrs={'class':'form-control',}),
            'terms_accepted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
        }
        error_messages = {
            'fname': {'required': 'Full name is required.'},
            'lname': {'required': 'Full name is required.'},
             
            'pan_num': {'required': 'Pan number is required.'},
            'phone_number':{'required':'mobilenumber is required'},
            
            'Dob': {'required': 'Date of birth is required.'},
            'required_loan_amount': {'required': 'Required loan amount is required.'},
            'terms_accepted': {'required': 'You must accept the terms and conditions to proceed.'},
        }


    def clean_phone_number(self):
        mobile_number = str(self.cleaned_data.get('phone_number'))  # Convert to string
        if not re.fullmatch(r'\d{10}', mobile_number):
           raise forms.ValidationError("Phone number must be exactly 10 digits.")        
        if goldbasicdetailform.objects.filter(phone_number=mobile_number).exists():
            record=goldbasicdetailform.objects.filter(phone_number=mobile_number).last()
            if date.today() > record.expiry_at:
                return mobile_number
            raise forms.ValidationError("Mobile Number already exist! Please try after 3Months.")
        return mobile_number
    
    def clean_pan_num(self):
        pan_num = self.cleaned_data.get('pan_num')
        if goldbasicdetailform.objects.filter(pan_num=pan_num).exists():
            record=goldbasicdetailform.objects.filter(pan_num=pan_num).last()
            if date.today() > record.expiry_at:
                return pan_num
            raise forms.ValidationError("PAN Number already exist! Please try after 3Months.")
        return pan_num

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance
    
    def clean_Aadhar_number(self):
        Aadhar_number = self.cleaned_data.get('Aadhar_number')
        if not re.match(r'^\d{12}$', Aadhar_number):
            raise ValidationError("Aadhar number must be 12 digits.")
        return Aadhar_number 

class BasicDetailForm(forms.ModelForm):
    terms_accepted = forms.BooleanField(required=True, error_messages={'required': 'You must accept the terms and conditions to proceed.'})


    class Meta:
        model = basicdetailform
        fields = ['fname', 'lname', 'Dob', 'phone_number', 'pan_num', 
                  'Aadhar_number', 'gender', 'email', 
                  'marital_status', 'required_loan_amount','terms_accepted']
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'pan_num': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'maxlength': '10',
                'onkeypress': 'return event.charCode >= 48 && event.charCode <= 57',
                'min': '0',
                
            }),               'Aadhar_number':forms.TextInput(attrs={'class':'form-control'}),
            'Dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'marital_status': forms.Select(attrs={'class': 'form-control'}),

            'required_loan_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'created_at':forms.DateInput(attrs={'class':'form-control',}),
            'terms_accepted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
        }
        error_messages = {
            'fname': {'required': 'Full name is required.'},
            'lname': {'required': 'Full name is required.'},
             
            'pan_num': {'required': 'Pan number is required.'},
            'phone_number':{'required':'mobilenumber is required'},
            
            'Dob': {'required': 'Date of birth is required.'},
            'required_loan_amount': {'required': 'Required loan amount is required.'},
            'terms_accepted': {'required': 'You must accept the terms and conditions to proceed.'},
        }

    def clean_phone_number(self):
        mobile_number = str(self.cleaned_data.get('phone_number'))  # Convert to string
        if not re.fullmatch(r'\d{10}', mobile_number):
           raise forms.ValidationError("Phone number must be exactly 10 digits.")        
        if basicdetailform.objects.filter(phone_number=mobile_number).exists():
            record=basicdetailform.objects.filter(phone_number=mobile_number).last()
            if date.today() > record.expiry_at:
                return mobile_number
            raise forms.ValidationError("Mobile Number already exist! Please try after 3Months.")
        return mobile_number
    
    def clean_pan_num(self):
        pan_num = self.cleaned_data.get('pan_num')
        if basicdetailform.objects.filter(pan_num=pan_num).exists():
            record=basicdetailform.objects.filter(pan_num=pan_num).last()
            if date.today() > record.expiry_at:
                return pan_num
            raise forms.ValidationError("PAN Number already exist! Please try after 3Months.")
        return pan_num

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance

    def clean_Aadhar_number(self):
        Aadhar_number = self.cleaned_data.get('Aadhar_number')
        if not re.match(r'^\d{12}$', Aadhar_number):
            raise ValidationError("Aadhar number must be 12 digits.")
        return Aadhar_number    

class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = '__all__'
        exclude=['basic_detail']
        
        
        def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.fields['have_gst_certificate'].label = "Do you have GST certificate?"
           self.fields['gst_number'].label = "GST Number (if available)"
        widgets = {
            'loan_type': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'pan_card_number': forms.TextInput(attrs={'class': 'form-control'}),
            'aadhar_card_number': forms.TextInput(attrs={'class': 'form-control'}),
            'marital_status': forms.Select(attrs={'class': 'form-control'}),
            'email_id': forms.EmailInput(attrs={'class': 'form-control'}),
            'current_address_type': forms.Select(attrs={'class': 'form-control'}),

            'current_address': forms.Textarea(attrs={'class': 'form-control','rows':3}),
            'current_address_pincode': forms.TextInput(attrs={'class': 'form-control'}),
            'aadhar_address_type': forms.Select(attrs={'class': 'form-control'}),

            'aadhar_address': forms.Textarea(attrs={'class': 'form-control','rows':3}),
            'aadhar_pincode': forms.TextInput(attrs={'class': 'form-control'}),
            'income_source': forms.Select(attrs={'class': 'form-control'}),
            'net_salary_per_month': forms.NumberInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_type': forms.TextInput(attrs={'class': 'form-control'}),
            'job_joining_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'job_location': forms.TextInput(attrs={'class': 'form-control'}),
            'total_job_experience': forms.NumberInput(attrs={'class': 'form-control'}),
            # Business fields
            'net_income_per_month': forms.NumberInput(attrs={'class': 'form-control'}),
            'business_name': forms.TextInput(attrs={'class': 'form-control'}),
            'business_type': forms.Select(attrs={'class': 'form-control'}),
            'business_establishment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gst_certificate': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'gst_number': forms.TextInput(attrs={'class': 'form-control'}),
            'nature_of_business': forms.Textarea(attrs={'class': 'form-control','rows':3}),
            'turnover_in_lakhs_per_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'property_value': forms.NumberInput(attrs={'class': 'form-control'}),
            'required_loan_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'existing_loan': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'existing_loan_details': forms.TextInput(attrs={'class': 'form-control'}),
            'existing_loan_amount': forms.TextInput(attrs={'class': 'form-control'}),

            'ref1_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ref1_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'ref2_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ref2_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control','rows':3}),
            # Co-Applicant fields
            'co_applicant_first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'co_applicant_last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'co_applicant_gender': forms.Select(attrs={'class': 'form-control'}),
            'co_applicant_age': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'co_applicant_relationship': forms.TextInput(attrs={'class': 'form-control'}),
            'co_applicant_mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'co_applicant_email_id': forms.EmailInput(attrs={'class': 'form-control'}),
            'co_applicant_occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'co_applicant_net_income_per_month': forms.NumberInput(attrs={'class': 'form-control'}),
            

        }
    def clean_aadhar_card_number(self):
        aadhar_card_number= self.cleaned_data.get('aadhar_card_number')
        if not re.match(r'^\d{12}$', aadhar_card_number):
            raise ValidationError("Aadhar number must be 12 digits.")
        return aadhar_card_number     

    



class LapDocumentUploadForm(forms.ModelForm):
    class Meta:
        model = lapDocumentUpload
        fields = '__all__'
        exclude=['personal_details']
        widgets = {
            'adhar_card_front': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload image format'}),
            'adhar_card_back': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload image format'}),
            'pan_card': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload image format'}),
            'customer_photo': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload image format'}),
            'property_photo1': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload image format'}),
            'property_photo2': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload image format'}),
            'property_photo3': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload image format'}),
            'property_photo4': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload image format'}),
            'pay_slips_1': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload pdf format'}),
            'pay_slips_2': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload pdf format'}),

            'pay_slips_3': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload pdf format'}),

            'bank_statement': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload pdf format'}),
            'employee_id_card': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload image format'}),
            'business_proof1': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload pdf format'}),
            'business_proof2': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload pdf format'}),
            'bank_statement_12m': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload pdf format'}),
            'business_office_photo': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload image format'}),
            'itr1': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload pdf format'}),
            'itr2': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload pdf format'}),
            'itr3': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload pdf format'}),
            'address_proof': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload pdf format'}),
            'existing_loan_statement': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload pdf format'}),
            'other_document1': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload pdf format'}),
            'other_document2': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload pdf format'}),
            'other_document3': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload pdf format'}),
            'other_document4': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload pdf format'}),

            'co_applicant_adhar_card_front': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload image format'}),
            'co_applicant_adhar_card_back': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload image format'}),
            'co_applicant_pan_card': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload image format'}),
            'co_applicant_selfie_photo': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'upload image format'}),
            
     }
class goldform(forms.ModelForm):

    class Meta:
        model=Goldloanapplication
        fields='__all__'
        exclude=['goldbasicdetail']
        widgets={
            
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'Pan_number':forms.TextInput(attrs={'class': 'form-control'}),
            'Aadhar_number':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile_number':forms.TextInput(attrs={'class':'form-control'},),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'pincode':forms.TextInput(attrs={'class':'form-control'})
        }
        def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
        # Set the mobile_number field to readonly and apply Bootstrap styling
          self.fields['mobile_number'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly'
        })
    def clean_Aadhar_number(self):
        Aadhar_number = self.cleaned_data.get('Aadhar_number')
        if not re.match(r'^\d{12}$', Aadhar_number):
            raise ValidationError("Aadhar number must be 12 digits.")
        return Aadhar_number  



class OTPForm(forms.Form):
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'placeholder': 'Enter email'}))

    otp = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'placeholder': 'Enter OTP'}))

class lapApplicationVerifyForm(forms.ModelForm):
     
    class Meta:
        model=lapApplicationVerification
        fields='__all__'
        exclude=['loan','status_approved_at']

    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
       
        for field in self.fields:
            
            if not getattr(instance, field):
                setattr(instance, field, 'Pending')
        
        if 'Rejected' in self.cleaned_data.values():
            
            for field in self.fields:
                if getattr(instance, field) == 'Pending':
                    setattr(instance, field,'Rejected')
        
        if commit:
            instance.save()
        return instance
    
class DisbursementDetailsForm(forms.ModelForm):
    class Meta:
        model=disbursementdetails
        fields='__all__'
        exclude=['verification']

class OtherBasicDetailForm(forms.ModelForm):
    terms_accepted = forms.BooleanField(required=True, error_messages={'required': 'You must accept the terms and conditions to proceed.'})

    class Meta:
        model=otherbasicdetailform
        fields = ['fname', 'lname', 'Dob', 'phone_number', 'pan_num', 
                  'Aadhar_number', 'gender', 'email', 
                  'marital_status', 'comment','terms_accepted']
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'pan_num': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'maxlength': '10',
                'onkeypress': 'return event.charCode >= 48 && event.charCode <= 57',
                'min': '0',
                
            }),           
            'Aadhar_number':forms.TextInput(attrs={'class':'form-control'}),
            'Dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'marital_status': forms.Select(attrs={'class': 'form-control'}),

            'comment': forms.Textarea(attrs={'class': 'form-control','rows':5}),
            'created_at':forms.DateInput(attrs={'class':'form-control',}),
            'terms_accepted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
        }
        error_messages = {
            'fname': {'required': 'Full name is required.'},
            'lname': {'required': 'Full name is required.'},
             
            'pan_num': {'required': 'Pan number is required.'},
            'phone_number':{'required':'mobilenumber is required'},
            
            'Dob': {'required': 'Date of birth is required.'},
            'comment': {'required': 'Required loan amount is required.'},
            'terms_accepted': {'required': 'You must accept the terms and conditions to proceed.'},
        }

    def clean_phone_number(self):
        mobile_number = str(self.cleaned_data.get('phone_number'))  # Convert to string
        if not re.fullmatch(r'\d{10}', mobile_number):
           raise forms.ValidationError("Phone number must be exactly 10 digits.")        
        if otherbasicdetailform.objects.filter(phone_number=mobile_number).exists():
            record=otherbasicdetailform.objects.filter(phone_number=mobile_number).last()
            if date.today() > record.expiry_at:
                return mobile_number
            raise forms.ValidationError("Mobile Number already exist! Please try after 3Months.")
        return mobile_number
    
    def clean_pan_num(self):
        pan_num = self.cleaned_data.get('pan_num')
        if otherbasicdetailform.objects.filter(pan_num=pan_num).exists():
            record=otherbasicdetailform.objects.filter(pan_num=pan_num).last()
            if date.today() > record.expiry_at:
                return pan_num
            raise forms.ValidationError("PAN Number already exist! Please try after 3Months.")
        return pan_num

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance
    
    def clean_Aadhar_number(self):
        Aadhar_number = self.cleaned_data.get('Aadhar_number')
        if not re.match(r'^\d{12}$', Aadhar_number):
            raise ValidationError("Aadhar number must be 12 digits.")
        return Aadhar_number 

class otherloansform(forms.ModelForm):
    class Meta:
        model=otherloans
        fields='__all__'
        exclude=['otherbasicdetail']
        widgets={
            
            'Full_name':forms.TextInput(attrs={'class': 'form-control'}),
            'pan_number':forms.TextInput(attrs={'class': 'form-control'}),
            'Aadhar_number':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile_number':forms.TextInput(attrs={'class':'form-control'},),
            'date_of_birth':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'pincode':forms.TextInput(attrs={'class':'form-control'}),
            'comments':forms.Textarea(attrs={'class':'form-control'}),
            'loan_type':forms.TextInput(attrs={'class':'form-control'})


        }
    def clean_Aadhar_number(self):
        Aadhar_number = self.cleaned_data.get('Aadhar_number')
        if not re.match(r'^\d{12}$', Aadhar_number):
            raise ValidationError("Aadhar number must be 12 digits.")
        return Aadhar_number 
        

from django import forms
from .models import dsa
from django.core.exceptions import ValidationError
import re

class dsaform(forms.ModelForm):
    class Meta:
        model = dsa
        fields = '__all__'
        exclude=['dsa_id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'required': True}),
            'email_id': forms.EmailInput(attrs={'pattern': r'^[^\s@]+@[^\s@]+\.[^\s@]+$', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number', 'maxlength': '10', 'required': True}),
            'pan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your PAN number'}),
            'aadhar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Aadhar number', 'maxlength': '12'}),
            'profession': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city', 'required': True}),
            'acc_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your bank account number', 'required': True}),
            'acc_holder_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter account holder name', 'required': True}),
            'bank_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your bank name', 'required': True}),
            'ifsc_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter IFSC code', 'required': True}),
            'branch_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter branch name', 'required': True}),
            'franchiserefcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Franchise (Referral Code)'}),
            'agreeCheck': forms.CheckboxInput(attrs={'required': True}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit() or len(phone) != 10:
            raise ValidationError('Phone number must be a 10-digit number.')
        return phone

    def clean_pan(self):
        pan = self.cleaned_data.get('pan')
        if pan and not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', pan):
            raise ValidationError('Invalid PAN format. Expected format: ABCDE1234F.')
        return pan

    def clean_aadhar(self):
        aadhar = self.cleaned_data.get('aadhar')
        if not aadhar.isdigit() or len(aadhar) != 12:
            raise ValidationError('Aadhar number must be a 12-digit numeric value.')
        return aadhar

    def clean_ifsc_code(self):
        ifsc_code = self.cleaned_data.get('ifsc_code')
        if not re.match(r'^[A-Z]{4}[0-9]{6}$', ifsc_code):
            raise ValidationError('Invalid IFSC Code format. Expected format: ABCD0123456.')
        return ifsc_code

class franchiseform(forms.ModelForm):
        class Meta:
            model=franchise
            fields='__all__'
            exclude=['franchise_id']    
            widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email_id': forms.EmailInput(attrs={'pattern': r'^[^\s@]+@[^\s@]+\.[^\s@]+$', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10', 'placeholder': 'Enter your phone number'}),
            'pan': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '12', 'placeholder': 'Enter your PAN number'}),
            'aadhar': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '12', 'placeholder': 'Enter your Aadhar number'}),
            'profession': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}),
            'agreeCheck': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ifsc_code' :forms.TextInput(attrs={'class': 'form-control','maxlength': '11','placeholder': 'Enter IFSC Code','id': 'ifsc_code','oninput': 'validateIFSC()'})
    
        } 
    
        def clean_name(self):
            name = self.cleaned_data.get('name')
            if not re.match(r'^[A-Za-z\s]+$', name):
                raise ValidationError("Name should only contain alphabets and spaces.")
            return name
        
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if email:
                if not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email):
                    raise ValidationError("Invalid email format.")
                return email
            
        def clean_phone(self):
            phone = self.cleaned_data.get('phone')
            if not phone.isdigit() or len(phone) != 10:
                raise ValidationError('Phone number must be a 10-digit number.')
            return phone
        
        def clean_pan(self):
            pan = self.cleaned_data.get('pan')
            if pan and not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', pan):
                raise ValidationError('Invalid PAN format. Expected format: ABCDE1234F.')
            return pan  

        def clean_aadhar(self):
            aadhar = self.cleaned_data.get('aadhar')
            if not aadhar.isdigit() or len(aadhar) != 12:
                ValidationError('Aadhar number must be a 12-digit numeric value.')
            return aadhar          
            
        def clean_city(self):
            city = self.cleaned_data.get('city')
            if not re.match(r'^[A-Za-z\s]+$', city):
                raise ValidationError("City should only contain alphabets and spaces.")
            return city
        
        def clean_ifsc(self):
            ifsc_code = self.cleaned_data.get('ifsc')
            if not re.match(r'^[A-Z]{4}0[A-Z0-9]{7}$', ifsc_code):
                raise ValidationError('Invalid IFSC Code format. Expected format: ABCD0XXXXXXX.')
            return ifsc_code
        
                        
        def clean_dsaPhoto(self):
            dsaPhoto = self.cleaned_data.get('dsaPhoto')
            if not dsaPhoto:
                raise forms.ValidationError("A passport-size photo is required.")
            return dsaPhoto

        def clean_aadharFront(self):
            aadharFront = self.cleaned_data.get('aadharFront')
            if not aadharFront:
                raise forms.ValidationError("Aadhar front image is required.")
            return aadharFront

        def clean_aadharBack(self):
            aadharBack = self.cleaned_data.get('aadharBack')
            if not aadharBack:
                raise forms.ValidationError("Aadhar back image is required.")
            return aadharBack

        def clean_panCard(self):
            panCard = self.cleaned_data.get('panCard')
            if not panCard:
                raise forms.ValidationError("PAN card image is required.")
            return panCard

        def clean_bankDocument(self):
            bankDocument = self.cleaned_data.get('bankDocument')
            if not bankDocument:
                raise forms.ValidationError("Bank document image is required.")
            return bankDocument


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields= '__all__'