# flask_app
One Month flask app

This is a project that was built as a learning experience for a class on www.OneMonth.com. 
It's simply an example of how Flask works, and how I can use a python weather app that was built in the same class. 

Dependencies:
You'll need to pip install the following modules
(It's likely some will have already been installed): 
<br>flask
<br>forecastio
<br>geopy.geocoders
<br>os
<br>dotenv


In addition to that, you'll need to set up your own API keys at forecast.io.( https://developer.forecast.io/ )
Once your API keys are set up, you need to create your own .env file, and save the keys in it. (It will go in your flask_app folder)
Use the follwoing format in your .env file: FORECASTIO_API_KEY=[your_api_key_goes_here]  (remove the brackets)
Be sure to tell your .gitignore file to ignore your .env file. You don't want to upload your key for the whole world to see. That'd be bad!

Once you've installed everything, cd to the flask_app directory and run the app: python3 web.py
