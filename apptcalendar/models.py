from django.db import models


# Create your models here.
class Event(models.Model):
	#model fields
	Eventid = models.ForeignKey('appointments.Appointment', on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	start = models.DateTimeField()
	end = models.DateTimeField()
	# end = models.DateTimeField(
 #        _("end"),
 # You add indexes on columns when you want to speed up searches on that column. Typically, only the primary key is indexed by the database. This means look ups using the primary key are optimized.
 #        db_index=True,
 #        help_text=_("The end time must be later than the start time."),
 #    )
