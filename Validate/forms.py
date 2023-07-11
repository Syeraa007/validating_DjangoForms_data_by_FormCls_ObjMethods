from typing import Any, Dict
from django import forms

def validate_name(jelly):
    if jelly[0].lower()=='a':
        raise forms.ValidationError("Name shouldn't starts with A")
    
def validate_len(value):
    if len(value)<=5:
        raise forms.ValidationError("Name should be more than 5 chars")
    
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,help_text='Enter name',label="Name",validators=[validate_name,validate_len])
    age=forms.IntegerField(help_text='Enter age',label='Age')
    loc=forms.CharField(help_text='Enter location',label='Location')
    email=forms.EmailField(help_text='Enter email',label='Email')
    remail=forms.EmailField(help_text='Enter email',label='Re-Email')
    url=forms.URLField(label='URL',help_text='Enter URL')
    botcatch=forms.CharField(label='Bot Catch',help_text='Enter bot catcher',required=False,widget=forms.HiddenInput)
    def clean(self) -> Dict[str, Any]:
        e=self.cleaned_data['email']
        re=self.cleaned_data['remail']
        if e!=re:
            raise forms.ValidationError('No match found')
    def clean_botcatch(self):
        bot=self.cleaned_data['botcatch']
        if len(bot)>0:
            raise forms.ValidationError("Don't end url with m ")