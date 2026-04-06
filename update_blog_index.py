import os

index_path = '/root/.openclaw/workspace/digitaladexpert-site/blog/index.html'

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_cards = """
        <!-- Generated SEO Articles -->
        <a href="google-ads-pmax-kampanyalari-2026.html" class="glass p-6 rounded-2xl hover:bg-white/5 transition-all group block">
            <div class="flex items-center gap-3 mb-4"><span class="px-3 py-1 text-xs font-semibold text-primary bg-primary/10 rounded-full">TR - Google Ads</span></div>
            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-primary transition-colors">Google Ads PMax Kampanyaları ile ROI Artırma (2026)</h3>
            <p class="text-gray-400 text-sm mb-4">2026 yılında Maksimum Performans (PMax) kampanyalarını optimize ederek reklam bütçenizi en iyi şekilde değerlendirin.</p>
        </a>

        <a href="pmax-kampagnen-roi-maximieren-2026.html" class="glass p-6 rounded-2xl hover:bg-white/5 transition-all group block">
            <div class="flex items-center gap-3 mb-4"><span class="px-3 py-1 text-xs font-semibold text-primary bg-primary/10 rounded-full">DE - Google Ads</span></div>
            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-primary transition-colors">Wie PMax-Kampagnen (Google Ads) Ihren ROI 2026 maximieren</h3>
            <p class="text-gray-400 text-sm mb-4">Optimieren Sie Performance Max (PMax) Kampagnen in 2026 für maximalen Return on Investment (ROI).</p>
        </a>

        <a href="yerel-seo-google-haritalar-2026.html" class="glass p-6 rounded-2xl hover:bg-white/5 transition-all group block">
            <div class="flex items-center gap-3 mb-4"><span class="px-3 py-1 text-xs font-semibold text-accent bg-accent/10 rounded-full">TR - SEO</span></div>
            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-accent transition-colors">Yerel İşletmeler İçin Yerel SEO ve Google Haritalar Stratejisi</h3>
            <p class="text-gray-400 text-sm mb-4">Kuaförler, restoranlar ve doktorlar için 2026 Yerel SEO taktikleri.</p>
        </a>

        <a href="local-seo-google-maps-ranking-2026.html" class="glass p-6 rounded-2xl hover:bg-white/5 transition-all group block">
            <div class="flex items-center gap-3 mb-4"><span class="px-3 py-1 text-xs font-semibold text-accent bg-accent/10 rounded-full">DE - SEO</span></div>
            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-accent transition-colors">Local SEO: So dominieren Sie Google Maps in 2026</h3>
            <p class="text-gray-400 text-sm mb-4">Local SEO Strategien für lokale Unternehmen, Restaurants und Dienstleister.</p>
        </a>

        <a href="yapay-zeka-ile-seo-icerik-uretimi-2026.html" class="glass p-6 rounded-2xl hover:bg-white/5 transition-all group block">
            <div class="flex items-center gap-3 mb-4"><span class="px-3 py-1 text-xs font-semibold text-secondary bg-secondary/10 rounded-full">TR - AI</span></div>
            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-secondary transition-colors">Yapay Zeka (AI) Destekli İçerik Üretimi ile SEO'da Öne Geçmek</h3>
            <p class="text-gray-400 text-sm mb-4">2026 yılında ChatGPT ve Gemini gibi AI araçlarını kullanarak Google uyumlu içerik nasıl üretilir?</p>
        </a>

        <a href="ki-content-erstellung-seo-2026.html" class="glass p-6 rounded-2xl hover:bg-white/5 transition-all group block">
            <div class="flex items-center gap-3 mb-4"><span class="px-3 py-1 text-xs font-semibold text-secondary bg-secondary/10 rounded-full">DE - AI</span></div>
            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-secondary transition-colors">KI-gesteuerte Content-Erstellung: Der SEO-Gamechanger</h3>
            <p class="text-gray-400 text-sm mb-4">Wie Sie ChatGPT und KI nutzen, um rankende SEO-Texte in 2026 zu erstellen.</p>
        </a>

        <a href="almanya-b2b-lead-generation-2026.html" class="glass p-6 rounded-2xl hover:bg-white/5 transition-all group block">
            <div class="flex items-center gap-3 mb-4"><span class="px-3 py-1 text-xs font-semibold text-primary bg-primary/10 rounded-full">TR - B2B</span></div>
            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-primary transition-colors">Almanya Pazarında Türk Şirketleri İçin B2B Lead Generation</h3>
            <p class="text-gray-400 text-sm mb-4">Almanya (DACH) pazarına girmek isteyen Türk şirketleri için B2B müşteri bulma taktikleri.</p>
        </a>

        <a href="b2b-lead-generierung-dach-2026.html" class="glass p-6 rounded-2xl hover:bg-white/5 transition-all group block">
            <div class="flex items-center gap-3 mb-4"><span class="px-3 py-1 text-xs font-semibold text-primary bg-primary/10 rounded-full">DE - B2B</span></div>
            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-primary transition-colors">B2B Lead-Generierung im DACH-Raum: Strategien</h3>
            <p class="text-gray-400 text-sm mb-4">Erfolgreiche Lead-Generation Strategien für B2B Unternehmen im DACH Markt 2026.</p>
        </a>

        <a href="meta-ads-trendleri-hedefleme-2026.html" class="glass p-6 rounded-2xl hover:bg-white/5 transition-all group block">
            <div class="flex items-center gap-3 mb-4"><span class="px-3 py-1 text-xs font-semibold text-secondary bg-secondary/10 rounded-full">TR - Meta Ads</span></div>
            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-secondary transition-colors">Meta (Facebook/Instagram) Reklamlarında 2026 Trendleri</h3>
            <p class="text-gray-400 text-sm mb-4">Meta Ads tarafında 2026 yılında başarılı olmak için kullanmanız gereken hedefleme stratejileri.</p>
        </a>

        <a href="meta-ads-trends-2026-dach.html" class="glass p-6 rounded-2xl hover:bg-white/5 transition-all group block">
            <div class="flex items-center gap-3 mb-4"><span class="px-3 py-1 text-xs font-semibold text-secondary bg-secondary/10 rounded-full">DE - Meta Ads</span></div>
            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-secondary transition-colors">Meta Ads Trends 2026: Höhere Conversion-Raten</h3>
            <p class="text-gray-400 text-sm mb-4">Die wichtigsten Meta (Facebook & Instagram) Werbetrends und Strategien für 2026.</p>
        </a>
"""

if '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">' in content:
    content = content.replace('<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">', '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">\n' + new_cards)
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injected new cards into index.html")
else:
    print("Could not find grid element.")
