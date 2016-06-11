"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from first.views import list_medicine, get_medicament_form, save_medicine
from first.views import home
from first.views import drugstore, meds, home
from first import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^medicamente/$', list_medicine, name='list_medicine'),
    url(r'^get-medicament-form/$', get_medicament_form),
    url(r'^save-medicament/$', save_medicine, name='save_medicine'),
    url(r'^home/$', home, name = 'home'),
    url(r'^meds/$', views.meds, name = 'meds'),
    url(r'^drugstore/$', drugstore, name='drugstore'),
    url(r'^signup/$', views.signup, name='signup'),
   # url(r'^login/$', views.login, name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

