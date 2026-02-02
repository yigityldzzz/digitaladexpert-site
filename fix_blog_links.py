
import os

def fix_broken_blog_links(root_dir):
    langs = ['tr', 'de', 'en']
    
    for lang in langs:
        file_path = os.path.join(root_dir, lang, 'index.html')
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # The specific broken pattern observed
            broken_pattern = '<a /blog/"'
            fixed_pattern = '<a href="/blog/"'
            
            if broken_pattern in content:
                content = content.replace(broken_pattern, fixed_pattern)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed blog link in {file_path}")
            else:
                print(f"No broken link found in {file_path}")

root = 'site_update/digitaladexpert-cloudflare'
fix_broken_blog_links(root)
