# DiRPi Accelerator Diagnostics Project - Requirements Document

## Introduction

This document outlines the detailed requirements for the DiRPi Accelerator Diagnostics Project. The project aims to develop a web-based interface for monitoring and controlling a network of Raspberry Pi devices (DiRPis) connected to detector hardware at accelerator facilities. The project involves multiple stakeholders and locations, including LANL and FEL, and intends to serve different groups working on accelerator diagnostics.

## System Overview

### Hardware

- **DiRPi Devices**: Raspberry Pi computers equipped with detector hardware. There are 15 DiRPi devices distributed across multiple locations like Drift Tube #1, etc.
- **Server**: Latest Mac Mini with 14TB external storage for the database and 256GB local storage for metadata.

### Software Stack

- **Backend**: Django Framework
- **Database**: MongoDB for storing run data and configurations.
- **Frontend**: HTML, CSS, JavaScript for interface design.
- **Data Processing**: Python for data analytics and ROOT for specialized data processing tasks.
- **Job Queue Service**: To be determined for managing data processing tasks.


## Components and Features

### Apps

1. **core**
    - **User Authentication**: Secure access to the application with password-protected user accounts.
    - **User Profile Management**: Allows users to manage their profiles, including settings and preferences.
  
2. **control**
    - **DiRPi Device Management**: Enables users to manage individual DiRPi devices, send configurations, and initiate runs.
  
3. **monitor**
    - **DiRPi Monitoring**: Real-time status tracking of DiRPi devices and groups. Includes ping-based health checks and alerting mechanisms.
  
4. **analysis**
    - **Run Management**: Record, search, and monitor runs. Supports tagging and keyword-based search.
    - **Data Analysis and Visualization**: Data analytics with support for specialized data filters, anomaly detection, and various visualization options.
  
5. **docs**
    - **Documentation**: User guides, FAQs, technical documentation, and self-help resources.
  
6. **queue**
    - **Job Queue Management**: Enables users to queue data processing tasks for both real-time and batch processing.

### Models

1. **User**
    - Custom fields: `associated_groups`, `associated_runs`, `settings`
  
2. **DiRPiGroup**
    - Fields: `group_name`, `location`, `password`, `associated_users`, `health_status`
  
3. **DiRPiDevice**
    - Fields: `device_id`, `group_id`, `configurations`, `status`, `last_ping_time`, `health_status`
  
4. **Run**
    - Fields: `run_id`, `metadata`, `configurations`, `associated_group`, `tags`, `status`
  
5. **DataRecord**
    - Fields: `run_id`, `timestamp`, `data_values`, `anomalies`
  
6. **JobQueue**
    - Fields: `job_id`, `status`, `associated_run`, `created_at`, `completed_at`

7. **Documentation**
    - Fields: `doc_id`, `title`, `content`, `type`
  
### Forms

1. **UserRegistrationForm**
2. **UserLoginForm**
3. **UserSettingsForm**: For updating user settings.
4. **DiRPiGroupForm**
5. **DiRPiDeviceForm**
6. **RunForm**
7. **DataFilterForm**: For selecting data filters during analysis.
8. **JobQueueForm**
9. **DocumentationForm**: For adding or editing documentation.

### Views

1. **HomeView**: Dashboard with an overview of DiRPi groups, runs, and job queue status.
2. **AboutView**
3. **UserRegisterView**
4. **UserLoginView**
5. **UserSettingsView**: User settings page.
6. **DiRPiGroupListView**
7. **DiRPiGroupDetailView**
8. **DiRPiDeviceDetailView**
9. **RunListView**
10. **RunDetailView**
11. **DataAnalysisView**: For performing advanced analytics on a run.
12. **JobQueueView**
13. **DocumentationListView**: List all documentation.
14. **DocumentationDetailView**: View details of a specific document.

### URLs

- `/`: Home
- `/about/`: About
- `/register/`: User Registration
- `/login/`: User Login
- `/settings/`: User Settings
- `/logout/`: User Logout
- `/groups/`: DiRPi Groups
- `/groups/<id>`: DiRPi Group Details
- `/devices/<id>`: DiRPi Device Details
- `/runs/`: Run List
- `/runs/<id>`: Run Details
- `/analysis/<id>`: Data Analysis for a Run
- `/queue/`: Job Queue
- `/docs/`: Documentation List
- `/docs/<id>`: Documentation Details

## Functional Requirements

### User Authentication

- Users must be able to securely login and logout.
- Password recovery options must be available.

### DiRPi Management

- Create, modify, and delete password-protected DiRPi groups.
- Add, modify, and delete individual DiRPi devices within a group.
- View real-time status and configurations of DiRPi devices.
- Monitor for inactivity or malfunction based on DiRPi pings.
- Send configurations to DiRPi devices, which will be applied upon the next ping from the device.

### Data Management

- Initiate, terminate, and monitor data acquisition runs.
- Search for runs based on various metadata such as run number, tags, keywords, dates, number of events, and trigger settings.
- View detailed analytics for each run, including rate as a function of time, pulse height spectra, and other Data Quality Monitoring (DQM) plots.

### Data Processing

- Apply various data processing algorithms including filters for signal correction and anomaly detection.
- User-defined Python or ROOT scripts for custom data processing.
- Machine Learning algorithms for detecting anomalies based on characteristic functions.

### Job Queue

- Users should be able to queue jobs for data processing.
- Support for recalibration and reprocessing of old runs while preserving original data.
  
### Documentation

- Comprehensive user guides and technical documentation focusing on aspects like self-calibration of LYSO, etc.


## Non-Functional Requirements

- **Security**: All groups should be password protected. Additionally, the system should be protected against arbitrary code execution.
- **Concurrent Operations**: Multiple DiRPi devices and data processing jobs must be able to operate concurrently.
- **Extensibility**: The system should be designed to be easily extensible for future features and requirements.
- **Data Integrity**: Ensure all data is consistently recorded and stored. Implement checks to validate the integrity of the data.

## Future Features

- Integration of GPT for automated macro writing tasks and possibly for checking malicious code.
- Specialized data filters for signal correction based on peak width, double peak structure, etc.
