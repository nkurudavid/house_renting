from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, PasswordChangeForm
from django.core.exceptions import ValidationError

# get user model
User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    """The default """
    password1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name','last_name','email',]
        
    # EMAIL VARIDATION
    def clean_email(self):
        if not email:
           raise forms.ValidationError("User email is required")
       
        email = self.cleaned_data.get('email')
        # filter from user model where exist
        if User.objects.filter(email=email).exists():
           raise forms.ValidationError("User email already exist!!!")
        return email
    
    # PASSWORD VARIDATION
    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('password1')
        pass2 = cleaned_data.get('password2')
        
        if not pass1:
            raise forms.ValidationError("Password is required!")
        if pass1 is not None and pass1 != pass2 :
            raise forms.ValidationError("Password don't match!")
        
        return cleaned_data
    
    # IF SAVE DATA
    def save(self, commit=True):
        # save entry user data
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        
        return user
        

# update form
class UserUpdateForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(label=("Password"),
        help_text=("Click to <a href=\"../password/\">Change Password</a>."))
    
    # IF SAVE DATA
    def save(self, commit=True):
        # save entry user data
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        
        return user
        
class UpdatePasswordForm(PasswordChangeForm):
    """
    A custom form for changing the password of a user in the Django admin.
    """
    old_password = forms.CharField(label="Old Password", widget=forms.PasswordInput)
    password1 = forms.CharField(label="New Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].required = True
        self.fields['password2'].required = True
        

    def clean(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('password1')
        new_password2 = self.cleaned_data.get('password2')
        if old_password and not self.user.check_password(old_password):
            raise ValidationError("Your old password was entered incorrectly. Please enter it again.")
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise ValidationError("The two password fields didn't match.")
        return self.cleaned_data