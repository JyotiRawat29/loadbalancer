from locust import HttpUser, task, between

# 1Million request in 1 hour = 1000000/3600 = 278 Request per second(RPS)
class FastAPIUser(HttpUser):
    wait_time = between(1, 2)  # Wait 1-2 seconds between requests
    
    @task
    def hello_endpoint(self):
        self.client.get("/")

# For exactly 278 RPS, calculate:
# If 278 concurrent users with no wait time = 278 RPS
# OR fewer users with shorter wait times