from django import forms
from .models import Todo
from datetime import date

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "due_date", "is_done"]

    def clean_due_date(self):
        d = self.cleaned_data.get("due_date")
        if d and d < date.today():
            raise forms.ValidationError("期限は今日以降の日付を指定してください。")
        return d

