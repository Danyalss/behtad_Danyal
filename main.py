import threading
import requests

# Global counter for successful sends
i = 0

# Lock for thread-safe incrementing of counter
lock = threading.Lock()

def send(url):
    global i
    try:
        response = requests.get(url)
        with lock:
            i += 1
            print(f'send {i}')
    except Exception as e:
        print(e)

threads = []

for ai in range(100):
    thread = threading.Thread(target=send, args=('https://send.loyojif372.workers.dev',))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads completed")
