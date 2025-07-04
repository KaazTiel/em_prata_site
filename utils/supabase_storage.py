import requests

SUPABASE_URL = 'https://sskzbcnauqrvimqoplre.supabase.co'
SUPABASE_API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNza3piY25hdXFydmltcW9wbHJlIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MTUwMDMxNywiZXhwIjoyMDY3MDc2MzE3fQ.U_VF9Xj9jEYXeTOyDiEMs4zoyzxpnkb-hABTRPmKbYM'  # coloque a real aqui
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
