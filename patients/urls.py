from django.contrib import admin
from django.urls import path

from patients.views import (
	#patient_detail_view, 
    patient_create_view, 
    # patient_delete_view, 
    # patient_list_view, 
    # patient_update_view
    )

app_name = 'patient'
urlpatterns = [
    #path('', patient_list_view, name='patient-list'),
    path('create/', patient_create_view, name='patient-create'),
    # path('<int:id>/', patient_detail_view, name='patient-detail'),
    # path('<int:id>/update/', patient_update_view, name='patient-update'),
    # path('<int:id>/delete/', patient_delete_view, name='patient-delete'),
]
