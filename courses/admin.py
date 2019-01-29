from django.contrib import admin
from .models import Subject, Course, Module, Content, Item, FileTest
import nested_admin
# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

class ContentInline(nested_admin.NestedStackedInline):
    model = Item
    extra = 1

class ModuleInline(nested_admin.NestedStackedInline):
    model = Module
    extra = 1
    inlines = [ContentInline]

@admin.register(Course)
class CourseAdmin(nested_admin.NestedModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]

@admin.register(FileTest)
class FileTestAdmin(admin.ModelAdmin):
    pass
