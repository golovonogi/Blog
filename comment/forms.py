from django import forms

from comment.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        labels = {
            'comment': 'Комментировать туть ',
        }
        model = Comment
        fields = ('comment', )
