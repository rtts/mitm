from flask import Flask, request, make_response
import requests

TARGET = 'https://accounts.google.com/'

app = Flask(__name__, static_folder=None)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def proxy(path):
    if request.method == 'GET':
        r = requests.get(TARGET + path, cookies=request.cookies)

    if request.method == 'POST':
        s = request.headers['Referer']
        referer = TARGET + s.split('//', maxsplit=1)[1].split('/', maxsplit=1)[1]
        headers = {
            'Origin': request.headers['Origin'],
            'Content-Type': request.headers['Content-Type'],
            'Referer': referer,
        }
        r = requests.post(TARGET + path, data=request.form, headers=headers, cookies=request.cookies)

    response = make_response(r.content, r.status_code)
    for key, value in r.cookies.items():
        response.set_cookie(key, value)
    response.headers['Content-Type'] = r.headers['Content-Type']
    return response
