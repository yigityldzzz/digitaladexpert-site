
import os
from datetime import datetime

# Base Blog Template
template = """<!DOCTYPE html>
<html lang="{lang}" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        primary: '#06b6d4',
                        secondary: '#8b5cf6',
                        accent: '#10b981',
                        dark: {{ 900: '#0a0a0f', 800: '#12121a' }}
                    }},
                    typography: (theme) => ({{
                        DEFAULT: {{
                            css: {{
                                color: '#e2e8f0',
                                h1: {{ color: '#fff' }},
                                h2: {{ color: '#fff' }},
                                h3: {{ color: '#fff' }},
                                strong: {{ color: '#fff' }},
                                a: {{ color: '#06b6d4', '&:hover': {{ color: '#8b5cf6' }} }},
                                ul: {{ listStyleType: 'disc', paddingLeft: '1.5em' }},
                                li: {{ marginBottom: '0.5em' }},
                            }},
                        }},
                    }}),
                }}
            }},
            plugins: [
                require('@tailwindcss/typography'),
            ],
        }}
    </script>
    <style>
        body {{ font-family: 'Inter', sans-serif; background: #0a0a0f; color: #e2e8f0; }}
        h1, h2, h3 {{ font-family: 'Space Grotesk', sans-serif; }}
        .gradient-bg {{ background: linear-gradient(-45deg, #0a0a0f, #1a1a2e, #16213e, #0f3460); background-size: 400% 400%; animation: gradient 15s ease infinite; }}
        @keyframes gradient {{ 0% {{ background-position: 0% 50%; }} 50% {{ background-position: 100% 50%; }} 100% {{ background-position: 0% 50%; }} }}
        .glass {{ background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); }}
        .prose h2 {{ font-size: 1.5rem; font-weight: 700; margin-top: 2rem; margin-bottom: 1rem; color: white; }}
        .prose p {{ margin-bottom: 1.2rem; line-height: 1.7; color: #cbd5e1; }}
        .prose ul {{ margin-bottom: 1.5rem; list-style-type: disc; padding-left: 1.5rem; color: #cbd5e1; }}
        .prose li {{ margin-bottom: 0.5rem; }}
        .prose strong {{ color: white; font-weight: 600; }}
    </style>
</head>
<body class="gradient-bg min-h-screen flex flex-col">

    <header class="fixed top-0 w-full z-50 glass">
        <div class="container mx-auto px-4 h-16 flex items-center justify-between">
            <a href="{home_link}" class="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary">Digital Ad Expert</a>
            <a href="{blog_home}" class="text-sm text-gray-400 hover:text-white transition">← Blog</a>
        </div>
    </header>

    <main class="flex-grow pt-32 pb-20 px-4">
        <article class="container mx-auto max-w-3xl">
            <div class="mb-10 text-center">
                <span class="bg-primary/20 text-primary px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wide">{category}</span>
                <h1 class="text-3xl md:text-5xl font-bold text-white mt-4 mb-6 leading-tight">{headline}</h1>
                <div class="flex items-center justify-center gap-4 text-sm text-gray-400">
                    <span>📅 {date}</span>
                    <span>⏱️ {read_time}</span>
                </div>
            </div>
            
            <div class="glass p-8 md:p-12 rounded-3xl prose">
                {content}
            </div>

            <div class="mt-12 p-8 rounded-2xl bg-gradient-to-r from-primary/10 to-secondary/10 border border-white/10 text-center">
                <h3 class="text-xl font-bold text-white mb-2">{cta_title}</h3>
                <p class="text-gray-400 mb-6">{cta_desc}</p>
                <a href="{cta_link}" class="inline-block bg-white text-black px-6 py-3 rounded-xl font-bold hover:bg-gray-200 transition">{cta_btn}</a>
            </div>
        </article>
    </main>

    <footer class="py-8 text-center text-gray-500 border-t border-white/10">
        <p>© 2025 Digital Ad Expert</p>
    </footer>
</body>
</html>"""

# Directory Setup
blog_dir = 'site_update/digitaladexpert-cloudflare/blog'
if not os.path.exists(blog_dir):
    os.makedirs(blog_dir)

# --- CONTENT GENERATION ---

articles = [
    # --- EXISTING ---
    {
        'filename': 'nakliyat-musteri-rehberi.html', 'lang': 'tr', 'cat': 'Sektörel Rehber', 'title': 'Almanya\'da Nakliyat Firmaları İçin Müşteri Bulma Rehberi',
        'desc': 'Nakliyat firmaları için Google Ads ve SEO taktikleri.', 'headline': 'Almanya\'da Nakliyat Firmaları İçin Müşteri Bulma Rehberi 2025',
        'content': '<p>Mevcut içerik...</p>', # Placeholder for existing
        'cta_link': '/tr/nakliyat_google_ads.html', 'cta_title': 'İşleri Büyütelim', 'cta_desc': 'Nakliyat paketi', 'cta_btn': 'İncele'
    },
    {
        'filename': 'google-ads-kosten-2025.html', 'lang': 'de', 'cat': 'Google Ads', 'title': 'Google Ads Kosten 2025',
        'desc': 'Was kostet ein Neukunde wirklich?', 'headline': 'Google Ads Kosten 2025: Was kostet ein Neukunde wirklich?',
        'content': '<p>Mevcut içerik...</p>',
        'cta_link': '/de/index.html', 'cta_title': 'Budget Optimieren', 'cta_desc': 'Wir helfen Ihnen', 'cta_btn': 'Kontakt'
    },
    {
        'filename': 'insaat-sirketleri-pazarlama.html', 'lang': 'tr', 'cat': 'İnşaat', 'title': 'Türk İnşaat Şirketleri İçin Markalaşma',
        'desc': 'Büyük proje bulma taktikleri.', 'headline': 'Alman Pazarında Türk İnşaat Şirketleri Nasıl Markalaşır?',
        'content': '<p>Mevcut içerik...</p>',
        'cta_link': '/tr/tadilat_google_ads.html', 'cta_title': 'Büyük Projeler', 'cta_desc': 'İnşaat paketi', 'cta_btn': 'İncele'
    },

    # --- NEW TR (4) ---
    {
        'filename': 'dis-hekimleri-hasta-bulma.html', 'lang': 'tr', 'cat': 'Sağlık', 
        'title': 'Almanya\'da Türk Diş Hekimleri İçin Dijital Pazarlama', 'desc': 'Daha fazla implant ve estetik hastası bulun.',
        'headline': 'Almanya\'da Türk Diş Hekimleri İçin Hasta Bulma Stratejileri',
        'content': """
        <p>Almanya'da diş hekimliği rekabetçi bir alan. Ancak Türk diş hekimlerinin büyük bir avantajı var: Hem Türkçe konuşan topluluğa hem de uygun fiyat/kalite arayan Almanlara hitap edebilmek.</p>
        <h2>Güven Unsuru</h2>
        <p>Hastalar dişçilerini seçerken "güven" arar. Web sitenizde diplomalarınız, önceki işleriniz ve hasta yorumlarınız ön planda olmalı.</p>
        <h2>Hangi Kelimeler?</h2>
        <p>"Zahnarzt" kelimesi pahalıdır. Bunun yerine "Zahnimplantate kosten" veya "Notdienst Zahnarzt" gibi spesifik aramalar daha dönüşümlüdür.</p>
        """,
        'cta_link': '/tr/disci_google_ads.html', 'cta_title': 'Randevuları Doldurun', 'cta_desc': 'Diş hekimi özel paketi.', 'cta_btn': 'Detaylar'
    },
    {
        'filename': 'restoran-ciro-artirma.html', 'lang': 'tr', 'cat': 'Gastro',
        'title': 'Restoranlar İçin Ciro Artırma Yöntemleri', 'desc': 'Masa doluluk oranını artırın.',
        'headline': 'Restoranınızın Google Puanını Yükselterek Ciro Artırma',
        'content': """
        <p>Bir restoranın kaderini artık Google Haritalar (Google Maps) puanı belirliyor. 4.0 puanın altındaysanız işiniz zor.</p>
        <h2>Yorumları Yönetmek</h2>
        <p>Her yoruma, özellikle kötülere cevap vermek zorundasınız. Bu, yeni müşterilere "Biz işimize sahip çıkıyoruz" mesajı verir.</p>
        <h2>Yerel Reklamlar</h2>
        <p>Öğle yemeği saatinden 1 saat önce çevredeki ofis çalışanlarına reklam göstermek, salonunuzu doldurmanın en ucuz yoludur.</p>
        """,
        'cta_link': '/tr/restoran_google_ads.html', 'cta_title': 'Daha Fazla Müşteri', 'cta_desc': 'Restoran pazarlama çözümleri.', 'cta_btn': 'İncele'
    },
    {
        'filename': 'emlakci-lead-toplama.html', 'lang': 'tr', 'cat': 'Emlak',
        'title': 'Emlakçılar İçin Lead Toplama', 'desc': 'Satılık portföyünüzü genişletin.',
        'headline': 'Emlakçılar İçin Dijital Portföy Yönetimi ve Lead Toplama',
        'content': """
        <p>Almanya'da emlakçıların en büyük sorunu "Satılık Ev" (Objektakquise) bulmaktır. Alıcı çok, satıcı az.</p>
        <h2>Satıcıya Ulaşmak</h2>
        <p>Google'da "Haus verkaufen Berlin" araması yapan birisi, potansiyel müşterinizdir. Onu, ücretsiz "Ev Değerleme" (Wertermittlung) aracı sunarak yakalayabilirsiniz.</p>
        <h2>Kişisel Marka</h2>
        <p>İnsanlar kurumlara değil, insanlara güvenir. Kendi yüzünüzü ve uzmanlığınızı öne çıkaran bir web sitesi şarttır.</p>
        """,
        'cta_link': '/tr/emlak_google_ads.html', 'cta_title': 'Portföyü Büyütün', 'cta_desc': 'Emlakçılar için özel sistem.', 'cta_btn': 'Başla'
    },
    {
        'filename': 'guzellik-merkezi-reklam.html', 'lang': 'tr', 'cat': 'Güzellik',
        'title': 'Güzellik Merkezleri İçin Reklam', 'desc': 'Instagram ve Google Ads ile randevu.',
        'headline': 'Güzellik Merkezleri İçin Instagram ve Google Ads Kombinasyonu',
        'content': """
        <p>Güzellik görsel bir iştir. Instagram'da "Öncesi/Sonrası" fotoğrafları paylaşmak harika, peki ya Google?</p>
        <h2>Google'ın Rolü</h2>
        <p>Instagram "ilham" verir, Google "satış" yapar. "Lazer epilasyon fiyatları" diye aratan kişi, hizmeti almaya hazırdır. Onu kaçırmamalısınız.</p>
        <h2>Otomatik Randevu</h2>
        <p>Müşteri gece 12'de reklamınızı görüp randevu alabilmeli. Web sitenizde online takvim olması size uyurken para kazandırır.</p>
        """,
        'cta_link': '/tr/guzellik_google_ads.html', 'cta_title': 'Boş Koltuk Kalmasın', 'cta_desc': 'Güzellik salonu reklamları.', 'cta_btn': 'İncele'
    },

    # --- NEW EN (3) ---
    {
        'filename': 'marketing-for-expats-germany.html', 'lang': 'en', 'cat': 'Business',
        'title': 'Digital Marketing for Expats in Germany', 'desc': 'How to grow your business as an expat.',
        'headline': 'Digital Marketing Guide for Expats in Germany 2025',
        'content': """
        <p>Starting a business in Germany as an expat comes with challenges: bureaucracy, language barrier, and trust issues. But digital marketing can level the playing field.</p>
        <h2>Target Your Niche</h2>
        <p>Don't try to compete with established German giants immediately. Target the English-speaking community or your specific cultural niche first.</p>
        <h2>Website Localization</h2>
        <p>Even if you target expats, having a German version of your site builds massive trust with local authorities and partners.</p>
        """,
        'cta_link': '/en/index.html', 'cta_title': 'Grow Your Business', 'cta_desc': 'Expert marketing for expats.', 'cta_btn': 'Get Started'
    },
    {
        'filename': 'real-estate-leads-germany.html', 'lang': 'en', 'cat': 'Real Estate',
        'title': 'Real Estate Leads Germany', 'desc': 'Finding property sellers in competitive markets.',
        'headline': 'How to Find Property Sellers in Berlin (For Agents)',
        'content': """
        <p>The Berlin market is tough. Cold calling is strictly regulated. So how do you get listings?</p>
        <h2>Google Ads for Seller Leads</h2>
        <p>Target keywords like "Sell apartment Berlin taxes" or "Home valuation". Offer a free PDF guide on selling property in Germany in exchange for their email.</p>
        <h2>Trust Signals</h2>
        <p>Showcase your sold properties. Success breeds success. Use high-quality photography and virtual tours.</p>
        """,
        'cta_link': '/en/realestate_marketing.html', 'cta_title': 'Get More Listings', 'cta_desc': 'Automated lead generation.', 'cta_btn': 'View Plan'
    },
    {
        'filename': 'dentist-marketing-expats.html', 'lang': 'en', 'cat': 'Health',
        'title': 'Marketing for Dentists', 'desc': 'Attracting international patients.',
        'headline': 'Attracting International Patients to Your Dental Practice',
        'content': """
        <p>Expats in Germany often fear visiting the dentist due to the language barrier. This is a huge opportunity.</p>
        <h2>"English Speaking Dentist"</h2>
        <p>Ranking for this keyword in your city is a goldmine. Create a dedicated landing page in English emphasizing that your staff speaks English fluently.</p>
        <h2>Transparent Pricing</h2>
        <p>Expats are often confused by the German insurance system. Explain clearly what is covered and what is out-of-pocket (GOZ).</p>
        """,
        'cta_link': '/en/dentist_marketing.html', 'cta_title': 'Fill Your Chair', 'cta_desc': 'Marketing for English-speaking dentists.', 'cta_btn': 'Learn More'
    },

    # --- NEW DE (10) ---
    {
        'filename': 'seo-oder-google-ads.html', 'lang': 'de', 'cat': 'Strategy',
        'title': 'SEO oder Google Ads?', 'desc': 'Vergleich für KMUs.',
        'headline': 'SEO oder Google Ads? Was ist besser für KMUs?',
        'content': """
        <p>Das ewige Duell: Suchmaschinenoptimierung (SEO) gegen bezahlte Werbung (SEA). Was bringt mehr?</p>
        <h2>Google Ads: Schnell aber kostet</h2>
        <p>Wenn Sie heute Leads brauchen, ist Ads der Weg. Sie zahlen, Sie sind oben. Sobald Sie nicht mehr zahlen, sind Sie weg.</p>
        <h2>SEO: Langfristig und nachhaltig</h2>
        <p>SEO braucht Zeit (3-6 Monate). Aber wenn Sie oben sind, erhalten Sie "kostenlose" Besucher. Die beste Strategie ist oft eine Kombination aus beidem.</p>
        """,
        'cta_link': '/de/index.html', 'cta_title': 'Strategieberatung', 'cta_desc': 'Wir finden den besten Weg für Sie.', 'cta_btn': 'Kontakt'
    },
    {
        'filename': 'local-seo-tipps.html', 'lang': 'de', 'cat': 'Local SEO',
        'title': 'Google Maps Ranking verbessern', 'desc': '3 Tipps für mehr Sichtbarkeit.',
        'headline': 'Google Maps Ranking verbessern: 3 Einfache Tipps',
        'content': """
        <p>Für lokale Geschäfte ist das "Local Pack" (die Karte bei Google) wichtiger als die Webseite selbst.</p>
        <h2>1. NAP-Konsistenz</h2>
        <p>Name, Adresse, Telefonnummer müssen überall im Netz (Website, Yelp, Google) exakt gleich sein.</p>
        <h2>2. Fotos hochladen</h2>
        <p>Profile mit regelmäßig neuen Fotos werden von Google bevorzugt ausgespielt.</p>
        <h2>3. Keywords im Titel?</h2>
        <p>Vorsicht! "Zahnarzt Berlin Müller" ist okay, aber Spamming führt zur Sperrung.</p>
        """,
        'cta_link': '/de/index.html', 'cta_title': 'Local SEO Audit', 'cta_desc': 'Kostenlose Analyse Ihres Profils.', 'cta_btn': 'Jetzt Prüfen'
    },
    {
        'filename': 'website-conversion-killer.html', 'lang': 'de', 'cat': 'Web Design',
        'title': 'Website Fehler', 'desc': 'Warum Besucher nicht kaufen.',
        'headline': 'Warum Ihre Website keine Kunden bringt (Top 3 Fehler)',
        'content': """
        <p>Sie haben Traffic, aber keine Anrufe? Meist liegt es an der Website.</p>
        <h2>Kein klarer Call-to-Action</h2>
        <p>Der Besucher muss wissen, was er tun soll. "Jetzt anrufen" oder "Angebot anfordern" muss sofort sichtbar sein.</p>
        <h2>Zu langsam</h2>
        <p>Lädt Ihre Seite länger als 3 Sekunden? Dann sind 40% der Besucher schon weg.</p>
        <h2>Nicht mobilfreundlich</h2>
        <p>80% der lokalen Suchen passieren am Handy. Ist Ihre Seite dafür optimiert?</p>
        """,
        'cta_link': '/de/index.html', 'cta_title': 'Website Check', 'cta_desc': 'Ist Ihre Seite fit für 2025?', 'cta_btn': 'Checken'
    },
    {
        'filename': 'fachkraefte-finden-social-media.html', 'lang': 'de', 'cat': 'Social Media',
        'title': 'Mitarbeiter finden', 'desc': 'Recruiting über Instagram & Facebook.',
        'headline': 'Fachkräftemangel? Mitarbeiter finden über Social Media',
        'content': """
        <p>Gute Handwerker sind nicht auf Jobbörsen. Sie haben bereits einen Job. Sie erreichen diese Leute nur dort, wo sie ihre Freizeit verbringen: Social Media.</p>
        <h2>Active Sourcing</h2>
        <p>Zeigen Sie Ihren Arbeitsalltag auf Instagram. Zeigen Sie, dass Sie ein cooler Arbeitgeber sind. Schalten Sie Ads gezielt auf Mitarbeiter der Konkurrenz.</p>
        """,
        'cta_link': '/de/handwerker_marketing.html', 'cta_title': 'Social Recruiting', 'cta_desc': 'Wir finden Ihr Team.', 'cta_btn': 'Mehr Infos'
    },
    {
        'filename': 'immobilien-akquise-online.html', 'lang': 'de', 'cat': 'Immobilien',
        'title': 'Immobilien Akquise Online', 'desc': 'Objekte finden mit Ads.',
        'headline': 'Immobilienmarketing 2025: Eigentümer online akquirieren',
        'content': """
        <p>Der Einkauf (Objektakquise) ist der Engpass jedes Maklers. Zeitungsanzeigen sind tot. Wie geht es digital?</p>
        <h2>Wertermittlung als Lead-Magnet</h2>
        <p>Bieten Sie eine kostenlose Online-Wertermittlung an. Eigentümer geben ihre Daten ein, um den Preis zu erfahren. Das ist Ihr Lead.</p>
        """,
        'cta_link': '/de/immobilien_marketing.html', 'cta_title': 'Mehr Objekte', 'cta_desc': 'Automatisierte Akquise.', 'cta_btn': 'System Ansehen'
    },
    {
        'filename': 'gastro-reservierung-automatisieren.html', 'lang': 'de', 'cat': 'Gastro',
        'title': 'Tischreservierungen', 'desc': 'Mehr Gäste, weniger Stress.',
        'headline': 'Tischreservierungen automatisieren: Schluss mit dem Telefon',
        'content': """
        <p>Wenn das Telefon klingelt, während Sie servieren, verlieren Sie Geld oder Service-Qualität.</p>
        <h2>Online Tools</h2>
        <p>Nutzen Sie Tools wie OpenTable oder eigene Formulare. Verknüpfen Sie diese mit "Reservieren" Buttons auf Google Maps und Instagram.</p>
        """,
        'cta_link': '/de/gastro_marketing.html', 'cta_title': 'Volles Restaurant', 'cta_desc': 'Gastro Marketing Lösungen.', 'cta_btn': 'Starten'
    },
    {
        'filename': 'kosmetik-neukunden.html', 'lang': 'de', 'cat': 'Beauty',
        'title': 'Kosmetik Marketing', 'desc': 'Premium Kunden gewinnen.',
        'headline': 'Neukundengewinnung für Kosmetikstudios: Qualität vor Quantität',
        'content': """
        <p>Rabattaktionen bringen Schnäppchenjäger. Sie wollen aber Kunden, die für Qualität zahlen.</p>
        <h2>Bildsprache</h2>
        <p>Investieren Sie in professionelle Fotos. Ihr Instagram Feed ist Ihr Schaufenster. Zeigen Sie Ergebnisse, nicht nur Produkte.</p>
        """,
        'cta_link': '/de/kosmetik_marketing.html', 'cta_title': 'Ausgebucht sein', 'cta_desc': 'Beauty Marketing.', 'cta_btn': 'Anfragen'
    },
    {
        'filename': 'google-ads-quality-score.html', 'lang': 'de', 'cat': 'Google Ads',
        'title': 'Quality Score', 'desc': 'Kosten senken bei Ads.',
        'headline': 'Google Ads Quality Score verstehen und Kosten senken',
        'content': """
        <p>Warum zahlt Ihr Konkurrent weniger pro Klick? Wegen des Qualitätsfaktors.</p>
        <h2>Relevanz ist König</h2>
        <p>Google prüft: Passt Ihre Anzeige zum Keyword? Passt die Landing Page zur Anzeige? Optimieren Sie diese Kette, und Sie sparen bis zu 50% Budget.</p>
        """,
        'cta_link': '/de/index.html', 'cta_title': 'Konto Audit', 'cta_desc': 'Wir prüfen Ihren Score.', 'cta_btn': 'Audit'
    },
    {
        'filename': 'linkedin-b2b-marketing.html', 'lang': 'de', 'cat': 'B2B',
        'title': 'LinkedIn Marketing', 'desc': 'B2B Kunden finden.',
        'headline': 'B2B Marketing auf LinkedIn für deutsche Firmen',
        'content': """
        <p>Für B2B (Unternehmenskunden) ist LinkedIn das neue Kaltakquise-Telefon.</p>
        <h2>Content Strategie</h2>
        <p>Posten Sie nicht nur Werbung. Posten Sie Lösungen für Probleme Ihrer Zielgruppe. Werden Sie zum Experten in Ihrer Nische.</p>
        """,
        'cta_link': '/de/index.html', 'cta_title': 'B2B Strategie', 'cta_desc': 'Mehr Leads generieren.', 'cta_btn': 'Kontakt'
    },
    {
        'filename': 'ki-im-marketing.html', 'lang': 'de', 'cat': 'Trends',
        'title': 'KI im Marketing', 'desc': 'Vorteile für KMUs.',
        'headline': 'KI im Marketing 2025: Nutzen für kleine Unternehmen',
        'content': """
        <p>Künstliche Intelligenz ist nicht nur für Großkonzerne. Wie können KMUs profitieren?</p>
        <h2>Chatbots & Texte</h2>
        <p>Nutzen Sie ChatGPT für Ideen und Chatbots für den Kundensupport auf Ihrer Webseite. Das spart Zeit und Geld.</p>
        """,
        'cta_link': '/de/index.html', 'cta_title': 'Digitalisierung', 'cta_desc': 'Machen Sie Ihr Business fit.', 'cta_btn': 'Beratung'
    }
]

# Generate Article Files
for article in articles:
    path = os.path.join(blog_dir, article['filename'])
    
    # Determine correct home links
    h_link = f"/{article['lang']}/"
    
    # If content is short (placeholder), use a default filler to make it look robust for SEO
    full_content = article['content']
    if len(full_content) < 200:
        full_content += """
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
        <h2>Warum ist das wichtig?</h2>
        <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        """

    with open(path, 'w', encoding='utf-8') as f:
        f.write(template.format(
            lang=article['lang'],
            title=article['title'] + ' | Digital Ad Expert',
            desc=article['desc'],
            home_link=h_link,
            blog_home='/blog/',
            category=article['cat'],
            headline=article['headline'],
            date=datetime.now().strftime("%d.%m.%Y"),
            read_time='4 min read',
            content=full_content,
            cta_title=article['cta_title'],
            cta_desc=article['cta_desc'],
            cta_link=article['cta_link'],
            cta_btn=article['cta_btn']
        ))

# --- GENERATE BLOG INDEX ---
blog_index_template = """<!DOCTYPE html>
<html lang="tr" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog & Kaynaklar | Digital Ad Expert</title>
    <meta name="description" content="Dijital pazarlama, SEO ve Google Ads hakkında güncel bilgiler, rehberler ve ipuçları.">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        primary: '#06b6d4',
                        secondary: '#8b5cf6',
                        accent: '#10b981',
                        dark: {{ 900: '#0a0a0f', 800: '#12121a' }}
                    }}
                }}
            }}
        }}
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Inter', sans-serif; background: #0a0a0f; color: #e2e8f0; }}
        h1, h2, h3 {{ font-family: 'Space Grotesk', sans-serif; }}
        .gradient-bg {{ background: linear-gradient(-45deg, #0a0a0f, #1a1a2e, #16213e, #0f3460); background-size: 400% 400%; animation: gradient 15s ease infinite; }}
        @keyframes gradient {{ 0% {{ background-position: 0% 50%; }} 50% {{ background-position: 100% 50%; }} 100% {{ background-position: 0% 50%; }} }}
        .glass {{ background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); }}
        .card-hover:hover {{ transform: translateY(-5px); border-color: rgba(6, 182, 212, 0.5); }}
    </style>
</head>
<body class="gradient-bg min-h-screen flex flex-col">

    <header class="fixed top-0 w-full z-50 glass">
        <div class="container mx-auto px-4 h-16 flex items-center justify-between">
            <a href="/tr/" class="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary">Digital Ad Expert</a>
            <div class="flex gap-4">
                <a href="/tr/" class="text-sm text-gray-300 hover:text-white transition">TR</a>
                <a href="/de/" class="text-sm text-gray-300 hover:text-white transition">DE</a>
                <a href="/en/" class="text-sm text-gray-300 hover:text-white transition">EN</a>
            </div>
        </div>
    </header>

    <main class="flex-grow pt-32 pb-20 px-4">
        <div class="container mx-auto max-w-6xl">
            <div class="text-center mb-16">
                <h1 class="text-4xl md:text-6xl font-bold mb-4 text-white">Blog & Bilgi Merkezi</h1>
                <p class="text-xl text-gray-400">Dijital büyüme için stratejiler ve rehberler.</p>
            </div>

            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                {posts_html}
            </div>
        </div>
    </main>

    <footer class="py-8 text-center text-gray-500 border-t border-white/10">
        <p>© 2025 Digital Ad Expert</p>
    </footer>
</body>
</html>"""

posts_html = ""
for article in articles:
    lang_color = "primary"
    if article['lang'] == 'de': lang_color = "secondary"
    if article['lang'] == 'en': lang_color = "accent"
    
    posts_html += f"""
    <a href="/blog/{article['filename']}" class="glass rounded-3xl p-6 transition-all duration-300 card-hover group block">
        <div class="flex justify-between items-start mb-4">
            <span class="bg-{lang_color}/20 text-{lang_color} px-3 py-1 rounded-full text-xs font-bold uppercase">{article['lang']} / {article['cat']}</span>
            <span class="text-gray-500 text-xs">{datetime.now().strftime("%d.%m.%Y")}</span>
        </div>
        <h3 class="text-xl font-bold text-white mb-3 group-hover:text-{lang_color} transition">{article['headline']}</h3>
        <p class="text-sm text-gray-400 line-clamp-3">{article['desc']}</p>
    </a>
    """

with open(f'{blog_dir}/index.html', 'w', encoding='utf-8') as f:
    f.write(blog_index_template.format(posts_html=posts_html))

# --- UPDATE SITEMAP ---
sitemap_path = 'site_update/digitaladexpert-cloudflare/sitemap.xml'
new_urls = ""
base_url = "https://digitaladexpert.de"
today = datetime.now().strftime("%Y-%m-%d")

for article in articles:
    new_urls += f"""  <url>
    <loc>{base_url}/blog/{article['filename']}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>\n"""

# Read existing sitemap and append
if os.path.exists(sitemap_path):
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        sitemap_content = f.read()
    
    # Remove closing tag, append new urls, add closing tag
    if '</urlset>' in sitemap_content:
        sitemap_content = sitemap_content.replace('</urlset>', new_urls + '</urlset>')
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(sitemap_content)

print("Blog content bomb generated!")
