from flask import Flask, request, jsonify, render_template
import pickle
import Functions as f
app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/predict',methods=['POST'])
def predict():
    inputValue = request.form['SMS']
    inputValue = f.expand_contractions(inputValue)
    inputValue = f.preprocessStepOne(inputValue)
    inputValue = f.remove_stopwords(inputValue)
    inputValue = f.get_stem(inputValue)
    print(inputValue)
    prediction = model.predict_proba([inputValue])
    
    ham = prediction[0][0]
    spam = prediction[0][1]

    return render_template('index.html', prediction_text=f'spam : {spam} \n , ham : {ham}')

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict_proba(data.values())

    ham = prediction[0][0]
    spam = prediction[0][1]
    return jsonify(ham,spam)

if __name__ == "__main__":
    app.run(debug=True)