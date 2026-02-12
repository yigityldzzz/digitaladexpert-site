import os

# Google Ads Dönüşüm Etkinlik Kodu
conversion_code = """
<!-- Google Ads Conversion Event -->
<script>
  gtag('event', 'conversion_event_submit_lead_form_4', {
    // <event_parameters>
  });
</script>
"""

def inject_conversion_event(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Zaten varsa ekleme
    if "conversion_event_submit_lead_form_4" in content:
        print(f"Skipped (Already exists): {file_path}")
        return

    # </head> etiketinden hemen önce ekle (Global Tag'den sonra çalışması için)
    if "</head>" in content:
        new_content = content.replace("</head>", f"{conversion_code}\n</head>")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected into: {file_path}")
    else:
        print(f"Skipped (No head tag): {file_path}")

# Sadece thanks.html dosyalarını hedefle
target_files = [
    "digitaladexpert-site/thanks.html",
    "digitaladexpert-site/tr/thanks.html",
    "digitaladexpert-site/en/thanks.html",
    "digitaladexpert-site/de/thanks.html"
]

for file_path in target_files:
    if os.path.exists(file_path):
        inject_conversion_event(file_path)
    else:
        print(f"File not found: {file_path}")

print("Conversion Event injection complete.")
