from django.forms import ModelForm
from .models import IssueModel

class IssueForm(ModelForm):
    class Meta:
        model = IssueModel
        fields = '__all__'
