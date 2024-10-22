from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

STATUS_CHOICES = (
    ('open', _('Open')),
    ('closed', _('Closed')),
)


class Status(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)
    default = models.BooleanField(
        blank=True,
        help_text=_('New feedback will have this status'))
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="open")

    def save(self, *args, **kwargs):
        if self.default == True:
            try:
                default_project = Status.objects.get(default=True)
                default_project.default = False
                default_project.save()
            except:
                pass
        super(Status, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class Type(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)

    def __unicode__(self):
        return self.title


class Feedback(models.Model):
    type = models.ForeignKey(Type, verbose_name=_("Type"))
    title = models.CharField(_("Title"), max_length=500)
    description = models.TextField(_("Description"),
        blank=True,
        help_text=_('This wiill be viewable by other people - '
                    'do not include any private details such as '
                    'passwords or phone numbers here.'))
    anonymous = models.BooleanField(_("Anonymous"),
        blank=True,
        help_text=_('Do not show who sent this'))
    private = models.BooleanField(_("Private"),
        blank=True,
        help_text=_('Hide from public pages. Only site administrators '
                    'will be able to view and respond to this.'))
    user = models.ForeignKey(User, blank=True, null=True,
        verbose_name=_("User"))
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True,
        verbose_name=_("Created at"))
    status = models.ForeignKey(Status, verbose_name=_("Status"))
    duplicate = models.ForeignKey('self', null=True, blank=True,
        verbose_name=_("Duplicate"))

    def save(self, *args, **kwargs):
        try:
            self.status
        except:
            try:
                default = Status.objects.get(default=True)
            except:
                default = Status.objects.filter()[0]
            self.status = default
        super(Feedback, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return ('djangovoice_item', (self.id,))
    get_absolute_url = models.permalink(get_absolute_url)

    def __unicode__(self):
        return self.title
