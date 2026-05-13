# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- Instead of viewing every enrollments, the developers changed it so that only the information of the enrollee is displayed after their initial enrollment.

### Changed
- Changed our mode of displaying the results for security reasons
- Modified our workflow to prevent deploying when there are edits and commits on markdowns and reports

### Fixed
- Fixed major deployment issues in the Connection String to proceed with Deployment to Azure

### Removed
- Removed frontend and backend directory. The developers decided to merge the frontend and backend since it's a simple web application. And the focus of the task is Cloud Architecture.

---

## [2026-05-12] - Azure Web App Deployment with Flask Enrollment System

### Added
- `johnlouie2004` - Added diagram to the repository
- `jarichooo` - Initial directories and files for project structure
- `ven-62` - Initial HTML and CSS for enrollment UI
- `jarichooo` - Backend Flask API with core functionality
- `jarichooo` - Azure App Service build and deployment workflow configuration
- `jarichooo` - Index and results HTML templates for enrollment forms
- `ven-62` - Frontend-backend connection and template rendering functionality

### Changed
- `jarichooo` - Modified app.py multiple times for routing and functionality improvements
- `jarichooo` - Switched to REST API routes for better API design
- `jarichooo` - Modified requirements.txt to include necessary Python dependencies
- `ven-62` - Refactored Flask app to unified app/ folder structure and fixed CI/CD workflow paths
- `jarichooo` - Modified index and results templates for improved UI/UX
- `jarichooo` - Updated app.py for enhanced form processing

### Fixed
- `jarichooo` - Fixed workflow configuration for GitHub Actions CI/CD pipeline
- `jarichooo` - Fixed and corrected workflow code for Azure deployment
- `jarichooo` - Corrected CI/CD workflow paths and package structure
- `jarichooo` - Fixed package path in deployment workflow from `app/` to `.` for proper artifact deployment
- `ven-62` - Fixed workflow code and requirements compatibility issues

### Removed
- `jarichooo` - Removed .env file from version control to protect sensitive credentials


## [2026-05-13] - Azure Web App Deployment with Flask Enrollment System

### Added
- `johnlouie2004` - Added azure_cost-estimate.png
- `johnlouie2004` - Added cost_estimate.png
- `johnlouie2004` - Added estimate.png

### Chamged
- `johnlouie2004` - Updated cost-estimate.md

### Removed
- `johnlouie2004` - Removed azure_cost-estimate.png
- `johnlouie2004` - Removed cost_estimate.png
- `johnlouie2004` - Removed estimate.png
