from django import forms

class getInfoForm(forms.Form):
    station = forms.CharField(required=False, label='駅名', max_length=20, widget=forms.HiddenInput)
    radius = forms.IntegerField(label='半径', max_value=10000, widget=forms.HiddenInput)
    category = forms.CharField(label='ジャンル', max_length=20, widget=forms.HiddenInput)
    line = forms.CharField(required=False, label='線名', max_length=20, widget=forms.HiddenInput)
    keyword = forms.CharField(label='キーワード', max_length=20, widget=forms.HiddenInput)
