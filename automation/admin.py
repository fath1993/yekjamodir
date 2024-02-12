from django.contrib import admin

from automation.models import Role, ProjectMember, Project, Envelop, ProjectInvite, Announcement


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'access_level',
        'created_at',
        'created_by',
    )

    readonly_fields = (
        'created_at',
        'created_by',
    )

    fields = (
        'title',
        'access_level',
        'created_at',
        'created_by',
    )

    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.created_by = request.user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = (
        'member',
        'role',
        'updated_at',
        'updated_by',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
    )

    fields = (
        'member',
        'role',
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
    )

    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.created_by = request.user
            instance.updated_by = request.user
        else:
            instance.updated_by = request.user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'updated_at',
        'updated_by',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
    )

    fields = (
        'title',
        'description',
        'members',
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
    )

    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.created_by = request.user
            instance.updated_by = request.user
        else:
            instance.updated_by = request.user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(ProjectInvite)
class ProjectInviteAdmin(admin.ModelAdmin):
    list_display = (
        'project',
        'suggested_role',
        'user',
        'is_accepted',
        'updated_at',
        'updated_by',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
    )

    fields = (
        'project',
        'suggested_role',
        'user',
        'is_accepted',
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
    )

    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.created_by = request.user
            instance.updated_by = request.user
        else:
            instance.updated_by = request.user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(Envelop)
class EnvelopAdmin(admin.ModelAdmin):
    list_display = (
        'project',
        'title',
        'description',
        'updated_at',
        'updated_by',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
    )

    fields = (
        'project',
        'title',
        'description',
        'content',
        'member_from',
        'member_to',
        'mailing_history',
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
    )

    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.created_by = request.user
            instance.updated_by = request.user
        else:
            instance.updated_by = request.user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = (
        'receiver',
        'message',
        'created_at',
        'created_by',
    )

    readonly_fields = (
        'created_at',
        'created_by',
    )

    fields = (
        'receiver',
        'message',
        'created_at',
        'created_by',
    )

    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.created_by = request.user
        instance.save()
        form.save_m2m()
        return instance
