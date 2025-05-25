terraform {
  required_providers {
    manifest = {
      source  = "goodtune/manifest"
      version = "0.1.0"
    }
  }
}

provider "manifest" {
  server_url = "http://127.0.0.1:8000"
}
