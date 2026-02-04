import os

# Define the script content directly or read from file
with open('digitaladexpert-site/force_redirect.html', 'r') as f:
    script_content = f.read()

files_to_patch = [
    'digitaladexpert-site/de/index.html',
    'digitaladexpert-site/tr/index.html',
    'digitaladexpert-site/en/index.html'
]

for file_path in files_to_patch:
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Check if already patched to avoid duplication
        if 'Smart Redirect based on current path' in content:
            print(f"Skipping {file_path}, already patched.")
            continue
            
        # Inject before closing body tag
        if '</body>' in content:
            new_content = content.replace('</body>', script_content + '\n</body>')
            with open(file_path, 'w') as f:
                f.write(new_content)
            print(f"Patched {file_path}")
        else:
            print(f"Could not find </body> in {file_path}")
    else:
        print(f"File not found: {file_path}")
