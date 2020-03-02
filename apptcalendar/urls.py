from django.contrib import admin
from django.urls import path

from appointments.views import (
	MakeMaps
	)
from apptcalendar.views import (
	CalendarWeek,
    )

app_name = 'calendar'
urlpatterns = [
    #path('', AppointmentListView.as_view(), name='calendar-month'),
    path('week/<str:week_start>', CalendarWeek.as_view(), name='calendar-week'),
    path('week/getmaps/<str:timeframe>/<int:month>/<int:day>/<int:year>', MakeMaps.as_view()), 
]
    