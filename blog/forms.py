from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        labels = {'title':'Заголовок:',
                  'text':'Текст:',
                  'img':'Картинка:',}
        model = Post
        fields = ('title', 'text', 'img', )

