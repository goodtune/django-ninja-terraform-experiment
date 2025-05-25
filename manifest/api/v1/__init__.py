from ast import Mod
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
        fields = ["id", "name", "location"]

    model_config = ConfigDict(json_schema_extra={"x-speakeasy-entity": "Datacenter"})


class DatacenterCreate(ModelSchema):
    class Meta:
        model = models.Datacenter
        fields = ["name", "location"]

    model_config = ConfigDict(json_schema_extra={"x-speakeasy-entity": "Datacenter"})


class Rack(ModelSchema):
    class Meta:
        model = models.Rack
        fields = "__all__"

    model_config = ConfigDict(json_schema_extra={"x-speakeasy-entity": "Rack"})


@api.post(
    "/datacenter",
    response=Datacenter,
    openapi_extra={
        "x-speakeasy-entity-operation": "Datacenter#create",
        "x-speakeasy-match": [
            {
                "operationId": "manifest_api_v1_get_datacenter",
                "parameters": {"id": "$response.body.id"},
            }
        ],
    },
)
def create_datacenter(request, payload: Datacenter):
    datacenter = models.Datacenter.objects.create(**payload.dict())
    return datacenter


@api.get(
    "/datacenter/{id}",
    response=Datacenter,
    openapi_extra={"x-speakeasy-entity-operation": "Datacenter#read"},
)
def get_datacenter(request, id: int):
    return get_object_or_404(models.Datacenter, id=id)


@api.post(
    "/datacenter/{id}",
    response=Datacenter,
    openapi_extra={"x-speakeasy-entity-operation": "Datacenter#update"},
)
def update_datacenter(request, id: int, payload: Datacenter):
    datacenter = get_object_or_404(models.Datacenter, id=id)
    for attr, value in payload.dict().items():
        setattr(datacenter, attr, value)
    datacenter.save()
    return datacenter


@api.delete(
    "/datacenter/{id}",
    response=Datacenter,
    openapi_extra={"x-speakeasy-entity-operation": "Datacenter#delete"},
)
def delete_datacenter(request, id: int):
    datacenter = get_object_or_404(models.Datacenter, id=id)
    datacenter.delete()
    return {"success": True}
