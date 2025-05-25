from django.views.generic import DetailView, ListView
from manifest.models import Datacenter, Rack, Server, Switch


class DatacenterListView(ListView):
    model = Datacenter
    context_object_name = "datacenters"


class DatacenterDetailView(DetailView):
    model = Datacenter
    context_object_name = "datacenter"


class RackListView(ListView):
    model = Rack
    context_object_name = "racks"


class RackDetailView(DetailView):
    model = Rack
    context_object_name = "rack"


class SwitchListView(ListView):
    model = Switch
    context_object_name = "switches"


class SwitchDetailView(DetailView):
    model = Switch
    context_object_name = "switch"


class ServerListView(ListView):
    model = Server
    context_object_name = "servers"


class ServerDetailView(DetailView):
    model = Server
    context_object_name = "server"
