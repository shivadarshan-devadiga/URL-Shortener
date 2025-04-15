import requests
from bs4 import BeautifulSoup
import random
import string
import time
import threading
import os

url_shortener_url='http://url-shortener.local/'

def generate_random_url():
    domain='http://longurl.com/'
    path=''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return domain+path

def simulate_user(user_id, num_requests):
    print(f"User {user_id} started")
    for _ in range(num_requests):
        long_url = generate_random_url()
        data = {'url': long_url}
        headers = {
            'User-Agent': random.choice([
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0',
                'Mozilla/5.0 (Linux; Android 10; Pixel 4 XL Build/QD3A.200805.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36'
            ])
        }
        try:
            response = requests.post(url_shortener_url, data=data, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                short_url_tag = soup.find('a', href=True)
                if short_url_tag:
                    print(f"User {user_id} => Long URL: {long_url} => Short URL: {short_url_tag['href']}")
                else:
                    print(f"User {user_id} => No short URL found for {long_url}")
            else:
                print(f"User {user_id} => Failed to shorten URL: {long_url}")
        except requests.exceptions.RequestException as e:
            print(f"User {user_id} => Error: {e}")

        time.sleep(random.uniform(0.5, 2.0))
    print(f"User {user_id} finished")

def run_stress_test(num_users, num_requests_per_user):
    threads = []
    for user_id in range(1, num_users + 1):
        thread = threading.Thread(target=simulate_user, args=(user_id, num_requests_per_user))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

num_users = 200
num_requests_per_user = 100
run_stress_test(num_users, num_requests_per_user)
