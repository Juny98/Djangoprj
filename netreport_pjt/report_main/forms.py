from django import forms
from .models import Contents

class ContentsForm(forms.ModelForm):
    # title = forms.CharField(max_length=30)
    # content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contents
        fields = '__all__'

        # exclude = ('title',)

    # def clean_title(self):
    #     title = self.cleaned_data('title')
    #     if 'django' in title:
    #         return True
    #     return False

