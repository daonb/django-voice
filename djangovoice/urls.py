from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from voting.views import vote_on_object
from djangovoice.models import Feedback
from djangovoice.views import *
from djangovoice.feeds import LatestFeedback


feedback_dict = {
    'model': Feedback,
    'template_object_name': 'feedback'
}

# NOTE: can we do something for pep8 here? lines are too long.
urlpatterns = patterns(
    '',
    url(r'^$', view=FeedbackListView.as_view(), name='djangovoice_home'),
    url(r'^(?P<list>all|open|closed|mine)/$', view=FeedbackListView.as_view(), name='djangovoice_list'),
    url(r'^(?P<list>all|open|closed|mine)/(?P<type>[-\w]+)/$', view=FeedbackListView.as_view(), name='djangovoice_list_type'),
    url(r'^(?P<list>all|open|closed|mine)/(?P<type>[-\w]+)/(?P<status>[-\w]+)/$', view=FeedbackListView.as_view(), name='djangovoice_list_type_status'),
    url(r'^widget/$', view=FeedbackWidgetView.as_view(), name='djangovoice_widget'),
    url(r'^submit/$', view=FeedbackSubmitView.as_view(), name='djangovoice_submit'),
    url(r'^(?P<pk>\d+)/$', view=FeedbackDetailView.as_view(), name='djangovoice_item'),
    url(r'^(?P<pk>\d+)/edit/$', view=FeedbackEditView.as_view(), name='djangovoice_edit'),
    url(r'^(?P<pk>\d+)/delete/$', view=FeedbackDeleteView.as_view(), name='djangovoice_delete'),
    url(r'^(?P<object_id>\d+)/(?P<direction>up|down|clear)/?$', vote_on_object, feedback_dict, name='djangovoice_vote'),
    url(r'^feeds/latest/$', view=LatestFeedback(), name='feeds_latest'),
)
