import json
import os

import jdatetime
from django.contrib import admin
from django.http import FileResponse
from django.utils.safestring import mark_safe

from warehouse.models import DigitalProperty, HouseProperty, CulturalPropertyAssignment, CulturalProperty, \
    CulturalPropertyAddUp
# from warehouse.serializer import DigitalPropertySerializer


@admin.register(DigitalProperty)
class DigitalPropertyAdmin(admin.ModelAdmin):
    using = 'warehouse_db'

    list_display = (
        'digital_property_type',
        'title',
        'registration_code',
        'images_link_display',
        'location',
    )
    list_filter = (
        'digital_property_type',
    )
    readonly_fields = (
        'created_at',
        'created_by',
        'updated_at',
        'updated_by',
    )
    search_fields = (
        'title',
        'registration_code',
        'serial_code_1',
        'serial_code_2',
        'description',
    )

    fields = (
        'digital_property_type',
        'title',
        'description',
        'buying_price',
        'condition',
        'images',
        'registration_code',

        'serial_code_1',
        'serial_code_2',

        'warranty_company',
        'warranty_expiration_date',
        'created_at',
        'created_by',
        'updated_at',
        'updated_by',
        'property_assigned_to',
        'date_of_assignment',
        'date_of_return',
        'location',

    )

    change_form_template = 'custom-warehouse-admin.html'

    @admin.display(description="لینک تصاویر", empty_value='???')
    def images_link_display(self, obj):
        images = obj.images.all()
        html_image_link = f""""""
        i = 1
        for image in images:
            html_image_link += f"""
                            <span>
                                <a href="{image.file.url}" target="_blank">{i}-<img style="max-height: 24px" src="../../../media/file.png" alt="media-file"></a>
                            <span>
                        """
            i += 1
        return mark_safe(html_image_link)

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
            instance.updated_by = user
        if change:
            instance.updated_by = user
        instance.save()
        form.save_m2m()
        return instance

    # @admin.action(description="ساخت بک آپ")
    # def create_backup(self, request, queryset):
    #     digital_properties_serializer = DigitalPropertySerializer(
    #         DigitalProperty.objects.filter(created_by=request.user), many=True)
    #
    #     backup_file_name = 'warehouse-digital-property-section-backup-' + jdatetime.datetime.now().strftime('%Y-%m-%d-%H-%M') + '.json'
    #     os.makedirs(os.path.join('', 'backups'))
    #     with open(os.path.join('backups', backup_file_name), "w") as json_file:
    #         json_response = {
    #             'digital_properties': digital_properties_serializer.data,
    #         }
    #         json_file.write(json.dumps(json_response))
    #     return FileResponse(open(os.path.join('backups', backup_file_name), "rb"))
    #
    # actions = ['create_backup', 'restore_backup', 'export_as_xlsx', ]


@admin.register(HouseProperty)
class HousePropertyAdmin(admin.ModelAdmin):
    using = 'warehouse_db'

    list_display = (
        'house_property_type',
        'title',
        'registration_code',
        'images_link_display',
        'location',
    )
    list_filter = (
        'house_property_type',
    )
    readonly_fields = (
        'created_at',
        'created_by',
        'updated_at',
        'updated_by',
    )
    search_fields = (
        'title',
        'registration_code',
        'full_name',
        'description',
    )

    fields = (
        'house_property_type',
        'title',
        'description',
        'buying_price',
        'condition',
        'images',
        'registration_code',

        'created_at',
        'created_by',
        'updated_at',
        'updated_by',
        'property_assigned_to',
        'date_of_assignment',
        'date_of_return',
        'location',

    )

    change_form_template = 'custom-warehouse-admin.html'

    @admin.display(description="لینک تصاویر", empty_value='???')
    def images_link_display(self, obj):
        images = obj.images.all()
        html_image_link = f""""""
        i = 1
        for image in images:
            html_image_link += f"""
                            <span>
                                <a href="{image.file.url}" target="_blank">{i}-<img style="max-height: 24px" src="../../../media/file.png" alt="media-file"></a>
                            <span>
                        """
            i += 1
        return mark_safe(html_image_link)

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
            instance.updated_by = user
        if change:
            instance.updated_by = user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(CulturalProperty)
class CulturalPropertyAdmin(admin.ModelAdmin):
    using = 'warehouse_db'

    list_display = (
        'cultural_property_type',
        'full_name',
        'description',
        'number_of_inventory',
    )
    list_filter = (
        'cultural_property_type',
    )
    readonly_fields = (
        'number_of_inventory',
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
    )
    search_fields = (
        'cultural_property_type',
        'full_name',
        'description',
    )

    fields = (
        'cultural_property_type',
        'full_name',
        'description',
        'images',
        'number_of_inventory',
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',

    )

    change_form_template = 'custom-warehouse-admin.html'

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
            instance.updated_by = user
        if change:
            instance.updated_by = user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(CulturalPropertyAddUp)
class CulturalPropertyAddUpAdmin(admin.ModelAdmin):
    using = 'warehouse_db'

    list_display = (
        'cultural_property',
        'date_of_addup_display',
        'add_up_number',
    )

    readonly_fields = (
        'created_at',
        'created_by',
    )

    fields = (
        'cultural_property',
        'date_of_addup',
        'add_up_number',
        'created_at',
        'created_by',
    )

    @admin.display(description="تاریخ افزودن", empty_value='???')
    def date_of_addup_display(self, obj):
        data_time = str(obj.date_of_addup.strftime('%Y-%m-%d - %H:%M %Z'))
        return data_time

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
            instance.updated_by = user
        if change:
            instance.updated_by = user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(CulturalPropertyAssignment)
class CulturalPropertyAssignmentAdmin(admin.ModelAdmin):
    using = 'warehouse_db'

    list_display = (
        'cultural_property',
        'send_to',
        'date_of_assign_display',
        'number_of_assigned_property',
    )
    readonly_fields = (
        'created_at',
        'created_by',
    )
    search_fields = (
        'cultural_property',
    )

    fields = (
        'cultural_property',
        'send_to',
        'date_of_assign',
        'number_of_assigned_property',
        'created_at',
        'created_by',

    )

    @admin.display(description="تاریخ تحویل", empty_value='???')
    def date_of_assign_display(self, obj):
        data_time = str(obj.date_of_assign.strftime('%Y-%m-%d - %H:%M %Z'))
        return data_time

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
        instance.save()
        form.save_m2m()
        return instance
