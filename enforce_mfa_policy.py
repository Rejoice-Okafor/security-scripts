import msal
import requests
import sys

tenant_id     = "YOUR_TENANT_ID"
client_id     = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

authority = f"https://login.microsoftonline.com/{tenant_id}"
scope     = ["https://graph.microsoft.com/.default"]
graph_url = "https://graph.microsoft.com/beta/identity/conditionalAccess/policies"

app = msal.ConfidentialClientApplication(
    client_id, authority=authority, client_credential=client_secret
)
token = app.acquire_token_for_client(scopes=scope)
if "access_token" not in token:
    sys.exit("Authentication failed")

headers = {
    "Authorization": f"Bearer {token['access_token']}",
    "Content-Type": "application/json"
}

policy_body = {
    "displayName": "Require MFA for all users",
    "state": "enabled",
    "conditions": {
        "users": {
            "includeUsers": ["All"]
        },
        "applications": {
            "includeApplications": ["All"]
        }
    },
    "grantControls": {
        "operator": "OR",
        "builtInControls": ["mfa"]
    }
}

# Check if a policy with that name already exists
existing = requests.get(graph_url, headers=headers).json().get("value", [])
match = next((p for p in existing if p["displayName"] == policy_body["displayName"]), None)

if match:
    policy_id = match["id"]
    resp = requests.patch(f"{graph_url}/{policy_id}", headers=headers, json=policy_body)
    action = "updated"
else:
    resp = requests.post(graph_url, headers=headers, json=policy_body)
    action = "created"

if resp.status_code in (200, 201, 204):
    print(f"Policy {action} successfully")
else:
    print("Error:", resp.status_code, resp.text)
