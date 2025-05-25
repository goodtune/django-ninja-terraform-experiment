from django.urls import path
from manifest.views import (
    DatacenterDetailView,
    DatacenterListView,
    RackDetailView,
    RackListView,
    ServerDetailView,
    ServerListView,
    SwitchDetailView,
    SwitchListView,
)

app_name = "manifest"

urlpatterns = [
    path("datacenters/", DatacenterListView.as_view(), name="datacenter"),
    path("datacenters/<int:pk>/", DatacenterDetailView.as_view(), name="datacenter"),
    path("racks/", RackListView.as_view(), name="rack"),
    path("racks/<int:pk>/", RackDetailView.as_view(), name="rack"),
    path("switches/", SwitchListView.as_view(), name="switch"),
    path("switches/<int:pk>/", SwitchDetailView.as_view(), name="switch"),
    path("servers/", ServerListView.as_view(), name="server"),
    path("servers/<int:pk>/", ServerDetailView.as_view(), name="server"),
]
