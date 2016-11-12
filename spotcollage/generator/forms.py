from django import forms

class EmailForm(forms.Form):
    your_email = forms.CharField(label='Spotify email:', max_length=30)
    
    