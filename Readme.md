# Apply flask on a Simple application

1. First we create a virtual environment "flask_env" and activate this
    follow these command
        * python -m venv flask_env
        * flask_env\Scripts\activate

2. then we install flask in virtual environment 
    follow this command
        -> pip install flask

3. then we create a flask application [local host application](app.py)

4. then run the app.py
    follow this command
        -> python app.py

5. after run we see a localhost address like http://127.0.0.1:5000
    -> press ctrl and click on this address for excute

6. Done


## Create a StandardScaler api using flask

1. Create a [StandardScaler api](scaler.py) file 

2. than we import some library for running StandardScaler api
    -> Flask
    -> pandas
    -> numpy
    -> StandardScaler
    -> train_test_split

3. use flask 
    -> app.route("/StandardScaler/") this is a url part of local host

4. define a function scaler()

5. return result

6. then run the app.py
    follow this command
        -> python scaler.py

7. after run we see a localhost address like http://127.0.0.1:5000
    -> press ctrl and click on this address for excute

8. and update url with http://127.0.0.1:5000/StandardScaler

9. Done