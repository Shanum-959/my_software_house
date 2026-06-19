<div align="center">

# My Software House

### A Full-Stack Django Platform for Software Agencies

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.3-0C4B33?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![REST API](https://img.shields.io/badge/DRF-REST%20API-A30000?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![License](https://img.shields.io/badge/License-MIT-2D9CDB?style=for-the-badge)](#license)

</div>

---

## Overview

**My Software House** is a modular Django web application designed to power the digital presence of a software development agency. It brings together a public-facing marketing site, a careers portal, a blog, a portfolio showcase, and a newsletter system into a single, maintainable codebase.

The project is structured around independent Django apps, each responsible for a single area of the business — making it straightforward to extend, maintain, or deploy individual modules as the platform grows.

> **Project Status:** Actively developed. Core modules are functional; some features such as the client portal and AI chatbot are in progress.

---

## Table of Contents

- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Running the Project](#running-the-project)
- [Modules](#modules)
- [Security Notes](#security-notes)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)

---

## Key Features

| Capability | Description |
|---|---|
| Modular Architecture | 12+ independent Django apps, each scoped to a single domain (blog, careers, portfolio, services, etc.) |
| REST API Layer | Built with Django REST Framework for integration with external clients and frontends |
| Admin Dashboard | Full Django admin for managing content, applications, and submissions |
| Careers Module | Job listings with resume upload and application tracking |
| Newsletter System | Subscriber capture with serializer-based API support |
| Portfolio Showcase | Dynamic project/case study listings with detail pages |
| Media Handling | Image uploads via Pillow with organized media storage |
| Environment-Based Config | Separate settings for development and production via environment variables |
| CORS Support | Configurable cross-origin access for frontend integrations |

---

## Tech Stack

**Backend**
Django 5.2.3 · Django REST Framework · PostgreSQL · SQLite (development)

**Supporting Libraries**
Pillow (media processing) · django-cors-headers · django-meta · django-robots · django-seo2 · sqlparse

**Tooling**
Git & GitHub · Python Virtual Environments · `.env`-based configuration

---

## Project Structure

```
my_software_house/
├── assets/                 Centralized static files (CSS, JS, images)
├── blog/                   Blog posts and listings
├── careers/                 Job postings and applications
├── chatbot/                 Chatbot integration module
├── core/                    Landing pages, shared templates, error pages
├── newsletter/               Newsletter subscription and API
├── portfolio/                Portfolio and case study showcase
├── services/                  Services offered by the agency
├── media/                    Uploaded media files
├── mysite/
│   ├── settings/
│   │   ├── base.py         Shared settings
│   │   ├── dev.py          Development overrides
│   │   └── prod.py         Production overrides
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
├── requirements.txt
└── backup.py
```

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- PostgreSQL (for production use; SQLite is used by default in development)
- pip and virtualenv

### Installation

```bash
git clone https://github.com/Shanum-959/my_software_house.git
cd my_software_house
```

Create and activate a virtual environment:

```bash
python -m venv venv

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

This project reads sensitive configuration from environment variables rather than storing them in source code. Create a `.env` file in the project root (this file is excluded from version control via `.gitignore`):

```
SECRET_KEY=your-django-secret-key
DEBUG=True
DB_NAME=mysoftwarehouse
DB_USER=postgres
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=5432
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-app-password
```

A `SECRET_KEY` can be generated with:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## Running the Project

Apply migrations:

```bash
python manage.py migrate
```

Create an administrator account:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`, and the admin dashboard at `http://127.0.0.1:8000/admin/`.

---

## Modules

| App | Purpose |
|---|---|
| `core` | Home page, about/contact pages, shared header and footer templates, custom error pages |
| `services` | Listing and detail pages for agency services |
| `portfolio` | Project case studies and portfolio detail views |
| `blog` | Blog post listing and detail pages |
| `careers` | Job listings, applications, and resume submissions |
| `newsletter` | Subscriber capture with API serializer support |
| `chatbot` | Chatbot interface and supporting logic |
| `assets` | Shared static assets used across the platform |

---

## Security Notes

- No credentials, API keys, or database passwords are hardcoded in this repository. All sensitive values are loaded through environment variables.
- The `.env` file is excluded from version control via `.gitignore` and must be created locally by each developer or deployment environment.
- `DEBUG` should always be set to `False` in any production deployment.
- Before deploying, generate a unique `SECRET_KEY` and configure `ALLOWED_HOSTS` with your actual domain.

---

## Roadmap

- [ ] Complete client portal module
- [ ] Expand chatbot functionality
- [ ] Add automated test coverage across all apps
- [ ] Containerize the application with Docker
- [ ] Set up CI/CD pipeline for automated deployment

---

## Contributing

Contributions are welcome. If you would like to propose a significant change, please open an issue first to discuss what you would like to modify.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## Contact

**Developed by:** Shanum Shahzad
**Email:** shanumshahzad01@gmail.com
**Repository:** [github.com/Shanum-959/my_software_house](https://github.com/Shanum-959/my_software_house)

---

## License

This project is available for personal and educational use. Contact the developer for licensing inquiries regarding commercial use.

<div align="center">

---

Built with Django

</div>
