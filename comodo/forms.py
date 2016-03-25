from django.contrib.auth.forms import UserCreationForm, User

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Div
from .models import MyUser, Post, Comment, Material
from registration.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django_comments.forms import CommentForm, CommentDetailsForm

class RegistrationsForm(RegistrationForm):

    email = forms.EmailField(required = True)
    city = forms.CharField(max_length=129)
    # user_status = forms.ChoiceField(choices=MyUser.USER_STATUS_DICT, widget=forms.RadioSelect)

    class Meta:
        model = MyUser
        fields = ('username','email', 'city','user_status',)

class MyUserProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('username',)



class LoginForm(AuthenticationForm):
    username = forms.EmailField(required=True)
    password = forms.CharField(required=True,widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'message',)
    # user = forms.IntegerField(required=False, widget=forms.HiddenInput())

class CreateMaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ('material_name', 'material_message','material_image',)


    def __init__(self, *args, **kwargs):
        super(CreateMaterialForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'material_name',
            'material_message',
            'material_image',

            ButtonHolder(
                Submit('post_edit', 'Done', css_class='btn-success')
            )
        )


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'message',)

    def __init__(self, *args, **kwargs):
        super(EditPostForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'message',

            ButtonHolder(
                Submit('post_edit', 'Done', css_class='btn-success')
            )
        )


# class CommentForms(CommentForm):
#     class Meta:
#         model = Comment
#         fields = ('author', 'text',)

    # def __init__(self, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         'author',
    #         'text',
    #         ButtonHolder(
    #             Submit('post_edit', 'Done', css_class='btn-success')
    #         )
    #     )