from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect 
from django.urls import reverse
from django.views import View
from appointments.models import Appointment
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core.serializers import serialize

#from Appointment.forms import AppointmentForm

#from .models import Appointment
#from patients.models import Patient

class AppointmentObjectMixin(object):
	model = Appointment
	def get_object(self):
		id = self.kwargs.get('id')
		#print('we have reached mixinobject')
		obj = None
		if id is not None:
			obj = get_object_or_404(self.model, id=id)
		return obj

# Create your views here.
# need to pass current day, 
class CalendarWeek(View, AppointmentObjectMixin):
	template_name = "apptcalendar/calendarweek.html"
	#queryset = Appointment.objects.all()
	queryset = Appointment.objects.filter(apptdate__range=["2019-12-02", "2019-12-08"])

	def get_queryset(self):
		return self.queryset
	#just "id" means that it is required, "id=None" creates a default
	def get(self, request, *args, **kwargs):
		data = self.get_queryset()
		#data = Appointment.objects.filter(id=id).values_list('apptdate', 'starthour', 'startmin', 'startampm')
		apptdic = {}
		if data is not None:
			for counter, appointment in enumerate(data):
				#print('appointment[\'Appointment\']')
				#print(appointment['Appointment'])
				print(str(counter) + ') ' + str(appointment))
				#print(str(appointment))

				apptdic[appointment.id] = model_to_dict(appointment)
				# print('printing apptdic[appointment.id]')
				# print(apptdic[appointment.id])
				# print('printing apptdic[appointment.id][apptdate]')
				# print(apptdic[appointment.id]['apptdate'])
				# print('printing apptdic[appointment.id][starthour]')
				# print(apptdic[appointment.id]['starthour'])
				apptdic[appointment.id]['starttime'] = ''
				apptdic[appointment.id]['endtime'] = ''

				if apptdic[appointment.id]['apptdate'] != '' and apptdic[appointment.id]['apptdate'] != None:
					apptdic[appointment.id]['apptdate'] = str(apptdic[appointment.id]['apptdate'])
				if apptdic[appointment.id]['starthour'] != None  and apptdic[appointment.id]['startmin'] != None and apptdic[appointment.id]['startampm'] != None:
					apptdic[appointment.id]['starttime'] = str(appointment.starttime());
				# else:
				# 	apptdic[appointment.id]['starthour'] = ''
				# 	apptdic[appointment.id]['startmin'] = ''
				# 	apptdic[appointment.id]['startampm'] = ''
				if apptdic[appointment.id]['endhour'] != None and apptdic[appointment.id]['endmin'] != None and apptdic[appointment.id]['endampm'] != None:
					apptdic[appointment.id]['endtime'] = str(appointment.endtime());
				# else:
				# 	apptdic[appointment.id]['endhour'] = ''
				# 	apptdic[appointment.id]['endmin'] = ''
				# 	apptdic[appointment.id]['endampm'] = ''



				for key in apptdic[appointment.id].keys():
					if apptdic[appointment.id][key] == None:
						apptdic[appointment.id][key] = ''
					elif apptdic[appointment.id][key] == False:
						apptdic[appointment.id][key] = 0
					elif apptdic[appointment.id][key] == True:
						apptdic[appointment.id][key] = 1


		
			#appointment = model_to_dict(appointment)
			#print(appointment)
			
			#print(json.dumps(appointment, cls=DjangoJSONEncoder))
		#data = Appointment.objects.filter(product=product).values_list('price','valid_from')
		#print('\n\nprinting dictionary...')
		#print(apptdic)
		#data_list = list(data)
		#data_json = json.dumps(apptdic, cls=DjangoJSONEncoder)
		# for item in data:
	 	# item['Appointment'] = model_to_dict(item['Appointment'])
		context = {'data_list': apptdic}
		print('printing context..')
		print(apptdic)
		#context = {'appt_list': serialize('json', data_json)}
		#print(context)
		#context = {'object': appointment, 'time':time}
		return render(request, self.template_name, context)