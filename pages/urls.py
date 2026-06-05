from django.urls import path

from .views import HomePageView, AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]


# DevOps Autopilot: Prometheus instrumentation
from django.urls import include as _dap_include, path as _dap_path
urlpatterns = list(urlpatterns) + [_dap_path('', _dap_include('django_prometheus.urls'))]
