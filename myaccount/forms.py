from django import forms

class Quiz(forms.Form):
    age = forms.IntegerField(label='Age', min_value=0, max_value=100,required=False)
    weight = forms.FloatField(label='Weight', min_value=0, max_value=1000.0,required=False)
    height = forms.FloatField(label='Height', min_value=0, max_value=20.0,required=False)