from django import forms

class GradeForm(forms.Form):
    student_id = forms.IntegerField()
    subject_id = forms.IntegerField()
    grade = forms.DecimalField(max_digits=5, decimal_places=2)
