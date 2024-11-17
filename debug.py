from googleapiclient.discovery import build

def list_services():
    service = build('discovery', 'v1')
    apis = service.apis().list().execute()
    for api in apis['items']:
        print(f"API: {api['name']}, Version: {api['version']}")

list_services()
