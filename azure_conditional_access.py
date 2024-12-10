from azure.identity import ClientSecretCredential
from msgraph.core import GraphClient

# Authenticate using Azure AD App Registration
tenant_id = "<YOUR_TENANT_ID>"
client_id = "<YOUR_CLIENT_ID>"
client_secret = "<YOUR_CLIENT_SECRET>"
credential = ClientSecretCredential(tenant_id, client_id, client_secret)
client = GraphClient(credential)

# Create Conditional Access Policy
policy = {
    "displayName": "Enforce MFA for External Users",
    "state": "enabled",
    "conditions": {
        "users": {"includeExternalUsersOnly": True},
        "applications": {"includeAllApplications": True},
    },
    "grantControls": {"builtInControls": ["mfa"]},
}
response = client.post("/identity/conditionalAccess/policies", json=policy)
print("Policy Created:", response.json())
