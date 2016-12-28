from django.conf.urls import url
from schedule import views

urlpatterns = [
    url(r'^newrepair$', views.NewRepair, name='NewRepair'),
    # url(r'^myrepairs$', views.my_repairs, name='AllRepairs'),
    # url(r'^post/newrepair$', views.post_new, name='post_new'),

]
