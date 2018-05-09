from django import forms
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from resume.models import *


class Regestation(forms.Form):
    first_name = forms.CharField(label='Name*', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='last name*', max_length=20,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    b_date = forms.DateField(label='date of birth*',
                             widget=forms.DateInput(attrs={'type': 'date',
                                                           'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.DateInput(attrs={
        'class': 'form-control'}))
    phone = forms.CharField()

    twitter = forms.CharField(label='twitter', max_length=30)
    facebook = forms.CharField(max_length=30, )
    instagram = forms.CharField(max_length=30, )
    telegram = forms.CharField(max_length=30, )
    skype = forms.CharField(max_length=30, )

    start_date = forms.DateField()
    finish_date = forms.DateField()
    place_study = forms.CharField(max_length=30, )
    speciality = forms.CharField(max_length=30, )
    type = forms.CharField(max_length=10, )

    start_date_job = forms.DateField()
    finish_date_job = forms.DateField()
    place_job = forms.CharField(max_length=30, )
    position = forms.CharField(max_length=30, )

    sport = forms.CharField(max_length=10, )
    music = forms.CharField(max_length=10, )
    food = forms.CharField(max_length=10, )


class EditUser(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
                   }


class SocialEdit(forms.ModelForm):
    class Meta:
        model = Social
        fields = '__all__'


class JobEdit(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'


class ContactEdit(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class EducationEdit(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'


class InterestEdit(forms.ModelForm):
    class Meta:
        model = Interest
        fields = '__all__'


class Info(forms.Form):
    twitter = models.CharField(max_length=30, blank=True)
    facebook = models.CharField(max_length=30, blank=True)
    instagram = models.CharField(max_length=30, blank=True)
    telegram = models.CharField(max_length=30, blank=True)
    skype = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    phone2 = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    email2 = models.EmailField()


class NewUser(forms.Form):
    first_name = forms.CharField(label=_("First name *"),
                                 max_length=50,
                                 widget=forms.TextInput())
    last_name = forms.CharField(label=_("Last name *"),
                                max_length=50,
                                widget=forms.TextInput())
    birthday = forms.DateField(label=_("Birthday *"),
                               widget=forms.TextInput())
    city = forms.CharField(label=_("City *"),
                           max_length=25,
                           widget=forms.TextInput())
    photo = forms.ImageField(label=_("Photo"),
                             required=False,
                             widget=forms.FileInput())
    bio = forms.CharField(label=_("bio "),
                          max_length=100,
                          required=False,
                          widget=forms.Textarea())

    email = forms.EmailField(label=_("Email"),
                            max_length=50,
                            required=False,
                            widget=forms.EmailInput())

    phone = forms.CharField(label=_("Phone"),
                            max_length=20,
                            required=False,
                            widget=forms.TextInput())

    facebook = forms.CharField(label=_("Facebook"),
                               max_length=50,
                               required=False,
                               widget=forms.TextInput())
    skype = forms.CharField(label=_("Skype"),
                            max_length=50,
                            required=False,
                            widget=forms.TextInput())
    twitter = forms.CharField(label=_("Twitter"),
                              max_length=50,
                              required=False,
                              widget=forms.TextInput())
    instagram = forms.CharField(label=_("Instagram"),
                                max_length=50,
                                required=False,
                                widget=forms.TextInput())
    telegram = forms.CharField(label=_("Telegram"),
                               max_length=50,
                               required=False,
                               widget=forms.TextInput())

    edu_place = forms.CharField(label=_("Educational institution"),
                                max_length=50,
                                required=False,
                                widget=forms.TextInput())
    edu_start = forms.CharField(label=_("Start year"),
                                max_length=50,
                                required=False,
                                widget=forms.NumberInput())
    edu_finish = forms.CharField(label=_("Graduate year"),
                                 max_length=50,
                                 required=False,
                                 widget=forms.NumberInput())
    edu_specialization = forms.CharField(label=_("Specialization"),
                                         max_length=50,
                                         required=False,
                                         widget=forms.TextInput())

    job_place = forms.CharField(label=_("Job place"),
                                max_length=50,
                                required=False,
                                widget=forms.TextInput())
    job_position = forms.CharField(label=_("Position"),
                                   max_length=50,
                                   required=False,
                                   widget=forms.TextInput())
    job_start = forms.CharField(label=_("Start year"),
                                max_length=4,
                                required=False,
                                widget=forms.NumberInput())
    job_finish = forms.CharField(label=_("End year"),
                                 max_length=4,
                                 required=False,
                                 widget=forms.NumberInput())

    def save(self,  form):
            #photo = 'photo' in request.FILES and request.FILES['photo'] or None

            person = Person(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                #photo=photo,
               # birthday=form.cleaned_data['birthday'],
                city=form.cleaned_data['city'],
                bio=form.cleaned_data['bio'],
            )
            person.save()

            contact = Contact(
               person=person,
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
            )
            contact.save()



            social = Social(
                person=person,
                facebook=form.cleaned_data['facebook'],
                telegram=form.cleaned_data['telegram'],
                skype=form.cleaned_data['skype'],
                twitter=form.cleaned_data['twitter'],
                instagram=form.cleaned_data['instagram']
            )
            social.save()

            education = Education(
                person=person,
                place=form.cleaned_data['edu_place'],
                start_date=form.cleaned_data['edu_start'],
                finish_date=form.cleaned_data['edu_finish'],
                speciality=form.cleaned_data['edu_specialization']
            )
            education.save()
            job = Job(
                person=person,
                place=form.cleaned_data['job_place'],
                start_date=form.cleaned_data['job_start'],
                finish_date=form.cleaned_data['job_finish'],
                position=form.cleaned_data['job_position']
            )
            job.save()