# Detection System

Show probability of SMS is spam or ham  
This repository of project has written with flask 
and used base of machine learning algorithm such as Logistic Regression, etc.

## Dataset
Attached .sql file in Jupyter notebook  
dataset has two columns : 
1. Category 
2. Content  

First, content need to preprocess as far as I could, I did it   
but if you know another solution, please tell me  
<br>
![DataSet](https://github.com/hoco1/Spam-detection/blob/main/img/dataset.jpg)

## Algorithm and Preprocessing

**Algorithm** 

* MultionialNB
* LogisticRegression
* SGDClassifier 
 
**Preprocessing**
* Expanding Contraction
* lowercase
* remove numbers
* remove punctuation
* remove accented characters
* remove extra whitespaces and tabs
* remove stop words
* text stemming

## Deployment

**Flask application**

![WebSite](https://github.com/hoco1/Spam-detection/blob/main/img/main.jpg)
<br>
<br>
![How Does It Work](https://github.com/hoco1/Spam-detection/blob/main/img/How%20does%20it%20work.gif)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

