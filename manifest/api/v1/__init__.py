from typing import List

from django.shortcuts import get_object_or_404
from ninja import ModelSchema, NinjaAPI
from pydantic.json_schema import GenerateJsonSchema
from pydantic import BaseModel, ConfigDict

from manifest import models

api = NinjaAPI(title="Manifest API", version="1.0.0")


class Datacenter(ModelSchema):
    class Meta:
        model = models.Datacenter
        fields = "__all__"

    model_config = ConfigDict(json_schema_extra={"x-speakeasy-entity": "Datacenter"})


class Rack(ModelSchema):
    class Meta:
        model = models.Rack
        fields = "__all__"

    model_config = ConfigDict(json_schema_extra={"x-speakeasy-entity": "Rack"})


@api.post(
    "/datacenter",
    response=Datacenter,
    openapi_extra={"x-speakeasy-entity-operation": "Datacenter#create"},
)
def create_datacenter(request, payload: Datacenter):
    datacenter = Datacenter.objects.create(**payload.dict())
    return datacenter


@api.get(
    "/datacenter/{datacenter_id}",
    response=Datacenter,
    openapi_extra={"x-speakeasy-entity-operation": "Datacenter#read"},
)
def get_datacenter(request, datacenter_id: int):
    return get_object_or_404(Datacenter, id=datacenter_id)


@api.post(
    "/datacenter/{datacenter_id}",
    response=Datacenter,
    openapi_extra={"x-speakeasy-entity-operation": "Datacenter#update"},
)
def update_datacenter(request, datacenter_id: int, payload: Datacenter):
    datacenter = get_object_or_404(Datacenter, id=datacenter_id)
    for attr, value in payload.dict().items():
        setattr(datacenter, attr, value)
    datacenter.save()
    return datacenter


@api.delete(
    "/datacenter/{datacenter_id}",
    response=Datacenter,
    openapi_extra={"x-speakeasy-entity-operation": "Datacenter#delete"},
)
def delete_datacenter(request, datacenter_id: int):
    datacenter = get_object_or_404(Datacenter, id=datacenter_id)
    datacenter.delete()
    return {"success": True}
