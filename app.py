from flask import Flask, render_template

app = Flask(__name__)

# Rota principal
@app.route('/')
def home():
    # O Flask vai procurar esse arquivo dentro da pasta 'templates'
    return render_template('index.html')

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000, debug=True)