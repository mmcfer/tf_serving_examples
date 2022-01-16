import requests
import os
import io
import json
direc=os.path.dirname(os.path.realpath(__file__))


print(direc)

url=  'http://localhost:8501/v1/models/resnet:predict'



image = os.path.join(direc, 'example.png')

with open(image, "rb") as image_file:
    file_bytes = image_file.read()
    data = dict(
        file=(io.BytesIO(bytearray(file_bytes)), "example.png"),
    )
print(data)

headers = {'content-type': 'multipart/form-data', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=data, headers=headers)
print(r.text)