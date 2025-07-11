import requests
from decouple import config

SUPABASE_URL = config('SUPABASE_URL')
SUPABASE_API_KEY = config('SUPABASE_API_KEY')
BUCKET = 'media'

def upload_file_to_supabase(filename, file_bytes):
    url = f"{SUPABASE_URL}/storage/v1/object/{BUCKET}/{filename}"
    headers = {
        "apikey": SUPABASE_API_KEY,
        "Authorization": f"Bearer {SUPABASE_API_KEY}",
        "Content-Type": "application/octet-stream",
    }
    response = requests.put(url, headers=headers, data=file_bytes)
    if response.status_code == 200:
        return f"{SUPABASE_URL}/storage/v1/object/public/{BUCKET}/{filename}"
    else:
        raise Exception(f"Erro ao enviar arquivo: {response.text}")
