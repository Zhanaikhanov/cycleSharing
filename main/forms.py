from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label='username', max_length=100)
	password = forms.CharField(label='password', max_length=32, widget=forms.PasswordInput)

class SignForm(forms.Form):
	username = forms.CharField(label='username', max_length=100)
	password = forms.CharField(label='password', max_length=32, widget=forms.PasswordInput)
	password1 = forms.CharField(label='confirm password', max_length=32, widget=forms.PasswordInput)

	# class Meta:
	# 	model=User
	# 	fields=('username','password')

	def clean(self):
		cleaned_data = super(SignForm, self).clean()
		password = cleaned_data.get('password')
		password1 = cleaned_data.get('password1')


		if password != password1:
			raise forms.ValidationError(
				"passwords are does not match."
			)