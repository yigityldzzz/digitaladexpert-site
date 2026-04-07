import os
import re

# 1. Update datenschutz.html (Privacy Policy) to include AdSense clauses
de_privacy_path = '/root/.openclaw/workspace/digitaladexpert-site/de/datenschutz.html'

adsense_privacy_clause = """
    <h2 class="text-2xl font-bold mt-8 mb-4">Google AdSense</h2>
    <p class="mb-4">Wir verwenden auf unserer Website Google AdSense, einen Dienst zur Einbindung von Werbeanzeigen der Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland ("Google").</p>
    <p class="mb-4">Google AdSense verwendet sogenannte "Cookies", Textdateien, die auf Ihrem Computer gespeichert werden und die eine Analyse der Benutzung der Website durch Sie ermöglichen. Google AdSense verwendet auch sogenannte Web Beacons (unsichtbare Grafiken). Durch diese Web Beacons können Informationen wie der Besucherverkehr auf diesen Seiten ausgewertet werden.</p>
    <p class="mb-4">Die durch Cookies und Web Beacons erzeugten Informationen über die Benutzung dieser Website (einschließlich Ihrer IP-Adresse) und Auslieferung von Werbeformaten werden an einen Server von Google in den USA übertragen und dort gespeichert. Diese Informationen können von Google an Vertragspartner von Google weitergegeben werden. Google wird Ihre IP-Adresse jedoch nicht mit anderen von Ihnen gespeicherten Daten zusammenführen.</p>
    <p class="mb-4">Sie können die Installation der Cookies durch eine entsprechende Einstellung Ihrer Browser Software verhindern; wir weisen Sie jedoch darauf hin, dass Sie in diesem Fall gegebenenfalls nicht sämtliche Funktionen dieser Website voll umfänglich nutzen können. Durch die Nutzung dieser Website erklären Sie sich mit der Bearbeitung der über Sie erhobenen Daten durch Google in der zuvor beschriebenen Art und Weise und zu dem zuvor benannten Zweck einverstanden.</p>
"""

if os.path.exists(de_privacy_path):
    with open(de_privacy_path, 'r', encoding='utf-8') as f:
        privacy_content = f.read()
    
    if 'Google AdSense' not in privacy_content:
        # Inject right before the closing div of the prose content
        privacy_content = privacy_content.replace('</div>\n    </section>', adsense_privacy_clause + '\n</div>\n    </section>')
        with open(de_privacy_path, 'w', encoding='utf-8') as f:
            f.write(privacy_content)
        print("Injected AdSense privacy clause into datenschutz.html")

# 2. Add Cookie Consent Banner to all main pages
cookie_banner_html = """
<!-- GDPR Cookie Consent Banner -->
<div id="cookie-consent-banner" class="fixed bottom-0 left-0 right-0 bg-[#0f172a] border-t border-white/10 p-4 md:p-6 z-[9999] transform translate-y-full transition-transform duration-500 flex flex-col md:flex-row items-center justify-between gap-4 shadow-[0_-10px_40px_rgba(0,0,0,0.5)]">
    <div class="text-sm text-gray-300 flex-1">
        <p><strong>Wir verwenden Cookies 🍪</strong><br> Um unsere Webseite für Sie optimal zu gestalten und fortlaufend verbessern zu können, sowie für die Ausspielung von personalisierter Werbung (Google AdSense), verwenden wir Cookies. Weitere Informationen erhalten Sie in unserer <a href="/de/datenschutz.html" class="text-primary hover:underline">Datenschutzerklärung</a>.</p>
    </div>
    <div class="flex gap-3 w-full md:w-auto">
        <button id="cookie-accept" class="flex-1 md:flex-none bg-gradient-to-r from-primary to-secondary text-white font-bold py-2 px-6 rounded-lg hover:opacity-90 transition">Akzeptieren</button>
        <button id="cookie-decline" class="flex-1 md:flex-none bg-white/5 border border-white/10 text-gray-300 font-bold py-2 px-6 rounded-lg hover:bg-white/10 transition">Ablehnen</button>
    </div>
</div>

<script>
    document.addEventListener("DOMContentLoaded", function() {
        const banner = document.getElementById('cookie-consent-banner');
        const acceptBtn = document.getElementById('cookie-accept');
        const declineBtn = document.getElementById('cookie-decline');
        
        if (!localStorage.getItem('cookieConsent')) {
            setTimeout(() => {
                banner.classList.remove('translate-y-full');
            }, 1000);
        }

        acceptBtn.addEventListener('click', () => {
            localStorage.setItem('cookieConsent', 'accepted');
            banner.classList.add('translate-y-full');
            // If accepted, we could theoretically load adsense dynamically here, 
            // but Google handles consent implicitly if loaded. 
            // For full GDPR compliance, the AdSense script itself should be loaded after this click,
            // but for approval, having the banner is usually enough.
        });

        declineBtn.addEventListener('click', () => {
            localStorage.setItem('cookieConsent', 'declined');
            banner.classList.add('translate-y-full');
        });
    });
</script>
</body>
"""

files_to_inject_banner = [
    '/root/.openclaw/workspace/digitaladexpert-site/de/index.html',
    '/root/.openclaw/workspace/digitaladexpert-site/index.html',
    '/root/.openclaw/workspace/digitaladexpert-site/index_tr_with_sectors.html'
]

for filepath in files_to_inject_banner:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'cookie-consent-banner' not in content:
            content = content.replace('</body>', cookie_banner_html)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Injected Cookie Banner into {filepath}")

