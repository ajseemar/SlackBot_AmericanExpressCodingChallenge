from flask import Flask, request, jsonify, abort
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World from Flask App'

@app.route('/parse', methods=["POST"])
def parse():
    # token = request.form.get('token', None)  # TODO: validate the token

    text = request.form.get('text', None).split(" ")
    if len(text) != 3:
        image_url = "https://pbs.twimg.com/media/CuLpTqtWYAIiu1l.jpg"
        attachments = [{"title": "", "image_url": image_url}]
        payload = {
            'response_type': 'in_channel',
            'text': 'Please enter the command followed by: url html_tag class_or_id_attribute',
            'attachments': attachments
        }

        return jsonify(payload)

    url = text[0]
    tag = text[1]
    class_or_id = text[2].split("=")

    source = urlopen(url)
    soup = BeautifulSoup(source, 'lxml')

    if class_or_id[0] == 'class':
        element = soup.find(tag, class_=class_or_id[1])
    else:
        element = soup.select("#{}".format(class_or_id[1]))[0]

    # image_url = element['src']
    image_url = urljoin(url, element['src'])
    attachments = [{"title": "", "image_url": image_url}]
    payload = {
        'response_type': 'in_channel',
        'text': '',
        'attachments': attachments
    }
    return jsonify(payload)


if __name__ == '__main__':
    app.run()