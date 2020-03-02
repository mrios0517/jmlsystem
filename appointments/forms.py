from django import forms 
from .models import Appointment
from patients.models import Patient 
from .fields import ListTextWidget

import datetime

class AppointmentForm(forms.ModelForm):	
	#choices
	#ampmchoices = [('am', 'AM'), ('pm', 'PM')]


	#claimnum 	= forms.CharField(label='Claim #')
	apptdate 	= forms.DateField(label='When is the appointment?', widget=forms.SelectDateWidget, required=True)
	#starthour	= forms.IntegerField(label='Start hour:', required=True)
	#startmin	= forms.IntegerField(label='Start minute:', required=True)	
	#startampm	= forms.CharField(label='AM or PM', max_length=2, required=True)
	#endhour		= forms.IntegerField(required=False)
	#endmin		= forms.IntegerField(required=False)
	#endampm	= forms.ChoiceField(label='AM or PM', required=False, choices=ampmchoices)
	#starttime 	= forms.TimeField(widget = forms.HiddenInput())
	#endtime 	= forms.TimeField(widget = forms.HiddenInput(), required=False)
	#apptadd   	= forms.CharField(label='Appointment Address', required=True)
	#hcname 	  	= forms.CharField(label='Healthcare or Vocational Provider\'s name')
	#startadd = models.CharField(widget = forms.HiddenInput())
	#nextadd	= models.CharField(widget = forms.HiddenInput())
	#ynchoices 	= [(True, 'yes'), (False, 'no')]
	#group 	  	= forms.BooleanField(label='Is this a group session?')
	#firstlastappt 	= forms.BooleanField(label='Is this your first or last appointment?', widget=forms.HiddenInput())
	#interpreter = forms.CharField(label='Interpreters name')

	#You can specify the labels, help_texts and error_messages attributes of the inner Meta class if you want to further customize a field.
	class Meta:
		model = Appointment
		fields = [			
			'claimnum',
			'apptdate', 
			#'apptdate', 
			'starthour',
			'startmin',
			'startampm',	
			'endhour',
			'endmin',
			'endampm',
			#'apptadd',
			#'appttype',
			#'hcname', 
			#'group', 
			#'firstappt', 
			'interpreter',
		]
		labels = {
			'claimnum': 'Claim #', 
			'starthour' : '(start) hour', 
			'startmin' : '(start) min',
			'startampm': '(start) AM or PM', 
			'endhour' : '(end) hour', 
			'endmin' : '(end) min', 
			'endampm': '(end) AM or PM', 
			'appttype': 'Appointment Type', 
			'hcname': 'Healthcare or Vocational Provider\'s name', 
			'group': 'Is this a group appointment?', 
			'interpreter': 'Interpreter', 
		}

	#next step: reduce redundency in validation

	def clean(self, *args, **kwargs):
		interpreter = self.cleaned_data.get("interpreter")
		apptdate = self.cleaned_data.get("apptdate")
		starthour = self.cleaned_data.get("starthour")
		startmin = self.cleaned_data.get("startmin")
		startampm = self.cleaned_data.get("startampm")
		endhour = self.cleaned_data.get("starthour")
		endmin = self.cleaned_data.get("startmin")
		endampm = self.cleaned_data.get("startampm")
		if starthour is not None and startmin is not None and startampm is not None:
			if starthour == 12 and startampm == 'am':
				_starthour = 0
			elif starthour != 12 and startampm == 'pm':
				_starthour = starthour + 12
			else: _starthour = starthour
		if endhour is not None and endmin is not None and endampm is not None:
			if endhour == 12 and endampm == 'am':
				_endhour = 0
			elif endhour != 12 and endampm == 'pm':
				 _endhour = endhour + 12
			else: _endhour = endhour
		starttime = datetime.time(_starthour, startmin, 0)
		endtime = datetime.time(_endhour, endmin, 0)
		queryset = Appointment.objects.filter(apptdate=apptdate, interpreter=interpreter)
		for appointment in queryset:
			_starttime = appointment.starttime()
			_endtime = appointment.endtime()
			if (starttime >= _starttime and starttime <= _endtime) or (endtime >= _starttime  and endtime <= _endtime) or (starttime <= _starttime  and _endtime >= _endtime):
				raise forms.ValidationError('You have another appointment for this interpreter overlaping at this time');
		return self.cleaned_data
	






	def clean_starthour(self, *args, **kwargs):
		starthour = self.cleaned_data.get("starthour")
		if starthour is not None:
			if starthour < 1 or starthour > 12:
				raise forms.ValidationError("This is not a valid hour. Select an hour between 1 and 12")
			# can have multiple if statements/validation statements 
			else:
				return starthour

	def clean_startmin(self, *args, **kwargs):
		startmin = self.cleaned_data.get("startmin")
		if startmin is not None:
			if startmin < 0 or startmin > 59:
				raise forms.ValidationError("This is not a valid minute. Select an minute between 0 and 59")
			# can have multiple if statements/validation statements 
			else:
				return startmin

	def clean_endhour(self, *args, **kwargs):
		endhour = self.cleaned_data.get("endhour")
		if endhour is not None:
			if endhour < 1 or endhour > 12:
				raise forms.ValidationError("This is not a valid hour. Select an hour between 1 and 12")
			# can have multiple if statements/validation statements 
			else:
				return endhour

	def clean_endmin(self, *args, **kwargs):
		endmin = self.cleaned_data.get("endmin")
		if endmin is not None:
			if endmin < 0 or endmin > 59:
				raise forms.ValidationError("This is not a valid minute. Select an minute between 0 and 59")
			# can have multiple if statements/validation statements 
			else:
				return endmin
	
	def __init__(self, *args, **kwargs):
		#_country_list = kwargs.pop('data_list', None)
		_data_list = kwargs.pop('data_list', None)
		patient = kwargs.pop('patient', None)
		#_timestart = kwargs.pop('timestart', None)
		#_timeend = kwargs.pop('timeend', None)
		super(AppointmentForm, self).__init__(*args, **kwargs)
		if(patient is not None):
			#print('patient object exist')
			self.fields['claimnum'] = forms.ModelChoiceField(queryset=Patient.objects.filter(claimnum=patient.claimnum))
			self.fields['apptadd'] = forms.ChoiceField(choices=[(str(o), str(o)[2:len(str(o))-2]) for o in patient.get_locations()])
			self.fields['apptadd'].widget = ListTextWidget(data_list=patient.get_locations(), name='location-list')
			self.fields['hcname'] = forms.ChoiceField(choices=[(str(o), str(o)[2:len(str(o))-2]) for o in patient.get_doctors()])
			self.fields['hcname'].widget = ListTextWidget(data_list=patient.get_doctors(), name='doctor-list')
			self.fields['agency'] = forms.ChoiceField(choices=[(patient.agency, patient.agency)], required=False)
			self.fields['interpreter'] = forms.ChoiceField(choices=[(patient.interpreter, patient.interpreter)], required=False)

		# if(_timestart is not None):
		# 	#if starthour is not None and startmin is not None and startampm is not None:
		# 	self.clean_starthour()
		# 	starthour = int(_timestart['starthour'])
		# 	if starthour == 12 and _timestart['startampm'] == 'am':
		# 		starthour=0
		# 	elif starthour != 12 and _timestart['startampm'] == 'pm':
		# 		 starthour+=12
		# 	self.fields['starttime'] = forms.TimeField(initial=datetime.time(starthour, int(_timestart['startmin']), 0))
		# if(_timeend is not None):
		# 	#if starthour is not None and startmin is not None and startampm is not None:
		# 	endhour = int(_timeend['endhour'])
		# 	if endhour == 12 and _timeend['endampm'] == 'am':
		# 		endhour=0
		# 	elif endhour != 12 and _timeend['endampm'] == 'pm':
		# 		 endhour+=12
		# 	self.fields['endtime'] = forms.TimeField(initial=datetime.time(endhour, int(_timestart['endmin']), 0))

		
		

	
 
    # the "name" parameter will allow you to use the same widget more than once in the same
    # form, not setting this parameter differently will cuse all inputs display the
    # same list.


    # def __init__(self, user, *args, **kwargs):
    #     super(AppointmentForm, self).__init__(*args, **kwargs)
    #     self.fields['apptadd'] = forms.ChoiceField(

    #         choices=[(o.id, str(o)) for o in Waypoint.objects.filter(user=user)]
    #     )
    #     self.fields['hcname'] = forms.ChoiceField(
    #         choices=[(o.id, str(o)) for o in Waypoint.objects.filter(user=user)]
    #     )

	#def clean title - form validation 


