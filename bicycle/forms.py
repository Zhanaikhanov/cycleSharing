from django import forms

class PostForm(forms.Form):

	type_b = forms.CharField(label='type of bicycle', max_length=100)
	style = forms.CharField(label='style', max_length=100)
	image = forms.CharField(label='image link:', max_length=100)
	cost = forms.IntegerField()
	stars = forms.IntegerField()


