import shutil
import os

source_dir = '/root/clawd/site_update/digitaladexpert-cloudflare'
output_filename = '/root/clawd/digitaladexpert_seo_update_v2'

shutil.make_archive(output_filename, 'zip', '/root/clawd/site_update', 'digitaladexpert-cloudflare')
