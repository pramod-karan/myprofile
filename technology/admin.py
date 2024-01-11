from django.contrib import admin
from .models import Technology,ResumeTech,Project,Review,Blog
# Register your models here.
class TechnologyAdmin(admin.ModelAdmin):
    list_display=['tachnology']
admin.site.register(Technology,TechnologyAdmin)

class ResumeTechAdmin(admin.ModelAdmin):
    list_display=['tachnology','side_show','title','working_timeline']
admin.site.register(ResumeTech,ResumeTechAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display=['project_name','delay_time']
admin.site.register(Project,ProjectAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display=['customer_name','description','profession']
admin.site.register(Review,ReviewAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display=['writer_name','description','profession']
admin.site.register(Blog,BlogAdmin)
