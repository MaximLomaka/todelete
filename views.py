from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from django.http import HttpResponseRedirect, Http404
from .form import *
from django.utils import translation


class PersonView(ListView):
    model = Person
    template_name = 'resumepr/user_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        z = super().get_context_data(object_list=None, **kwargs)

        return z


class InfoView(DetailView):
    template_name = 'resumepr/detail.html'
    model = Person

    def get_context_data(self, **kwargs):
        z = super().get_context_data(**kwargs)
        z['object_list'] = Person.objects.all()
        z['education'] = Education.objects.get(person=kwargs['object'].id)

        z['interest'] = Interest.objects.get(person=kwargs['object'].id)

        z['job'] = Job.objects.get(person=kwargs['object'].id)

        z['contact'] = Contact.objects.get(person=kwargs['object'].id)

        z['social'] = Social.objects.get(person=kwargs['object'].id)
        return z


def get_user(request, pk):
    person = get_object_or_404(Person, pk=pk)
    user_language = 'ru'
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language

    context = {
        'person': person,

    }
    return render(request, 'resumepr/detail.html', context)


class UserUpdate(UpdateView):
    model = Person
    template_name = 'resumepr/form.html'
    form_class = EditUser
    success_url = '/'


class UserSocialCreate(UpdateView):
    form_class = SocialEdit
    model = Social

    template_name = 'resumepr/form.html'
    success_url = '/'


class UserJobCreate(UpdateView):
    form_class = JobEdit
    model = Job

    template_name = 'resumepr/form.html'
    success_url = '/'

    def form_valid(self, form):
        form.save(self.request)
        return redirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit_unit'] = 'edit_phone'
        return context

    def get_object(self, queryset=None):
        obj = Job.objects.get(pk=self.kwargs['job'])
        return obj


class UserContactCreate(UpdateView):
    form_class = ContactEdit
    model = Contact

    template_name = 'resumepr/form.html'
    success_url = '/'


class UserInterestCreate(UpdateView):
    form_class = InterestEdit
    model = Interest

    template_name = 'resumepr/form.html'
    success_url = '/'


class UserEducationCreate(UpdateView):
    form_class = EducationEdit
    model = Education

    template_name = 'resumepr/form.html'
    success_url = '/'


class DeleteUser(DeleteView):
    model = Person
    success_url = reverse_lazy('person-list')
    template_name = 'resumepr/edit_form.html'


class CreateUser(FormView):
    form_class = NewUser
    template_name = 'resumepr/form.html'
    success_url = '/'

    def form_valid(self, form):
        form.save(form)
        return redirect('/')
