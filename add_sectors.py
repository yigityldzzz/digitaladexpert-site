
def update_index_with_sectors(file_path, lang):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Define sector content based on language
    if lang == 'tr':
        header = "Sektörel Çözümler"
        subheader = "İşletmenize özel hazır stratejiler"
        sectors = [
            {'icon': '🚚', 'name': 'Nakliyat', 'link': '/tr/nakliyat_google_ads.html', 'desc': 'Daha fazla taşıma işi'},
            {'icon': '🦷', 'name': 'Diş Hekimi', 'link': '/tr/disci_google_ads.html', 'desc': 'İmplant ve estetik hasta'},
            {'icon': '🏘️', 'name': 'Emlak', 'link': '/tr/emlak_google_ads.html', 'desc': 'Satılık portföy artırma'},
            {'icon': '🍽️', 'name': 'Restoran', 'link': '/tr/restoran_google_ads.html', 'desc': 'Daha çok masa doluluğu'},
            {'icon': '🥙', 'name': 'Döner/Büfe', 'link': '/tr/donerci_google_ads.html', 'desc': 'Yerel sipariş artışı'},
            {'icon': '💅', 'name': 'Güzellik', 'link': '/tr/guzellik_google_ads.html', 'desc': 'Randevu takvimi doldurma'},
            {'icon': '🔨', 'name': 'Tadilat', 'link': '/tr/tadilat_google_ads.html', 'desc': 'Büyük proje işleri'}
        ]
    elif lang == 'de':
        header = "Branchenlösungen"
        subheader = "Spezialisierte Strategien für Ihren Sektor"
        sectors = [
            {'icon': '🚚', 'name': 'Umzug', 'link': '/de/umzug_marketing.html', 'desc': 'Mehr Umzugsaufträge'},
            {'icon': '🦷', 'name': 'Zahnarzt', 'link': '/de/zahnarzt_marketing.html', 'desc': 'Privatpatienten gewinnen'},
            {'icon': '🏘️', 'name': 'Immobilien', 'link': '/de/immobilien_marketing.html', 'desc': 'Mehr Eigentümer-Leads'},
            {'icon': '🍽️', 'name': 'Gastro', 'link': '/de/gastro_marketing.html', 'desc': 'Volles Restaurant'},
            {'icon': '🥙', 'name': 'Imbiss', 'link': '/de/imbiss_marketing.html', 'desc': 'Mehr Bestellungen'},
            {'icon': '💅', 'name': 'Kosmetik', 'link': '/de/kosmetik_marketing.html', 'desc': 'Ausgebuchte Termine'},
            {'icon': '🔨', 'name': 'Handwerk', 'link': '/de/handwerker_marketing.html', 'desc': 'Lukrative Bauprojekte'}
        ]
    elif lang == 'en':
        header = "Industry Solutions"
        subheader = "Tailored strategies for your niche"
        sectors = [
            {'icon': '🚚', 'name': 'Movers', 'link': '/en/movers_marketing.html', 'desc': 'Get more moving jobs'},
            {'icon': '🦷', 'name': 'Dentist', 'link': '/en/dentist_marketing.html', 'desc': 'Attract private patients'},
            {'icon': '🏘️', 'name': 'Real Estate', 'link': '/en/realestate_marketing.html', 'desc': 'Get more listings'},
            {'icon': '🍽️', 'name': 'Restaurant', 'link': '/en/restaurant_marketing.html', 'desc': 'Full tables & orders'},
            {'icon': '🥙', 'name': 'Street Food', 'link': '/en/kebab_marketing.html', 'desc': 'Local food marketing'},
            {'icon': '💅', 'name': 'Beauty', 'link': '/en/beauty_marketing.html', 'desc': 'Fully booked calendar'},
            {'icon': '🔨', 'name': 'Contractor', 'link': '/en/renovation_marketing.html', 'desc': 'Win big projects'}
        ]

    # Construct HTML for sectors grid
    sector_html = f'''
    <!-- SECTOR SECTION START -->
    <section class="py-12 relative border-t border-white/5">
        <div class="container mx-auto px-4 max-w-6xl">
            <div class="text-center mb-10" data-aos="fade-up">
                <h2 class="text-2xl sm:text-3xl font-bold mb-2 text-white">{header}</h2>
                <p class="text-gray-400 text-sm sm:text-base">{subheader}</p>
            </div>
            
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-7 gap-3 sm:gap-4">
    '''
    
    for s in sectors:
        sector_html += f'''
                <a href="{s['link']}" class="glass p-3 sm:p-4 rounded-xl text-center hover:bg-white/10 transition-all group" data-aos="fade-up">
                    <div class="text-2xl sm:text-3xl mb-2 group-hover:scale-110 transition-transform">{s['icon']}</div>
                    <div class="font-bold text-white text-xs sm:text-sm mb-1">{s['name']}</div>
                    <div class="text-[10px] sm:text-xs text-gray-500 leading-tight">{s['desc']}</div>
                </a>
        '''
        
    sector_html += '''
            </div>
        </div>
    </section>
    <!-- SECTOR SECTION END -->
    '''
    
    # Insert before the "Services" section or after "Hero"
    # Let's insert it after the Stats section for high visibility
    if '<section class="py-12 sm:py-20 relative">' in html:
        # Finding the closing of stats section to insert after
        # A bit risky with string replace, let's look for a safe anchor.
        # Inserting before "About" section seems safe and logical flow.
        target = '<section id="about"'
        html = html.replace(target, sector_html + '\n' + target)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated {file_path}")
    else:
        print(f"Could not find anchor in {file_path}")

update_index_with_sectors('site_update/digitaladexpert-cloudflare/tr/index.html', 'tr')
update_index_with_sectors('site_update/digitaladexpert-cloudflare/de/index.html', 'de')
update_index_with_sectors('site_update/digitaladexpert-cloudflare/en/index.html', 'en')
