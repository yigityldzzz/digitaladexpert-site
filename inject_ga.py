
import os

def inject_analytics(root_dir, analytics_id):
    # Google Analytics Global Site Tag
    ga_code = f"""
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={analytics_id}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());

      gtag('config', '{analytics_id}');
    </script>
    """
    
    # Walk through all HTML files
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            if filename.endswith(".html"):
                filepath = os.path.join(root, filename)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if GA is already there
                if analytics_id not in content:
                    # Inject right after <head>
                    if '<head>' in content:
                        content = content.replace('<head>', f'<head>\n{ga_code}')
                        
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        print(f"GA added to {filepath}")
                    else:
                        print(f"No <head> found in {filepath}")
                else:
                    print(f"GA already in {filepath}")

target_dir = 'site_update/digitaladexpert-cloudflare'
ga_id = 'G-R5LP3YD04Z'

inject_analytics(target_dir, ga_id)
