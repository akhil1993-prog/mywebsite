from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # ഇവിടെ നമ്മൾ index.html ഫയലിനെ കാണിക്കാൻ ഫ്ലാസ്കിനോട് ആവശ്യപ്പെടുന്നു
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)