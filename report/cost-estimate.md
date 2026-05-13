# Cost Estimate Report — Student Enrollment System on Azure

## Architecture Summary

The Student Enrollment System is deployed on Microsoft Azure using the following resources:

- **App Service (Basic B1)** — hosts the Flask web application on Linux
- **Azure SQL Database (Basic DTU)** — stores student enrollment records
- **Azure Monitor** — provides application monitoring, alerts, and Application Insights telemetry
- **GitHub Actions (CI/CD)** — free, handles automated deployment on every push to main

All resources are deployed in the **Malaysia West** region under the **Azure for Students** subscription.

---

## Itemized Cost Breakdown

| Service | Description | Est. Monthly Cost |
|---|---|---|
| App Service | Basic B1 — 1 Core, 1.75 GB RAM, 10 GB Storage, Linux OS | $12.46 |
| Azure SQL Database | Single DB, Basic DTU, 5 DTUs, 2 GB storage, 1 instance | $4.97 |
| Azure Monitor | Log analytics, Application Insights, Alert rules | $0.00 |
| GitHub Actions | CI/CD pipeline (free tier) | $0.00 |
| **Total** | | **~$17.43/month** |

*Estimates generated via Azure Pricing Calculator on May 12, 2026.*

---

## Cost Optimization Notes

1. **Scale down after grading** — Delete or stop the App Service and SQL Database immediately after grading to avoid continued charges. The Azure for Students $100 credit covers ~5 months at this rate.

2. **Use Free tier App Service for development** — The F1 (Free) tier is sufficient for testing and development. Upgrade to B1 only when demonstrating the live app.

3. **Use Azure Functions instead of App Service** — Refactoring the Flask app to Azure Functions (Consumption Plan) would reduce cost to near zero since billing is per-execution rather than per-hour. For a low-traffic enrollment system this would be significantly cheaper.

4. **Downsize SQL to Serverless** — Switching to Azure SQL Serverless (auto-pause after inactivity) would eliminate costs during idle periods like nights and weekends.
