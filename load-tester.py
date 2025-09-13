import requests
import time
import threading

BASE_URL = "http://127.0.0.1:8000"
NUM_THREADS = 20  # number of parallel threads
CLICKS = 100
DELAY = 0.1  # seconds between clicks (per thread)


def send_click():
    try:
        res = requests.post(f"{BASE_URL}/click")
        if res.status_code == 200:
            data = res.json()
            print(f"Click successful! Current count = {data['count']}")
        else:
            print(f"Error: {res.status_code}")
    except Exception as e:
        print("Request failed:", e)


def worker():
    while True:
        for i in range(CLICKS):
            send_click()
        time.sleep(DELAY)


threads = []
for i in range(NUM_THREADS):
    t = threading.Thread(target=worker, daemon=True)
    threads.append(t)
    t.start()

print(f"🚀 Started {NUM_THREADS} threads sending requests every {DELAY}s.")
print("Press Ctrl+C to stop.\n")

# Keep main thread alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n Stopped.")
