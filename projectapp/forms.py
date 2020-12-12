from .models import Project
from django.forms import ModelForm


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ["image", "title", "description"]
