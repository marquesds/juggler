from django.conf.urls import url

urlpatterns = [
    url(r'^', 'web.workers.views.index', name='index')
]
