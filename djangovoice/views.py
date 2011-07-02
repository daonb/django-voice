from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.util import ValidationError
from django.contrib.auth.decorators import login_required
from djangovoice.models import Feedback
from djangovoice.forms import *
from djangovoice.utils import paginate
from django.utils import simplejson
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
import datetime
import time


class FeedbackDetailView(DetailView):

    template_name = 'djangovoice/detail.html'
    model = Feedback

    def get(self, request, *args, **kwargs):
        feedback = self.get_object()

        if feedback.private:
            if not request.user.is_staff and reuqesst.user != feedback.user:
                return Http404

        return super(FeedbackDetailView, self).get(request, *args, **kwargs)

# FIXME: Can not we use ListView?
class FeedbackListView(TemplateView):

    template_name = 'djangovoice/list.html'

    def get_context_data(self, **kwargs):
        context = super(FeedbackListView, self).get_context_data(**kwargs)
        feedback = Feedback.objects.all().order_by('-created')
        feedback_list = kwargs.get('list', 'open')
        feedback_type = kwargs.get('type', 'all')
        feedback_status = kwargs.get('status', 'all')

        if feedback_list == 'open':
            title = _("Open Feedback")
            feedback = feedback.filter(status__status='open')
        elif feedback_list == 'closed':
            title = _("Closed Feedback")
            feedback = feedback.filter(status__status='closed')
        elif feedback_list == 'mine':
            title = _("My Feedback")
            feedback = feedback.filter(user=self.request.user)
        else:
            title = _("Feedback")

        if feedback_type != 'all':
            feedback = feedback.filter(type__slug=feedback_type)

        if feedback_status != 'all':
            feedback = feedback.filter(status__slug=feedback_status)

        if not self.request.user.is_staff:
            feedback = feedback.filter(private=False)

        feedback_page = paginate(feedback, 10, self.request)

        context.update({
                'feedback_list': feedback_page.object_list,
                'pagination': feedback_page,
                'list': feedback_list,
                'status': feedback_status,
                'type': feedback_type,
                'navigation_active': feedback_list,
                'title': title})

        return context

    def get(self, request, *args, **kwargs):
        if kwargs.get('list') == 'mine' and not request.user.is_authenticated():
            return HttpResponseRedirect(
                '%s?next=%s' % (reverse('django.contrib.auth.views.login'),
                                request.path))
        return super(FeedbackListView, self).get(request, *args, **kwargs)

@login_required
def widget(request):
    if request.method == 'POST':
        form = WidgetForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            try:
                if form.data['anonymous'] != "on":
                    feedback.user = request.user
            except:
                    feedback.user = request.user
            feedback.save()
            data = simplejson.dumps(
                {'url': feedback.get_absolute_url(),
                 'errors': False})
        else:
            data = simplejson.dumps({'errors': True})

        return HttpResponse(data, mimetype='application/json')
    else:
        form = WidgetForm()

    return render_to_response(
        'djangovoice/widget.html', {
            'form': form},
        context_instance=RequestContext(request))


class FeedbackSubmitView(FormView):

    template_name = 'djangovoice/submit.html'
    form_class = WidgetForm

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super(FeedbackSubmitView, self).get(request, *args, **kwargs)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        return super(FeedbackSubmitView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        feedback = form.save(commit=False)
        if form.data.get('anonymous') != 'on':
            feedback.user = request.user

        feedback.save()

        return HttpResponseRedirect(feedback.get_absolute_url())


@login_required
def edit(request, object_id):
    feedback = get_object_or_404(Feedback, pk=object_id)

    if request.user.is_staff:
        form_class = EditForm
    elif request.user == feedback.user:
        form_class = WidgetForm
    else:
        return Http404

    if request.method == 'POST':
        form = form_class(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(feedback.get_absolute_url())
    else:
        form = form_class(instance=feedback)

    return render_to_response(
        'djangovoice/edit.html', {
            'form': form,
            'feedback': feedback},
        context_instance=RequestContext(request))


@login_required
def delete(request, object_id):
    feedback = get_object_or_404(Feedback, pk=object_id)
    if request.user != feedback.user and not request.user.is_staff:
        return Http404
    if request.method == 'POST':
        feedback.delete()
        return HttpResponseRedirect(reverse('feedback_home'))

    return render_to_response(
        'djangovoice/delete.html', {
            'feedback': feedback},
        context_instance=RequestContext(request))
