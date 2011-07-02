from django.http import HttpResponse

def home(request):
    # TODO: target of url of feedback is hardcoded, make it use 
    # django.core.urlresolvers.reverse.
    return HttpResponse("""
<h1 style="text-align:center">Say hello to my App!</h1>

<p style="text-align:center">Do you want to give feedback to
my app? Than you can use <a href="/feedback/">feedback</a></p>
""")
