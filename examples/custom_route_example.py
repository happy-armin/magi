# this is an example of how to use magi with custom routes

from magi import create_app, register_function

app = create_app('/dashboard')

@register_function()
def another_custom_function():
    return "Hello from another custom function!"

@app.route('/')
def home():
    return f"Welcome to the main app. Visit <a href=\"/dashboard\">/dashboard</a> for magi dashboard."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
