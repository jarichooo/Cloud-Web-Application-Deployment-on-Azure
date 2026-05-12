# Azure Resource Deployment Steps (GUI)

The following steps outline the process taken to provision the Azure infrastructure for the Student Enrollment System using the Azure Portal.

## 1. Set up the Resource Group
* **Resource Group:** Created a new Resource Group named `rg-enrollment-project`.
* **Region:** Selected `Malaysia West` as the primary region for all resources.

## 2. Provision the Azure SQL Database
* **SQL Server:** Created a new Azure SQL Server named `enrollment-server`.
* **SQL Database:** Created a new database named `enrollmentdb`.
* **Compute Tier:** Selected the **Basic DTU** tier (5 DTUs, 2GB Storage) for cost-effective hosting.
* **Networking & Security:** 
  * Navigated to the SQL Server's Networking settings.
  * Enabled **"Allow Azure services and resources to access this server"** so the App Service can connect.
  * Ensured public network access was restricted/denied for external IPs.

## 3. Set up the App Service (Web App)
* **App Service Plan:** Created a new plan named `ASP-rgenrollmentproject`.
* **Pricing Tier:** Selected **Basic B1** (Linux OS).
* **Web App:** Created a new Web App named `enrollment-app-csec3`.
* **Runtime Stack:** Selected **Python 3.11**.
* **Security Configuration:** 
  * Enforced **HTTPS Only**.
  * Set the minimum TLS version to **1.2**.

## 4. Configure Authentication & Managed Identity
* **Managed Identity:** Created a **User-Assigned Managed Identity** named `oidc-msi-a2b8`.
* **Assignment:** Assigned this managed identity to the Web App to enable secure, secretless authentication (OIDC) between the App Service and the SQL Database.

## 5. Enable Monitoring & Telemetry
* **Log Analytics Workspace:** Created a `DefaultWorkspace` in Malaysia West for log querying and analytics.
* **Application Insights:** Created an Application Insights resource named `enrollment-app-csec3` and linked it to the Web App for real-time monitoring and exception tracking.
* **Azure Monitor:** Configured Metric Alerts and Smart Detection to trigger email notifications based on resource health.

## 6. Set up Continuous Deployment (CI/CD)
* **Deployment Center:** Navigated to the Deployment Center within the Web App.
* **Source Control:** Selected **GitHub** and authorized the connection.
* **Repository & Branch:** Selected the `jarichooo/Cloud-Web-Application-Deployment-on-Azure` repository and the `main` branch.
* **GitHub Actions:** Allowed Azure to automatically generate and commit the GitHub Actions workflow file to handle the Build and Deploy pipeline on every push.
