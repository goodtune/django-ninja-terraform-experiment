resource "manifest_datacenter" "use1" {
  name     = "us-east-1"
  location = "North Virginia"
}

resource "manifest_datacenter" "apse2" {
  name     = "ap-southeast-2"
  location = "Sydney"
}

resource "manifest_datacenter" "apse1" {
  location = "Singapore"
  name     = "ap-southeast-1"
}
