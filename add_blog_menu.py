
import os

def add_blog_link_to_menus(root_dir, lang):
    lang_dir = os.path.join(root_dir, lang)
    index_path = os.path.join(lang_dir, 'index.html')
    
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Link Data
        link_text = "Blog"
        link_href = "/blog/"
        
        # 1. Desktop Header
        # Insert before "Contact" (İletişim/Kontakt)
        # We need to find the specific contact link anchor
        
        contact_map = {
            'tr': 'İletişim',
            'de': 'Kontakt',
            'en': 'Contact'
        }
        contact_text = contact_map[lang]
        
        desktop_link = f'<a href="{link_href}" class="text-gray-300 hover:text-white transition-colors text-sm">{link_text}</a>'
        mobile_link = f'<a href="{link_href}" class="mobile-nav-link text-gray-300 hover:text-white transition-colors py-3 border-b border-white/10">{link_text}</a>'
        
        # Target: <a href="#contact" ...>{contact_text}</a>
        # We use a broader match to ensure we catch the desktop link class structure
        desktop_target = f'href="#contact" class="text-gray-300 hover:text-white transition-colors text-sm">{contact_text}</a>'
        
        if desktop_target in content and link_href not in content:
            # Insert Desktop Link BEFORE Contact
            content = content.replace(desktop_target, f'{link_href}" class="text-gray-300 hover:text-white transition-colors text-sm">{link_text}</a>\n                    <a {desktop_target}')
            
            # 2. Mobile Menu
            # Target: <a href="#contact" ...>{contact_text}</a> inside mobile menu has different classes
            mobile_target = f'href="#contact" class="mobile-nav-link text-gray-300 hover:text-white transition-colors py-3 border-b border-white/10">{contact_text}</a>'
            
            if mobile_target in content:
                content = content.replace(mobile_target, f'{link_href}" class="mobile-nav-link text-gray-300 hover:text-white transition-colors py-3 border-b border-white/10">{link_text}</a>\n                <a {mobile_target}')
            
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added Blog link to {index_path}")

root = 'site_update/digitaladexpert-cloudflare'
add_blog_link_to_menus(root, 'tr')
add_blog_link_to_menus(root, 'de')
add_blog_link_to_menus(root, 'en')
