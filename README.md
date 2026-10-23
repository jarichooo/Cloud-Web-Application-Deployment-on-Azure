# Cloud Web Application Deployment on Azure

A student enrollment web application built with Flask and deployed on Microsoft Azure, demonstrating cloud optimization best practices and CI/CD automation.

## Project Overview

This project showcases a full-stack web application that manages student enrollments with a Flask backend, HTML/CSS frontend, and Azure SQL Database integration. The application is deployed on Azure App Service with automated CI/CD pipelines using GitHub Actions, implementing cloud optimizations for security, reliability, and performance.

### Key Features

- **Student Enrollment System** - Web form for students to enroll in courses
- **Enrollment Results** - View the most recent enrollment in the web page and list enrollments through the API
- **Automated Deployment** - GitHub Actions CI/CD pipeline to Azure
- **Secure Authentication** - Azure Managed Identities (OpenID Connect)
- **Application Monitoring** - Azure Application Insights integration
- **Cloud Optimized** - Application Insights, CI/CD automation, and Alerting System

### Technology Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | HTML5, CSS3 |
| **Backend** | Python 3.11, Flask |
| **Database** | Azure SQL Database |
| **Cloud Platform** | Microsoft Azure (App Service, SQL DB) |
| **CI/CD** | GitHub Actions |
| **Monitoring** | Azure Application Insights |
| **Authentication** | Azure Managed Identities (OIDC) |

##  Team Members

- **John Louie Bagaporo** - Documentation 
- **Joshua Jericho D. Barja** - Backend Development & DevOps
- **Ven John Lavapie** - Project Setup and Frontend

##  Youtube Video URL
- [https://youtu.be/ujz42kVA6qs](https://youtu.be/ujz42kVA6qs)

##  Demo URL
- [https://enrollment-app-csec3-hthrfvcxbagcb7bq.malaysiawest-01.azurewebsites.net/](https://enrollment-app-csec3-hthrfvcxbagcb7bq.malaysiawest-01.azurewebsites.net/)

## Methodology

The Flask application accepts student enrollment details through an HTML form or JSON API, inserts them into Azure SQL with parameterized queries, and retrieves enrollment records for display. Azure App Service hosts the application. The deployment workflow uses GitHub Actions, while the documented Azure configuration adds monitoring and alerts.

## Results and Evidence

The source implements form submission (`/submit`), a results page for the latest enrollment (`/results`), and JSON endpoints for creating and listing enrollments (`/api/enroll` and `/api/enrollments`). The [deployment guide](deployment/README.md) records Azure resource setup, database connectivity checks, monitoring, and continuous deployment with screenshots. The demo and video above document the project presentation; current service availability and performance benchmarks are not established by this README.

## Source, Data, and Documentation

- [app/app.py](app/app.py) — Flask routes and SQL access.
- [app/templates/](app/templates/) and [app/static/](app/static/) — frontend templates and styles.
- [app/requirements.txt](app/requirements.txt) — Python dependencies.
- [.github/workflows/](.github/workflows/) — Azure deployment automation.
- [deployment/README.md](deployment/README.md) — resource setup and verification screenshots.
- [diagram/](diagram/) — architecture diagrams.
- [report/cost-estimate.md](report/cost-estimate.md) and [CHANGELOG.md](CHANGELOG.md) — cost planning and development history.

Enrollment records are application data stored in Azure SQL; no downloadable research dataset or database export is included. Use fictional or authorized student details for demonstrations. The application reads its database connection from `AZURE_SQL_CONNECTIONSTRING`.

## Topics

`python` · `flask` · `azure` · `azure-app-service` · `azure-sql` · `github-actions` · `cloud-computing`
