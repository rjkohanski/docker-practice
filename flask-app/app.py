from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from Docker!</h1><p>This app is running in a container.</p>'

@app.route('/health')
def health():
    return {'status': 'healthy', 'message': 'Container is running'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

