
import os
from datetime import datetime

# --- 1. SITEMAP GENERATION ---

base_url = "https://digitaladexpert.de"
last_mod = datetime.now().strftime("%Y-%m-%d")

# Define all pages
pages = [
    # Home
    {"loc": "/", "priority": "1.0", "changefreq": "daily"},
    {"loc": "/tr/", "priority": "0.9", "changefreq": "weekly"},
    {"loc": "/de/", "priority": "0.9", "changefreq": "weekly"},
    {"loc": "/en/", "priority": "0.9", "changefreq": "weekly"},
    
    # TR Pages
    {"loc": "/tr/nakliyat_google_ads.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/tr/disci_google_ads.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/tr/emlak_google_ads.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/tr/restoran_google_ads.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/tr/donerci_google_ads.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/tr/guzellik_google_ads.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/tr/tadilat_google_ads.html", "priority": "0.8", "changefreq": "monthly"},
    
    # DE Pages
    {"loc": "/de/umzug_marketing.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/de/zahnarzt_marketing.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/de/immobilien_marketing.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/de/gastro_marketing.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/de/imbiss_marketing.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/de/kosmetik_marketing.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/de/handwerker_marketing.html", "priority": "0.8", "changefreq": "monthly"},

    # EN Pages
    {"loc": "/en/movers_marketing.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/en/dentist_marketing.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/en/realestate_marketing.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/en/restaurant_marketing.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/en/kebab_marketing.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/en/beauty_marketing.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/en/renovation_marketing.html", "priority": "0.8", "changefreq": "monthly"},
]

sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for page in pages:
    sitemap_content += '  <url>\n'
    sitemap_content += f'    <loc>{base_url}{page["loc"]}</loc>\n'
    sitemap_content += f'    <lastmod>{last_mod}</lastmod>\n'
    sitemap_content += f'    <changefreq>{page["changefreq"]}</changefreq>\n'
    sitemap_content += f'    <priority>{page["priority"]}</priority>\n'
    sitemap_content += '  </url>\n'

sitemap_content += '</urlset>'

with open('site_update/digitaladexpert-cloudflare/sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
print("Generated sitemap.xml")


# --- 2. FOOTER LINKS INJECTION ---

def add_footer_links(root_dir, lang):
    sectors = []
    header = ""
    
    if lang == 'tr':
        header = "Sektörel Çözümler"
        sectors = [
            ('/tr/nakliyat_google_ads.html', 'Nakliyat'),
            ('/tr/disci_google_ads.html', 'Diş Hekimi'),
            ('/tr/emlak_google_ads.html', 'Emlak'),
            ('/tr/restoran_google_ads.html', 'Restoran'),
            ('/tr/donerci_google_ads.html', 'Döner/Büfe'),
            ('/tr/guzellik_google_ads.html', 'Güzellik'),
            ('/tr/tadilat_google_ads.html', 'Tadilat')
        ]
    elif lang == 'de':
        header = "Branchenlösungen"
        sectors = [
            ('/de/umzug_marketing.html', 'Umzug'),
            ('/de/zahnarzt_marketing.html', 'Zahnarzt'),
            ('/de/immobilien_marketing.html', 'Immobilien'),
            ('/de/gastro_marketing.html', 'Gastro'),
            ('/de/imbiss_marketing.html', 'Imbiss'),
            ('/de/kosmetik_marketing.html', 'Kosmetik'),
            ('/de/handwerker_marketing.html', 'Handwerk')
        ]
    elif lang == 'en':
        header = "Industry Solutions"
        sectors = [
            ('/en/movers_marketing.html', 'Movers'),
            ('/en/dentist_marketing.html', 'Dentist'),
            ('/en/realestate_marketing.html', 'Real Estate'),
            ('/en/restaurant_marketing.html', 'Restaurant'),
            ('/en/kebab_marketing.html', 'Street Food'),
            ('/en/beauty_marketing.html', 'Beauty'),
            ('/en/renovation_marketing.html', 'Contractor')
        ]

    # HTML snippet to inject into footer
    links_html = f'<div class="text-center sm:text-left"><h4 class="text-base sm:text-lg font-semibold text-white mb-3 sm:mb-4">{header}</h4><ul class="space-y-2 sm:space-y-3">'
    for link, name in sectors:
        links_html += f'<li><a href="{link}" class="text-gray-400 hover:text-primary transition-colors text-sm sm:text-base">{name}</a></li>'
    links_html += '</ul></div>'

    # Walk through files
    lang_dir = os.path.join(root_dir, lang)
    for filename in os.listdir(lang_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(lang_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find insertion point in footer (before "Social Media" column usually, or replacing it/adding next to it)
            # Our current footer has 3 columns: Brand, Legal, Social. Let's make it 4 columns or insert into existing grid.
            # Best strategy: Insert as a new column before "Legal" or "Social".
            
            # Target: <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8 sm:gap-12 mb-8 sm:mb-12">
            # We will change grid-cols-3 to grid-cols-4 and insert the new div
            
            if 'grid-cols-3' in content and header not in content:
                content = content.replace('md:grid-cols-3', 'md:grid-cols-4')
                # Insert after Brand column closing div
                # Looking for the first column's closing div is tricky with regex/string.
                # Let's try to insert BEFORE the "Legal" column
                
                legal_heading_search = {
                    'tr': '<h4 class="text-base sm:text-lg font-semibold text-white mb-3 sm:mb-4">Yasal</h4>',
                    'de': '<h4 class="text-base sm:text-lg font-semibold text-white mb-3 sm:mb-4">Rechtliches</h4>',
                    'en': '<h4 class="text-base sm:text-lg font-semibold text-white mb-3 sm:mb-4">Legal</h4>'
                }
                
                target_str = '<div class="text-center sm:text-left">' + legal_heading_search[lang]
                
                if target_str in content:
                    content = content.replace(target_str, links_html + '\n' + target_str)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated footer in {filepath}")
                else:
                    print(f"Could not find insertion point in {filepath}")

root = 'site_update/digitaladexpert-cloudflare'
add_footer_links(root, 'tr')
add_footer_links(root, 'de')
add_footer_links(root, 'en')
