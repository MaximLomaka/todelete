from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from resume.models import Person
from . import views
from django.views.generic import DeleteView

urlpatterns = [path('', views.PersonView.as_view(), name='index'),
               path('<int:pk>/', views.InfoView.as_view(), name='info'),
               path('reg/', views.CreateUser.as_view(), name='create user'),
               path('<int:pk>/edit/', views.UserUpdate.as_view(), name='edit'),
               path('<int:pk>/delete/',
                    DeleteView.as_view(model=Person, template_name='resumepr/edit_form.html', success_url='/',
                                       queryset=Person.objects.all())),
               path('<int:pk>/social/', views.UserSocialCreate.as_view(), name='social'),
               path('<int:pk>/job/', views.UserJobCreate.as_view(), name='job'),
               path('<int:pk>/interest/', views.UserInterestCreate.as_view(), name='interest'),
               path('<int:pk>/edu/', views.UserEducationCreate.as_view(), name='education'),
               path('<int:pk>/cont/', views.UserContactCreate.as_view(), name='contact'),

               ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
