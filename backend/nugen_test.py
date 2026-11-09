import os
import httpx
from dotenv import load_dotenv

load_dotenv()  # reads NUGEN_API_KEY from a .env file next to this script

r = httpx.post(
    "https://api.nugen.in/api/v3/inference/chat/completions",
    headers={"Authorization": f"Bearer {os.environ['NUGEN_API_KEY']}"},
    json={
        "model": "model_01m6etmmhvzxbm41",
        "messages": [
            {"role": "system", "content": "You are an ESG report writer for data centres."},
            {"role": "user", "content": "Say hello in one sentence."},
        ],
        "max_tokens": 200,
        "temperature": 1,
        "stream": False,
    },
    timeout=60,
)
print(r.status_code)
print(r.text)
