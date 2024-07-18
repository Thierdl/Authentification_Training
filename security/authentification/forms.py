from django import forms

class LoginForm(forms.Form):
  user_name = forms.CharField(
    widget=forms.TextInput(attrs={"class": "form-control"})
                              )
                              
  pass_word = forms.CharField(
    widget=forms.PasswordInput(attrs={"class": "form-control"})
                              )
  


class SignupForm(forms.Form):
  user_name = forms.CharField(
    widget=forms.TextInput(attrs={"class":"form-control"})
  )

  email = forms.CharField(
    widget=forms.EmailInput(attrs={"class":"form-control"})

  )

  password_1 = forms.CharField(
    widget=forms.PasswordInput(attrs={"cass":"form-control"})
  )

  password_2 = forms.CharField(
    widget=forms.PasswordInput(attrs={"class":"form-control"})
  )



  