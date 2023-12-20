from .models import Profile
from django import forms



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username','profession','picture','about']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add placeholders for each field
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['profession'].widget.attrs['placeholder'] = 'profession'
        self.fields['picture'].widget.attrs['placeholder'] = 'picturee'
        self.fields['about'].widget.attrs['placeholder'] = 'about' 


        # Add a class to the body field
        self.fields['username'].widget.attrs['class'] = 'custom-username' 
        self.fields['profession'].widget.attrs['class'] = 'custom-profession'    
        self.fields['picture'].widget.attrs['class'] = 'custom-picture'    
        self.fields['about'].widget.attrs['class'] = 'custom-about'    