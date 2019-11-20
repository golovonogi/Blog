from django import forms

from comment.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        labels = {
            'comment': 'Комментировать: ',
        }
        model = Comment
        fields = ('comment', )
