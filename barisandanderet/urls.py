from django.contrib import admin
from django.urls import path
from about.views import indexabout
from allynda.views import indexallynda
from barisanbilangan.views import indexbarisanbilangan
from deretbilangan.views import indexderetbilangan
from polabilangan.views import indexpolabilangan
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', indexabout),
    path('allynda/', indexallynda),
    path('barisanbilangan/', indexbarisanbilangan),
    path('deretbilangan/', indexderetbilangan),
    path('polabilangan/', indexpolabilangan),
]
