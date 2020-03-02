from django import forms 
from .models import Patient

class PatientForm(forms.ModelForm):	
	claimnum = forms.CharField(label='Claim #')
	phonenum = forms.CharField(label='Phone #')
	email 	 = forms.EmailField(required=False)
	dob 	 = forms.DateField(label='Date of birth')
	doj 	 = forms.DateField(label='Date of injury')

	class Meta:
		model = Patient
		fields = [
			'claimnum', 
			'name',
			'phonenum',
			'email', 
			'language', 
			'dob',
			'doj',
			'agency',
			'interpreter',
			'doctors',
			'locations'
		]

	#def clean title - form validation 


