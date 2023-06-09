from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    title = forms.CharField(
        label='할 일',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': '할 일을 입력해주세요',
            },
        ),
    )

    deadline = forms.DateField(
        label='마감일',
        widget=forms.DateInput(
            attrs={'type': 'date'},
        ),
    )

    CHOICES = (('집안일', '집안일'), ('문화생활', '문화생활'), ('업무', '업무'), ('자기계발', '자기계발'))

    category = forms.ChoiceField(
        label='카테고리',
        choices=CHOICES,
        widget=forms.Select,
    )

    content = forms.CharField(
        label='내 용',
        widget=forms.Textarea(
            attrs={
                'cols': 44,
                'rows': 3,
                'class': 'my-content',
                'placeholder': '내용을 입력해주세요',
            },
        ),
    )
    
    class Meta:
        model = Todo
        exclude = ('completed',)


class CompleteForm(forms.ModelForm):
    completed = forms.BooleanField(
        widget=forms.CheckboxInput(
        attrs={
            'class': 'check-box',
            },
        ),
    )
    class Meta:
        model = Todo
        fields = ('completed',)