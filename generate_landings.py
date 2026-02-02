import os

# Base template is the Nakliyat one, but we will replace specific sections
template_path = 'site_update/digitaladexpert-cloudflare/tr/nakliyat_google_ads.html'

with open(template_path, 'r', encoding='utf-8') as f:
    base_html = f.read()

# Helper to replace text content safely
def generate_page(lang, filename, data):
    html = base_html
    
    # Common replacements
    html = html.replace('lang="tr"', f'lang="{lang}"')
    if lang == 'de':
        html = html.replace('/tr/"', '/de/"')
        html = html.replace('← Ana Sayfaya Dön', '← Zurück zur Startseite')
        html = html.replace('Hemen Başlayalım', 'Jetzt Starten')
        html = html.replace('İşinizi Büyütmeye Hazır Mısınız?', 'Bereit für mehr Umsatz?')
        html = html.replace('Sitenizi ve rakiplerinizi inceleyip size özel bir plan çıkarayım.', 'Ich analysiere Ihre Website und Konkurrenz für einen maßgeschneiderten Plan.')
        html = html.replace('Firma Adı / Adınız', 'Firmenname / Ihr Name')
        html = html.replace('Telefon Numaranız', 'Telefonnummer')
        html = html.replace('Gönder', 'Senden')
        html = html.replace('Ücretsiz Analiz İstiyorum', 'Kostenlose Analyse anfordern')
        footer_text = "© 2025 Digital Ad Expert. Spezialisierte Lösungen für Ihre Branche."
    elif lang == 'en':
        html = html.replace('/tr/"', '/en/"')
        html = html.replace('← Ana Sayfaya Dön', '← Back to Home')
        html = html.replace('Hemen Başlayalım', 'Get Started Now')
        html = html.replace('İşinizi Büyütmeye Hazır Mısınız?', 'Ready to Grow Your Business?')
        html = html.replace('Sitenizi ve rakiplerinizi inceleyip size özel bir plan çıkarayım.', 'I will analyze your site and competitors to create a custom plan.')
        html = html.replace('Firma Adı / Adınız', 'Company Name / Your Name')
        html = html.replace('Telefon Numaranız', 'Phone Number')
        html = html.replace('Gönder', 'Send')
        html = html.replace('Ücretsiz Analiz İstiyorum', 'Get Free Analysis')
        footer_text = "© 2025 Digital Ad Expert. Niche Marketing Solutions."

    # Specific Data Replacements
    # We will replace large blocks or specific unique strings
    # Title
    html = html.replace('Almanya Nakliyat Firmaları İçin Google Ads & SEO | Digital Ad Expert', data['title'])
    html = html.replace('Almanya\'daki Türk nakliyat (Umzug) firmaları için özel Google Ads ve SEO hizmeti. Boşa para harcamayın, sadece gerçek müşteri telefonları alın.', data['meta_desc'])
    
    # Hero Badge
    html = html.replace('🚛', data['icon'])
    html = html.replace('Nakliyat (Umzug) Sektörüne Özel', data['badge_text'])
    
    # Hero H1
    html = html.replace('Tırlarınız Yatmasın,', data['h1_line1'])
    html = html.replace('Telefonlarınız Sussmasın!', data['h1_line2'])
    
    # Hero Sub
    html = html.replace('Almanya\'daki nakliyat firmaları Google Ads\'te servet harcayıp karşılığını alamıyor.', data['hero_sub_1'])
    html = html.replace('Sektörü bilen bir uzmanla', data['hero_sub_bold'])
    html = html.replace('çalışın, boşa giden tıklamalara son verin.', data['hero_sub_2'])
    
    # Pain Points Header
    html = html.replace('Nakliyecilerin En Büyük', data['pain_header'])
    html = html.replace('Hataları', data['pain_header_red'])
    
    # Solutions Header
    html = html.replace('Benim', data['solution_header'])
    html = html.replace('Çözümlerim', data['solution_header_grad'])
    
    # Pain Points Items (Hard replace of the UL block would be safer, but let's try strict string replacement for the specific Nakliyat text found in template)
    # Nakliyat specifics to remove:
    html = html.replace('"Kiralık Kamyon" arayanlara reklam gösterip paranızı yakıyorsunuz.', data['pain_1'])
    html = html.replace('Yanlış Kelimeler:', data['pain_1_title'])
    
    html = html.replace('Berlin\'de iş yaparken Münih\'ten tıklama alıyorsunuz.', data['pain_2'])
    html = html.replace('Konum Hatası:', data['pain_2_title'])
    
    html = html.replace('Reklamınız Google\'da pahalıya çıkıyor, rakipleriniz daha ucuza müşteri buluyor.', data['pain_3'])
    html = html.replace('Düşük Kalite Puanı:', data['pain_3_title'])
    
    # Solution Items
    html = html.replace('Sadece taşınmak isteyen (Umzug) gerçek müşterileri hedeflerim.', data['sol_1'])
    html = html.replace('Negatif Kelime Listesi:', data['sol_1_title'])
    
    html = html.replace('Müşteri web sitesinde kaybolmaz, tek tıkla sizi arar.', data['sol_2'])
    html = html.replace('Telefon Odaklı Reklam:', data['sol_2_title'])
    
    html = html.replace('Bölgenizdeki diğer Türk ve Alman firmaların önüne geçmenizi sağlarım.', data['sol_3'])
    html = html.replace('Rakip Analizi:', data['sol_3_title'])
    
    # Services Section
    html = html.replace('Nakliyecilere Özel Paket', data['package_title'])
    html = html.replace('Sadece bir reklamcı değil, iş ortağınız gibi çalışıyorum.', data['package_sub'])
    
    # Service Cards
    html = html.replace('📞', data['card_1_icon'])
    html = html.replace('Telefon Aramaları', data['card_1_title'])
    html = html.replace('Form doldurmakla uğraşmayan, acil taşınacak müşterileri doğrudan telefonunuza yönlendiriyorum.', data['card_1_desc'])
    
    html = html.replace('📍', data['card_2_icon'])
    html = html.replace('Bölgesel Hakimiyet', data['card_2_title'])
    html = html.replace('Hangi şehirdeyseniz (Berlin, Köln, Hamburg) o bölgenin kralı siz olun. Uzak mesafeye boşa reklam yok.', data['card_2_desc'])
    
    html = html.replace('📉', data['card_3_icon'])
    html = html.replace('Düşük Maliyet', data['card_3_title'])
    html = html.replace('Gereksiz kelimeleri engelleyerek reklam bütçenizi %40\'a kadar düşürüyorum.', data['card_3_desc'])
    
    # Form Placeholder
    html = html.replace('Hangi şehirde hizmet veriyorsunuz? Kaç aracınız var?', data['form_placeholder'])
    
    # Footer
    html = html.replace('© 2025 Digital Ad Expert. Nakliyat Sektörü Özel Çözümleri.', footer_text)

    # Write file
    output_path = f'site_update/digitaladexpert-cloudflare/{lang}/{filename}'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {output_path}")

# DATA DEFINITIONS

# --- GERMAN (DE) ---
de_data = {
    'umzug_marketing.html': {
        'title': 'Google Ads für Umzugsunternehmen | Digital Ad Expert',
        'meta_desc': 'Mehr Umzugsaufträge, weniger Streuverluste. Spezielles Google Ads & SEO Marketing für Umzugsunternehmen in Deutschland.',
        'icon': '🚛',
        'badge_text': 'Spezialisiert auf Umzugsunternehmen',
        'h1_line1': 'Keine leeren LKW mehr,',
        'h1_line2': 'Voller Terminkalender!',
        'hero_sub_1': 'Viele Umzugsfirmen verbrennen Geld bei Google Ads.',
        'hero_sub_bold': 'Arbeiten Sie mit einem Experten,',
        'hero_sub_2': 'der Ihre Branche versteht.',
        'pain_header': 'Häufige',
        'pain_header_red': 'Fehler',
        'pain_1_title': 'Falsche Keywords:',
        'pain_1': 'Sie zahlen für Leute, die "LKW mieten" suchen, statt einen Umzugsservice.',
        'pain_2_title': 'Falscher Standort:',
        'pain_2': 'Sie arbeiten in Berlin, bezahlen aber für Klicks aus München.',
        'pain_3_title': 'Teure Klicks:',
        'pain_3': 'Ohne Optimierung zahlen Sie das Doppelte Ihrer Konkurrenz.',
        'solution_header': 'Meine',
        'solution_header_grad': 'Lösungen',
        'sol_1_title': 'Präzises Targeting:',
        'sol_1': 'Nur Kunden, die wirklich einen Umzugsservice (Privat/Gewerbe) suchen.',
        'sol_2_title': 'Anrufe statt Klicks:',
        'sol_2': 'Optimiert für mobile Anrufe. Der Kunde ruft direkt an.',
        'sol_3_title': 'Konkurrenzanalyse:',
        'sol_3': 'Dominieren Sie Ihre lokale Region gegen andere Anbieter.',
        'package_title': 'Das Umzugs-Paket',
        'package_sub': 'Maßgeschneidert für Speditionen und Umzugshelfer.',
        'card_1_icon': '📞',
        'card_1_title': 'Echte Leads',
        'card_1_desc': 'Kunden, die jetzt umziehen wollen und ein Angebot brauchen.',
        'card_2_icon': '📍',
        'card_2_title': 'Lokale Dominanz',
        'card_2_desc': 'Seien Sie die Nr. 1 in Ihrer Stadt (Berlin, Hamburg, Köln, etc.).',
        'card_3_icon': '📉',
        'card_3_title': 'Kosten senken',
        'card_3_desc': 'Durch Ausschluss negativer Keywords sparen wir bis zu 40% Budget.',
        'form_placeholder': 'In welcher Stadt sind Sie tätig? Wie viele Fahrzeuge haben Sie?'
    },
    'zahnarzt_marketing.html': {
        'title': 'Patientengewinnung für Zahnärzte | Digital Ad Expert',
        'meta_desc': 'Mehr Privatpatienten und Implantat-Kunden. Google Ads Marketing speziell für Zahnarztpraxen.',
        'icon': '🦷',
        'badge_text': 'Praxismarketing Spezialist',
        'h1_line1': 'Mehr Wunschpatienten',
        'h1_line2': 'für Ihre Praxis.',
        'hero_sub_1': 'Klassische Werbung funktioniert nicht mehr.',
        'hero_sub_bold': 'Erreichen Sie Patienten,',
        'hero_sub_2': 'die jetzt nach einem Zahnarzt suchen.',
        'pain_header': 'Typische',
        'pain_header_red': 'Probleme',
        'pain_1_title': 'Zu wenig Privatpatienten:',
        'pain_1': 'Ihre Werbung bringt nur Kontrolltermine, keine hochwertigen Behandlungen.',
        'pain_2_title': 'Unsichtbar:',
        'pain_2': 'Patienten finden die Konkurrenz, nicht Sie.',
        'pain_3_title': 'Kein Vertrauen:',
        'pain_3': 'Ihre Website überzeugt Besucher nicht, einen Termin zu buchen.',
        'solution_header': 'Mein',
        'solution_header_grad': 'Ansatz',
        'sol_1_title': 'High-Value Fokus:',
        'sol_1': 'Kampagnen für Implantate, Ästhetik und Privatleistungen.',
        'sol_2_title': 'Lokales SEO:',
        'sol_2': 'Top-Platzierung bei "Zahnarzt in [Ihre Stadt]".',
        'sol_3_title': 'Vertrauensaufbau:',
        'sol_3': 'Landing Pages, die Kompetenz ausstrahlen und Termine generieren.',
        'package_title': 'Praxis-Wachstum',
        'package_sub': 'Marketing, das Ihren Terminkalender füllt.',
        'card_1_icon': '📅',
        'card_1_title': 'Online Termine',
        'card_1_desc': 'Automatisierte Anfragen direkt über Ihre Website.',
        'card_2_icon': '💎',
        'card_2_title': 'Premium Patienten',
        'card_2_desc': 'Gezielte Ansprache für hochwertige Behandlungen.',
        'card_3_icon': '🛡️',
        'card_3_title': 'Reputation',
        'card_3_desc': 'Stärken Sie Ihre Marke als führender Experte in der Region.',
        'form_placeholder': 'Wie viele Behandlungsstühle haben Sie? Welcher Schwerpunkt (Implantate, etc.)?'
    },
    'gastro_marketing.html': {
        'title': 'Restaurant & Lieferservice Marketing | Digital Ad Expert',
        'meta_desc': 'Volles Haus und mehr Bestellungen. Google Ads & Social Media für Gastronomie.',
        'icon': '🍔',
        'badge_text': 'Gastronomie Marketing',
        'h1_line1': 'Volle Tische,',
        'h1_line2': 'Heißes Telefon!',
        'hero_sub_1': 'Gutes Essen reicht nicht, wenn niemand es kennt.',
        'hero_sub_bold': 'Machen Sie Ihr Restaurant',
        'hero_sub_2': 'zum Stadtgespräch.',
        'pain_header': 'Gastro',
        'pain_header_red': 'Herausforderungen',
        'pain_1_title': 'Leere Tische:',
        'pain_1': 'Unter der Woche bleibt das Restaurant oft leer.',
        'pain_2_title': 'Hohe Gebühren:',
        'pain_2': 'Lieferportale nehmen Ihnen die ganze Marge weg.',
        'pain_3_title': 'Schlechte Sichtbarkeit:',
        'pain_3': 'Touristen und Einheimische finden Sie nicht bei Google Maps.',
        'solution_header': 'Das',
        'solution_header_grad': 'Rezept',
        'sol_1_title': 'Direktbestellungen:',
        'sol_1': 'Eigenes System statt hoher Provisionen an Portale.',
        'sol_2_title': 'Local SEO:',
        'sol_2': 'Nr. 1 bei "Restaurant in der Nähe" und Google Maps.',
        'sol_3_title': 'Social Buzz:',
        'sol_3': 'Instagram & Facebook Ads, die Appetit machen.',
        'package_title': 'Gastro-Booster',
        'package_sub': 'Für Restaurants, Imbisse und Cafés.',
        'card_1_icon': '🛵',
        'card_1_title': 'Mehr Bestellungen',
        'card_1_desc': 'Systeme, um Kunden direkt zu Ihnen zu leiten.',
        'card_2_icon': '⭐',
        'card_2_title': 'Bewertungen',
        'card_2_desc': 'Strategien für mehr 5-Sterne Google Rezensionen.',
        'card_3_icon': '📸',
        'card_3_title': 'Sichtbarkeit',
        'card_3_desc': 'Professionelle Darstellung Ihrer Speisen online.',
        'form_placeholder': 'Welche Art von Küche bieten Sie an? Haben Sie einen Lieferservice?'
    },
        'handwerker_marketing.html': {
        'title': 'Marketing für Handwerker & Bau | Digital Ad Expert',
        'meta_desc': 'Mehr Aufträge für Handwerker. Regionale Kunden für Sanierung, Bau und Renovierung.',
        'icon': '🔨',
        'badge_text': 'Handwerk & Bau',
        'h1_line1': 'Gute Aufträge',
        'h1_line2': 'statt Preiskampf.',
        'hero_sub_1': 'Verlassen Sie sich nicht nur auf Empfehlungen.',
        'hero_sub_bold': 'Gewinnen Sie aktiv',
        'hero_sub_2': 'die besten Bauprojekte in Ihrer Region.',
        'pain_header': 'Handwerker',
        'pain_header_red': 'Probleme',
        'pain_1_title': 'Preiskampf:',
        'pain_1': 'Kunden wollen immer nur den billigsten Preis.',
        'pain_2_title': 'Kleine Aufträge:',
        'pain_2': 'Viel Aufwand für Kleinkram, der sich kaum lohnt.',
        'pain_3_title': 'Unzuverlässigkeit:',
        'pain_3': 'Leads von Portalen sind oft von schlechter Qualität.',
        'solution_header': 'Meine',
        'solution_header_grad': 'Strategie',
        'sol_1_title': 'Qualitäts-Leads:',
        'sol_1': 'Kunden, die Qualität suchen und bereit sind zu zahlen.',
        'sol_2_title': 'Projekt-Fokus:',
        'sol_2': 'Gezielte Werbung für Komplettsanierung, Neubau, etc.',
        'sol_3_title': 'Vertrauen:',
        'sol_3': 'Professionelle Webseite, die Ihre Meisterarbeit zeigt.',
        'package_title': 'Handwerker-Spezial',
        'package_sub': 'Für Maler, Elektriker, Bauunternehmen und mehr.',
        'card_1_icon': '🏠',
        'card_1_title': 'Große Projekte',
        'card_1_desc': 'Fokus auf lukrative Aufträge statt Kleinarbeit.',
        'card_2_icon': '📍',
        'card_2_title': 'Regional',
        'card_2_desc': 'Aufträge in Ihrem Umkreis. Keine langen Anfahrten.',
        'card_3_icon': '🤝',
        'card_3_title': 'Direkter Kontakt',
        'card_3_desc': 'Kunden rufen Sie direkt an oder senden Pläne.',
        'form_placeholder': 'Welches Gewerk? In welchem Umkreis arbeiten Sie?'
    },
    'immobilien_marketing.html': {
        'title': 'Makler Marketing & Lead Gen | Digital Ad Expert',
        'meta_desc': 'Mehr Eigentümer-Leads und Objekt-Akquise für Immobilienmakler.',
        'icon': '🏠',
        'badge_text': 'Immobilienmakler',
        'h1_line1': 'Mehr Objekte,',
        'h1_line2': 'Schnellerer Verkauf.',
        'hero_sub_1': 'Der Markt ist hart.',
        'hero_sub_bold': 'Erreichen Sie Eigentümer,',
        'hero_sub_2': 'bevor es die Konkurrenz tut.',
        'pain_header': 'Makler',
        'pain_header_red': 'Herausforderungen',
        'pain_1_title': 'Objektmangel:',
        'pain_1': 'Schwierig, an neue Verkaufsaufträge zu kommen.',
        'pain_2_title': 'Teure Portale:',
        'pain_2': 'Immoscout etc. sind teuer und vergleichbar.',
        'pain_3_title': 'Zeitverschwendung:',
        'pain_3': 'Viele Besichtigungen, wenig Abschlüsse.',
        'solution_header': 'Der',
        'solution_header_grad': 'Plan',
        'sol_1_title': 'Eigentümer-Targeting:',
        'sol_1': 'Werbung gezielt für Leute, die verkaufen wollen.',
        'sol_2_title': 'Lead Qualifizierung:',
        'sol_2': 'Vorab-Filterung, damit Sie nur mit ernsthaften Interessenten sprechen.',
        'sol_3_title': 'Personal Brand:',
        'sol_3': 'Positionierung als der Top-Makler der Region.',
        'package_title': 'Makler-System',
        'package_sub': 'Automatisierte Objekt-Akquise.',
        'card_1_icon': '🔑',
        'card_1_title': 'Verkaufsaufträge',
        'card_1_desc': 'Leads von Eigentümern, die verkaufen wollen.',
        'card_2_icon': '📋',
        'card_2_title': 'Datenbank',
        'card_2_desc': 'Aufbau einer eigenen Käufer-Liste.',
        'card_3_icon': '🏆',
        'card_3_title': 'Marktführer',
        'card_3_desc': 'Dominieren Sie Ihren Stadtteil.',
        'form_placeholder': 'Region? Fokus (Verkauf/Vermietung)?'
    },
    'imbiss_marketing.html': {
        'title': 'Döner & Imbiss Marketing | Digital Ad Expert',
        'meta_desc': 'Der beste Döner der Stadt? Zeigen Sie es! Marketing für Imbiss & Fast Food.',
        'icon': '🥙',
        'badge_text': 'Döner & Imbiss',
        'h1_line1': 'Die Schlange',
        'h1_line2': 'bis zur Straße!',
        'hero_sub_1': 'Sie haben den besten Geschmack.',
        'hero_sub_bold': 'Ich bringe Ihnen',
        'hero_sub_2': 'die hungrigen Kunden.',
        'pain_header': 'Imbiss',
        'pain_header_red': 'Alltag',
        'pain_1_title': 'Mittagspause:',
        'pain_1': 'Kurzer Ansturm, dann Leerlauf.',
        'pain_2_title': 'Konkurrenz:',
        'pain_2': 'An jeder Ecke gibt es einen anderen Laden.',
        'pain_3_title': 'Online:',
        'pain_3': 'Keine Website, nur eine alte Facebook Seite.',
        'solution_header': 'Mein',
        'solution_header_grad': 'Turbo',
        'sol_1_title': 'Lokale Sichtbarkeit:',
        'sol_1': 'Wer "Döner in der Nähe" sucht, findet SIE.',
        'sol_2_title': 'Aktionen:',
        'sol_2': 'Werbung für Mittagsmenüs und Angebote.',
        'sol_3_title': 'TikTok & Insta:',
        'sol_3': 'Virale Videos von Ihrem Essen.',
        'package_title': 'Streetfood-Paket',
        'package_sub': 'Schnell, günstig, effektiv.',
        'card_1_icon': '🤤',
        'card_1_title': 'Hunger wecken',
        'card_1_desc': 'Bilder, bei denen das Wasser im Mund zusammenläuft.',
        'card_2_icon': '📍',
        'card_2_title': 'Google Maps',
        'card_2_desc': 'Top-Platzierung auf der Karte.',
        'card_3_icon': '🚀',
        'card_3_title': 'Bekanntheit',
        'card_3_desc': 'Jeder im Kiez wird Sie kennen.',
        'form_placeholder': 'Was verkaufen Sie (Döner, Pizza, Burger)?'
    },
    'kosmetik_marketing.html': {
        'title': 'Kosmetikstudio & Beauty Marketing | Digital Ad Expert',
        'meta_desc': 'Voller Terminkalender für Ihr Kosmetikstudio. Neukunden für Beauty & Wellness.',
        'icon': '💅',
        'badge_text': 'Beauty & Kosmetik',
        'h1_line1': 'Ausgebucht',
        'h1_line2': 'statt Lücken.',
        'hero_sub_1': 'Lücken im Kalender kosten Geld.',
        'hero_sub_bold': 'Füllen Sie Ihre Termine',
        'hero_sub_2': 'mit treuen Stammkunden.',
        'pain_header': 'Studio',
        'pain_header_red': 'Sorgen',
        'pain_1_title': 'Absagen:',
        'pain_1': 'Kunden kommen nicht oder sagen kurzfristig ab.',
        'pain_2_title': 'Preiskunden:',
        'pain_2': 'Leute wollen Rabatte statt Qualität.',
        'pain_3_title': 'Instagram Frust:',
        'pain_3': 'Viele Posts, aber keine Buchungen.',
        'solution_header': 'Der',
        'solution_header_grad': 'Glow-Up',
        'sol_1_title': 'Wunschkunden:',
        'sol_1': 'Frauen/Männer, die Wert auf Pflege legen und gut zahlen.',
        'sol_2_title': 'Online Buchung:',
        'sol_2': 'Verbindliche Termine direkt über Werbung.',
        'sol_3_title': 'Behandlungs-Fokus:',
        'sol_3': 'Werbung für High-Ticket Services (Laser, Anti-Aging).',
        'package_title': 'Beauty-Booster',
        'package_sub': 'Für Studios, Friseure und Ästhetik.',
        'card_1_icon': '📅',
        'card_1_title': 'Auto-Buchung',
        'card_1_desc': 'Kunden buchen selbstständig Termine.',
        'card_2_icon': '✨',
        'card_2_title': 'Image',
        'card_2_desc': 'Premium-Auftritt für Premium-Preise.',
        'card_3_icon': '💌',
        'card_3_title': 'Stammkunden',
        'card_3_desc': 'Marketing, das Kunden immer wieder bringt.',
        'form_placeholder': 'Welche Behandlungen (Laser, Nägel, Haut)?'
    }
}

# --- ENGLISH (EN) ---
en_data = {
    'movers_marketing.html': {
        'title': 'Google Ads for Moving Companies | Digital Ad Expert',
        'meta_desc': 'Get more moving jobs, stop wasting budget. Specialized Google Ads & SEO for movers in Germany.',
        'icon': '🚛',
        'badge_text': 'Specialized for Movers',
        'h1_line1': 'Keep Your Trucks Moving,',
        'h1_line2': 'Phones Ringing!',
        'hero_sub_1': 'Many moving companies waste a fortune on Google Ads.',
        'hero_sub_bold': 'Work with an expert',
        'hero_sub_2': 'who knows the moving industry.',
        'pain_header': 'Common',
        'pain_header_red': 'Mistakes',
        'pain_1_title': 'Wrong Keywords:',
        'pain_1': 'Paying for people looking to "rent a truck" instead of hiring movers.',
        'pain_2_title': 'Location Errors:',
        'pain_2': 'Serving Berlin but paying for clicks from Munich.',
        'pain_3_title': 'Low Quality Score:',
        'pain_3': 'Paying double per click because your ads aren\'t optimized.',
        'solution_header': 'My',
        'solution_header_grad': 'Solutions',
        'sol_1_title': 'Negative Keywords:',
        'sol_1': 'Filter out DIY movers. Target only high-value full-service moves.',
        'sol_2_title': 'Call-Focused:',
        'sol_2': 'Campaigns designed to generate phone calls, not just visits.',
        'sol_3_title': 'Competitor Analysis:',
        'sol_3': 'Outrank other movers in your specific city.',
        'package_title': 'The Movers Package',
        'package_sub': 'Designed for removal and relocation companies.',
        'card_1_icon': '📞',
        'card_1_title': 'Phone Leads',
        'card_1_desc': 'Direct calls from people who need to move ASAP.',
        'card_2_icon': '📍',
        'card_2_title': 'Local Domination',
        'card_2_desc': 'Be the #1 choice in your city (Berlin, Munich, etc.).',
        'card_3_icon': '📉',
        'card_3_title': 'Lower Costs',
        'card_3_desc': 'Save up to 40% budget by eliminating waste traffic.',
        'form_placeholder': 'Which city do you serve? How many trucks do you have?'
    },
    'dentist_marketing.html': {
        'title': 'Dental Marketing Expert | Digital Ad Expert',
        'meta_desc': 'Attract more private patients and implant cases. Google Ads for Dentists in Germany.',
        'icon': '🦷',
        'badge_text': 'Dental Marketing',
        'h1_line1': 'More High-Value',
        'h1_line2': 'Patients.',
        'hero_sub_1': 'Stop relying on random walk-ins.',
        'hero_sub_bold': 'Target patients seeking',
        'hero_sub_2': 'implants, aesthetics, and private treatments.',
        'pain_header': 'Practice',
        'pain_header_red': 'Challenges',
        'pain_1_title': 'Low Value Visits:',
        'pain_1': 'Full calendar but low revenue per patient.',
        'pain_2_title': 'Invisible Online:',
        'pain_2': 'Expats and locals can\'t find you on Google.',
        'pain_3_title': 'No Trust:',
        'pain_3': 'Website doesn\'t convey the quality of your work.',
        'solution_header': 'My',
        'solution_header_grad': 'Approach',
        'sol_1_title': 'Treatment Focus:',
        'sol_1': 'Campaigns specifically for implants, veneers, and orthodontics.',
        'sol_2_title': 'English Speaking:',
        'sol_2': 'Target the huge expat community in Germany (they need dentists too!).',
        'sol_3_title': 'Authority:',
        'sol_3': 'Build trust before they even call you.',
        'package_title': 'Practice Growth',
        'package_sub': 'Fill your chair with the right patients.',
        'card_1_icon': '📅',
        'card_1_title': 'Appointments',
        'card_1_desc': 'Automated booking flow from ads.',
        'card_2_icon': '💎',
        'card_2_title': 'Premium Cases',
        'card_2_desc': 'Focus on high-margin treatments.',
        'card_3_icon': '🌍',
        'card_3_title': 'Expat Market',
        'card_3_desc': 'Capture the English-speaking market in your city.',
        'form_placeholder': 'How many chairs? Main focus (General/Implants)?'
    },
    'restaurant_marketing.html': {
        'title': 'Restaurant Marketing | Digital Ad Expert',
        'meta_desc': 'Full tables and more orders. Google Ads & Social Media for Restaurants.',
        'icon': '🍔',
        'badge_text': 'Restaurant Marketing',
        'h1_line1': 'Full Tables,',
        'h1_line2': 'Busy Kitchen!',
        'hero_sub_1': 'Great food isn\'t enough if nobody knows about it.',
        'hero_sub_bold': 'Make your venue',
        'hero_sub_2': 'the hottest spot in town.',
        'pain_header': 'Restaurant',
        'pain_header_red': 'Struggle',
        'pain_1_title': 'Empty Weekdays:',
        'pain_1': 'Busy weekends but dead Tuesdays.',
        'pain_2_title': 'Platform Fees:',
        'pain_2': 'Delivery apps taking 30% of your margin.',
        'pain_3_title': 'Hard to Find:',
        'pain_3': 'Tourists can\'t find you on Maps.',
        'solution_header': 'The',
        'solution_header_grad': 'Recipe',
        'sol_1_title': 'Direct Orders:',
        'sol_1': 'Drive traffic to YOUR ordering system, keep the margin.',
        'sol_2_title': 'Local SEO:',
        'sol_2': 'Rank #1 for "Best food near me".',
        'sol_3_title': 'Visual Ads:',
        'sol_3': 'Mouth-watering ads on Instagram & Google.',
        'package_title': 'Gastro Booster',
        'package_sub': 'For Restaurants, Cafes, and Delivery.',
        'card_1_icon': '🛵',
        'card_1_title': 'More Orders',
        'card_1_desc': 'Increase delivery volume directly.',
        'card_2_icon': '⭐',
        'card_2_title': 'Reviews',
        'card_2_desc': 'Get more 5-star reviews on Google.',
        'card_3_icon': '📸',
        'card_3_title': 'Visibility',
        'card_3_desc': 'Showcase your menu to hungry locals.',
        'form_placeholder': 'Cuisine type? Do you offer delivery?'
    },
    'realestate_marketing.html': {
        'title': 'Real Estate Marketing | Digital Ad Expert',
        'meta_desc': 'Get more seller leads and listings. Google Ads for Real Estate Agents.',
        'icon': '🏠',
        'badge_text': 'Real Estate',
        'h1_line1': 'More Listings,',
        'h1_line2': 'Faster Sales.',
        'hero_sub_1': 'The market is tough.',
        'hero_sub_bold': 'Reach home owners',
        'hero_sub_2': 'before your competitors do.',
        'pain_header': 'Agent',
        'pain_header_red': 'Challenges',
        'pain_1_title': 'Low Inventory:',
        'pain_1': 'Struggling to find new properties to sell.',
        'pain_2_title': 'Expensive Leads:',
        'pain_2': 'Portal leads are shared with 5 other agents.',
        'pain_3_title': 'Wasted Time:',
        'pain_3': 'Endless viewings with buyers who can\'t afford it.',
        'solution_header': 'My',
        'solution_header_grad': 'Strategy',
        'sol_1_title': 'Seller Targeting:',
        'sol_1': 'Ads targeting people looking to "sell my house".',
        'sol_2_title': 'Lead Qualifying:',
        'sol_2': 'Filter out tire-kickers before you call.',
        'sol_3_title': 'Personal Brand:',
        'sol_3': 'Become the go-to agent in your neighborhood.',
        'package_title': 'Agent System',
        'package_sub': 'Automated listing acquisition.',
        'card_1_icon': '🔑',
        'card_1_title': 'Seller Leads',
        'card_1_desc': ' Exclusive leads from owners ready to sell.',
        'card_2_icon': '📋',
        'card_2_title': 'Database',
        'card_2_desc': 'Build your own list of buyers and sellers.',
        'card_3_icon': '🏆',
        'card_3_title': 'Market Leader',
        'card_3_desc': 'Dominate your farming area.',
        'form_placeholder': 'Area of focus? (Sales/Rentals)?'
    },
    'kebab_marketing.html': {
        'title': 'Kebab & Food Stall Marketing | Digital Ad Expert',
        'meta_desc': 'Best Kebab in town? Prove it. Local marketing for food stalls and takeaways.',
        'icon': '🥙',
        'badge_text': 'Street Food & Kebab',
        'h1_line1': 'Lines Out',
        'h1_line2': 'The Door!',
        'hero_sub_1': 'You have the best taste.',
        'hero_sub_bold': 'I bring you',
        'hero_sub_2': 'the hungry crowd.',
        'pain_header': 'Street Food',
        'pain_header_red': 'Reality',
        'pain_1_title': 'Lunch Rush Only:',
        'pain_1': 'Busy for 2 hours, empty the rest of the day.',
        'pain_2_title': 'Competition:',
        'pain_2': 'A new shop opens every week.',
        'pain_3_title': 'No Online Presence:',
        'pain_3': 'Just an old Facebook page nobody sees.',
        'solution_header': 'My',
        'solution_header_grad': 'Boost',
        'sol_1_title': 'Local Visibility:',
        'sol_1': 'Be the first result for "Food near me".',
        'sol_2_title': 'Promotions:',
        'sol_2': 'Push notifications for lunch deals.',
        'sol_3_title': 'Social Viral:',
        'sol_3': 'TikTok style videos of your food.',
        'package_title': 'Street Food Pack',
        'package_sub': 'Fast, affordable, effective.',
        'card_1_icon': '🤤',
        'card_1_title': 'Cravings',
        'card_1_desc': 'Photos that make people hungry instantly.',
        'card_2_icon': '📍',
        'card_2_title': 'Maps Ranking',
        'card_2_desc': 'Stand out on Google Maps.',
        'card_3_icon': '🚀',
        'card_3_title': 'Fame',
        'card_3_desc': 'Become a local legend.',
        'form_placeholder': 'What do you sell (Kebab, Pizza, Burger)?'
    },
    'beauty_marketing.html': {
        'title': 'Beauty Salon Marketing | Digital Ad Expert',
        'meta_desc': 'Fully booked calendar. High-value clients for Beauty & Wellness salons.',
        'icon': '💅',
        'badge_text': 'Beauty & Wellness',
        'h1_line1': 'Fully Booked,',
        'h1_line2': 'No Gaps.',
        'hero_sub_1': 'Empty slots cost you money.',
        'hero_sub_bold': 'Fill your schedule',
        'hero_sub_2': 'with loyal, high-paying clients.',
        'pain_header': 'Salon',
        'pain_header_red': 'Issues',
        'pain_1_title': 'Cancellations:',
        'pain_1': 'Clients cancelling last minute or no-shows.',
        'pain_2_title': 'Bargain Hunters:',
        'pain_2': 'People asking for discounts constantly.',
        'pain_3_title': 'Instagram Fatigue:',
        'pain_3': 'Posting daily but getting no bookings.',
        'solution_header': 'The',
        'solution_header_grad': 'Glow Up',
        'sol_1_title': 'Dream Clients:',
        'sol_1': 'Target people who value quality and pay well.',
        'sol_2_title': 'Auto Booking:',
        'sol_2': 'Get confirmed appointments while you sleep.',
        'sol_3_title': 'Treatment Focus:',
        'sol_3': 'Promote high-ticket services (Laser, Botox, etc.).',
        'package_title': 'Beauty Booster',
        'package_sub': 'For Salons, Hairdressers, and Spas.',
        'card_1_icon': '📅',
        'card_1_title': 'Auto-Booking',
        'card_1_desc': 'Seamless online booking experience.',
        'card_2_icon': '✨',
        'card_2_title': 'Premium Brand',
        'card_2_desc': 'Look expensive, charge accordingly.',
        'card_3_icon': '💌',
        'card_3_title': 'Loyalty',
        'card_3_desc': 'Systems to bring clients back every month.',
        'form_placeholder': 'Main treatments (Laser, Nails, Skin)?'
    },
    'renovation_marketing.html': {
        'title': 'Construction & Renovation Marketing | Digital Ad Expert',
        'meta_desc': 'More construction jobs. Leads for renovation, painting, and building.',
        'icon': '🔨',
        'badge_text': 'Construction & Reno',
        'h1_line1': 'Big Projects,',
        'h1_line2': 'Better Margins.',
        'hero_sub_1': 'Don\'t rely on word-of-mouth alone.',
        'hero_sub_bold': 'Actively win',
        'hero_sub_2': 'the best projects in your area.',
        'pain_header': 'Contractor',
        'pain_header_red': 'Problems',
        'pain_1_title': 'Price War:',
        'pain_1': 'Clients always looking for the cheapest quote.',
        'pain_2_title': 'Small Jobs:',
        'pain_2': 'Running around for small repairs that don\'t pay.',
        'pain_3_title': 'Bad Leads:',
        'pain_3': 'Portal leads that waste your time.',
        'solution_header': 'My',
        'solution_header_grad': 'Strategy',
        'sol_1_title': 'Quality Leads:',
        'sol_1': 'Clients looking for quality work, not cheap fixes.',
        'sol_2_title': 'Project Focus:',
        'sol_2': 'Ads for full renovations, new builds, roofing, etc.',
        'sol_3_title': 'Trust:',
        'sol_3': 'A professional site that showcases your best work.',
        'package_title': 'Contractor Pack',
        'package_sub': 'For Painters, Builders, Electricians.',
        'card_1_icon': '🏠',
        'card_1_title': 'Big Jobs',
        'card_1_desc': 'Focus on high-value projects.',
        'card_2_icon': '📍',
        'card_2_title': 'Local Area',
        'card_2_desc': 'Jobs within your radius. No long drives.',
        'card_3_icon': '🤝',
        'card_3_title': 'Direct Contact',
        'card_3_desc': 'Clients call you or send blueprints directly.',
        'form_placeholder': 'Trade type? Service area radius?'
    }
}

# GENERATE DE
for filename, data in de_data.items():
    generate_page('de', filename, data)

# GENERATE EN
for filename, data in en_data.items():
    generate_page('en', filename, data)
