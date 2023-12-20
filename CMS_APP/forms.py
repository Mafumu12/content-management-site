from .models import Post,categories
from django import forms
from ckeditor.widgets import CKEditorWidget 



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','image','tag']

    body = forms.CharField(widget=CKEditorWidget())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add placeholders for each field
        self.fields['title'].widget.attrs['placeholder'] = 'Title'
        self.fields['body'].widget.attrs['placeholder'] = 'Start Writing...'
        self.fields['image'].widget.attrs['placeholder'] = 'Choose an image'
        self.fields['tag'].widget.attrs['placeholder'] = 'Category' 


        # Add a class to the body field
        self.fields['body'].widget.attrs['class'] = 'custom-textarea' 
        self.fields['image'].widget.attrs['class'] = 'custom-file'    
        self.fields['tag'].widget.attrs['class'] = 'category-f'    