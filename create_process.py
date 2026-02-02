
import os

# Create Process Page Content
def create_process_pages():
    
    # Common Template (Glassmorphism Style)
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
                    }}
                }}
            }}
        }}
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <style>
        body {{ font-family: 'Inter', sans-serif; background: #0a0a0f; color: #e2e8f0; }}
        h1, h2, h3 {{ font-family: 'Space Grotesk', sans-serif; }}
        .gradient-bg {{ background: linear-gradient(-45deg, #0a0a0f, #1a1a2e, #16213e, #0f3460); background-size: 400% 400%; animation: gradient 15s ease infinite; }}
        @keyframes gradient {{ 0% {{ background-position: 0% 50%; }} 50% {{ background-position: 100% 50%; }} 100% {{ background-position: 0% 50%; }} }}
        .glass {{ background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); }}
        .step-card:hover {{ transform: translateY(-5px); border-color: rgba(6, 182, 212, 0.5); }}
        .step-number {{ -webkit-text-stroke: 1px rgba(255,255,255,0.1); color: transparent; }}
    </style>
</head>
<body class="gradient-bg min-h-screen flex flex-col">

    <!-- Header -->
    <header class="fixed top-0 w-full z-50 glass">
        <div class="container mx-auto px-4 h-16 flex items-center justify-between">
            <a href="{home_link}" class="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary">Digital Ad Expert</a>
            <a href="{home_link}" class="text-sm text-gray-400 hover:text-white transition">← {back_text}</a>
        </div>
    </header>

    <!-- Main Content -->
    <main class="flex-grow pt-32 pb-20 px-4">
        <div class="container mx-auto max-w-5xl">
            <div class="text-center mb-16" data-aos="fade-up">
                <span class="text-primary text-sm font-bold tracking-wider uppercase mb-2 block">{sub_title}</span>
                <h1 class="text-4xl md:text-6xl font-bold mb-6 text-white">{main_title}</h1>
                <p class="text-xl text-gray-400 max-w-2xl mx-auto">{hero_text}</p>
            </div>

            <!-- Steps Grid -->
            <div class="grid md:grid-cols-2 gap-8 relative">
                <!-- Connecting Line (Desktop) -->
                <div class="hidden md:block absolute left-1/2 top-0 bottom-0 w-1 bg-gradient-to-b from-primary via-secondary to-transparent -translate-x-1/2 opacity-20"></div>

                <!-- Step 1 -->
                <div class="step-card glass p-8 rounded-3xl relative transition-all duration-300" data-aos="fade-right">
                    <span class="absolute -top-6 -left-4 text-8xl font-bold step-number opacity-50">01</span>
                    <div class="relative z-10">
                        <div class="w-12 h-12 bg-primary/20 rounded-xl flex items-center justify-center text-2xl mb-4">🔍</div>
                        <h3 class="text-2xl font-bold text-white mb-3">{step1_title}</h3>
                        <p class="text-gray-400 leading-relaxed">{step1_desc}</p>
                    </div>
                </div>
                <div class="md:block hidden"></div> <!-- Spacer -->

                <!-- Step 2 -->
                <div class="md:block hidden"></div> <!-- Spacer -->
                <div class="step-card glass p-8 rounded-3xl relative transition-all duration-300" data-aos="fade-left">
                    <span class="absolute -top-6 -right-4 text-8xl font-bold step-number opacity-50">02</span>
                    <div class="relative z-10">
                        <div class="w-12 h-12 bg-secondary/20 rounded-xl flex items-center justify-center text-2xl mb-4">🎯</div>
                        <h3 class="text-2xl font-bold text-white mb-3">{step2_title}</h3>
                        <p class="text-gray-400 leading-relaxed">{step2_desc}</p>
                    </div>
                </div>

                <!-- Step 3 -->
                <div class="step-card glass p-8 rounded-3xl relative transition-all duration-300" data-aos="fade-right">
                    <span class="absolute -top-6 -left-4 text-8xl font-bold step-number opacity-50">03</span>
                    <div class="relative z-10">
                        <div class="w-12 h-12 bg-accent/20 rounded-xl flex items-center justify-center text-2xl mb-4">🚀</div>
                        <h3 class="text-2xl font-bold text-white mb-3">{step3_title}</h3>
                        <p class="text-gray-400 leading-relaxed">{step3_desc}</p>
                    </div>
                </div>
                <div class="md:block hidden"></div> <!-- Spacer -->

                <!-- Step 4 -->
                <div class="md:block hidden"></div> <!-- Spacer -->
                <div class="step-card glass p-8 rounded-3xl relative transition-all duration-300" data-aos="fade-left">
                    <span class="absolute -top-6 -right-4 text-8xl font-bold step-number opacity-50">04</span>
                    <div class="relative z-10">
                        <div class="w-12 h-12 bg-blue-500/20 rounded-xl flex items-center justify-center text-2xl mb-4">📈</div>
                        <h3 class="text-2xl font-bold text-white mb-3">{step4_title}</h3>
                        <p class="text-gray-400 leading-relaxed">{step4_desc}</p>
                    </div>
                </div>
            </div>

            <!-- CTA -->
            <div class="mt-20 text-center" data-aos="fade-up">
                <a href="{home_link}#contact" class="inline-block bg-gradient-to-r from-primary to-secondary px-8 py-4 rounded-xl text-lg font-bold text-white hover:shadow-lg hover:shadow-primary/25 transition-all transform hover:-translate-y-1">
                    {cta_text}
                </a>
            </div>
        </div>
    </main>

    <footer class="py-8 text-center text-gray-500 border-t border-white/10">
        <p>{footer_text}</p>
    </footer>

    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>AOS.init({{duration: 800, once: true}});</script>
</body>
</html>"""

    # 1. TÜRKÇE (TR)
    with open('site_update/digitaladexpert-cloudflare/tr/nasil-calisiyoruz.html', 'w', encoding='utf-8') as f:
        f.write(template.format(
            lang='tr',
            title='Nasıl Çalışıyoruz? | Digital Ad Expert',
            desc='Adım adım dijital pazarlama sürecimiz. Analiz, strateji, kurulum ve optimizasyon ile başarıya giden yol.',
            home_link='/tr/',
            back_text='Ana Sayfa',
            sub_title='BAŞARIYA GİDEN YOL',
            main_title='Çalışma Sürecimiz',
            hero_text='Sürprizlere yer yok. Başarısı kanıtlanmış 4 adımlı "Sniper" metodolojimizle işletmenizi büyütüyoruz.',
            step1_title='Analiz & Keşif',
            step1_desc='Önce sizi dinliyoruz. Rakipleriniz ne yapıyor? Sizin farkınız ne? Hangi anahtar kelimelerde fırsat var? Detaylı bir pazar röntgeni çekiyoruz.',
            step2_title='Strateji Kurgusu',
            step2_desc='Bütçenizi en verimli nasıl kullanırız? "Sniper" hedefleme ile sadece gerçek müşterilere odaklanan, negatif kelimelerin elendiği bir plan hazırlıyoruz.',
            step3_title='Kurulum & Yayına Alma',
            step3_desc='Profesyonel reklam metinleri, göz alıcı görseller ve dönüşüm odaklı landing page\'ler. Her şeyi sizin için kuruyor ve "Başlat" düğmesine basıyoruz.',
            step4_title='Optimizasyon & Rapor',
            step4_desc='Reklamı açıp bırakmıyoruz. Her gün verileri izliyor, tıklama maliyetlerini düşürüyor ve size "Bu ay şu kadar kazandırdık" diye şeffaf rapor sunuyoruz.',
            cta_text='Hemen Başlayalım',
            footer_text='© 2025 Digital Ad Expert'
        ))

    # 2. ALMANCA (DE)
    with open('site_update/digitaladexpert-cloudflare/de/prozess.html', 'w', encoding='utf-8') as f:
        f.write(template.format(
            lang='de',
            title='Unser Prozess | Digital Ad Expert',
            desc='Transparenter Marketing-Prozess. Analyse, Strategie und Optimierung für Ihren Erfolg.',
            home_link='/de/',
            back_text='Startseite',
            sub_title='DER WEG ZUM ERFOLG',
            main_title='Wie wir arbeiten',
            hero_text='Keine Überraschungen. Wir skalieren Ihr Geschäft mit unserer bewährten 4-Schritte-Methodik.',
            step1_title='Analyse & Audit',
            step1_desc='Wir analysieren Ihren Markt, Ihre Konkurrenz und Ihre Ziele. Wo liegen die ungenutzten Chancen? Wir erstellen ein detailliertes Markt-Röntgenbild.',
            step2_title='Strategie',
            step2_desc='Präzises Targeting statt Gießkannenprinzip. Wir entwickeln einen Plan, der Streuverluste minimiert und nur Ihre idealen Kunden anspricht.',
            step3_title='Setup & Launch',
            step3_desc='Professionelle Anzeigentexte, conversion-starke Landing Pages und technisches Tracking. Wir richten alles ein und starten die Kampagne.',
            step4_title='Optimierung',
            step4_desc='Wir lassen Ihre Anzeigen nicht allein. Tägliche Optimierung der Klickpreise (CPC) und Qualität. Monatliche, transparente Berichte für Sie.',
            cta_text='Projekt Starten',
            footer_text='© 2025 Digital Ad Expert'
        ))

    # 3. İNGİLİZCE (EN)
    with open('site_update/digitaladexpert-cloudflare/en/process.html', 'w', encoding='utf-8') as f:
        f.write(template.format(
            lang='en',
            title='Our Process | Digital Ad Expert',
            desc='Step-by-step digital marketing workflow. Analysis, strategy, and optimization for measurable growth.',
            home_link='/en/',
            back_text='Home',
            sub_title='PATH TO SUCCESS',
            main_title='How We Work',
            hero_text='No guesswork. We grow your business using our proven 4-step "Sniper" methodology.',
            step1_title='Analysis & Discovery',
            step1_desc='We dive deep into your market. What are competitors doing? Where are the gaps? We create a detailed roadmap before spending a cent.',
            step2_title='Strategy Design',
            step2_desc='Budget efficiency is key. We build a campaign structure that targets only high-intent users and filters out waste traffic.',
            step3_title='Setup & Launch',
            step3_desc='High-converting landing pages, compelling ad copy, and precise tracking setup. We handle everything and push the launch button.',
            step4_title='Optimization',
            step4_desc='We don\'t set and forget. Continuous monitoring to lower CPC and increase conversions. Transparent reporting every month.',
            cta_text='Start Now',
            footer_text='© 2025 Digital Ad Expert'
        ))

    print("Process pages created.")

create_process_pages()
