from django.db import models

from .icons import ICON_CHOICES


class ContentItem(models.Model):
    """Shared base for the editable homepage cards (icon + bilingual text)."""

    icon = models.CharField(max_length=32, choices=ICON_CHOICES)
    title_en = models.CharField('Title (EN)', max_length=120)
    title_ro = models.CharField('Title (RO)', max_length=120)
    desc_en = models.TextField('Description (EN)')
    desc_ro = models.TextField('Description (RO)')
    order = models.PositiveIntegerField(default=0, db_index=True,
                                        help_text='Lower numbers show first.')
    is_active = models.BooleanField(default=True,
                                    help_text='Untick to hide from the site without deleting.')

    class Meta:
        abstract = True
        ordering = ['order', 'id']

    def __str__(self):
        return self.title_en


class Service(ContentItem):
    class Meta(ContentItem.Meta):
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class AIService(ContentItem):
    badge_en = models.CharField('Badge (EN)', max_length=40, blank=True,
                                help_text='Small pill on the card, e.g. "RAG", "Voice".')
    badge_ro = models.CharField('Badge (RO)', max_length=40, blank=True)

    class Meta(ContentItem.Meta):
        verbose_name = 'AI Service'
        verbose_name_plural = 'AI Services'


class Project(ContentItem):
    CATEGORY_CHOICES = [
        ('web', 'Web'),
        ('ai', 'AI'),
        ('cloud', 'Cloud'),
        ('software', 'Software'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,
                                help_text='Drives the "Our work" filter buttons.')
    tag = models.CharField(max_length=40,
                           help_text='Badge label on the card, e.g. "E-commerce", "WordPress".')

    class Meta(ContentItem.Meta):
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
