
import os

# --- 1. GENERATE 404 PAGE ---
def create_404():
    html = """<!DOCTYPE html>
<html lang="de" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Seite nicht gefunden | Digital Ad Expert</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: { primary: '#06b6d4', secondary: '#8b5cf6', accent: '#10b981', dark: { 900: '#0a0a0f', 800: '#12121a' } }
                }
            }
        }
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background: #0a0a0f; color: #e2e8f0; }
        h1 { font-family: 'Space Grotesk', sans-serif; }
        .glass { background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); }
        .neon-text { text-shadow: 0 0 20px rgba(6, 182, 212, 0.5); }
    </style>
</head>
<body class="min-h-screen flex items-center justify-center p-4 bg-[url('https://digitaladexpert.de/assets/grid.svg')] bg-cover">
    <div class="glass p-12 rounded-3xl text-center max-w-2xl relative overflow-hidden">
        <div class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-primary to-secondary"></div>
        
        <h1 class="text-9xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-primary to-secondary mb-4 neon-text">404</h1>
        <h2 class="text-2xl md:text-3xl font-bold text-white mb-6">Ups! Kaybolmuş gibisin.</h2>
        <p class="text-gray-400 text-lg mb-8">
            Ama merak etme, biz <strong>Google Ads</strong> ile müşterilerinin seni asla kaybetmemesini sağlıyoruz.
            Senin yerin burası değil, zirve.
        </p>
        
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <a href="/" class="px-8 py-3 bg-white text-black rounded-xl font-bold hover:bg-gray-200 transition">Ana Sayfaya Dön</a>
            <a href="/tr/nasil-calisiyoruz.html" class="px-8 py-3 border border-white/20 rounded-xl font-bold hover:bg-white/10 transition">Sürecimizi İncele</a>
        </div>
    </div>
</body>
</html>"""
    
    with open('site_update/digitaladexpert-cloudflare/404.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("404 Page created.")

# --- 2. GENERATE ROI CALCULATOR PAGES ---
def create_roi_pages():
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
                    colors: {{ primary: '#06b6d4', secondary: '#8b5cf6', accent: '#10b981', dark: {{ 900: '#0a0a0f', 800: '#12121a' }} }}
                }}
            }}
        }}
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Inter', sans-serif; background: #0a0a0f; color: #e2e8f0; }}
        h1, h2 {{ font-family: 'Space Grotesk', sans-serif; }}
        .gradient-bg {{ background: linear-gradient(-45deg, #0a0a0f, #1a1a2e, #16213e, #0f3460); background-size: 400% 400%; animation: gradient 15s ease infinite; }}
        @keyframes gradient {{ 0% {{ background-position: 0% 50%; }} 50% {{ background-position: 100% 50%; }} 100% {{ background-position: 0% 50%; }} }}
        .glass {{ background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); }}
        input[type="range"] {{ -webkit-appearance: none; background: rgba(255,255,255,0.1); border-radius: 10px; height: 8px; }}
        input[type="range"]::-webkit-slider-thumb {{ -webkit-appearance: none; width: 24px; height: 24px; background: #06b6d4; border-radius: 50%; cursor: pointer; }}
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

    <main class="flex-grow pt-32 pb-20 px-4">
        <div class="container mx-auto max-w-4xl">
            <div class="text-center mb-12">
                <h1 class="text-4xl md:text-5xl font-bold text-white mb-4">{headline}</h1>
                <p class="text-gray-400">{subhead}</p>
            </div>

            <div class="grid md:grid-cols-2 gap-8">
                <!-- Calculator Inputs -->
                <div class="glass p-8 rounded-3xl">
                    <h2 class="text-2xl font-bold text-white mb-6">{inputs_title}</h2>
                    
                    <div class="space-y-6">
                        <div>
                            <label class="block text-sm text-gray-400 mb-2">{label_budget} (€)</label>
                            <input type="number" id="budget" value="1000" class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-primary text-xl font-bold" oninput="calculate()">
                        </div>
                        
                        <div>
                            <label class="block text-sm text-gray-400 mb-2">{label_cpc} (€)</label>
                            <input type="range" id="cpc" min="0.5" max="10" step="0.1" value="1.5" class="w-full mb-2" oninput="calculate()">
                            <div class="text-right text-primary font-bold" id="cpc-display">1.50 €</div>
                        </div>

                        <div>
                            <label class="block text-sm text-gray-400 mb-2">{label_conv} (%)</label>
                            <input type="range" id="conv" min="1" max="20" step="0.5" value="5" class="w-full mb-2" oninput="calculate()">
                            <div class="text-right text-secondary font-bold" id="conv-display">5 %</div>
                        </div>
                        
                        <div>
                            <label class="block text-sm text-gray-400 mb-2">{label_value} (€)</label>
                            <input type="number" id="value" value="500" class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-primary text-xl font-bold" oninput="calculate()">
                        </div>
                    </div>
                </div>

                <!-- Results -->
                <div class="glass p-8 rounded-3xl bg-gradient-to-br from-white/5 to-primary/10 border-primary/30 flex flex-col justify-center">
                    <h2 class="text-2xl font-bold text-white mb-8 text-center">{results_title}</h2>
                    
                    <div class="space-y-8">
                        <div class="text-center">
                            <div class="text-gray-400 text-sm mb-1">{res_traffic}</div>
                            <div class="text-4xl font-bold text-white" id="res-clicks">0</div>
                        </div>
                        
                        <div class="text-center">
                            <div class="text-gray-400 text-sm mb-1">{res_leads}</div>
                            <div class="text-5xl font-bold text-accent" id="res-leads">0</div>
                        </div>
                        
                        <div class="text-center">
                            <div class="text-gray-400 text-sm mb-1">{res_revenue}</div>
                            <div class="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-primary to-secondary" id="res-eur">0 €</div>
                        </div>
                    </div>

                    <div class="mt-8 pt-8 border-t border-white/10 text-center">
                        <p class="text-xs text-gray-500 mb-4">{disclaimer}</p>
                        <a href="{home_link}#contact" class="block w-full py-4 rounded-xl bg-white text-black font-bold hover:scale-105 transition-transform">{cta_btn}</a>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <script>
        function calculate() {{
            const budget = parseFloat(document.getElementById('budget').value) || 0;
            const cpc = parseFloat(document.getElementById('cpc').value) || 0;
            const conv = parseFloat(document.getElementById('conv').value) || 0;
            const value = parseFloat(document.getElementById('value').value) || 0;

            document.getElementById('cpc-display').innerText = cpc.toFixed(2) + ' €';
            document.getElementById('conv-display').innerText = conv.toFixed(1) + ' %';

            const clicks = Math.floor(budget / cpc);
            const leads = Math.floor(clicks * (conv / 100));
            const revenue = leads * value;

            document.getElementById('res-clicks').innerText = clicks;
            document.getElementById('res-leads').innerText = leads;
            document.getElementById('res-eur').innerText = revenue.toLocaleString() + ' €';
        }}
        calculate(); // Init
    </script>
</body>
</html>"""

    # TR
    with open('site_update/digitaladexpert-cloudflare/tr/roi-hesaplama.html', 'w', encoding='utf-8') as f:
        f.write(template.format(
            lang='tr', title='Google Ads Getiri Hesaplayıcı | Digital Ad Expert', desc='Reklam bütçenizle ne kadar kazanabilirsiniz? Hesaplayın.',
            home_link='/tr/', back_text='Ana Sayfa', headline='Yatırım Getirisi (ROI) Hesaplayıcı', subhead='Bütçenizin potansiyelini görün. Rakamlarla konuşalım.',
            inputs_title='Verilerinizi Girin', label_budget='Aylık Bütçe', label_cpc='Ort. Tıklama Başı Maliyet', label_conv='Dönüşüm Oranı', label_value='Müşteri Başına Kazanç',
            results_title='Tahmini Sonuçlar', res_traffic='Web Sitesi Ziyaretçisi', res_leads='Yeni Potansiyel Müşteri', res_revenue='Tahmini Ciro',
            disclaimer='Bu rakamlar tahmindir. Gerçek sonuçlar sektöre göre değişebilir.', cta_btn='Bu Sonuçlara Ulaşın'
        ))
    
    # DE
    with open('site_update/digitaladexpert-cloudflare/de/roi-rechner.html', 'w', encoding='utf-8') as f:
        f.write(template.format(
            lang='de', title='Google Ads ROI Rechner | Digital Ad Expert', desc='Berechnen Sie Ihren potenziellen Gewinn mit Google Ads.',
            home_link='/de/', back_text='Startseite', headline='Google Ads ROI Rechner', subhead='Sehen Sie das Potenzial Ihres Budgets.',
            inputs_title='Ihre Daten', label_budget='Monatliches Budget', label_cpc='Ø Klickpreis (CPC)', label_conv='Conversion Rate', label_value='Kundenwert',
            results_title='Geschätzte Ergebnisse', res_traffic='Webseiten-Besucher', res_leads='Neue Anfragen (Leads)', res_revenue='Geschätzter Umsatz',
            disclaimer='Diese Zahlen sind Schätzungen. Ergebnisse variieren je nach Branche.', cta_btn='Kampagne Starten'
        ))

    # EN
    with open('site_update/digitaladexpert-cloudflare/en/roi-calculator.html', 'w', encoding='utf-8') as f:
        f.write(template.format(
            lang='en', title='Google Ads ROI Calculator | Digital Ad Expert', desc='Calculate your potential return on investment.',
            home_link='/en/', back_text='Home', headline='ROI Calculator', subhead='See the potential of your budget.',
            inputs_title='Input Data', label_budget='Monthly Budget', label_cpc='Avg. CPC', label_conv='Conversion Rate', label_value='Value per Customer',
            results_title='Estimated Results', res_traffic='Website Visitors', res_leads='New Leads', res_revenue='Estimated Revenue',
            disclaimer='Figures are estimates. Actual results vary by industry.', cta_btn='Get These Results'
        ))
    
    print("ROI Pages created.")

# --- 3. INJECT TECH MARQUEE ---
def inject_tech_marquee():
    marquee_html = """
    <!-- TECH STACK MARQUEE -->
    <div class="py-10 bg-black/20 border-y border-white/5 overflow-hidden">
        <div class="container mx-auto px-4 mb-4 text-center">
            <span class="text-xs font-bold text-gray-500 uppercase tracking-widest">Powered By Tech</span>
        </div>
        <div class="marquee relative flex overflow-x-hidden">
            <div class="animate-marquee whitespace-nowrap flex gap-12 items-center">
                <!-- Logos (Text/Icon based to avoid images) -->
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-blue-500">G</span>oogle Ads</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-orange-500">A</span>nalytics 4</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-blue-400">∞</span> Meta Ads</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-orange-400">☁</span> Cloudflare</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-green-500">⚡</span> OpenAI</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-purple-500">🔍</span> Semrush</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-red-500">H</span>TML5</span>
                
                <!-- Duplicate for infinite loop -->
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2 ml-12"><span class="text-blue-500">G</span>oogle Ads</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-orange-500">A</span>nalytics 4</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-blue-400">∞</span> Meta Ads</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-orange-400">☁</span> Cloudflare</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-green-500">⚡</span> OpenAI</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-purple-500">🔍</span> Semrush</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-red-500">H</span>TML5</span>
            </div>
        </div>
    </div>
    <style>
        .animate-marquee { animation: marquee 20s linear infinite; }
        @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
    </style>
    """
    
    root = 'site_update/digitaladexpert-cloudflare'
    for lang in ['tr', 'de', 'en']:
        index_path = os.path.join(root, lang, 'index.html')
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Insert before Footer
            if '<footer' in content and 'Powered By Tech' not in content:
                content = content.replace('<footer', f'{marquee_html}\n<footer')
                with open(index_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Marquee added to {index_path}")

# --- 4. ADD LINKS TO FOOTER ---
def add_tools_to_footer():
    root = 'site_update/digitaladexpert-cloudflare'
    links = {
        'tr': {'text': 'Hesaplayıcı', 'href': '/tr/roi-hesaplama.html'},
        'de': {'text': 'ROI Rechner', 'href': '/de/roi-rechner.html'},
        'en': {'text': 'Calculator', 'href': '/en/roi-calculator.html'}
    }
    
    for lang in ['tr', 'de', 'en']:
        index_path = os.path.join(root, lang, 'index.html')
        data = links[lang]
        link_html = f'<li><a href="{data["href"]}" class="text-gray-400 hover:text-primary transition-colors text-sm sm:text-base">{data["text"]}</a></li>'
        
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Insert into the "Legal" or similar list in footer
            # Look for Privacy Policy link to insert after
            privacy_link_part = 'datenschutz.html"'
            if privacy_link_part in content and data['href'] not in content:
                # Find the closing </a></li> of privacy link and append new li
                # Regex or string find is hard because of variations.
                # Let's target the UL closing tag of the Legal section if possible.
                
                # Simpler: Just find datenschutz.html link and replace the closing </li> with </li>\n{link_html}
                # We need to find the full line approx
                
                # Let's search for the Privacy Policy href
                if f'/{lang}/datenschutz.html' in content:
                    # Rough replace
                    content = content.replace(f'/{lang}/datenschutz.html" class="text-gray-400 hover:text-primary transition-colors text-sm sm:text-base">', f'/{lang}/datenschutz.html" class="text-gray-400 hover:text-primary transition-colors text-sm sm:text-base">')
                    # This doesn't help inserting AFTER.
                    
                    # Let's assume the structure <li><a ... datenschutz.html ...>...</a></li>
                    # We will append to the end of the list.
                    # Find </ul> inside the "Legal" column.
                    
                    # Let's just create a new small section or append to the Legal list which is safer manually if structure is known.
                    # Structure: <ul class="space-y-2 sm:space-y-3">...datenschutz...</ul>
                    
                    # Let's try to replace "Gizlilik Politikası</a></li>" with "Gizlilik Politikası</a></li>" + link_html
                    # But text differs by lang.
                    
                    closing_tag = '</a></li>'
                    # We iterate to find the one with datenschutz
                    lines = content.split('\n')
                    new_lines = []
                    for line in lines:
                        new_lines.append(line)
                        if f'/{lang}/datenschutz.html' in line and closing_tag in line:
                            new_lines.append(link_html)
                    
                    content = '\n'.join(new_lines)
                    
                    with open(index_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Footer link added to {index_path}")

create_404()
create_roi_pages()
inject_tech_marquee()
add_tools_to_footer()
