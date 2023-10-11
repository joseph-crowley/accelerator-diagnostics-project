# DiRPi Accelerator Diagnostics Project - README

## Table of Contents

1. [Introduction](#introduction)
2. [System Overview](#system-overview)
3. [Components and Features](#components-and-features)
4. [Project Structure](#project-structure)
5. [Documentation](#documentation)
6. [Installation](#installation)
7. [Configuration](#configuration)
8. [Usage](#usage)
9. [Contributing](#contributing)
10. [License](#license)

## Introduction

The DiRPi Accelerator Diagnostics Project aims to provide a web-based interface for monitoring and controlling a network of Raspberry Pi devices (DiRPis) connected to detector hardware at accelerator facilities. Developed using the Django framework, the system supports features like user authentication, device management, run management, and advanced data analytics.

## System Overview

### Hardware

- **DiRPi Devices**: Raspberry Pi computers equipped with detector hardware, located in various accelerator facilities.
- **Server**: Latest Mac Mini with 14TB external storage for the database and 256GB local storage for metadata.

### Software Stack

- **Backend**: Django Framework
- **Database**: sqlite3, MongoDB
- **Frontend**: HTML, CSS, JavaScript
- **Data Processing**: Python, ROOT
- **Job Queue Service**: TBD

## Components and Features

The project consists of several Django apps, each responsible for a specific set of features:

### Apps

- **Core**: Manages user authentication and profile settings.
- **Control**: Responsible for DiRPi device and group management.
- **Monitor**: Real-time status tracking of DiRPi devices.
- **Analysis**: Manages data runs and provides analytics and visualization tools.
- **Docs**: Houses documentation, guides, FAQs.
- **Queue**: Manages data processing job queues.

For a more detailed description of the components, models, forms, views, and URLs, please refer to the [Requirements Document](documentation/design.md).

## Project Structure

The Django project is structured into multiple apps, each containing models, views, forms, and templates related to its functionalities. Below is an overview of the directory layout and the role of each component.

- `./DiRPi_Website/`: Root directory for Django settings and configurations.
- `./analysis/`: App for data recording, data analytics, and data visualization.
- `./core/`: App for user authentication, registration, and profile management.
- `./control/`: App for managing DiRPi devices and their configurations.
- `./docs/`: App for documentation and guides.
- `./monitor/`: App for real-time device monitoring and health checks.
- `./queue/`: App for the job queue system.
- `./static/`: Contains static assets like CSS, JavaScript, and images.
- `./templates/`: Contains global templates.
- `./documentation/`: Additional notes and guidelines for developers.

Each app's directory contains:

- `models/`: Defines the data models for the app.
- `views/`: Handles page logic and rendering.
- `forms/`: Contains form classes for user input.
- `templates/`: Contains HTML templates specific to the app.
- `templatetags/`: Contains custom template tags and filters.
- `management/commands/`: Contains custom management commands.
- `tests.py`: For unit tests.
- `urls.py`: Defines URL patterns for the app.

## Documentation

For a detailed overview of the project, including design notes and guidelines for new developers, refer to the files within the `./documentation/` directory.

- `create_app.md`: Guidelines for creating a new app.
- `design.md`: High-level design notes.
- `new_developer.md`: Onboarding guide for new developers.
- `project_structure.md`: Detailed explanation of the project structure.

Feel free to explore the codebase and the accompanying documentation to gain a complete understanding of the project.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/joseph-crowley/accelerator-diagnostics-project.git
   ```

2. Navigate to the project directory:

   ```
   cd accelerator-diagnostics-project
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the server:

   ```
   python manage.py runserver
   ```

## Configuration

- To add a new DiRPi device, navigate to `/devices/` and fill out the form.
- To initiate a new run, go to `/runs/` and click "New Run".

## Usage

- To log in, visit `/login/`.
- To view all DiRPi groups, navigate to `/groups/`.
- For data analytics, visit `/analysis/`.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See `LICENSE.md` for details.

---

For more details, please refer to the [Requirements Document](documentation/design.md). Feel free to reach out for any issues or feature requests.