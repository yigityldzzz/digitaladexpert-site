
import os

def fix_localization():
    root = 'site_update/digitaladexpert-cloudflare'
    
    # --- 1. UNIVERSAL 404 PAGE ---
    # Smart 404 that speaks all languages
    universal_404 = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found | Digital Ad Expert</title>
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
    <div class="glass p-12 rounded-3xl text-center max-w-3xl relative overflow-hidden">
        <div class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-primary to-secondary"></div>
        
        <h1 class="text-9xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-primary to-secondary mb-8 neon-text">404</h1>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-center mb-8 divide-y md:divide-y-0 md:divide-x divide-white/10">
            <div class="px-2">
                <h3 class="text-xl font-bold text-white mb-2">Seite nicht gefunden</h3>
                <p class="text-sm text-gray-400">Der gesuchte Link existiert nicht.</p>
                <a href="/de/" class="mt-4 inline-block text-primary hover:text-white transition">Zur Startseite →</a>
            </div>
            <div class="px-2 pt-4 md:pt-0">
                <h3 class="text-xl font-bold text-white mb-2">Page Not Found</h3>
                <p class="text-sm text-gray-400">The link you followed is broken.</p>
                <a href="/en/" class="mt-4 inline-block text-primary hover:text-white transition">Go Home →</a>
            </div>
            <div class="px-2 pt-4 md:pt-0">
                <h3 class="text-xl font-bold text-white mb-2">Sayfa Bulunamadı</h3>
                <p class="text-sm text-gray-400">Aradığınız sayfa mevcut değil.</p>
                <a href="/tr/" class="mt-4 inline-block text-primary hover:text-white transition">Ana Sayfaya Dön →</a>
            </div>
        </div>
        
        <p class="text-xs text-gray-600 mt-8">Error Code: 404_NOT_FOUND</p>
    </div>
</body>
</html>"""

    with open('site_update/digitaladexpert-cloudflare/404.html', 'w', encoding='utf-8') as f:
        f.write(universal_404)
    print("Fixed 404 page (Universal).")


    # --- 2. LOCALIZED TECH MARQUEE ---
    
    # We need to replace the PREVIOUS marquee injection with the localized one.
    # Since we can't easily "undo", we will read the file, remove the old marquee block (by identifying it), and insert the correct one.
    # Or simpler: Re-read the file, replace the marquee section entirely.
    
    marquee_data = {
        'tr': {
            'title': 'TEKNOLOJİ GÜCÜ',
            'meta': 'Meta Reklamlar',
            'openai': 'Yapay Zeka'
        },
        'de': {
            'title': 'TECHNOLOGIE STACK',
            'meta': 'Meta Ads',
            'openai': 'Künstliche Intelligenz'
        },
        'en': {
            'title': 'POWERED BY TECH',
            'meta': 'Meta Ads',
            'openai': 'Artificial Intelligence'
        }
    }

    for lang in ['tr', 'de', 'en']:
        file_path = os.path.join(root, lang, 'index.html')
        if not os.path.exists(file_path): continue
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Identify the old marquee block to replace
        # It starts with <!-- TECH STACK MARQUEE --> and ends with </style> (approx)
        # But regex replacement on large blocks is risky.
        
        # Better strategy: Construct the NEW marquee HTML for this lang
        data = marquee_data[lang]
        
        new_marquee = f"""
    <!-- TECH STACK MARQUEE -->
    <div class="py-10 bg-black/20 border-y border-white/5 overflow-hidden">
        <div class="container mx-auto px-4 mb-4 text-center">
            <span class="text-xs font-bold text-gray-500 uppercase tracking-widest">{data['title']}</span>
        </div>
        <div class="marquee relative flex overflow-x-hidden">
            <div class="animate-marquee whitespace-nowrap flex gap-12 items-center">
                <!-- Logos -->
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-blue-500">G</span>oogle Ads</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-orange-500">A</span>nalytics 4</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-blue-400">∞</span> {data['meta']}</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-orange-400">☁</span> Cloudflare</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-green-500">⚡</span> OpenAI</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-purple-500">🔍</span> Semrush</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-red-500">H</span>TML5</span>
                
                <!-- Duplicate -->
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2 ml-12"><span class="text-blue-500">G</span>oogle Ads</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-orange-500">A</span>nalytics 4</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-blue-400">∞</span> {data['meta']}</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-orange-400">☁</span> Cloudflare</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-green-500">⚡</span> OpenAI</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-purple-500">🔍</span> Semrush</span>
                <span class="text-2xl font-bold text-gray-600 flex items-center gap-2"><span class="text-red-500">H</span>TML5</span>
            </div>
        </div>
    </div>
    <style>
        .animate-marquee {{ animation: marquee 20s linear infinite; }}
        @keyframes marquee {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-50%); }} }}
    </style>
    """
        
        # We need to find the OLD marquee and replace it.
        # The old one had 'Powered By Tech' title hardcoded.
        # Let's search for the start tag and try to replace until the style tag.
        
        # Finding the block boundaries
        start_marker = '<!-- TECH STACK MARQUEE -->'
        end_marker = '</style>'
        
        if start_marker in content:
            # We have an existing marquee to replace
            # We need to find the specific block. Since there's only one, we can split.
            parts = content.split(start_marker)
            if len(parts) > 1:
                # parts[0] is everything before
                # parts[1] is marquee + everything after
                
                after_part = parts[1].split(end_marker, 1)
                if len(after_part) > 1:
                    # after_part[1] is everything after the style tag
                    
                    new_content = parts[0] + new_marquee + after_part[1]
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Localized Marquee in {file_path}")
        else:
            print(f"Warning: Could not find marquee to replace in {file_path}")

fix_localization()
