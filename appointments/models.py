from django.db import models
import json
import datetime

# Create your models here.
class Appointment(models.Model):
	#choices
	ampmchoices = [('am', 'AM'), ('pm', 'PM')]

	#model fields
	claimnum = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
	apptdate = models.DateField(auto_now=False, blank=True, null=True)
	starthour	= models.IntegerField(blank=True, null=True)
	startmin	= models.IntegerField(blank=True, null=True)
	startampm	= models.CharField(max_length=2, blank=True, null=True, choices=ampmchoices)
	endhour		= models.IntegerField(blank=True, null=True)
	endmin		= models.IntegerField(blank=True, null=True)
	endampm		= models.CharField(max_length=2, blank=True, null=True, choices=ampmchoices)
	#startttime and endtime are filled automatically by the overwritten save() function 
	#starttime = models.TimeField(auto_now=False, blank=True, null=True)
	#endtime = models.TimeField(auto_now=False, blank=True, null=True)
	apptadd = models.CharField(max_length=200, blank=True, null=True)
	appttype = models.CharField(max_length=120, blank=True, null=True)
	hcname = models.CharField(max_length=120, blank=True, null=True)
	#startadd and nextadd are filled once the day is approved from calendar view
	startadd = models.CharField(max_length=200, blank=True, null=True)
	nextadd	= models.CharField(max_length=200, blank=True, null=True)
	group = models.BooleanField(default=False, blank=True, null=True)
	#firstlastappt is filled once the day is approved from calendar view
	firstlastappt = models.BooleanField(default=False, blank=True, null=True)
	#interpreter needs to be made a foreign key for the interpreter model
	interpreter = models.CharField(max_length=120, blank=True, null=True)
	agency = models.CharField(max_length=120, blank=True, null=True)

	def starttime(self):
		starthour = self.starthour
		startmin = self.startmin
		startampm = self.startampm
		_starthour = None
		if starthour is not None and startmin is not None and startampm is not None:
			if starthour == 12 and startampm == 'am':
				_starthour = 0
			elif starthour != 12 and startampm == 'pm':
				_starthour = starthour + 12
			else: _starthour = starthour
			return datetime.time(_starthour, startmin, 0)
		else: return None


	def endtime(self):
		endhour = self.endhour
		endmin = self.endmin
		endampm = self.endampm
		_endhour = None
		if endhour is not None and endmin is not None and endampm is not None:
			if endhour == 12 and endampm == 'am':
				_endhour = 0
			elif endhour != 12 and endampm == 'pm':
				 _endhour = endhour + 12
			else: _endhour = endhour
			return datetime.time(_endhour, endmin, 0)	
		else: return None

	# def save(self, *args, **kwargs):
	# 	starthour = self.starttime
	# 	startmin = self.startmin
	# 	startampm = self.startampm
	# 	endhour = self.endhour
	# 	endmin = self.endmin
	# 	endampm = self.endampm
	# 	if starthour is not None and startmin is not None and startampm is not None:
	# 		if starthour == 12 and startampm == 'am':
	# 			_starthour=0
	# 		elif starthour != 12 and startampm == 'pm':
	# 			 _starthour= starthour + 12
	# 		self.startime = datetime.time(_starthour, startmin, 0)
	# 	if endhour is not None and endmin is not None and endampm is not None:
	# 		if endhour == 12 and endampm == 'am':
	# 			_endhour=0
	# 		elif endhour != 12 and endampm == 'pm':
	# 			 _endhour+=12
	# 		self.endtime = datetime.time(_endhour, endmin, 0)	
	# 	super(Appointment, self).save(*args, **kwargs)



#class pdf(models.Model):

class map(models.Model):
	apptid = models.ForeignKey('Appointment', on_delete=models.CASCADE)
	apptadd = models.CharField(max_length=200, blank=True, null=True)
	startadd = models.CharField(max_length=200, blank=True, null=True)
	nextadd	= models.CharField(max_length=200, blank=True, null=True)

class jsontest(models.Model):
    foo = models.CharField(max_length=200)

    def set_foo(self, field, x):
    	self.field = json.dumps(x)
    def get_foo(self, field):
    	return json.loads(self.field)


def get_absolute_url(self):
        return reverse("appointments:appointment-detail", kwargs={"id": self.id})




