from flask import Flask, request, jsonify, abort
import os
# from config import VERIFICATION_TOKEN as VT
import pdb

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World from Flask App'

@app.route('/parse', methods=["POST"])
def parse():
    token = request.form.get('token', None)  # TODO: validate the token
    print('token: {}'.format(token))
    # pdb.set_trace()
    # if token != VT:
    #     print('invalid token')
    #     return
    command = request.form.get('command', None)
    text = request.form.get('text', None)
    print("command: {}".format(command))
    print("text: {}".format(text))
    print()
    print(request.form)
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
    image_url = "https://api.slack.com/img/blocks/bkb_template_images/beagle.png"
    attachments = [{"title": "", "image_url": image_url}]
    
    payload = {
		"type": "image",
		"title": {
			"type": "plain_text",
			"text": "image1",
			"emoji": True
		},
		"image_url": "https://api.slack.com/img/blocks/bkb_template_images/beagle.png",
		"alt_text": "image1"
	}

    payload = {
        'response_type': 'in_channel',
        'text': '',
        'attachments': attachments
    }
    return jsonify(payload)

    # return 'Responding to slash command...'
    # return 'Retrieving requested HTML content...'


if __name__ == '__main__':
    app.run()