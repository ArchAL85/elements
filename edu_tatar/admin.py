from django.contrib import admin
from edu_tatar.models import Teachers, Students, StatusBot, Classes, ClassAbsent, Absent, Reasons, Subjects, Marks

# Register your models here.
admin.site.register(Teachers)
admin.site.register(Students)
admin.site.register(StatusBot)
admin.site.register(Classes)
admin.site.register(ClassAbsent)
admin.site.register(Absent)
admin.site.register(Reasons)
admin.site.register(Subjects)
admin.site.register(Marks)

