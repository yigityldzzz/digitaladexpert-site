import os

# Google Ads GTAG Kodu
ads_code = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-17910543951"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'AW-17910543951');
</script>
"""

def inject_ads_tag(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Zaten varsa ekleme
    if "AW-17910543951" in content:
        print(f"Skipped (Already exists): {file_path}")
        return

    # <head> başlangıcından hemen sonrasına ekle (En üste)
    if "<head>" in content:
        new_content = content.replace("<head>", f"<head>\n{ads_code}")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected into: {file_path}")
    else:
        print(f"Skipped (No head tag): {file_path}")

# Tüm .html dosyalarını tara
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            inject_ads_tag(os.path.join(root, file))

print("Google Ads Tag injection complete.")
