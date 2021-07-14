from django import forms

from .models import job_data


class JobForm(forms.Form):
    job_title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Job Title"}), required=False)
    job_special = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Job Specialization"}), required=False)
    location = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Location"}), required=False)
    date_posted = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Date Posted"}), required=False)



