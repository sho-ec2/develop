from django import forms

class getInfoForm(forms.Form):
    station = forms.CharField(label='駅名', max_length=20, widget=forms.HiddenInput)
    radius = forms.IntegerField(label='半径', max_value=1000, widget=forms.HiddenInput)
    category = forms.CharField(label='ジャンル', max_length=20, widget=forms.HiddenInput)
