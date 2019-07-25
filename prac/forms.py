from django import forms
from .models import Post

class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = ['title', 'content']
    
    '''
    title = forms.CharField(validators=[min_length_3_validator])
    content = forms.CharField(widget=forms.Textarea)
    
    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post
    '''


