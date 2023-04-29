# IDS721 Group-Final-Project India Population Predictor

In this project, we used regression model and imported dataset from kaggle to train it. We used Flask to build a light-weight web framework to predict the future population in China. And then we deploy our service in GCP and used locust to load test it.


## Architecture
![image](https://github.com/xyli1233/721_final_project/blob/main/static/css/5.png) 

   




## How to Run the App

1) Clone the repo

```bash
git@https://github.com/xyli1233/721_final_project.git
```

2) Create & enter python virtual environment

```bash
# first cd to the project directory
# create virtual environment
python -m venv env

# enter the virtual environment
source env/bin/activate
```

3) Setup - Install the required packages

```bash
make all
```

4) Train the model

```bash
python model.py
```

5) Run the application

```bash
python main.py
```

The dataset is from https://www.kaggle.com/datasets/anandhuh/population-data-india

## Containerization

```bash
# create image
docker build -t population-predictor:latest .

# create and run container
docker run --rm -p 5000:5000 --name population-predictor-app population-predictor:latest
```

Now you can access service on http://127.0.0.1:5000/

## Set up on GCP

1. Create a new project and check if the project correct and set working project if not. In this step you need to record the <PROJECT-ID>, which will be used in next steps:

   ```
   gcloud projects describe $GOOGLE_CLOUD_PROJECT
   ```

   ```
   gcloud config set project $GOOGLE_CLOUD_PROJECT 
   ```

2.  Paste command below on the GCP shell:

   ```
   git clone git@github.com/xyli1233/721_final_project.git
   ```

3. In the project folder, build the containerized flask application image:

   ~~~
   gcloud builds submit --tag gcr.io/<PROJECT-ID>/app 
   ~~~

4.  Last step, deploy the image on the cloud run service:

   ``` 
   gcloud run deploy --image gcr.io/<PROJECT-ID>/app --platform managed
   ```

   And you will need to name your service and select region you want to deploy. 

   

   Lastly, you can see the service running on the given URL: https://ids721-2jiswkh77q-ue.a.run.app

 
![image](https://github.com/xyli1233/721_final_project/blob/main/static/css/1.png) 
![image](https://github.com/xyli1233/721_final_project/blob/main/static/css/2.png) 

   


## Load Testing

I used https://locust.io/ to start load testing for the flask project. 

1. Download locust

   ```
   pip3 install locust
   ```

2. Write locustfile.py:

   ```
   import time
   from locust import HttpUser, task, between
   
   class QuickstartUser(HttpUser):
   
       @task
       def submitForm(self):
           self.client.post("/predict", {"Year":"2024"})
   ```

3. Run "locust". Once you’ve started Locust, open up a browser and point it to [http://localhost:8089](http://localhost:8089/). You will be greeted with something like this:

![image](https://github.com/xyli1233/721_final_project/blob/main/static/css/3.png) 

4. Here is our test result. 

![image](https://github.com/xyli1233/721_final_project/blob/main/static/css/4.png)
