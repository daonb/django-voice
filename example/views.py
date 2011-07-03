from django.core.urlresolvers import reverse
from django.http import HttpResponse

template = """\
<h1 style="text-align:center">Say hello to my App!</h1>
<script type="text/javascript" src="/static/djangovoice/js/djangovoice.js"></script>
<p style="text-align:center">
    Do you want to give feedback to my app? Than you can use <a href="%(feedback_url)s">feedback</a>.
</p>
"""

def home(request):
    return HttpResponse(template % {'feedback_url': reverse('djangovoice_home')})
