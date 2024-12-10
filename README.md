# Cloud Zero Trust Security Lab

This repository demonstrates advanced cloud security techniques with a focus on **Zero Trust Architecture (ZTA)** principles. It includes practical implementations for securing multi-cloud environments (AWS, Azure, GCP) using tools and frameworks like **Zero Trust Network Access (ZTNA)**, identity management, and workload isolation.

## Key Features
1. **Micro-Segmentation in AWS VPC**  
   - Implements fine-grained network segmentation in AWS.  
   - [Guide](./aws_microsegmentation.md)

2. **Azure AD Conditional Access Policy Automation**  
   - Enforces access restrictions based on user and device context.  
   - [Script](./azure_conditional_access.py)

3. **GCP Workload Identity Federation**  
   - Replaces long-lived credentials with short-lived tokens for GCP workloads.  
   - [Script](./gcp_identity_federation.py)

4. **Zero Trust Policy-as-Code**  
   - Automates security policies using Infrastructure as Code (IaC).  
   - [Policies](./policy_as_code/)

5. **Zero Trust SOC Use Case Mapping**  
   - Maps lab configurations to actionable SOC use cases.  
   - [Document](./zero_trust_soc_use_cases.md)

## Trending Technologies Covered
- Zero Trust Network Access (ZTNA)  
- Identity and Access Management (IAM) Best Practices  
- Security Policy Automation  
- Workload and Data Isolation in Cloud  

## Disclaimer
This repository is for educational purposes. Please test these implementations in a controlled environment.
