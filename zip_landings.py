import shutil
import os

files_to_zip = [
    'disci_google_ads.html',
    'restoran_google_ads.html',
    'donerci_google_ads.html',
    'guzellik_google_ads.html',
    'tadilat_google_ads.html'
]

# Create a temporary directory for zipping
os.makedirs('landing_pages_pack', exist_ok=True)

# Copy files
for f in files_to_zip:
    if os.path.exists(f):
        shutil.copy(f, f'landing_pages_pack/{f}')

# Create zip
shutil.make_archive('/root/clawd/landing_pages_pack', 'zip', 'landing_pages_pack')
