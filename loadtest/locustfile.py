import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):

    @task
    def submitForm(self):
        self.client.post("/predict", {"Year":"2024"})
