from django import forms
from .models import Comment, Vote


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
