
import os
import re

def optimize_meta_tags(file_path, lang):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define optimization rules based on filename keywords
    title = ""
    desc = ""
    
    filename = os.path.basename(file_path)

    # --- TR (TÜRKÇE) ---
    if lang == 'tr':
        if 'nakliyat' in filename:
            title = "Almanya Nakliyat Müşterisi Bulma Uzmanı | Digital Ad Expert"
            desc = "Boş kamyon kalmasın! Almanya'daki Türk nakliyatçılar için özel Google Ads stratejisi. Tıklama değil, telefon garantili reklam yönetimi."
        elif 'disci' in filename:
            title = "Almanya Diş Hekimi Hasta Bulma Reklamları | Digital Ad Expert"
            desc = "Muayenehanenizi doldurun. İmplant ve estetik diş hekimliği için yüksek kazançlı hasta bulma stratejileri. Google Ads & SEO."
        elif 'emlak' in filename:
            title = "Emlakçılar İçin Satılık Daire & Müşteri Bulma | Digital Ad Expert"
            desc = "Almanya'da emlak portföyünüzü büyütün. Evini satmak isteyen mülk sahiplerine doğrudan ulaşın. Emlak sektörüne özel pazarlama."
        elif 'restoran' in filename:
            title = "Restoranlar İçin Masa Doldurma & Sipariş Artırma | Digital Ad Expert"
            desc = "Müşteriler sizi arıyor! Restoranınız için Google Haritalar ve Instagram reklamlarıyla doluluk oranını artırın."
        elif 'donerci' in filename:
            title = "Döner & Imbiss İçin Yerel Müşteri Reklamları | Digital Ad Expert"
            desc = "Mahallenin en iyisi siz olun. Dönerci ve büfeler için acıkan müşteriyi dükkana çeken Google ve Sosyal Medya reklamları."
        elif 'guzellik' in filename:
            title = "Güzellik Merkezi & Kuaför Randevu Artırma | Digital Ad Expert"
            desc = "Boş koltuk kalmasın. Güzellik merkezleri için online randevu ve müşteri bulma sistemi. Lazer, cilt bakımı ve saç ekimi odaklı."
        elif 'tadilat' in filename:
            title = "İnşaat & Tadilat Firmaları İçin Proje Bulma | Digital Ad Expert"
            desc = "Büyük projeler alın. Almanya'daki Türk inşaat ve tadilat ustaları için iş getiren Google reklamları."

    # --- DE (ALMANCA) ---
    elif lang == 'de':
        if 'umzug' in filename:
            title = "Google Ads für Umzugsunternehmen | Mehr Aufträge Garantiert"
            desc = "Keine leeren LKWs mehr! Spezialisiertes Google Ads Marketing für Umzugsspeditionen. Echte Leads, keine kalten Anrufe."
        elif 'zahnarzt' in filename:
            title = "Patientengewinnung für Zahnärzte | Implantate & Ästhetik"
            desc = "Gewinnen Sie Privatpatienten für hochwertige Behandlungen. Exklusives Praxismarketing und SEO für Zahnärzte in Deutschland."
        elif 'immobilien' in filename:
            title = "Lead-Generierung für Immobilienmakler | Eigentümer Finden"
            desc = "Mehr Verkaufsaufträge für Makler. Erreichen Sie Immobilienbesitzer, die jetzt verkaufen wollen. Zielgerichtetes Immobilienmarketing."
        elif 'gastro' in filename:
            title = "Restaurant Marketing & Reservierungen | Volles Haus"
            desc = "Machen Sie Ihr Restaurant zum Hotspot. Lokales SEO und Social Media Ads für mehr Gäste und Reservierungen."
        elif 'imbiss' in filename:
            title = "Marketing für Imbiss & Döner | Mehr Kunden im Laden"
            desc = "Der beste Döner der Stadt? Zeigen Sie es! Lokale Werbung, die hungrige Kunden direkt zu Ihnen führt."
        elif 'kosmetik' in filename:
            title = "Marketing für Kosmetikstudios | Terminbuchung Automatisieren"
            desc = "Füllen Sie Ihren Terminkalender mit Premium-Kunden. Performance Marketing für Beauty, Laser und Ästhetik."
        elif 'handwerker' in filename:
            title = "Aufträge für Handwerker & Baufirmen | Regionale Projekte"
            desc = "Hochwertige Bauaufträge statt Preiskampf. Google Ads für Maler, Elektriker und Sanierungsfirmen. Jetzt anfragen."

    # --- EN (İNGİLİZCE) ---
    elif lang == 'en':
        if 'movers' in filename:
            title = "Google Ads for Moving Companies | Get More Jobs"
            desc = "Stop wasting budget. Specialized Google Ads & SEO for movers in Germany. Get high-paying relocation jobs now."
        elif 'dentist' in filename:
            title = "Dental Marketing Expert Germany | Attract Expats & Private Patients"
            desc = "Grow your practice with high-value patients. Specialized marketing for English-speaking dentists in Germany."
        elif 'realestate' in filename:
            title = "Real Estate Lead Gen Germany | Get More Listings"
            desc = "Connect with home sellers before your competitors. Automated lead generation for Real Estate Agents in Germany."
        elif 'restaurant' in filename:
            title = "Restaurant Marketing Agency | Get More Bookings"
            desc = "Fill your tables every night. Local SEO and Social Media advertising for restaurants and cafes in Germany."
        elif 'kebab' in filename:
            title = "Street Food & Kebab Marketing | Local SEO Expert"
            desc = "Be the #1 choice nearby. Drive foot traffic to your food stall or kebab shop with targeted local ads."
        elif 'beauty' in filename:
            title = "Beauty Salon Marketing | Get Fully Booked"
            desc = "Attract premium clients for your salon. Automated booking systems and ads for beauty, hair, and spa services."
        elif 'renovation' in filename:
            title = "Marketing for Contractors Germany | Win Big Projects"
            desc = "Get quality construction leads. Google Ads for renovation, painting, and building companies. English support available."

    # Replace Title
    if title:
        content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content)
    
    # Replace Description
    if desc:
        content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    if title:
        print(f"Optimized {filename}")

# Run optimization
root = 'site_update/digitaladexpert-cloudflare'
for lang in ['tr', 'de', 'en']:
    lang_dir = os.path.join(root, lang)
    if os.path.exists(lang_dir):
        for filename in os.listdir(lang_dir):
            if filename.endswith('.html') and 'index' not in filename:
                optimize_meta_tags(os.path.join(lang_dir, filename), lang)

