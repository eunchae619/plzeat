from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField(
        initial="test@a.com", widget=forms.TextInput(attrs={"placeholder": "이메일 주소"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "비밀번호"})
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("email",)
        widgets = {
            "email": forms.TextInput(attrs={"placeholder": "이메일 주소"}),
        }

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "비밀번호"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "비밀번호 재확인"}),
        label="Confirm Password",
    )

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("Password Confirmation does not match")
        else:
            return password

    def save(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = super().save(commit=False)
        user.username = email
        listed_email = email.split("@")
        user.nickname = listed_email[0]
        user.set_password(password)
        user.save()
