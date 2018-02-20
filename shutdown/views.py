from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render

from shutdown.models import ShutDown

try:
    module_path, ctx_class = settings.SHUTDOWN_CONTEXT.rsplit('.', 1)
    module = __import__(module_path, fromlist=[ctx_class])
    context = getattr(module, ctx_class)
except AttributeError:
    raise ImproperlyConfigured(
        'You must supply a path your own context object by setting a '
        'SHUTDOWN_CONTEXT in your settings.py file.'
    )


def shutdown_view(request):
    objects = ShutDown.objects.all()
    msg = objects[0].message
    ctx = {}
    ctx.update({
        'msg': msg,
    })
    ctx = context(
        request,
        ctx,
        title='Service Outage',
        page_title='Service Outage',
        window_title='Service Outage',
    ).flatten()
    return render(request, template_name='shutdown/shutdown.html', context=ctx)
