from django import template
from django.utils.safestring import mark_safe

from ..icons import ICONS, DEFAULT_ICON

register = template.Library()


@register.filter
def icon_paths(name):
    """Return the inner SVG markup for an icon name (safe), falling back to the
    default glyph for unknown names. Used by core/includes/icon.html."""
    return mark_safe(ICONS.get(name, DEFAULT_ICON))
