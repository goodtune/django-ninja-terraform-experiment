from typing import List

from django.shortcuts import get_object_or_404
from ninja import ModelSchema, NinjaAPI

from manifest.models import Datacenter, Rack

api = NinjaAPI(title="Manifest API", version="1.0.0")


class DatacenterSchema(ModelSchema):
    class Meta:
        model = Datacenter
        fields = "__all__"


class DatacenterCreateSchema(ModelSchema):
    class Meta:
        model = Datacenter
        fields = ["name", "location"]


class RackSchema(ModelSchema):
    class Meta:
        model = Rack
        fields = "__all__"


class RackCreateSchema(ModelSchema):
    class Meta:
        model = Rack
        fields = ["name", "position", "datacenter"]


@api.get("/datacenters", response=List[DatacenterSchema])
def list_datacenters(request):
    return Datacenter.objects.all()


@api.get("/datacenters/{datacenter_id}", response=DatacenterSchema)
def get_datacenter(request, datacenter_id: int):
    return get_object_or_404(Datacenter, id=datacenter_id)


@api.post("/datacenters", response=DatacenterSchema)
def create_datacenter(request, payload: DatacenterCreateSchema):
    datacenter = Datacenter.objects.create(**payload.dict())
    return datacenter


# Add endpoints for Racks
@api.get("/racks", response=List[RackSchema])
def list_racks(request):
    return Rack.objects.all()


@api.get("/racks/{rack_id}", response=RackSchema)
def get_rack(request, rack_id: int):
    return get_object_or_404(Rack, id=rack_id)


@api.post("/racks", response=RackSchema)
def create_rack(request, payload: RackCreateSchema):
    rack = Rack.objects.create(**payload.dict())
    return rack
