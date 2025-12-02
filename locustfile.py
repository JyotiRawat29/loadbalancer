from locust import HttpUser, task, between
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class FastAPILoadTest(HttpUser):
    """
    Load test for FastAPI hello endpoint
    Target: 1 Million requests in 1 hour (~278 RPS)
    """
    
    # Wait time between requests per user
    # With 278 users and ~1 second wait, we get ~278 RPS
    wait_time = between(0.5, 1.5)
    
    @task
    def test_hello_endpoint(self):
        """Test the root endpoint"""
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                try:
                    json_response = response.json()
                    if json_response.get("message") == "hello is it working":
                        response.success()
                    else:
                        response.failure(f"Unexpected message: {json_response}")
                except Exception as e:
                    response.failure(f"Failed to parse JSON: {e}")
            else:
                response.failure(f"Got status code {response.status_code}")
    
    def on_start(self):
        """Called when a user starts"""
        logging.info("User started")
    
    def on_stop(self):
        """Called when a user stops"""
        logging.info("User stopped")


# To run this:
# 
# 1. Install locust:
#    pip install locust
#
# 2. Run with UI:
#    locust -f locustfile.py
#    Then open http://localhost:8089
#    Set users=278, spawn rate=10, host=http://localhost:8000
#
# 3. Run headless (1 million requests in 1 hour):
#    locust -f locustfile.py --headless --users 278 --spawn-rate 10 \
#           --run-time 1h --host http://localhost:8000
#
# 4. Run with custom RPS (alternative calculation):
#    locust -f locustfile.py --headless --users 100 --spawn-rate 10 \
#           --run-time 1h --host http://localhost:8000
#    (Adjust wait_time to control actual RPS)