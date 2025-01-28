from .models import Comment
from django import forms


# We created a class called CommentForm that inherited from Django's forms.ModelForm class. 
# Because this class is inherited from a built-in Django class, we can simply use the Meta class 
# to tell the ModelForm class what models and fields we want in our form. form.ModelForm will 
# then build this for us.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)