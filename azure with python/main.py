import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential as D
from azure.mgmt.resource import ResourceManagementClient as R
load_dotenv()

subscription_id =os.environ['AZURE_SUBSCRIPTION_ID']
creds=D()
client=R(creds,subscription_id)

resource_group_name = "my-resource-groupasdf"
location = "centralindia"  

resource_group_params = {
    "location": location
}
client.resource_groups.create_or_update(resource_group_name,resource_group_params)

resourcegroup= client.resource_groups.list()
for i in resourcegroup:
    print(i.name)


