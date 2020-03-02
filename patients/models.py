from django.db import models
import json

# Create your models here.
class Patient(models.Model):
	claimnum 	= models.CharField(primary_key=True, max_length=10)  
	name 		= models.CharField(max_length=120)
	phonenum 	= models.CharField(max_length=10)
	email	 	= models.EmailField(default='test@example.com')
	dob			= models.DateField(auto_now=False, blank=True, null=True) #date of birth
	address		= models.TextField(blank=True, null=True)
	language 	= models.CharField(max_length=120, blank=True, null=True)
	doj 		= models.DateField(auto_now=False) #date of injury
	interpreter = models.CharField(max_length=120, blank=True, null=True)
	agency 		= models.CharField(max_length=120, blank=True, null=True)
	#doctors = string '[["doctor1"], ["doctor2"], ["doctor3"]]' 
	doctors 	= models.TextField(blank=True, null=True) # doctor 1, doctor 2, 
	#locations = string '[["loc1"], ["loc2"], ["loc3"]]' 
	locations 	= models.TextField(blank=True, null=True)
	notes 		= models.TextField(blank=True, null=True)
	employer	= models.CharField(max_length=120, blank=True, null=True)
	employernum	= models.CharField(max_length=10, blank=True, null=True)
	managerphone	 = models.CharField(max_length=120, blank=True, null=True)
	managerphone = models.CharField(max_length=120, blank=True, null=True)
	
	def set_locations(self, x):
		self.locations = json.dumps(x)

	def get_locations(self):
		return json.loads(self.locations)

	def set_doctors(self, x):
		self.doctors = json.dumps(x)

	def get_doctors(self):
		return json.loads(self.doctors)

	def get_absolute_url(self):
		#develop url path based on what the path is named 
		return reverse('patients:patient-detail', kwargs={"id":self.id})

	def __str__(self):
		return self.name + "(" + self.claimnum + ")"