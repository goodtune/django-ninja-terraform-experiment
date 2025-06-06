// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package operations

import (
	"github.com/speakeasy/terraform-provider-manifest/internal/sdk/models/shared"
	"net/http"
)

type ManifestAPIV1UpdateDatacenterRequest struct {
	ID         int64             `pathParam:"style=simple,explode=false,name=id"`
	Datacenter shared.Datacenter `request:"mediaType=application/json"`
}

func (o *ManifestAPIV1UpdateDatacenterRequest) GetID() int64 {
	if o == nil {
		return 0
	}
	return o.ID
}

func (o *ManifestAPIV1UpdateDatacenterRequest) GetDatacenter() shared.Datacenter {
	if o == nil {
		return shared.Datacenter{}
	}
	return o.Datacenter
}

type ManifestAPIV1UpdateDatacenterResponse struct {
	// HTTP response content type for this operation
	ContentType string
	// HTTP response status code for this operation
	StatusCode int
	// Raw HTTP response; suitable for custom response parsing
	RawResponse *http.Response
	// OK
	DatacenterResponse *shared.DatacenterResponse
}

func (o *ManifestAPIV1UpdateDatacenterResponse) GetContentType() string {
	if o == nil {
		return ""
	}
	return o.ContentType
}

func (o *ManifestAPIV1UpdateDatacenterResponse) GetStatusCode() int {
	if o == nil {
		return 0
	}
	return o.StatusCode
}

func (o *ManifestAPIV1UpdateDatacenterResponse) GetRawResponse() *http.Response {
	if o == nil {
		return nil
	}
	return o.RawResponse
}

func (o *ManifestAPIV1UpdateDatacenterResponse) GetDatacenterResponse() *shared.DatacenterResponse {
	if o == nil {
		return nil
	}
	return o.DatacenterResponse
}
