terraform {
  backend "azurerm" {
    resource_group_name  = "hihi"          
    storage_account_name = "tfmasterhi"                              
    container_name       = "tfstate"                              
    key                  = "terraform.tfstate"               
    use_oidc             = true                                  
    client_id            = "value" 
    subscription_id      = "value"  
    tenant_id            = "value"
    
   
   
   
   
  }
}
