from django.contrib import admin
from .models import Profile, Course, Lesson, Enrollment, Assignment, Submission, Grade, Discussion, Notification, Payment

admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(Grade)
admin.site.register(Discussion)
admin.site.register(Notification)
admin.site.register(Payment)
