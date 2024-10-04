terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "4.3.0"
    }
    github = {
      source = "integrations/github"
      version = "6.3.0"
    }
  }
}
provider "github" {
  token = var.github_token
}
provider "azurerm" {
  storage_use_azuread = true
  features {}
}

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Variable

variable "github_token" {
  description = "GitHub Personal Access Token"
  type        = string
}
