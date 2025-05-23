from flask import Flask, render_template_string
import os

app = Flask(__name__)
REPORT_PATH = "report.txt"

@app.route('/')
def home():
    if not os.path.exists(REPORT_PATH):
        return "No report found. Run logger first."
    with open(REPORT_PATH, 'r') as f:
        content = f.read()
    return render_template_string("""
    <h2>Keystroke Logger Report</h2>
    <pre>{{ content }}</pre>
    """, content=content)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
