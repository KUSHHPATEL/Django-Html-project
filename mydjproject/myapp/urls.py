from django.urls import path
from  . import views
urlpatterns = [
      path ("",views.homepage),
      path ("home",views.homepage),
      path ("about",views.aboutpage),
      path ("contact",views.contactpage),
      path ("contact/Kush",views.contactpage),
      path ("contact/Hemil",views.contactpage),
      path ("form",views.formpageview),
      path ("process",views.formpageprocess)
]