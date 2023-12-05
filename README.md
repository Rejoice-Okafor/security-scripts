# Azure Security Playbooks

This repository contains Ansible playbooks for automating security tasks in Microsoft Azure.

## Playbooks

1. **Enforce MFA for New Users in Azure AD**
   - Playbook: `Enforce_MFA_Azure.yml`
   - Description: Enforces Multi-Factor Authentication (MFA) for new users in Azure Active Directory (Azure AD).
   - Prerequisites:
     - Ansible installed
     - Azure SDK for Python installed
     - Azure authentication credentials configured
   - Instructions:
     1. Modify the playbook with your Azure AD user details.
     2. Run the playbook using the `ansible-playbook` command.

## How to Use

1. Clone this repository to your local machine:

   ```bash
   https://github.com/Rejoice-Okafor/security-scripts.git
Navigate to the playbook you want to use.

Modify the playbook as needed, including specifying your Azure AD user details.

Run the playbook using the following command:

```bash
ansible-playbook Enforce_MFA_Azure.yml
```
