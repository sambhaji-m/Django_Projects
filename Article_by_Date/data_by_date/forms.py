# # forms.py

# from django import forms
# from .models import article # Replace YourModel with the name of your model

# class data(forms.ModelForm):
#     class Meta:
#         model = article # Replace YourModel with the name of your model
#         fields = ['date', 'name', 'description']


from django import forms
from .models import article
from django.utils import timezone
from datetime import date, timedelta




class data(forms.ModelForm):
    class Meta:
        model = article
        fields = ['date', 'name', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = date.today()
        three_months_ago = today - timedelta(days=90)
        self.fields['date'].widget.attrs.update({
            'min': three_months_ago.strftime('%Y-%m-%d'),
            'max': today.strftime('%Y-%m-%d')
        })


    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')

        # Check if an article with the same date already exists
        if article.objects.filter(date=date).exists():
            raise forms.ValidationError("An article with the same date already exists.")

        return cleaned_data