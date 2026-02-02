
import os

def add_process_link_to_header(root_dir, lang):
    link_data = {
        'tr': {'text': 'Süreç', 'href': '/tr/nasil-calisiyoruz.html', 'insert_after': 'Hizmetler'},
        'de': {'text': 'Prozess', 'href': '/de/prozess.html', 'insert_after': 'Leistungen'},
        'en': {'text': 'Process', 'href': '/en/process.html', 'insert_after': 'Services'}
    }
    
    data = link_data[lang]
    new_link = f'<a href="{data["href"]}" class="text-gray-300 hover:text-white transition-colors text-sm">{data["text"]}</a>'
    
    # Also add to mobile menu
    mobile_link = f'<a href="{data["href"]}" class="mobile-nav-link text-gray-300 hover:text-white transition-colors py-3 border-b border-white/10">{data["text"]}</a>'

    lang_dir = os.path.join(root_dir, lang)
    index_path = os.path.join(lang_dir, 'index.html')
    
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Desktop Header Injection
        # Find the anchor link to insert after
        # <a href="#services" ...>Hizmetler</a>
        # We need a regex or string find that matches the specific link text
        
        target_str = f'>{data["insert_after"]}</a>'
        if target_str in content and data['href'] not in content:
            content = content.replace(target_str, target_str + '\n                    ' + new_link)
            
            # 2. Mobile Menu Injection
            # Find mobile link to insert after
            mobile_target = f'>{data["insert_after"]}</a>'
            # Note: The text is same, but context is different. The first replace might have hit the header nav.
            # We need to be careful not to double insert if the string is identical.
            # Actually, `content.replace` replaces ALL occurrences.
            # So the first replacement likely added the link to BOTH Desktop Nav and Mobile Nav if the text pattern matched both.
            # Let's check if mobile menu has different structure.
            # Desktop: class="... text-sm"
            # Mobile: class="... py-3 border-b ..."
            
            # Let's do it safer: Split logic
            
            # Re-read original to be safe
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Desktop
            desktop_anchor = f'>{data["insert_after"]}</a>'
            # We look for the one inside <nav class="hidden md:flex ...">
            # Simple string replace might be risky but let's try to target the href="#services"
            
            # Let's just insert before "Portfolio" / "Portfolyo" / "Kontakt"
            # It's safer to append to the end of the menu list or insert at specific position.
            
            # Strategy: Insert BEFORE "Contact" (İletişim/Kontakt)
            contact_map = {
                'tr': 'İletişim',
                'de': 'Kontakt',
                'en': 'Contact'
            }
            contact_text = contact_map[lang]
            
            # Desktop Insert
            desktop_contact = f'<a href="#contact" class="text-gray-300 hover:text-white transition-colors text-sm">{contact_text}</a>'
            if desktop_contact in content:
                content = content.replace(desktop_contact, new_link + '\n                    ' + desktop_contact)
            
            # Mobile Insert
            mobile_contact = f'<a href="#contact" class="mobile-nav-link text-gray-300 hover:text-white transition-colors py-3 border-b border-white/10">{contact_text}</a>'
            if mobile_contact in content:
                content = content.replace(mobile_contact, mobile_link + '\n                ' + mobile_contact)

            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated header in {index_path}")

root = 'site_update/digitaladexpert-cloudflare'
add_process_link_to_header(root, 'tr')
add_process_link_to_header(root, 'de')
add_process_link_to_header(root, 'en')
