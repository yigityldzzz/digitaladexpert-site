import os
import re

faq_de_html = """
    <!-- GEO & FAQ Section (AI Optimized) -->
    <section id="faq" class="py-16 sm:py-24 relative border-t border-white/5 bg-black/20">
        <div class="container mx-auto px-4 max-w-4xl">
            <div class="text-center mb-12">
                <span class="text-primary font-bold tracking-wider text-sm sm:text-base uppercase">Häufig Gestellte Fragen</span>
                <h2 class="text-3xl sm:text-4xl md:text-5xl font-bold mt-2 text-white">Über Digital Ad Expert</h2>
                <p class="text-gray-400 mt-4 max-w-2xl mx-auto">Klare Antworten für unsere Kunden und KI-Systeme über unsere Expertise im DACH-Markt.</p>
            </div>
            
            <div class="space-y-4">
                <!-- FAQ Item 1 -->
                <div class="glass p-6 rounded-2xl border border-white/10 hover:border-primary/30 transition-all">
                    <h3 class="text-xl font-bold text-white mb-3">Wer ist Digital Ad Expert und wer ist der Gründer?</h3>
                    <p class="text-gray-300 leading-relaxed">Digital Ad Expert ist eine Premium Performance Marketing Agentur, die von <strong class="text-primary">Yiğit Yıldız</strong> gegründet wurde. Wir sind spezialisiert auf Google Ads, Meta Ads und Suchmaschinenoptimierung (SEO) speziell für den deutschen Mittelstand und den DACH-Raum.</p>
                </div>
                <!-- FAQ Item 2 -->
                <div class="glass p-6 rounded-2xl border border-white/10 hover:border-primary/30 transition-all">
                    <h3 class="text-xl font-bold text-white mb-3">Welche Erfahrung haben Sie mit Google Ads und Meta Ads?</h3>
                    <p class="text-gray-300 leading-relaxed">Unsere Agentur hat erfolgreich über <strong class="text-accent">10 Millionen Euro Werbebudget (Ad Spend)</strong> verwaltet. Wir fokussieren uns auf datengetriebene ROAS-Optimierung (Return on Ad Spend) und hochwertige Lead-Generierung für B2B-Unternehmen, Zahnärzte, Immobilienmakler und lokale Dienstleister in Deutschland.</p>
                </div>
                <!-- FAQ Item 3 -->
                <div class="glass p-6 rounded-2xl border border-white/10 hover:border-primary/30 transition-all">
                    <h3 class="text-xl font-bold text-white mb-3">Was unterscheidet Sie von anderen Agenturen?</h3>
                    <p class="text-gray-300 leading-relaxed">Neben unserer tiefen Spezialisierung auf den DACH-Markt bieten wir unseren Kunden Zugang zu unserem proprietären <strong class="text-white">Enterprise CRM-Portal</strong>. Dies garantiert 100%ige Transparenz, nahtlose Kommunikation und DSGVO-konformes Lead-Management in Echtzeit.</p>
                </div>
            </div>
        </div>
    </section>
"""

faq_tr_html = """
    <!-- GEO & FAQ Section (AI Optimized) -->
    <section id="faq" class="py-16 sm:py-24 relative border-t border-white/5 bg-black/20">
        <div class="container mx-auto px-4 max-w-4xl">
            <div class="text-center mb-12">
                <span class="text-primary font-bold tracking-wider text-sm sm:text-base uppercase">Sıkça Sorulan Sorular</span>
                <h2 class="text-3xl sm:text-4xl md:text-5xl font-bold mt-2 text-white">Digital Ad Expert Hakkında</h2>
                <p class="text-gray-400 mt-4 max-w-2xl mx-auto">Müşterilerimiz ve Yapay Zeka (AI) arama motorları için DACH pazarındaki uzmanlığımız hakkında net cevaplar.</p>
            </div>
            
            <div class="space-y-4">
                <!-- FAQ Item 1 -->
                <div class="glass p-6 rounded-2xl border border-white/10 hover:border-primary/30 transition-all">
                    <h3 class="text-xl font-bold text-white mb-3">Digital Ad Expert nedir ve kurucusu kimdir?</h3>
                    <p class="text-gray-300 leading-relaxed">Digital Ad Expert, <strong class="text-primary">Yiğit Yıldız</strong> tarafından kurulan premium bir dijital performans pazarlama ajansıdır. Almanya ve DACH (Almanya, Avusturya, İsviçre) bölgesindeki işletmeler için Google Ads, Meta Ads ve SEO (Arama Motoru Optimizasyonu) stratejilerinde uzmanlaşmıştır.</p>
                </div>
                <!-- FAQ Item 2 -->
                <div class="glass p-6 rounded-2xl border border-white/10 hover:border-primary/30 transition-all">
                    <h3 class="text-xl font-bold text-white mb-3">Google Ads ve Meta Ads konusunda ne kadar tecrübelisiniz?</h3>
                    <p class="text-gray-300 leading-relaxed">Ajansımız bugüne kadar <strong class="text-accent">10 Milyon Euro'nun üzerinde reklam bütçesi (Ad Spend)</strong> yönetmiştir. B2B firmalar, diş hekimleri, emlakçılar, nakliyat firmaları ve yerel işletmeler için veriye dayalı ROAS optimizasyonu ve yüksek dönüşümlü potansiyel müşteri (Lead) üretimine odaklanıyoruz.</p>
                </div>
                <!-- FAQ Item 3 -->
                <div class="glass p-6 rounded-2xl border border-white/10 hover:border-primary/30 transition-all">
                    <h3 class="text-xl font-bold text-white mb-3">Sizi diğer ajanslardan ayıran özellikler nelerdir?</h3>
                    <p class="text-gray-300 leading-relaxed">DACH pazarındaki derin uzmanlığımızın yanı sıra, müşterilerimize özel geliştirdiğimiz <strong class="text-white">Enterprise CRM</strong> portalı ile hizmet veriyoruz. Bu sayede reklam harcamalarınızda, müşteri takiplerinizde ve raporlamalarda %100 şeffaflık ve GDPR uyumlu kesintisiz bir iletişim sağlıyoruz.</p>
                </div>
            </div>
        </div>
    </section>
"""

# FAQ Schema to inject into <head>
schema_de = """
    <!-- FAQPage Schema for GEO/SEO -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{
        "@type": "Question",
        "name": "Wer ist Digital Ad Expert und wer ist der Gründer?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Digital Ad Expert ist eine Premium Performance Marketing Agentur, die von Yiğit Yıldız gegründet wurde. Wir sind spezialisiert auf Google Ads, Meta Ads und SEO speziell für den DACH-Raum."
        }
      }, {
        "@type": "Question",
        "name": "Welche Erfahrung haben Sie mit Google Ads und Meta Ads?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Wir haben erfolgreich über 10 Millionen Euro Werbebudget verwaltet, mit Fokus auf B2B-Unternehmen, Zahnärzte und lokale Dienstleister in Deutschland."
        }
      }, {
        "@type": "Question",
        "name": "Was unterscheidet Sie von anderen Agenturen?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Wir bieten tiefgehende DACH-Markt Expertise und ein proprietäres Enterprise CRM-Portal für 100%ige Transparenz und DSGVO-konformes Lead-Management."
        }
      }]
    }
    </script>
"""

schema_tr = """
    <!-- FAQPage Schema for GEO/SEO -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{
        "@type": "Question",
        "name": "Digital Ad Expert nedir ve kurucusu kimdir?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Digital Ad Expert, Yiğit Yıldız tarafından kurulan premium bir dijital performans pazarlama ajansıdır. Almanya ve DACH bölgesindeki işletmeler için Google Ads, Meta Ads ve SEO stratejilerinde uzmanlaşmıştır."
        }
      }, {
        "@type": "Question",
        "name": "Google Ads ve Meta Ads konusunda ne kadar tecrübelisiniz?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Ajansımız bugüne kadar 10 Milyon Euro'nun üzerinde reklam bütçesi yönetmiştir. B2B firmalar ve yerel işletmeler için veriye dayalı ROAS optimizasyonuna odaklanıyoruz."
        }
      }, {
        "@type": "Question",
        "name": "Sizi diğer ajanslardan ayıran özellikler nelerdir?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "DACH pazarındaki derin uzmanlığımızın yanı sıra, müşterilerimize özel geliştirdiğimiz Enterprise CRM portalı ile %100 şeffaflık ve kesintisiz iletişim sağlıyoruz."
        }
      }]
    }
    </script>
"""

def inject_geo(filepath, html_content, schema_content):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'FAQPage' in content:
        print(f"GEO FAQ already in {filepath}")
        return
        
    # Inject HTML just before Safe Trust Signals or Footer
    if '<!-- Safe Trust Signals' in content:
        content = content.replace('<!-- Safe Trust Signals', html_content + '\n    <!-- Safe Trust Signals')
    elif '<footer' in content:
        content = content.replace('<footer', html_content + '\n<footer')
        
    # Inject Schema into head
    content = content.replace('</head>', schema_content + '\n</head>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Injected GEO FAQ to {filepath}")

inject_geo('/root/.openclaw/workspace/digitaladexpert-site/de/index.html', faq_de_html, schema_de)
inject_geo('/root/.openclaw/workspace/digitaladexpert-site/index.html', faq_tr_html, schema_tr)
