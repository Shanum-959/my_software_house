# # backup.py
# import os
# import datetime
# from django.conf import settings
# from django.core.management import call_command

# # Make sure this uses the correct path for your environment
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # Format: backup_YYYYMMDD_HHMMSS.json
# filename = f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
# backup_path = os.path.join(BASE_DIR, "backups")

# # Ensure the folder exists
# os.makedirs(backup_path, exist_ok=True)

# # Full path to the backup file
# full_path = os.path.join(backup_path, filename)

# # Dump data
# call_command("dumpdata", "--natural-foreign", "--natural-primary", "--exclude", "contenttypes", "--exclude", "auth.permission", output=full_path)

# print(f"✔ Backup created at: {full_path}")
