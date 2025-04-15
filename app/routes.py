from flask import render_template, request, redirect
from app import app
import redis
import string
import os
import random

SHORT_URL_LEN = 6
EXPIRY_SECONDS = 30 * 24 * 60 * 60
redis_password = os.environ.get("REDIS_PASSWORD")

redis_short_to_long = redis.StrictRedis(
    host=os.environ.get("REDIS_HOST", "redis"),
    port=int(os.environ.get("REDIS_PORT", 6379)),
    db=0,
    password=redis_password,
    decode_responses=True
)

redis_long_to_short = redis.StrictRedis(
    host=os.environ.get("REDIS_HOST", "redis"),
    port=int(os.environ.get("REDIS_PORT", 6379)),
    db=1,
    password=redis_password,
    decode_responses=True
)

def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(SHORT_URL_LEN))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        existing_short = redis_long_to_short.get(original_url)
        if existing_short:
            return render_template('index.html', short_url=existing_short, host_url=request.host_url)
        short_url = generate_short_url()
        while redis_short_to_long.exists(short_url):
            short_url = generate_short_url()
        redis_short_to_long.setex(short_url, EXPIRY_SECONDS, original_url)
        redis_long_to_short.setex(original_url, EXPIRY_SECONDS, short_url)
        return render_template('index.html', short_url=short_url, host_url=request.host_url)
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_original_url(short_url):
    original_url = redis_short_to_long.get(short_url)
    if original_url:
        return redirect(original_url)
    else:
        return "Short URL not found", 404
