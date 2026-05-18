async function shortenURL() {
    const url = document.getElementById('urlInput').value.trim();
    const custom_code = document.getElementById('customCode').value.trim();
    if (!url) return alert('Please enter a URL');

    const res = await fetch('/shorten', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({url, custom_code})
    });
    const data = await res.json();
    if (data.error) return alert(data.error);  // shows "already taken" etc.

    document.getElementById('shortUrl').href = data.short_url;
    document.getElementById('shortUrl').textContent = data.short_url;
    document.getElementById('result').style.display = 'block';
    loadHistory();
}

function copyURL() {
    const url = document.getElementById('shortUrl').textContent;
    navigator.clipboard.writeText(url);
    alert('Copied!');
}

async function loadHistory() {
    const res = await fetch('/all');
    const urls = await res.json();
    
    const history = document.getElementById('history');
    if (urls.length === 0) return;
    
    history.innerHTML = '<h3>Recent URLs</h3>' + urls.reverse().slice(0,5).map(u => `
        <div class="url-item">
            <a href="${u.short_url}" target="_blank">${u.short_url}</a>
            <div class="original">${u.original_url}</div>
        </div>
    `).join('');
}

loadHistory();