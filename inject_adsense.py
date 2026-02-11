import os

# AdSense kodu
adsense_code = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8641074364970025"
     crossorigin="anonymous"></script>
"""

def inject_adsense(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Eğer kod zaten varsa ekleme
    if "client=ca-pub-8641074364970025" in content:
        print(f"Skipped (Already exists): {file_path}")
        return

    # <head> kapanış etiketinden hemen önce ekle
    if "</head>" in content:
        new_content = content.replace("</head>", f"{adsense_code}\n</head>")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected into: {file_path}")
    else:
        print(f"Skipped (No head tag): {file_path}")

# Ana dizindeki ve alt klasörlerdeki tüm .html dosyalarını bul
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            inject_adsense(os.path.join(root, file))

print("AdSense injection complete.")
