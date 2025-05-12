Azure Security Scripts
======================

This repository contains code samples for automating security controls in Microsoft Azure.

Contents
--------

1. enforce_mfa_policy.json  
   ARM template that deploys a Conditional Access policy requiring Multi-Factor Authentication (MFA) for every user. New users are covered automatically.

2. create_mfa_policy.py  
   Python script that uses Microsoft Graph to create (or update) the same Conditional Access policy.

Prerequisites
-------------

* Global Administrator or Conditional Access Administrator role
* Azure CLI 2.58 or later (for ARM deployment)  
  or Python 3.8+ with `msal` and `requests` modules (for the script)
* An Azure AD app registration with the permission `Policy.ReadWrite.ConditionalAccess` (application type) and admin consent granted

Quick start
-----------

### Option 1: Deploy with an ARM Template

Log in to Azure:

```bash
az login --tenant <tenant-id>
```

Deploy the policy:

```
az deployment tenant create \
  --name enforceMfaPolicy \
  --location westus \
  --template-file enforce_mfa_policy.json


