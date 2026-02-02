
import os
from datetime import datetime

# Base Blog Template (Same as before)
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

# --- CORRECTED CONTENT FOR FIRST 3 ---

content_nakliyat = """
<p>Almanya'da nakliyat sektörü (Umzug) her geçen yıl daha rekabetçi hale geliyor. Berlin, Hamburg, Münih veya Köln fark etmeksizin, artık "sadece kamyonum var" demek iş almak için yeterli değil. Peki, Türk nakliyat firmaları Alman rakiplerinin önüne nasıl geçer?</p>

<h2>1. "Kiralık Kamyon" Tuzağına Düşmeyin</h2>
<p>Google Ads reklamlarında yapılan en büyük hata, negatif kelime kullanmamaktır. Eğer reklamlarınız "LKW mieten" (Kamyon kiralamak) veya "Umzugshelfer studenten" (Öğrenci taşıyıcı) gibi kelimelerde çıkıyorsa, bütçenizi çöpe atıyorsunuz demektir. Siz komple ev taşıma (Privatumzug) hizmeti satıyorsunuz, ucuza kaçanları değil.</p>

<h2>2. Güven: Alman Müşterinin Olmazsa Olmazı</h2>
<p>Web sitenizde mutlaka şunlar olmalı:</p>
<ul>
    <li>Net bir "Impressum" sayfası.</li>
    <li>Sigorta (Transportversicherung) bilgisi.</li>
    <li>Sabit hat numarası (Sadece cep telefonu güven vermez).</li>
</ul>

<h2>3. Yerel SEO'nun Gücü</h2>
<p>Müşteriler genellikle "Umzugsfirma Berlin" veya "Umzug in der Nähe" diye arama yapar. Google Haritalar kaydınızın (Google My Business) optimize edilmiş olması ve yorumlarınızın (Rezensionen) yönetilmesi sizi bedavadan üst sıralara taşır.</p>

<h2>Sonuç</h2>
<p>Dijital pazarlama bir masraf değil, yatırımdır. Doğru kurgulanmış bir Google Ads kampanyası ile 100€ harcayıp 1000€'luk iş alabilirsiniz. Önemli olan "Sniper" gibi nokta atışı yapmaktır.</p>
"""

content_ads = """
<p>Viele Unternehmer fragen sich: "Lohnt sich Google Ads für mich?" oder "Ist das nicht zu teuer?". Die kurze Antwort: Es ist nur teuer, wenn man es falsch macht. Hier ist die Wahrheit über Klickpreise (CPC) in Deutschland für 2025.</p>

<h2>Durchschnittliche Klickpreise nach Branchen</h2>
<p>Basierend auf Daten von 2024/2025 sehen wir folgende Trends in Deutschland:</p>
<ul>
    <li><strong>Schlüsseldienst / Notdienste:</strong> Sehr hoch (15€ - 40€ pro Klick).</li>
    <li><strong>Finanzen & Versicherung:</strong> Hoch (5€ - 15€ pro Klick).</li>
    <li><strong>Handwerk & Dienstleistung:</strong> Mittel (2€ - 6€ pro Klick).</li>
    <li><strong>E-Commerce:</strong> Variabel (0,50€ - 3€ pro Klick).</li>
</ul>

<h2>Qualitätsfaktor: Ihr Geheimwaffe</h2>
<p>Google belohnt relevante Werbung. Wenn Ihre Anzeige und Ihre Landing Page perfekt zusammenpassen, zahlen Sie WENIGER als Ihre Konkurrenz, um GANZ OBEN zu stehen. Das nennt man den "Qualitätsfaktor" (Quality Score).</p>

<h2>Budget-Tipp für KMUs</h2>
<p>Starten Sie nicht mit einem riesigen Budget. Starten Sie "Lokal". Wenn Sie ein Zahnarzt in Köln sind, schalten Sie keine Werbung in ganz NRW. Konzentrieren Sie Ihr Budget auf einen 5-10km Radius. So dominieren Sie Ihre Nachbarschaft mit minimalen Kosten.</p>
"""

content_insaat = """
<p>Almanya'da inşaat ve tadilat (Handwerk) sektörü altın çağını yaşıyor. Ancak büyük projeleri kapmak eskisi kadar kolay değil. "Tavsiye usulü" (Mundpropaganda) hala önemli ama yetersiz. Peki dijital dünyada nasıl marka olunur?</p>

<h2>Güven Veren Bir Vitrin Oluşturun</h2>
<p>Alman ev sahibi, evini teslim edeceği ustayı seçerken ince eler sık dokur. Web sitenizde mutlaka "Referanslar" bölümü olmalı. Yaptığınız banyoların, boyadığınız evlerin 'Öncesi/Sonrası' fotoğrafları, bin kelimeden daha etkilidir.</p>

<h2>Hangi Kelimeleri Hedeflemeli?</h2>
<p>Google'da "Maler" (Boyacı) kelimesi çok geneldir. Bunun yerine:</p>
<ul>
    <li>"Fassadensanierung" (Cephe yenileme)</li>
    <li>"Altbausanierung" (Eski bina tadilatı)</li>
    <li>"Badsanierung komplett" (Komple banyo tadilatı)</li>
</ul>
<p>Gibi spesifik ve yüksek bütçeli işleri hedefleyen kelimelere reklam vermek, kar marjınızı artırır.</p>

<h2>Türk Firmaları İçin Fırsat</h2>
<p>Alman firmaları genellikle çok doludur ve aylar sonrasına gün verir. "Hızlı ve Kaliteli" (Schnell & Qualitativ) vurgusu yaparak, acil iş arayan müşterileri kolayca kazanabilirsiniz.</p>
"""

# Re-Generate the 3 faulty pages
files_to_fix = [
    {
        'filename': 'nakliyat-musteri-rehberi.html', 'lang': 'tr', 'cat': 'Sektörel Rehber', 'title': 'Almanya\'da Nakliyat Firmaları İçin Müşteri Bulma Rehberi',
        'desc': 'Nakliyat firmaları için Google Ads ve SEO taktikleri.', 'headline': 'Almanya\'da Nakliyat Firmaları İçin Müşteri Bulma Rehberi 2025',
        'content': content_nakliyat,
        'cta_link': '/tr/nakliyat_google_ads.html', 'cta_title': 'İşleri Büyütelim', 'cta_desc': 'Nakliyat paketi', 'cta_btn': 'İncele'
    },
    {
        'filename': 'google-ads-kosten-2025.html', 'lang': 'de', 'cat': 'Google Ads', 'title': 'Google Ads Kosten 2025',
        'desc': 'Was kostet ein Neukunde wirklich?', 'headline': 'Google Ads Kosten 2025: Was kostet ein Neukunde wirklich?',
        'content': content_ads,
        'cta_link': '/de/index.html', 'cta_title': 'Budget Optimieren', 'cta_desc': 'Wir helfen Ihnen', 'cta_btn': 'Kontakt'
    },
    {
        'filename': 'insaat-sirketleri-pazarlama.html', 'lang': 'tr', 'cat': 'İnşaat', 'title': 'Türk İnşaat Şirketleri İçin Markalaşma',
        'desc': 'Büyük proje bulma taktikleri.', 'headline': 'Alman Pazarında Türk İnşaat Şirketleri Nasıl Markalaşır?',
        'content': content_insaat,
        'cta_link': '/tr/tadilat_google_ads.html', 'cta_title': 'Büyük Projeler', 'cta_desc': 'İnşaat paketi', 'cta_btn': 'İncele'
    }
]

for article in files_to_fix:
    path = os.path.join(blog_dir, article['filename'])
    h_link = f"/{article['lang']}/"
    
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
            content=article['content'],
            cta_title=article['cta_title'],
            cta_desc=article['cta_desc'],
            cta_link=article['cta_link'],
            cta_btn=article['cta_btn']
        ))
    print(f"Fixed {article['filename']}")

