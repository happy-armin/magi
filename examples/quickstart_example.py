

import magi
import os


app = magi.create_app('/dashboard')

# Add OpenAI key to enable automated descriptions and embedding of functions.
magi.add_key_wrapper('openai_api_key',os.environ['OPENAI_API_KEY'])


@app.route('/')
def home():
    return f"Welcome to the main app. Visit <a href=\"/dashboard\">/dashboard</a> for magi dashboard."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
