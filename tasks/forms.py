from django import forms
from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    deadline = forms.DateTimeField(
        label="Deadline",
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control",
                "type": "datetime-local",
            }
        ),
    )

    content = forms.CharField(
        label="Content",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Add content",
                "rows": 1,
                "cols": 50,
            }
        ),
    )

    class Meta:
        model = Task
        fields = ['content', 'deadline', 'tags']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
