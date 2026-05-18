from flask import Flask, redirect, request, jsonify, render_template
import sqlite3
import random
import string
import os
app = Flask(
    __name__,
    static_folder='static',
    template_folder='templates'
)

os.makedirs('instance', exist_ok=True)

# Database setup
def init_db():
    conn = sqlite3.connect('instance/urls.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS urls
                (short_code TEXT PRIMARY KEY,
                 original_url TEXT NOT NULL,
                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')
    custom_code = data.get('custom_code', '').strip()  # NEW

    if not original_url:
        return jsonify({'error': 'URL is required'}), 400

    if not original_url.startswith('http'):
        original_url = 'https://' + original_url

    # Use custom code if provided, else generate one
    short_code = custom_code if custom_code else generate_short_code()

    conn = sqlite3.connect('instance/urls.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO urls (short_code, original_url) VALUES (?, ?)',
                  (short_code, original_url))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({'error': 'That custom name is already taken! Try another.'}), 409
    conn.close()

    base_url = request.host_url
    short_url = f"{base_url}{short_code}"
    return jsonify({'short_url': short_url, 'short_code': short_code})
    

@app.route('/<short_code>')
def redirect_url(short_code):
    conn = sqlite3.connect('instance/urls.db')
    c = conn.cursor()
    c.execute('SELECT original_url FROM urls WHERE short_code = ?', (short_code,))
    result = c.fetchone()
    conn.close()
    
    if result:
        return redirect(result[0])
    return jsonify({'error': 'URL not found'}), 404

@app.route('/all', methods=['GET'])
def get_all_urls():
    conn = sqlite3.connect('instance/urls.db')
    c = conn.cursor()
    c.execute('SELECT short_code, original_url, created_at FROM urls')
    urls = c.fetchall()
    conn.close()

    return jsonify([{
        'short_code': u[0],
        'original_url': u[1],
        'created_at': u[2],
        'short_url': f'{request.host_url}{u[0]}'
    } for u in urls])

init_db()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
