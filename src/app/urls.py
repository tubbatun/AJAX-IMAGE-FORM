from django.conf.urls import url


from .views import (
    immage_add,
    )

urlpatterns = [
    url(r'^$', immage_add, name='image'),

]