from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Return a simple text response for the root path.
    return 'Hello, World from Google App Engine!'

if __name__ == '__main__':
    # Only used when running the script locally for development:
    # bind to 127.0.0.1:8080 so the local server listens on port 8080.
    app.run(host='127.0.0.1', port=8080, debug=True)
