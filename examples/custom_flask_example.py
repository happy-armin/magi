#this is an example of how to use the magi framework in a custom flask app

from flask import Flask
import magi
from magi import register_function, load_functions

app = Flask(__name__)

# Use the magi blueprints
magi.use_blueprints(app, dashboard_route='/dashboard')

@register_function()
def integrated_function():
    return "Hello from integrated function!"

load_functions('plugins/firecrawl')

@app.route('/')
def home():
    return "Welcome to the main app. Visit /dashboard for magi dashboard."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
