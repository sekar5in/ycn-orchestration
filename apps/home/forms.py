from django import forms



class CreateOrgForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))

    org = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Organization",
                "class": "form-control"
            }
        ))