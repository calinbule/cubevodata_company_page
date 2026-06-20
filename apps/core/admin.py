from django.contrib import admin
from unfold.admin import ModelAdmin

from .icons import render_icon
from .models import AIService, Project, Service
from .widgets import IconPickerWidget


class BaseContentAdmin(ModelAdmin):
    list_display = ('icon_preview', 'title_en', 'order', 'is_active')
    list_display_links = ('title_en',)
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title_en', 'title_ro')

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'icon':
            kwargs['widget'] = IconPickerWidget
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    @admin.display(description='Icon')
    def icon_preview(self, obj):
        return render_icon(obj.icon, size=22)


@admin.register(Service)
class ServiceAdmin(BaseContentAdmin):
    fieldsets = (
        (None, {'fields': ('icon', 'is_active', 'order')}),
        ('English', {'fields': ('title_en', 'desc_en')}),
        ('Română', {'fields': ('title_ro', 'desc_ro')}),
    )


@admin.register(AIService)
class AIServiceAdmin(BaseContentAdmin):
    list_display = ('icon_preview', 'title_en', 'badge_en', 'order', 'is_active')
    fieldsets = (
        (None, {'fields': ('icon', 'is_active', 'order')}),
        ('English', {'fields': ('title_en', 'desc_en', 'badge_en')}),
        ('Română', {'fields': ('title_ro', 'desc_ro', 'badge_ro')}),
    )


@admin.register(Project)
class ProjectAdmin(BaseContentAdmin):
    list_display = ('icon_preview', 'title_en', 'category', 'tag', 'order', 'is_active')
    list_filter = ('is_active', 'category')
    fieldsets = (
        (None, {'fields': ('icon', 'category', 'tag', 'is_active', 'order')}),
        ('English', {'fields': ('title_en', 'desc_en')}),
        ('Română', {'fields': ('title_ro', 'desc_ro')}),
    )
