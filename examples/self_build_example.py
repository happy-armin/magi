import magi
import os

# Add OpenAI key to enable automated descriptions and embedding of functions.
magi.add_key_wrapper('openai_api_key',os.environ['OPENAI_API_KEY'])

# Load below function packs to play with experimental self-building functions
magi.load_functions("drafts/code_writing_functions")
magi.load_functions("drafts/self_build")


magi.self_build("A growth marketer at an enterprise SaaS company.")

@app.route('/')
def home():
    return f"Welcome to the main app. Visit <a href=\"/dashboard\">/dashboard</a> for magi dashboard."

if __name__ == "__main__":
    app = magi.create_app('/dashboard')
    app.run(host='0.0.0.0', port=8080)
