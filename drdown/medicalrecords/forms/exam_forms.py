from drdown.medicalrecords.models.model_exams import Exam
from django import forms


class ExamForm(forms.ModelForm):

    class Meta:
        model = Exam
        fields = ["file", "day", "category", "observations"]
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date'})
        }
