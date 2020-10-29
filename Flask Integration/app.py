import numpy as np 
from flask import Flask, request, render_template
import pickle 

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

#Define home route
@app.route("/")
def home():
    return render_template("index.html")

#Define diagnosis route
@app.route("/diagnosis", methods=['POST'])
def diagnosis():
    '''
    For rendering results on HTML GUI 
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    

    if prediction == 1 :
        return render_template('index.html', prediction_text="Positive")
    else :
        return render_template('index.html', prediction_text="Negative")

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
