const fs = require('fs');
const path = require('path');

const files = [
    'nakliyat_google_ads.html',
    'emlak_google_ads.html',
    'disci_google_ads.html',
    'restoran_google_ads.html',
    'donerci_google_ads.html',
    'guzellik_google_ads.html',
    'tadilat_google_ads.html',
    'improved_index_de.html',
    'index_tr_with_sectors.html',
    'davetiye.html',
    'davetiye_v2.html',
    'davetiye_v3.html',
    'cv_yigit_yildiz.html',
    'digitaladexpert-site/index.html',
    'digitaladexpert-site/404.html'
];

const gtag = `<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-17910536535"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'AW-17910536535');
</script>
`;

files.forEach(file => {
    if (fs.existsSync(file)) {
        let content = fs.readFileSync(file, 'utf8');
        if (!content.includes('AW-17910536535')) {
            content = content.replace('</head>', `${gtag}\n</head>`);
            fs.writeFileSync(file, content);
            console.log(`Injected gtag into ${file}`);
        } else {
            console.log(`Skipped ${file} (already exists)`);
        }
    } else {
        console.log(`File not found: ${file}`);
    }
});
