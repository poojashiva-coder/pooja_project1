from django import forms
from .models import predict
class Predict(forms.ModelForm):
    class Meta:
        model = predict
        fields = ('type1', 'type2', 'type3', 'type4', 'type5', 'type6', 'type7', 'type8')