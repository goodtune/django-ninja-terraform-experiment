---
# generated by https://github.com/hashicorp/terraform-plugin-docs
page_title: "manifest Provider"
subcategory: ""
description: |-
  
---

# manifest Provider



## Example Usage

```terraform
terraform {
  required_providers {
    manifest = {
      source  = "speakeasy/manifest"
      version = "0.1.0"
    }
  }
}

provider "manifest" {
  # Configuration options
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `server_url` (String) Server URL
