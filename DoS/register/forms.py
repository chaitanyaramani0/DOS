from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import Form,ModelForm
from .models import PickUp
from django.forms import Form,ModelForm
from django.forms.widgets import Input
from django.forms import TextInput
from django.contrib.auth import get_user_model

user_model = get_user_model()


class RegisterForm(UserCreationForm):
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control",'placeholder' : 'Address'}))
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control",'placeholder' : 'Phone'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"class":"form-control",'placeholder' : 'Email'}))
    password1 = forms.CharField(
       
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'password'}),
    )
    password2 = forms.CharField(
       
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'Conform Password'}),
    )
    class Meta(UserCreationForm.Meta):
        model = user_model
        widgets = {
            'username': Input(attrs={
                "type" : "text",
                "class":"form-control",
                'placeholder' : 'Username'}),
                }

            
class PickUpForm(ModelForm):
    pickup_choices = {
        ("One_Time", "One Time"), 
        ("Recurring", "Recurring"),
    }

    bin_choices = {
        ("Compost","Compost"),
        ("Landfill","Landfill"),
        ("Wood","Wood"),
        ("Metal","Metal"),
        ("Paper/Cardboard","Paper/Cardboard"),
        ("Plastic-Wrap","Plastic-Wrap"),
        ("Plastic-Bottel/Container","Plastic-Bottel/Container"),
        ("Glass-Bottel/Container","Glass-Bottel/Container"),
        ("Aluminium-Cans/Container","Aluminium-Cans/Container"),
        ("E-Waste","E-Waste"),

    }

    notes = forms.CharField(required=False,widget=forms.Textarea(attrs={"class":"form-control", 'placeholder':'Additional Notes'}))
    recurring = forms.ChoiceField(required=True,choices=pickup_choices,widget=forms.Select(attrs={'class':'form-control'}))
    bin_type = forms.ChoiceField(required=True,choices=bin_choices,widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = PickUp
        fields = ['bin_type','weight','schedule_date','recurring','notes']
        widgets = {
            'weight' : Input(attrs={
                "type" : "number",
                "class":"form-control",
                'placeholder' : 'weight(lb)'
                }),
            'schedule_date' : Input(attrs={
                "type" : "date",
                "class":"form-control", 
                "placeholder" :"Schedule Date" 
                }),
            
        }

class PickUpedForm(ModelForm):
    class Meta:
        model = PickUp
        fields = ['bin_type','weight','schedule_date','recurring','notes',"is_pickedup",'picked_date']
        widgets = {
            'is_pickedup' : Input(attrs={
                "type" : "text",
                "class":"form-control",
                'placeholder' : 'weight(lb)'
                }),
            'picked_date' : Input(attrs={
                "type" : "date",
                "class":"form-control", 
                "placeholder" :"Pick up Date" 
                }),
            'weight' : Input(attrs={
                # "disabled":True,
                "type" : "number",
                "class":"form-control",
                # 'placeholder' : 'weight(lb)'
                }),
            'bin_type' : Input(attrs={
                # "disabled":True,
                "type" : "text",
                "class":"form-control",
                # 'placeholder' : 'weight(lb)'
                }),
            'schedule_date' : Input(attrs={
                # "disabled":True,
                "type" : "date",
                "class":"form-control",
                # 'placeholder' : 'weight(lb)'
                }),
            'recurring' : Input(attrs={
                # "disabled":True,
                "type" : "text",
                "class":"form-control",
                # 'placeholder' : 'weight(lb)'
                }),
            'notes' : Input(attrs={
                # "disabled":True,
                "type" : "text",
                "class":"form-control",
                # 'placeholder' : 'weight(lb)'
                }),
            
        }



