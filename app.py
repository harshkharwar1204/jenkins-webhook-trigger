from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Weather Monitor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 50px;
            text-align: center;
        }
        .container {
            background: rgba(255,255,255,0.1);
            padding: 30px;
            border-radius: 15px;
            max-width: 600px;
            margin: 0 auto;
        }
        h1 { font-size: 2.5em; margin-bottom: 20px; }
        .info { font-size: 1.2em; margin: 15px 0; }
        .timestamp { font-size: 0.9em; opacity: 0.8; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌤️ Weather Monitor</h1>
        <div class="info">Application Status: <strong>Running</strong></div>
        <div class="info">Jenkins Build: <strong>SUCCESS</strong></div>
        <div class="info">Build Trigger: <strong>GitHub Webhook</strong></div>
        <div class="timestamp">Deployed: {{ timestamp }}</div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(HTML_TEMPLATE, timestamp=timestamp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

