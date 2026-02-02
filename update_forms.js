const fs = require('fs');

const files = [
    'nakliyat_google_ads.html',
    'emlak_google_ads.html',
    'disci_google_ads.html',
    'restoran_google_ads.html',
    'donerci_google_ads.html',
    'guzellik_google_ads.html',
    'tadilat_google_ads.html',
    'improved_index_de.html',
    'index_tr_with_sectors.html'
];

const nextInput = '<input type="hidden" name="_next" value="https://digitaladexpert.de/thanks.html">';

files.forEach(file => {
    if (fs.existsSync(file)) {
        let content = fs.readFileSync(file, 'utf8');
        // Check if form exists and doesn't already have _next
        if (content.includes('formspree.io') && !content.includes('name="_next"')) {
            // Inject after the opening <form> tag
            content = content.replace(/(<form[^>]*action="[^"]*formspree[^"]*"[^>]*>)/i, `$1\n    ${nextInput}`);
            fs.writeFileSync(file, content);
            console.log(`Updated form in ${file}`);
        } else {
            console.log(`Skipped ${file} (no form or already updated)`);
        }
    }
});
