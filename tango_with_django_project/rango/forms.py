from django import forms
from rango.models import Page, Category, UserProfile
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text='Please enter the category name.')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name', )


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text='Please enter the title of the page')
    url = forms.URLField(max_length=200,
                         help_text='Please enter the url of the page')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):    # 规范用户输入
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startwith('http://'):
            url = 'http://' + url

            return cleaned_data

    class Meta:
        model = Page
        exclude = ('category',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')