from django import forms
from .models import Todo
from datetime import date

class TodoForm(forms.ModelForm):
    due_date = forms.DateField(
        required=False,
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )
    class Meta:
        model = Todo
        fields = ["title", "description", "due_date", "is_done"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            # "due_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "is_done": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def clean_due_date(self):
        d = self.cleaned_data.get("due_date")
        if d and d < date.today():
            raise forms.ValidationError("期限は今日以降の日付を指定してください。")
        return d

