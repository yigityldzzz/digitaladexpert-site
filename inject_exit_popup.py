import os

popup_tr = """
<!-- Exit Intent Pop-up -->
<div id="exit-popup" class="fixed inset-0 z-[100] flex items-center justify-center bg-black/80 backdrop-blur-sm hidden opacity-0 transition-opacity duration-300">
    <div class="glass p-8 md:p-10 rounded-3xl max-w-lg w-full mx-4 border border-white/10 relative transform scale-95 transition-transform duration-300" id="exit-popup-content">
        <button onclick="closeExitPopup()" class="absolute top-4 right-4 text-gray-400 hover:text-white transition">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>
        <div class="text-center mb-6">
            <span class="bg-primary/20 text-primary px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wide mb-4 inline-block">Ücretsiz Rehber</span>
            <h3 class="text-2xl font-bold text-white mb-2">Gitmeden Önce! 🛑</h3>
            <p class="text-gray-400 text-sm">Almanya pazarında rakiplerinizin Google Ads ve Web Tasarımda yaptığı 5 büyük hatayı ve çözümünü içeren 2026 rehberimizi ücretsiz indirin.</p>
        </div>
        <!-- Formspree Endpoint -->
        <form action="https://formspree.io/f/mwkgypzw" method="POST" class="space-y-4">
            <input type="text" name="name" placeholder="Adınız" required class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-primary transition">
            <input type="email" name="email" placeholder="E-posta Adresiniz" required class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-primary transition">
            <button type="submit" class="w-full bg-gradient-to-r from-primary to-secondary text-white font-bold py-3 rounded-xl hover:opacity-90 transition shadow-lg shadow-primary/30">Rehberi Mailime Gönder</button>
        </form>
        <p class="text-[10px] text-gray-500 text-center mt-4">Asla spam göndermeyiz. Sadece değer üretiyoruz.</p>
    </div>
</div>

<script>
    let popupShown = localStorage.getItem('exitPopupShown');
    const popup = document.getElementById('exit-popup');
    const popupContent = document.getElementById('exit-popup-content');

    document.addEventListener('mouseout', (e) => {
        if (e.clientY <= 0 && !popupShown) {
            showExitPopup();
        }
    });

    function showExitPopup() {
        if(!popup) return;
        popup.classList.remove('hidden');
        setTimeout(() => {
            popup.classList.remove('opacity-0');
            popupContent.classList.remove('scale-95');
        }, 10);
        localStorage.setItem('exitPopupShown', 'true');
        popupShown = 'true';
    }

    function closeExitPopup() {
        if(!popup) return;
        popup.classList.add('opacity-0');
        popupContent.classList.add('scale-95');
        setTimeout(() => {
            popup.classList.add('hidden');
        }, 300);
    }
</script>
</body>
"""

popup_de = """
<!-- Exit Intent Pop-up -->
<div id="exit-popup" class="fixed inset-0 z-[100] flex items-center justify-center bg-black/80 backdrop-blur-sm hidden opacity-0 transition-opacity duration-300">
    <div class="glass p-8 md:p-10 rounded-3xl max-w-lg w-full mx-4 border border-white/10 relative transform scale-95 transition-transform duration-300" id="exit-popup-content">
        <button onclick="closeExitPopup()" class="absolute top-4 right-4 text-gray-400 hover:text-white transition">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>
        <div class="text-center mb-6">
            <span class="bg-primary/20 text-primary px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wide mb-4 inline-block">Kostenloser Guide</span>
            <h3 class="text-2xl font-bold text-white mb-2">Warten Sie kurz! 🛑</h3>
            <p class="text-gray-400 text-sm">Vermeiden Sie die 5 größten Google Ads Fehler, an denen die meisten KMUs scheitern. Laden Sie unsere 2026 Checkliste jetzt kostenlos herunter.</p>
        </div>
        <!-- Formspree Endpoint -->
        <form action="https://formspree.io/f/mwkgypzw" method="POST" class="space-y-4">
            <input type="text" name="name" placeholder="Ihr Name" required class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-primary transition">
            <input type="email" name="email" placeholder="Ihre E-Mail-Adresse" required class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-primary transition">
            <button type="submit" class="w-full bg-gradient-to-r from-primary to-secondary text-white font-bold py-3 rounded-xl hover:opacity-90 transition shadow-lg shadow-primary/30">Checkliste jetzt anfordern</button>
        </form>
        <p class="text-[10px] text-gray-500 text-center mt-4">Wir hassen Spam genauso wie Sie. Ihre Daten sind sicher.</p>
    </div>
</div>

<script>
    let popupShown = localStorage.getItem('exitPopupShown');
    const popup = document.getElementById('exit-popup');
    const popupContent = document.getElementById('exit-popup-content');

    document.addEventListener('mouseout', (e) => {
        if (e.clientY <= 0 && !popupShown) {
            showExitPopup();
        }
    });

    function showExitPopup() {
        if(!popup) return;
        popup.classList.remove('hidden');
        setTimeout(() => {
            popup.classList.remove('opacity-0');
            popupContent.classList.remove('scale-95');
        }, 10);
        localStorage.setItem('exitPopupShown', 'true');
        popupShown = 'true';
    }

    function closeExitPopup() {
        if(!popup) return;
        popup.classList.add('opacity-0');
        popupContent.classList.add('scale-95');
        setTimeout(() => {
            popup.classList.add('hidden');
        }, 300);
    }
</script>
</body>
"""

def inject(file_path, popup_code):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'id="exit-popup"' in content:
        print(f"Popup already in {file_path}")
        return
        
    content = content.replace('</body>', popup_code)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Injected popup into {file_path}")

inject('/root/.openclaw/workspace/digitaladexpert-site/index.html', popup_tr)
inject('/root/.openclaw/workspace/digitaladexpert-site/index_tr_with_sectors.html', popup_tr)
inject('/root/.openclaw/workspace/digitaladexpert-site/de/index.html', popup_de)
