from flask import Flask, render_template, request
import yelphelp
from weather import get_weather
import os

app = Flask(__name__)

@app.route("/")
def index():
    address = request.values.get('address')
    business = None
    address1 = address
    weather1 = get_weather(address1)
    if address:
        business = yelphelp.get_businesses(address, "food")
      #  address1 = address
       # weather1 = get_weather(address)
    return render_template('index.html', business=business, address=address, weather1=weather1)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
