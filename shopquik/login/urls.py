from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
<<<<<<< HEAD
    url(r'^signin/$', views.signin, name="signin"),
    url(r'^signup/$', views.signup, name="signup")
=======
>>>>>>> origin/master
]