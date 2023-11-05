from django import forms
from .models import Post, Category, Comment


# choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment')]
choices = Category.objects.all().values_list('name', 'name')
category_list = []
for item in choices:
    category_list.append(item)

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'post_image', 'author', 'category', 'snippet', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'elder', 'value': '', 'type': 'hidden'}),
            'category': forms.Select(choices=category_list, attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        } 


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'post_image', 'category', 'snippet', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=category_list, attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        } 


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }
