from django import forms
from .models import Comment, Vote, Post, Image


class CommentForm(forms.ModelForm):
    """
    Form for adding comments to a post.
    """
    class Meta:
        model = Comment
        fields = ('body',)


class VoteForm(forms.ModelForm):
    """
    Form for adding votes to a post.
    """
    class Meta:
        model = Vote
        fields = ('user_vote',)
        widgets = {
            'user_vote': forms.RadioSelect(),
        }


class ArticleForm(forms.ModelForm):
    """
    Form for adding a new article.
    """
    location_name = forms.CharField(label='Location title', max_length=100)
    location_description = forms.CharField(label='About the location',
                                           widget=forms.Textarea)
    main_content_title = forms.CharField(label='About title', required=False)
    main_content = forms.CharField(label='Main article content',
                                   widget=forms.Textarea)
    longitude = forms.DecimalField(label='Longitude')
    latitude = forms.DecimalField(label='Latitude')
    secondary_content = forms.CharField(label='Secondary article content',
                                        widget=forms.Textarea)
    post_input_type = forms.CharField(label='Code input', required=False)

    class Meta:
        model = Post
        fields = (
            'location_name',
            'location_description',
            'main_content_title',
            'main_content',
            'longitude',
            'latitude',
            'secondary_content'
            )


class ImageForm(forms.ModelForm):
    """Form for adding images to a post."""
    class Meta:
        model = Image
        fields = ('image',)
