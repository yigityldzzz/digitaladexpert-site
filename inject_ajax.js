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

const ajaxScript = `
<script>
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form[action*="formspree.io"]');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const button = form.querySelector('button[type="submit"]');
            const originalText = button.innerText;
            button.innerText = 'Gönderiliyor...';
            button.disabled = true;

            const formData = new FormData(form);
            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'Accept': 'application/json'
                }
            }).then(response => {
                if (response.ok) {
                    window.location.href = '/thanks.html';
                } else {
                    alert('Bir hata oluştu. Lütfen tekrar deneyin.');
                    button.innerText = originalText;
                    button.disabled = false;
                }
            }).catch(error => {
                console.error('Error:', error);
                alert('Bir hata oluştu. Lütfen tekrar deneyin.');
                button.innerText = originalText;
                button.disabled = false;
            });
        });
    });
});
</script>
`;

files.forEach(file => {
    if (fs.existsSync(file)) {
        let content = fs.readFileSync(file, 'utf8');
        // Avoid duplicate injection
        if (!content.includes('button.innerText = \'Gönderiliyor...\'')) {
            content = content.replace('</body>', `${ajaxScript}\n</body>`);
            fs.writeFileSync(file, content);
            console.log(`Injected AJAX script into ${file}`);
        } else {
            console.log(`Skipped ${file} (already has AJAX script)`);
        }
    }
});
