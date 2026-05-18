# CodeAlpha URL Shortener

A simple and modern URL Shortener web application built using **Python Flask**, **SQLite**, **HTML/CSS**, and **JavaScript**.

Users can:

* Shorten long URLs
* Create custom short links
* Redirect using short URLs
* View URL history
* Copy shortened links easily

---

## Features

* Shorten long URLs instantly
* Custom short names support
* URL redirection
* SQLite database storage
* Simple responsive UI
* Error handling for duplicate custom names
* Localhost support and deployment-ready

---

## Tech Stack

### Backend

* Python
* Flask
* SQLite

### Frontend

* HTML
* CSS
* JavaScript

---

## Project Structure

```bash
CodeAlpha_URLShortener/
│
├── app.py
├── urls.db
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── requirements.txt
└── README.md
```

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/diya2405/CodeAlpha_URLShortener.git
cd CodeAlpha_URLShortener
```

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate virtual environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install flask
```

or

```bash
pip install -r requirements.txt
```

---

### 4. Run Application

```bash
python app.py
```

Server will start on:

```bash
http://localhost:5000
```

---

## API Endpoint

### Shorten URL

**POST** `/shorten`

#### Request Body

```json
{
  "url": "https://example.com",
  "custom_code": "my-link"
}
```

#### Response

```json
{
  "short_url": "http://localhost:5000/my-link",
  "short_code": "my-link"
}
```

---

## Screenshots

Add screenshots here after completing the UI.

Example:

```md
![Home Page](screenshots/home.png)
```

---

## Deployment

You can deploy this project for free using:

* [Render](https://render.com)
* [Railway](https://railway.app)
* [PythonAnywhere](https://www.pythonanywhere.com)

---

## Future Improvements

* User authentication
* Analytics dashboard
* QR code generation
* Expiry dates for URLs
* Click tracking
* Dark mode

---

## Author

Developed by Diya

GitHub: [diya2405 GitHub Profile](https://github.com/diya2405)
Live at: [Visit](https://codealpha-urlshortener-a0p2.onrender.com)
---

## License

This project is open-source and available under the MIT License.
