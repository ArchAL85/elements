from django.contrib import admin
from achieve.models import Levels, Results, Achievements, Subjects, Type, TypeAchieve

# Register your models here.
admin.site.register(Achievements)
admin.site.register(Levels)
admin.site.register(Results)
admin.site.register(Subjects)
admin.site.register(Type)
admin.site.register(TypeAchieve)