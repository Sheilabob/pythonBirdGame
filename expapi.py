import requests
# from requests_toolbelt.utils import dump
import json
import playsound

birdsounds_url = "https://www.xeno-canto.org/api/2/recordings?query=bearded+bellbird+q:A"
birdsounds_api = requests.get(birdsounds_url)
# print(birdsounds_api)

# data = dump.dump_all(birdsounds_api)
# print(data.decode('utf-8'))

birdsounds_json = json.loads(birdsounds_api.content)
# print(birdsounds_json)

# print(birdsounds_api.headers["Content-Type"])
# print(birdsounds_api.content)

for recording in birdsounds_json['recordings']:
    location = recording['cnt']
    name = recording['en']
    sound = recording['url']
    print(f"Name:\t{name}")
    print(f"Location:\t{location}")
    print(f"Sound:\t{sound}")
    print()
print(birdsounds_json['recordings'][0]['url'])
print(birdsounds_json['recordings'][0]['file-name'])


# playsound('https://xeno-canto.org/680642/download')
