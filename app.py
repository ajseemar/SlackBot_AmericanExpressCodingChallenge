from flask import Flask, request, jsonify, abort
import os
# from config import VERIFICATION_TOKEN as VT
import pdb
from bs4 import BeautifulSoup
import requests
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World from Flask App'

@app.route('/parse', methods=["POST"])
def parse():
    # token = request.form.get('token', None)  # TODO: validate the token
    # print('token: {}'.format(token))
    # pdb.set_trace()
    # if token != VT:
    #     print('invalid token')
    #     return
    # command = request.form.get('command', None)
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

    website = text[0]
    tag = text[1]
    class_or_id = text[2].split("=")

    # source = requests.get(website).text
    source = urllib.request.urlopen(website)
    soup = BeautifulSoup(source, 'lxml')

    if class_or_id[0] == 'class':
        element = soup.find(tag, class_=class_or_id[1])
    else:
        element = soup.find(tag, id=class_or_id[1])

    if tag == 'img':
        image_url = element.src
        attachments = [{"title": "", "image_url": image_url}]
        payload = {
            'response_type': 'in_channel',
            'text': '',
            'attachments': attachments
        }
        return jsonify(payload)
    else:
        msg = element.text
        payload = {
            'response_type': 'in_channel',
            'text': msg,
        }
        return jsonify(payload)

    # print("command: {}".format(command))
    # print("text: {}".format(text))
    # print()
    # print(request.form)
    # return {
	# 	"type": "section",
	# 	"text": {
	# 		"type": "mrkdwn",
	# 		"text": "Take a look at this image."
	# 	},
	# 	"accessory": {
	# 		"type": "image",
	# 		"image_url": "https://image.shutterstock.com/image-photo/funny-cat-ophthalmologist-appointmet-squinting-260nw-598805597.jpg",
	# 		"alt_text": "palm tree"
	# 	}
	# }
    
    
    # payload = {
	# 	"type": "image",
	# 	"title": {
	# 		"type": "plain_text",
	# 		"text": "image1",
	# 		"emoji": True
	# 	},
	# 	"image_url": "https://api.slack.com/img/blocks/bkb_template_images/beagle.png",
	# 	"alt_text": "image1"
	# }

    

    # return 'Responding to slash command...'
    # return 'Retrieving requested HTML content...'


if __name__ == '__main__':
    app.run()