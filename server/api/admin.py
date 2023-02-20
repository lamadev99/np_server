from django.contrib import admin
from api.models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class ApiInline(admin.StackedInline):
    model = Writer
    can_delete = False
    verbose_name_plural = 'Writers'

class CustomizedUserAdmin(UserAdmin):
    inlines = (ApiInline,)

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

class WriterAdmin(admin.ModelAdmin):
    list_display = ['writer', 'email', 'fname', 'lname', 'is_admin']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(writer=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "writer":
            kwargs['queryset'] = User.objects.filter(username = request.user.username)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Writer, WriterAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('slug','writer', 'title', 'category', 'subCategory', 'views', 'is_featured', 'keywords')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(writer=request.user.id)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "writer":
            kwargs['queryset'] = Writer.objects.filter(writer=request.user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(News, NewsAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('cId', 'fName', 'email', 'comment', 'is_save', 'created_at', 'updated_at')
admin.site.register(Comment, CommentAdmin)

class NewsSubsAdmin(admin.ModelAdmin):
    list_display = ('nsId', 'email', 'created_at')
admin.site.register(NewsSubscription, NewsSubsAdmin)

class PageGeneratorAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'meta_keywords', 'created_at')
admin.site.register(PageGenerator, PageGeneratorAdmin)

admin.site.register(Category)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'name' ]
admin.site.register(SubCategory, SubCategoryAdmin)

