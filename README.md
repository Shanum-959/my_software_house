# my_software_house

A professional software house project built with Django.

##  Features

- Django backend setup
- Modular app structure (16+ apps)
- PostgreSQL database support
- DRF APIs for integration
- File upload with Pillow
- Admin dashboard + client portal
- Newsletter & careers module with resume upload
- Version control with Git & GitHub
- Virtual environment & environment variable support
- Ready for deployment with `.env` support

##  Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Shanum-959/my_software_house.git
   cd my_software_house
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1     # For PowerShell on Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

## 📁 Project Structure

```
my_software_house/
├── accounts/
├── blog/
├── careers/
├── client_portal/
├── core/
├── newsletter/
├── services/
├── ...
├── my_software_house/
│   ├── __init__.py
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── templates/
├── static/
├── backup.py
├── requirements.txt
└── venv/

```
<!-- .env ki file must banani ha wo pari hui ha -->
## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📧 Contact

Developed by **Shanum Shahzad**  
Email: shanumshahzad01@gmail.com
