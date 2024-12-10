from google.auth.transport.requests import Request
from google.auth import impersonated_credentials
from google.oauth2 import service_account

# Load service account key
service_account_file = "service_account.json"
credentials = service_account.Credentials.from_service_account_file(service_account_file)

# Impersonate another service account
target_principal = "target-service-account@your-project.iam.gserviceaccount.com"
delegated_credentials = impersonated_credentials.Credentials(
    source_credentials=credentials,
    target_principal=target_principal,
    target_scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

# Use impersonated credentials to make an API call
from googleapiclient.discovery import build
service = build('compute', 'v1', credentials=delegated_credentials)
instances = service.instances().list(project='your-project', zone='your-zone').execute()
print(instances)
