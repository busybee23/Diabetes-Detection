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
    
    
    
    
    
    
    
    
    
    
    
    
    
#     name = request.form['name']
#     age = request.form['age']
#     pregnant = request.form['pregnant']
#     insulin = request.form['insulin']
#     bmi = request.form['bmi']
#     pedigree = request.form['pedigree']
#     glucose = request.form['glucose']
#     bp = request.form['bp']
#     #Predict on the given parameters
#     prediction = model.predict_class(pregnant,insulin,bmi,age,glucose,bp,pedigree)
#     print(prediction)
#     #Route for result
#     if prediction[0] == '1':
#         return render_template("positive.html", result="true")
#     elif prediction[0] == '0':
#         return render_template("negetive.html", result="true")
        
# # if __name__ == "__main__":
# #     app.run()