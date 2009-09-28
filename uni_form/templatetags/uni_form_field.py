from django import template

register = template.Library()

@register.filter
def is_checkbox(field):
    return field.field.widget.__class__.__name__.lower() == "checkboxinput"

@register.filter
def with_class(field):
    class_name = field.field.widget.__class__.__name__
    if class_name == 'FileInput':
        class_name = 'fileUpload'
    else: # make lowerCase
        class_name = ''.join((class_name[0].lower(), class_name[1:]))

    try:
        field.field.widget.attrs['class'] += ' %s' % class_name
    except KeyError:
        field.field.widget.attrs['class'] = class_name
    return unicode(field)

