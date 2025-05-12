Azure Security Scripts
======================

This repository contains code samples for automating security controls in Microsoft Azure.

Contents
--------

1. Enforce_mfa_policy.json  
   ARM template that deploys a Conditional Access policy requiring Multi-Factor Authentication (MFA) for every user. New users are covered automatically.

   Ccreate_mfa_policy.py  
   Python script that uses Microsoft Graph to create (or update) the same Conditional Access policy.
   
3. Enforce_password_policy.json**  
   ARM template that enforces password policies such as minimum length, expiration, history, and character requirements.

4. Create_password_policy.py**  
   Python script that uses Microsoft Graph to create (or update) a password policy in Azure Active Directory.


Prerequisites
-------------

* Global Administrator or Conditional Access Administrator and Security Administrator role
* Azure CLI 2.58 or later (for ARM deployment)  
  or Python 3.8+ with `msal` and `requests` modules (for the script)
* An Azure AD app registration with the permission `Policy.ReadWrite.ConditionalAccess` (application type) and admin consent granted

## How to Use

### Step 1: Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/Rejoice-Okafor/security-scripts.git

cd security-scripts
```

### Option 1: Deploy with an ARM Template

a) Log in to Azure:

```bash
az login --tenant <tenant-id>
```

b) Deploy the mfa policy:

```
az deployment tenant create \
  --name enforceMfaPolicy \
  --location westus \
  --template-file enforce_mfa_policy.json
```

c) Deploy passowrd Policy

```
az deployment tenant create \
  --name enforcePasswordPolicy \
  --location westus \
  --template-file enforce_password_policy.json
```

Option 2: Run the Python Script
a) Install the necessary Python libraries:

```
pip install msal requests
```
b) Run the script to create or update the MFA policy:

```
python create_mfa_policy.py
```
c) Run the password policy script

  ```
python create_password_policy.py
```
### Notes

Conditional Access is the recommended way to enforce MFA.

The policy targets All users. Adjust the JSON or Python body if you prefer to scope it to a group.


