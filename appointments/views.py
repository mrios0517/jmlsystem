from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect 
from django.urls import reverse
from django.views import View

from .forms import AppointmentForm

from .models import Appointment
from patients.models import Patient

key = 'AsO9sqiDfOBuv9fkNQRoC403WxlDFepCLyPhRfCMIPRHgR2x4HrQutjPmL3eWpYk'


class PatientObjectMixin(object):
	model = Patient
	def get_object(self):
		id = self.kwargs.get('claim_num')
		#print('we have reached mixinobject')
		obj = None
		if id is not None:
			obj = get_object_or_404(self.model, claimnum=id)
		return obj

class AppointmentObjectMixin(object):
	model = Appointment
	def get_object(self):
		id = self.kwargs.get('id')
		#print('we have reached mixinobject')
		obj = None
		if id is not None:
			obj = get_object_or_404(self.model, id=id)
		return obj

class MakeMaps(View):
	print('inside makemaps');
	template_name = "appointments/makemaps.html"
	queryset = Appointment.objects.filter(apptdate__range=["2019-12-02", "2019-12-08"])

	def get_queryset(self):
		return self.queryset
	

	def get(self, request, *args, **kwargs):
		day = self.kwargs.get('day')
		month = self.kwargs.get('month')
		year = self.kwargs.get('year')
		timeframe = self.kwargs.get('timeframe')

		month_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
		leap_years = [2020, 2024, 2028]
		if (year in leap_years):
			month_days[2] = 29

		if month < 10:
			month = '0' + str(month)
		if day < 10:
			_day = '0' + str(day)
		date_str = '' + str(year) + '-' + str(month) + '-' + str(_day)

		if timeframe == 'day':
			queryset = Appointment.objects.filter(apptdate=date_str)
		elif timeframe == 'week':
			end_day = day + 7
			end_month = month
			if (emd_day < 10):
				end_day = '0' + str(end_day)
			elif (end_day > month_days[month]):
				end_day = end_day - month_days[month]
				end_month =+ 1
				end_date_str = '' + str(year) + '-' + str(end_month) + '-' + str(end_day)
				queryset = Appointment.objects.filter(apptdate__range=[date_str, end_date_str])
		v = {}
		for value in queryset:
			v.setdefault(value.interpreter, []).append(value)
		print(v)
		for item in v:
			w = {}
			for _item in v[item]:
				print('ITEM:', _item)
				w.setdefault(_item.agency,[]).append(_item)
			v[item] = w
		print(v)

		print('PRINTING APPOINTMENTS')
		print(queryset)
		context =  {'appointments':v, 'day': day, 'month': month, 'year': year, 'timeframe': timeframe}
		return render(request, self.template_name, context)

# Create your views here.	
class AppointmentListView(View):
	template_name = "appointments/appointment_list.html"
	queryset = Appointment.objects.all()

	def get_queryset(self):
		return self.queryset
	
	def get(self, request, *args, **kwargs):
		context =  {'object_list': self.get_queryset()}
		return render(request, self.template_name, context)


class AppointmentStartView(View):
	template_name = "appointments/appointment_start.html"
	queryset = Patient.objects.all()

	def get_queryset(self):
		return self.queryset

	def get(self, request, *args, **kwargs):
		context =  {'patient_list': self.get_queryset()}
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		# POST method
		#context = {}
		claim_num = request.POST['claim_num']
		if claim_num is not None:
			#context['patient_list'] = None
			print(claim_num)
			return HttpResponseRedirect(reverse('appointments:appointment-create', kwargs={'claim_num': claim_num}))
			#return redirect('/appointments/')

		return render(request, self.template_name, {})	

	#def get_success_url(self):
		#claim_num = request.POST['claim_num']
		#print(claim_num)
		#return redirect('/appointments/')
		#return reverse('appointments:appointment-list')
		#return reverse('appointment-listments:appointment-create', claim_num)
	# def post(self, request, *args, **kwargs):
	# 	# POST method
		
	# 	return render(request, self.template_name, context)

class MyAppointmentForm(AppointmentForm):
	def __init__(self, *args, claimnum, hcname, apptadd, **kwargs):
		self.claimnum = claimnum
		self.hcname = hcname
		self.apptadd = apptadd
		super().__init__(*args, **kwargs)


class AppointmentCreateView(PatientObjectMixin, View):
	template_name = "appointments/appointment_create.html"

	data_list = {}
	def get(self, request, *args, **kwargs):
		context = {}
		patient = self.get_object()
		if patient is not None:
			context['patient'] = patient
			data_list = {'locations': patient.get_locations(), 'doctors': patient.get_doctors(), 'agency': patient.agency, 'interpreter': patient.interpreter}
			context['form'] = AppointmentForm(data_list=data_list, patient=patient)
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		# POST method
		patient = self.get_object()
		#data_list = {'locations': patient.get_locations(), 'doctors': patient.get_doctors()}
		if patient is not None:
			form = AppointmentForm(request.POST, patient=patient)
			if form.is_valid():
				#print('clean data: ' + str(form.cleaned_data))
				form.save()
				return HttpResponseRedirect(reverse('appointments:appointment-detail', kwargs={'id': form.instance.id}))
				#form = AppointmentForm
			context = {"form": form}
		return render(request, self.template_name, context)


class AppointmentDetailView(AppointmentObjectMixin, View):
	template_name = "appointments/appointment_detail.html"
	#just "id" means that it is required, "id=None" creates a default
	def get(self, request, id=None, *args, **kwargs):
		appointment = self.get_object()
		time = {'start':appointment.starttime, 'end':appointment.endtime}
		context = {'object': appointment, 'time':time}
		return render(request, self.template_name, context)

# class AppointmentWeekView(View):
# 	template_name = "appointments/appointment_week.html"

# 	def get(self, request, week=None, *args, **kwargs):
# 		startdate = self.kwargs.get('week')
#     	queryset = {}
# 		for i in range(6):
# 			day='day'+str(i)
# 			queryset[day] = Appointment.objects.filter(date= startdate + timedelta(days=i))
# 		return render(request, self.template_name, queryset)


	#return render(request, self.template_name, context)

	# def get(self, request, *args, **kwargs):
	# 	# GET method
	# 	patient = self.get_object()
	# 	context = {}
	# 	if patient is not None:
	# 		form = AppointmentForm
	# 		context['patient'] = patient
	# 		context['form'] = form
	# 	return render(request, self.template_name, context)

	# def post(self, request, *args, **kwargs):
	# 	# POST method
	# 	form = AppointmentForm(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		form = AppointmentForm
	# 	context = {"form": form}
	# 	return render(request, self.template_name, context)