# this is a simple example of registering two functions into magi, executing the function stored in the database, and loading the dashboard

import magi
import os

# Add OpenAI key to enable automated descriptions and embedding of functions.
magi.add_key_wrapper('openai_api_key',os.environ['OPENAI_API_KEY'])

@magi.register_function()
def world():
    return "world"

@magi.register_function(dependencies=["world"])
def hello_world():
    x = world()
    return f"Hello {x}!"

print(hello_world())

@app.route('/')
def home():
    return f"Welcome to the main app. Visit <a href=\"/dashboard\">/dashboard</a> for magi dashboard."

if __name__ == "__main__":
    app = magi.create_app('/dashboard')
    app.run(host='0.0.0.0', port=8080)
