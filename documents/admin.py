from django.contrib import admin

from documents.models import Folder, Document


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = (
        'folder_name_display',
        'parent',
    )
    search_fields = (
        'title',
        'parent',
    )
    readonly_fields = (
        'id',
        'created_at',
        'created_by',
    )
    fields = (
        'id',
        'parent',
        'title',
        'created_at',
        'created_by',
    )

    @admin.display(description="نام پوشه", empty_value='???')
    def folder_name_display(self, obj):
        return obj.title + ' | ' + str(obj.id)

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        instance.created_by = user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'folder',
        'title',
        'description',
        'date_of_edit_display',
    )
    search_fields = (
        'folder',
        'title',
        'description',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
        'created_by',
        'document_parent',
    )
    fields = (
        'id',
        'folder',
        'title',
        'description',
        'content',
        'files',
        'allowed_to',
        'created_at',
        'updated_at',
        'created_by',
        'document_parent',
    )

    @admin.display(description="تاریخ آخرین ویرایش", empty_value='???')
    def date_of_edit_display(self, obj):
        data_time = str(obj.updated_at.strftime('%Y-%m-%d - %H:%M'))
        return data_time

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change:
            instance.created_by = user
            instance.updated_by = user
        else:
            instance.updated_by = user
        instance.save()
        form.save_m2m()
        return instance