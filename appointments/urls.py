from django.contrib import admin
from django.urls import path

from appointments.views import (
	AppointmentCreateView,
    AppointmentStartView,
    AppointmentListView, 
    AppointmentDetailView
    )

app_name = 'appointments'
urlpatterns = [
    path('', AppointmentListView.as_view(), name='appointment-list'),
    path('create/', AppointmentStartView.as_view(), name='appointment-start'),
    path('<str:claim_num>/create/', AppointmentCreateView.as_view(), name='appointment-create'),
    path('<int:id>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    # path('<int:id>/update/', appointment_view, name='appointment-update'),
    # path('<int:id>/delete/', appointment_delete_view, name='appointment-delete'),
]
    