from django import forms
from .models import Comment, Vote, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ('user_vote',)
        widgets = {
            'user_vote': forms.RadioSelect(),
        }

class ArticleForm(forms.ModelForm):
    location_name = forms.CharField(label='Location title', max_length=100)
    location_description = forms.CharField(label='About the location', widget=forms.Textarea)
    main_content_title = forms.CharField(label='About title', required=False)
    main_content = forms.CharField(label='Main article content', widget=forms.Textarea)
    longitude = forms.DecimalField(label='Longitude')
    latitude = forms.DecimalField(label='Latitude')
    secondary_content = forms.CharField(label='Secondary article content', widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ('location_name', 'location_description', 'main_content_title', 'main_content', 'longitude', 'latitude', 'secondary_content')
        widgets = {
            'country': forms.Select(),
        }