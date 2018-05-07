from drdown.medicalrecords.models.model_specific_exams import SpecificExam
from django import forms


class SpecificExamsForm(forms.ModelForm):

    class Meta:
        model = SpecificExam
        fields = ["structured_physical_exam", "vision", "ear", "hearth",
                  "muscle_skeletal_system", "nervous_system"]
