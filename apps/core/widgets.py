from django import forms

from .icons import render_icon


class IconPickerWidget(forms.RadioSelect):
    """A visual icon picker: renders each choice as a clickable tile showing the
    actual SVG glyph (plus its name) instead of a plain text dropdown."""

    template_name = 'core/widgets/icon_picker.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        # Attach the rendered SVG to every option so the template can draw it.
        for _group, options, _index in context['widget']['optgroups']:
            for option in options:
                option['svg'] = render_icon(str(option['value']), size=26)
        return context
