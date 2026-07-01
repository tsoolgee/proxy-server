import os
import requests
import json

def run_proxy():
    url = os.environ.get('TARGET_URL')
    if not url:
        print('No URL provided')
        return
    
    try:
        response = requests.get(url)
        print(f'Status: {response.status_code}')
        print(f'Content: {response.text[:500]}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    run_proxy()