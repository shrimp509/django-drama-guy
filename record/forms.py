from django import forms
from .models import DramaRecord


class DramaRecordForm(forms.ModelForm):
    class Meta:
        model = DramaRecord
        fields = (
            'name',
            'source',
            'episode',
            'max_episode',
            'timestamp',
        )
