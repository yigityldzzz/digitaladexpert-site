
import os

def create_assets_and_logo():
    assets_dir = 'site_update/digitaladexpert-cloudflare/assets'
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)
        
    # Create a Modern SVG Logo (Hexagon shape with DAE initials)
    # Using Teal/Purple gradient colors from the theme
    logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#06b6d4;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#8b5cf6;stop-opacity:1" />
    </linearGradient>
  </defs>
  <path d="M250 50 L450 150 L450 350 L250 450 L50 350 L50 150 Z" fill="url(#grad1)" stroke="none"/>
  <text x="50%" y="55%" dominant-baseline="middle" text-anchor="middle" font-family="Arial, sans-serif" font-weight="bold" font-size="200" fill="white">D</text>
</svg>"""

    with open(f'{assets_dir}/logo.svg', 'w', encoding='utf-8') as f:
        f.write(logo_svg)
        
    # Also create a favicon.ico (using the same svg as source concept, but browsers handle svg favicons now)
    # We will just use the svg as favicon in the HTML
    print("Logo created in assets/logo.svg")

def apply_final_touches(root_dir):
    langs = ['tr', 'de', 'en']
    
    # Text for Floating Button per language
    btn_text = {
        'tr': 'Hızlı Teklif Al',
        'de': 'Angebot Anfordern',
        'en': 'Get Quote'
    }
    
    # Hreflang Tags Block
    hreflang_block = """
    <link rel="alternate" hreflang="de" href="https://digitaladexpert.de/de/" />
    <link rel="alternate" hreflang="tr" href="https://digitaladexpert.de/tr/" />
    <link rel="alternate" hreflang="en" href="https://digitaladexpert.de/en/" />
    <link rel="alternate" hreflang="x-default" href="https://digitaladexpert.de/" />
    """
    
    # Floating Button HTML
    # Fixed bottom-right, glass effect, pulse animation
    def get_fab_html(text):
        return f"""
    <!-- Floating Action Button -->
    <a href="#contact" class="fixed bottom-6 right-6 z-50 glass bg-gradient-to-r from-primary to-secondary px-6 py-4 rounded-full text-white font-bold shadow-lg hover:scale-105 transition-transform animate-bounce-slow flex items-center gap-2 group">
        <span>✉️</span>
        <span class="group-hover:inline-block transition-all">{text}</span>
    </a>
    <style>
        @keyframes bounce-slow {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-5px); }}
        }}
        .animate-bounce-slow {{ animation: bounce-slow 3s infinite; }}
    </style>
    """

    # Favicon HTML
    favicon_html = '<link rel="icon" type="image/svg+xml" href="/assets/logo.svg">'

    # Walk through all HTML files
    for lang in langs:
        lang_dir = os.path.join(root_dir, lang)
        if not os.path.exists(lang_dir): continue
        
        for filename in os.listdir(lang_dir):
            if filename.endswith(".html"):
                filepath = os.path.join(lang_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 1. Inject Favicon & Hreflang (Head)
                if '</head>' in content:
                    # Check if already exists to avoid dupes
                    if 'href="/assets/logo.svg"' not in content:
                        content = content.replace('</head>', f'{favicon_html}\n{hreflang_block}\n</head>')
                
                # 2. Inject Floating Button (Body end)
                if '</body>' in content:
                    # Don't add if already there
                    if 'Floating Action Button' not in content:
                        fab = get_fab_html(btn_text[lang])
                        content = content.replace('</body>', f'{fab}\n</body>')
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {filepath}")

# Execute
create_assets_and_logo()
root = 'site_update/digitaladexpert-cloudflare'
apply_final_touches(root)
