from django import forms
from helpers import FormHelper

# TODO: the helper is not inherited for some reason

class UniForm(forms.Form):
    
    helper = FormHelper()
    
    class Media:
        css = {
               'all': ('css/uni-form-generic.css', 'css/uni-form.css')
               }

class UniModelForm(forms.ModelForm):
    helper = FormHelper()
    
    class Media:
        css = {
               'all': ('css/uni-form-generic.css', 'css/uni-form.css')
               }