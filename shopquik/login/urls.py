from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin/$', views.signin, name="signin"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^signin/profile/$',views.profile,name="profile"),
    url(r'^signin/profile/createlist/$',views.createlist,name="createlist"),
    url(r'^signin/profile/updatestore/$',views.updatestore,name="updatestore"),
    url(r'^signin/profile/list/$',views.addItems,name="addItem"),
    url(r'^signin/profile/list/stores/$',views.stores,name="stores"),
    url(r'^signin/profile/list/stores/map$',views.map,name="map")

]