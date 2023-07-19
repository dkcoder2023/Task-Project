from django import forms

class ShareByEmailForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    recipient_email = forms.EmailField(label='Recipient Email')
    comments = forms.CharField(label='Comments', widget=forms.Textarea)
