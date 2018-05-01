from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Person


class PersonView(ListView):
    template_name = 'index.html'
    model = Person
    context_object_name = 'resume_list'
    queryset = Person.objects.all()

    def contect(self, request):
        return render(request)


class InfoView(ListView):
    template_name = 'detail.html'
    model = Person
    context_object_name = 'resume_list'


def show_user(request, user_id):
    user = get_object_or_404(Person, pk=user_id)
    # email = get_object_or_404(Email, user=user_id)
    context = {
        'user': user,
    }
    return render(request, 'detail.html', context)
