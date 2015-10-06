from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.template.response import TemplateResponse 
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.detail import *
from django.utils.translation import ugettext_lazy as _

from extra_views import ModelFormSetView

from mds.core.models import *
from mds.tasks.models import *
from mds.core.forms import *
from .forms import *
from ..views import ModelFormMixin, ModelListMixin, ModelSuccessMixin

__all__ = [
    'SurgicalSubjectListView',
    'SurgicalSubjectCreateView',
    'SurgicalSubjectUpdateView',
    'SurgicalSubjectDetailView',
]

class SurgicalSubjectListView(ModelListMixin, ListView):
    model = SurgicalSubject
    default_sort_params = ('system_id', 'asc')
    fields = ('system_id', 'family_name', 'given_name', 'gender', 'dob','voided')
    template_name = "web/list.html"
    paginate_by=10

class SurgicalSubjectCreateView(ModelFormMixin,ModelSuccessMixin,CreateView):
    model = SurgicalSubject
    form_class = SurgicalSubjectForm
    template_name = "web/form_new.html"

class SurgicalSubjectUpdateView(ModelFormMixin, ModelSuccessMixin,UpdateView):
    model = SurgicalSubject
    form_class = SurgicalSubjectForm
    template_name = 'web/form.html'

class SurgicalSubjectDetailView(ModelFormMixin,DetailView):
    model = SurgicalSubject
    template_name = 'web/detail.html'
    context_object_name = 'surgicalsubject'
    slug_field = 'uuid'

class EncounterTaskSetView(ModelFormSetView):
    template_name = 'web/formset.html'
    model = EncounterTask
    form_class = SimpleEncounterTaskSetForm
    