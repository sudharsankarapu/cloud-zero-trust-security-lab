# Micro-Segmentation in AWS VPC

## Objective
Implement micro-segmentation to isolate workloads in an AWS VPC and enforce least-privilege access.

### Steps
1. **Create Security Groups:**
   - Define separate security groups for application, database, and logging tiers.  
     Example:
     ```bash
     aws ec2 create-security-group --group-name AppSG --description "Application Tier Security Group"
     ```

2. **Configure Rules:**
   - Allow only specific ports between tiers:
     - App Tier to DB Tier: Port 3306
     - App Tier to Logging Tier: Port 9200
   - Example:
     ```bash
     aws ec2 authorize-security-group-ingress --group-name AppSG --protocol tcp --port 3306 --source-group DbSG
     ```

3. **Test Traffic:**
   - Use tools like `netcat` to validate allowed/blocked traffic.

## Benefits
- Reduces lateral movement.
- Enforces least privilege access.
