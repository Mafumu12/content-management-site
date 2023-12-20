from django.contrib import admin
from .models import Post,categories,Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


 





admin.site.register(Post,PostAdmin)
admin.site.register(categories)
admin.site.register(Comment)