from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def serve_world_map():
    html_path = os.path.join(os.path.dirname(__file__), 'world_map.html')
    with open(html_path, 'r') as file:
        html_content = file.read()
    return html_content  # Return HTML directly

if __name__ == '__main__':
    app.run(debug=True)