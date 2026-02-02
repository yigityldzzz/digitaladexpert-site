
import os

def create_blog_structure():
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
    <!-- Add Typography Plugin Script via CDN for Tailwind (simulated for simplicity in static HTML) -->
    <style>
        /* Custom typography simulation since CDN plugin might be tricky */
        .prose {{ max-width: 65ch; margin: 0 auto; color: #cbd5e1; }}
        .prose h2 {{ color: white; font-size: 1.5em; font-weight: bold; margin-top: 2em; margin-bottom: 1em; }}
        .prose h3 {{ color: white; font-size: 1.25em; font-weight: bold; margin-top: 1.5em; margin-bottom: 0.5em; }}
        .prose p {{ margin-bottom: 1.5em; line-height: 1.8; }}
        .prose ul {{ list-style-type: disc; padding-left: 1.5em; margin-bottom: 1.5em; }}
        .prose li {{ margin-bottom: 0.5em; }}
        .prose strong {{ color: white; font-weight: bold; }}
        
        body {{ font-family: 'Inter', sans-serif; background: #0a0a0f; color: #e2e8f0; }}
        .gradient-bg {{ background: linear-gradient(-45deg, #0a0a0f, #1a1a2e, #16213e, #0f3460); background-size: 400% 400%; animation: gradient 15s ease infinite; }}
        @keyframes gradient {{ 0% {{ background-position: 0% 50%; }} 50% {{ background-position: 100% 50%; }} 100% {{ background-position: 0% 50%; }} }}
        .glass {{ background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); }}
    </style>
</head>
<body class="gradient-bg min-h-screen flex flex-col">

    <!-- Header -->
    <header class="fixed top-0 w-full z-50 glass">
        <div class="container mx-auto px-4 h-16 flex items-center justify-between">
            <a href="{home_link}" class="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary">Digital Ad Expert</a>
            <a href="{blog_home}" class="text-sm text-gray-400 hover:text-white transition">← Blog</a>
        </div>
    </header>

    <!-- Content -->
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

            <!-- CTA -->
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

    # --- ARTICLE 1: Nakliyat (TR) ---
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
    
    with open(f'{blog_dir}/nakliyat-musteri-rehberi.html', 'w', encoding='utf-8') as f:
        f.write(template.format(
            lang='tr',
            title='Almanya Nakliyat Firmaları İçin Müşteri Bulma Rehberi | Digital Ad Expert',
            desc='Almanya\'daki Türk nakliyatçılar için Google Ads ve SEO taktikleri. Müşteri bulmanın püf noktaları.',
            home_link='/tr/',
            blog_home='/blog/',
            category='Sektörel Rehber',
            headline='Almanya\'da Nakliyat Firmaları İçin Müşteri Bulma Rehberi 2025',
            date='27.01.2025',
            read_time='4 dk okuma',
            content=content_nakliyat,
            cta_title='İşlerinizi Büyütmek İster misiniz?',
            cta_desc='Nakliyat sektörüne özel reklam stratejimizle tanışın.',
            cta_link='/tr/nakliyat_google_ads.html',
            cta_btn='Nakliyat Paketini İncele'
        ))

    # --- ARTICLE 2: Ads Kosten (DE) ---
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
    
    with open(f'{blog_dir}/google-ads-kosten-2025.html', 'w', encoding='utf-8') as f:
        f.write(template.format(
            lang='de',
            title='Google Ads Kosten 2025: Was kostet ein Neukunde? | Digital Ad Expert',
            desc='Aktuelle Klickpreise (CPC) in Deutschland. Wie Sie Ihr Budget effizient einsetzen.',
            home_link='/de/',
            blog_home='/blog/',
            category='Google Ads',
            headline='Google Ads Kosten 2025: Was kostet ein Neukunde wirklich?',
            date='27.01.2025',
            read_time='3 Min. Lesezeit',
            content=content_ads,
            cta_title='Wollen Sie Ihr Budget optimieren?',
            cta_desc='Lassen Sie uns Ihre Kampagnen profitabel machen.',
            cta_link='/de/index.html#contact',
            cta_btn='Kostenlose Analyse'
        ))

    # --- ARTICLE 3: Insaat (TR) ---
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
    
    with open(f'{blog_dir}/insaat-sirketleri-pazarlama.html', 'w', encoding='utf-8') as f:
        f.write(template.format(
            lang='tr',
            title='Alman Pazarında Türk İnşaat Şirketleri Nasıl Markalaşır? | Digital Ad Expert',
            desc='İnşaat ve tadilat firmaları için Almanya\'da büyüme rehberi. Google Ads ile büyük proje bulma.',
            home_link='/tr/',
            blog_home='/blog/',
            category='İnşaat & Handwerk',
            headline='Alman Pazarında Türk İnşaat Şirketleri Nasıl Markalaşır?',
            date='27.01.2025',
            read_time='5 dk okuma',
            content=content_insaat,
            cta_title='Büyük Projeler Arıyor musunuz?',
            cta_desc='İnşaat sektörüne özel pazarlama paketimizi inceleyin.',
            cta_link='/tr/tadilat_google_ads.html',
            cta_btn='Paketi İncele'
        ))

    # --- BLOG INDEX PAGE ---
    index_content = """<!DOCTYPE html>
<html lang="tr" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog & Kaynaklar | Digital Ad Expert</title>
    <meta name="description" content="Dijital pazarlama, SEO ve Google Ads hakkında güncel bilgiler, rehberler ve ipuçları.">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        primary: '#06b6d4',
                        secondary: '#8b5cf6',
                        accent: '#10b981',
                        dark: { 900: '#0a0a0f', 800: '#12121a' }
                    }
                }
            }
        }
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background: #0a0a0f; color: #e2e8f0; }
        h1, h2, h3 { font-family: 'Space Grotesk', sans-serif; }
        .gradient-bg { background: linear-gradient(-45deg, #0a0a0f, #1a1a2e, #16213e, #0f3460); background-size: 400% 400%; animation: gradient 15s ease infinite; }
        @keyframes gradient { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
        .glass { background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); }
        .card-hover:hover { transform: translateY(-5px); border-color: rgba(6, 182, 212, 0.5); }
    </style>
</head>
<body class="gradient-bg min-h-screen flex flex-col">

    <!-- Header -->
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

    <!-- Main -->
    <main class="flex-grow pt-32 pb-20 px-4">
        <div class="container mx-auto max-w-6xl">
            <div class="text-center mb-16">
                <h1 class="text-4xl md:text-6xl font-bold mb-4 text-white">Blog & Bilgi Merkezi</h1>
                <p class="text-xl text-gray-400">Dijital büyüme için stratejiler ve rehberler.</p>
            </div>

            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                
                <!-- Post 1 -->
                <a href="/blog/nakliyat-musteri-rehberi.html" class="glass rounded-3xl p-6 transition-all duration-300 card-hover group block">
                    <div class="flex justify-between items-start mb-4">
                        <span class="bg-primary/20 text-primary px-3 py-1 rounded-full text-xs font-bold">TR / Sektörel</span>
                        <span class="text-gray-500 text-xs">27.01.2025</span>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-3 group-hover:text-primary transition">Almanya'da Nakliyat Firmaları İçin Müşteri Bulma Rehberi</h3>
                    <p class="text-sm text-gray-400">Negatif kelimeler, güven inşası ve yerel SEO ile nakliyat işinizi nasıl büyütürsünüz?</p>
                </a>

                <!-- Post 2 -->
                <a href="/blog/google-ads-kosten-2025.html" class="glass rounded-3xl p-6 transition-all duration-300 card-hover group block">
                    <div class="flex justify-between items-start mb-4">
                        <span class="bg-secondary/20 text-secondary px-3 py-1 rounded-full text-xs font-bold">DE / Ads</span>
                        <span class="text-gray-500 text-xs">27.01.2025</span>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-3 group-hover:text-secondary transition">Google Ads Kosten 2025: Was kostet ein Neukunde?</h3>
                    <p class="text-sm text-gray-400">Aktuelle Klickpreise (CPC) in Deutschland und Tipps zur Budgetoptimierung.</p>
                </a>

                <!-- Post 3 -->
                <a href="/blog/insaat-sirketleri-pazarlama.html" class="glass rounded-3xl p-6 transition-all duration-300 card-hover group block">
                    <div class="flex justify-between items-start mb-4">
                        <span class="bg-accent/20 text-accent px-3 py-1 rounded-full text-xs font-bold">TR / İnşaat</span>
                        <span class="text-gray-500 text-xs">27.01.2025</span>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-3 group-hover:text-accent transition">Türk İnşaat Şirketleri İçin Markalaşma Rehberi</h3>
                    <p class="text-sm text-gray-400">Büyük projeler ve tadilat işleri almak için dijital stratejiler.</p>
                </a>

            </div>
        </div>
    </main>

    <footer class="py-8 text-center text-gray-500 border-t border-white/10">
        <p>© 2025 Digital Ad Expert</p>
    </footer>
</body>
</html>"""

    with open(f'{blog_dir}/index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)

    print("Blog pages created successfully.")

create_blog_structure()
