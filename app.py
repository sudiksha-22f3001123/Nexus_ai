from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the main LLM agent interface"""
    # Read the HTML file and serve it
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    return html_content

@app.route('/test')
def test():
    """Serve the test page"""
    with open('test.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    return html_content

@app.route('/health')
def health():
    """Health check endpoint"""
    return {"status": "ok", "message": "LLM Agent POC server is running"}

@app.route('/static/<path:filename>')
def static_files(filename):
    """Serve static files if needed"""
    return send_from_directory('.', filename)

if __name__ == '__main__':
    print("🚀 Starting LLM Agent POC Server...")
    print("📍 Open in browser: http://localhost:5000")
    print("🛠️  Tools available: Google Search, AI Pipe Proxy, JS Sandbox")
    print("💡 Make sure to set your AI Pipe token and Google API credentials!")
    
    # Run the Flask development server
    app.run(
        host='0.0.0.0',  # Allow external connections
        port=5000,
        debug=True,      # Enable auto-reload on file changes
        use_reloader=True
    )
