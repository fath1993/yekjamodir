from django.contrib.auth.models import User
from django.db import models
from django_jalali.db import models as jmodel

ROLE_ACCESS_LEVEL = (('همه', 'همه'), ('زیردست', 'زیردست'), ('خود', 'خود'))


class Role(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="عنوان")
    access_level = models.CharField(max_length=255, choices=ROLE_ACCESS_LEVEL, null=False, blank=False,
                                    verbose_name="سطح دسترسی")
    created_at = jmodel.jDateTimeField(auto_now_add=True, verbose_name="ساخته شده در")
    created_by = models.ForeignKey(User, related_name='role_created_by', on_delete=models.CASCADE, null=False,
                                   blank=False, verbose_name='ساخته شده توسط')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', ]
        verbose_name = "نقش"
        verbose_name_plural = "نقش ها"


class ProjectMember(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, verbose_name="عضو")
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="نقش")
    created_at = jmodel.jDateTimeField(auto_now_add=True, verbose_name="ساخته شده در")
    updated_at = jmodel.jDateTimeField(auto_now=True, verbose_name="بروز شده در")
    created_by = models.ForeignKey(User, related_name='project_member_created_by', on_delete=models.CASCADE, null=False,
                                   blank=False, verbose_name='ساخته شده توسط')
    updated_by = models.ForeignKey(User, related_name='project_member_updated_by', on_delete=models.CASCADE, null=False,
                                   blank=False, verbose_name='بروز شده توسط')

    def __str__(self):
        return self.member.username

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = "عضو پروژه"
        verbose_name_plural = "اعضای پروژه"


class Project(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="عنوان")
    description = models.CharField(max_length=255, null=False, blank=False, verbose_name="توضیحات")
    members = models.ManyToManyField(ProjectMember, blank=True, verbose_name="اعضا")
    created_at = jmodel.jDateTimeField(auto_now_add=True, verbose_name="ساخته شده در")
    updated_at = jmodel.jDateTimeField(auto_now=True, verbose_name="بروز شده در")
    created_by = models.ForeignKey(User, related_name='project_created_by', on_delete=models.CASCADE, null=False, blank=False, verbose_name='ساخته شده توسط')
    updated_by = models.ForeignKey(User, related_name='project_updated_by', on_delete=models.CASCADE, null=False, blank=False, verbose_name='بروز شده توسط')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه ها"


class ProjectInvite(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False, blank=False, verbose_name="پروژه")
    suggested_role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="نقش پیشنهادی")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, verbose_name="کاربر")
    is_accepted = models.BooleanField(default=False, verbose_name='وضعیت پذیرش')
    created_at = jmodel.jDateTimeField(auto_now_add=True, verbose_name="ساخته شده در")
    updated_at = jmodel.jDateTimeField(auto_now=True, verbose_name="بروز شده در")
    created_by = models.ForeignKey(User, related_name='project_invite_created_by', on_delete=models.CASCADE, null=False,
                                   blank=False, verbose_name='ساخته شده توسط')
    updated_by = models.ForeignKey(User, related_name='project_invite_updated_by', on_delete=models.CASCADE, null=False,
                                   blank=False, verbose_name='بروز شده توسط')

    def __str__(self):
        return f'user: {self.user.username} | project: {self.project.title}'

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = "دعوت به پروژه"
        verbose_name_plural = "دعوت های به پروژه"


class Envelop(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False, blank=False, verbose_name="پروژه")
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="عنوان")
    description = models.CharField(max_length=1000, null=False, blank=False, verbose_name="توضیحات")
    content = models.TextField(null=False, blank=False, verbose_name="محتوا")
    member_from = models.ForeignKey(User, related_name='envelop_member_from', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="ارسال شده از")
    member_to = models.ForeignKey(User, related_name='envelop_member_to', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="ارسال شده به")
    mailing_history = models.JSONField(null=True, blank=True, verbose_name="تاریخچه ارسال")
    created_at = jmodel.jDateTimeField(auto_now_add=True, verbose_name="ساخته شده در")
    updated_at = jmodel.jDateTimeField(auto_now=True, verbose_name="بروز شده در")
    created_by = models.ForeignKey(User, related_name='envelop_created_by', on_delete=models.CASCADE, null=False,
                                   blank=False, verbose_name='ساخته شده توسط')
    updated_by = models.ForeignKey(User, related_name='envelop_updated_by', on_delete=models.CASCADE, null=False,
                                   blank=False, verbose_name='بروز شده توسط')

    def __str__(self):
        return f'title: {self.title} | project: {self.project.title}'

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = "نامه"
        verbose_name_plural = "نامه ها"


class Announcement(models.Model):
    receiver = models.ForeignKey(Project, related_name='announcement_receiver', on_delete=models.CASCADE, null=False, blank=False, verbose_name="گیرنده")
    message = models.TextField(null=False, blank=False, verbose_name='پیام')
    created_at = jmodel.jDateTimeField(auto_now_add=True, verbose_name="ساخته شده در")
    created_by = models.ForeignKey(User, related_name='announcement_created_by', on_delete=models.CASCADE, null=False,
                                   blank=False, verbose_name='ساخته شده توسط')

    def __str__(self):
        return f'receiver: {self.receiver.title} | message: {self.message}'

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = "اعلان"
        verbose_name_plural = "اعلان ها"