const fs = require('fs');
const path = require('path');

const baseUrl = 'https://digitaladexpert.de';

const pages = [
    { file: 'nakliyat_google_ads.html', url: '/nakliyat_google_ads' },
    { file: 'emlak_google_ads.html', url: '/emlak_google_ads' },
    { file: 'disci_google_ads.html', url: '/disci_google_ads' },
    { file: 'restoran_google_ads.html', url: '/restoran_google_ads' },
    { file: 'donerci_google_ads.html', url: '/donerci_google_ads' },
    { file: 'guzellik_google_ads.html', url: '/guzellik_google_ads' },
    { file: 'tadilat_google_ads.html', url: '/tadilat_google_ads' }
];

// 1. Inject Canonical Tags
pages.forEach(page => {
    if (fs.existsSync(page.file)) {
        let content = fs.readFileSync(page.file, 'utf8');
        const canonicalTag = `<link rel="canonical" href="${baseUrl}${page.url}" />`;
        
        // Remove existing canonical if any (simple regex)
        content = content.replace(/<link rel="canonical"[^>]*>/g, '');
        
        // Add new canonical
        if (content.includes('</head>')) {
            content = content.replace('</head>', `${canonicalTag}\n</head>`);
            fs.writeFileSync(page.file, content);
            console.log(`Added canonical to ${page.file}`);
        }
    }
});

// 2. Update Sitemap (Create a new clean one for root landing pages)
// We will modify the existing sitemap in digitaladexpert-site/sitemap.xml if possible, or just create a new one to overwrite.

const sitemapPath = 'digitaladexpert-site/sitemap.xml';
let sitemapContent = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://digitaladexpert.de/</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>`;

pages.forEach(page => {
    sitemapContent += `
  <url>
    <loc>${baseUrl}${page.url}</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>`;
});

sitemapContent += `
</urlset>`;

fs.writeFileSync('sitemap.xml', sitemapContent);
console.log('Generated new sitemap.xml with clean URLs');

