from flask import Flask, request, jsonify, abort
import os
# from config import VERIFICATION_TOKEN as VT
import pdb

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World from Flask App'

@app.route('/parse-bot', methods=["POST"])
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

    payload = {
		"type": "image",
		"title": {
			"type": "plain_text",
			"text": "Example Image",
			"emoji": True
		},
		"image_url": "https://image.shutterstock.com/image-photo/funny-cat-ophthalmologist-appointmet-squinting-260nw-598805597.jpg",
		"alt_text": "Example Image"
	}

    payload = {
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": "This is a mrkdwn section block :ghost: *this is bold*, and ~this is crossed out~, and <https://google.com|this is a link>"
		}
	}
    
    return jsonify(payload)

    # return 'Responding to slash command...'
    # return 'Retrieving requested HTML content...'


if __name__ == '__main__':
    app.run()