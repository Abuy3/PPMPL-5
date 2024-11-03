import random
from locust import HttpUser, task, between

class LoadTestUser(HttpUser):
    wait_time = between(1, 3)  # Waktu tunggu antara setiap task (1-3 detik)
    
    @task(3)
    def get_users_list(self):
        # Mengakses endpoint GET /users
        self.client.get("/users")
    
    @task(2)
    def get_specific_user(self):
        # Mengakses endpoint GET /users/{id} dengan ID acak antara 1-3
        user_id = random.randint(1, 3)
        self.client.get(f"/users/{user_id}")
    
    @task(1)
    def create_user(self):
        # Mengakses endpoint POST /users
        self.client.post("/users")
    
    @task(1)
    def heavy_operation(self):
        # Mengakses endpoint GET /heavy
        self.client.get("/heavy")
    
    
    @task(4)
    def get_root(self):
        # Mengakses endpoint GET /
        self.client.get("/")