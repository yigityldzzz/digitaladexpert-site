const fs = require('fs');
const path = require('path');
const AdmZip = require('adm-zip');

const zipPath = '/root/.clawdbot/media/inbound/8a636e48-7212-42c2-9fc1-87ec7ca2685e.zip';
const outDir = '/root/clawd/site_update';

if (!fs.existsSync(outDir)){
    fs.mkdirSync(outDir, { recursive: true });
}

try {
    const zip = new AdmZip(zipPath);
    zip.extractAllTo(outDir, true);
    console.log('Extraction complete');
} catch (e) {
    console.error('Extraction failed:', e);
}
