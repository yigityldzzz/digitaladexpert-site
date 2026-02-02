
import os

def manual_footer_fix(root_dir, lang):
    sectors = []
    title = ""
    
    if lang == 'tr':
        title = "Diğer Sektörler:"
        sectors = [
            ('/tr/nakliyat_google_ads.html', 'Nakliyat'),
            ('/tr/disci_google_ads.html', 'Diş Hekimi'),
            ('/tr/emlak_google_ads.html', 'Emlak'),
            ('/tr/restoran_google_ads.html', 'Restoran'),
            ('/tr/donerci_google_ads.html', 'Döner'),
            ('/tr/guzellik_google_ads.html', 'Güzellik'),
            ('/tr/tadilat_google_ads.html', 'Tadilat')
        ]
    elif lang == 'de':
        title = "Weitere Branchen:"
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
        title = "Other Industries:"
        sectors = [
            ('/en/movers_marketing.html', 'Movers'),
            ('/en/dentist_marketing.html', 'Dentist'),
            ('/en/realestate_marketing.html', 'Real Estate'),
            ('/en/restaurant_marketing.html', 'Restaurant'),
            ('/en/kebab_marketing.html', 'Street Food'),
            ('/en/beauty_marketing.html', 'Beauty'),
            ('/en/renovation_marketing.html', 'Contractor')
        ]

    # Simple footer links HTML
    links_html = f'<div class="mt-8 pt-8 border-t border-white/10"><p class="text-sm text-gray-500 mb-4">{title}</p><div class="flex flex-wrap justify-center gap-4">'
    for link, name in sectors:
        links_html += f'<a href="{link}" class="text-xs text-gray-400 hover:text-primary transition-colors">{name}</a>'
    links_html += '</div></div>'

    # Walk through files
    lang_dir = os.path.join(root_dir, lang)
    for filename in os.listdir(lang_dir):
        if filename.endswith(".html") and "index" not in filename: # Apply only to landing pages
            filepath = os.path.join(lang_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Insert before the copyright paragraph in footer
            # Target: <footer class="py-10 border-t border-white/10 text-center text-gray-500">
            # Insert inside footer, before closing tag
            
            if '</footer>' in content and title not in content:
                content = content.replace('</footer>', links_html + '\n</footer>')
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated footer in {filepath}")

root = 'site_update/digitaladexpert-cloudflare'
manual_footer_fix(root, 'tr')
manual_footer_fix(root, 'de')
manual_footer_fix(root, 'en')
