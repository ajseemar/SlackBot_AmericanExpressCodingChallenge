from flask import Flask, request, jsonify, abort
import os
from config import VERIFICATION_TOKEN as VT
import pdb

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World from Flask App'

@app.route('/parse-bot', methods=["POST"])
def parse():
    token = request.form.get('token', None)  # TODO: validate the token
    pdb.set_trace()
    if token != VT:
        print('invalid token')
        return
    command = request.form.get('command', None)
    text = request.form.get('text', None)
    print(command)
    print(text)
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
    payload = {'text': 'DigitalOcean Slack slash command is successful!'}
    return jsonify(payload)

    # return 'Responding to slash command...'
    # return 'Retrieving requested HTML content...'



def slash_command():
    """Parse the command parameters, validate them, and respond.
    Note: This URL must support HTTPS and serve a valid SSL certificate.
    """
    # Parse the parameters you need
    token = request.form.get('token', None)  # TODO: validate the token
    command = request.form.get('command', None)
    text = request.form.get('text', None)
    print(command)
    print(text)
    # Validate the request parameters
    if not token:  # or some other failure condition
        abort(400)
    # Use one of the following return statements
    # 1. Return plain text
    return 'Simple plain response to the slash command received'
    # 2. Return a JSON payload
    # See https://api.slack.com/docs/formatting and
    # https://api.slack.com/docs/attachments to send richly formatted messages
    return jsonify({
        # Uncomment the line below for the response to be visible to everyone
        # 'response_type': 'in_channel',
        'text': 'More fleshed out response to the slash command',
        'attachments': [
            {
                'fallback': 'Required plain-text summary of the attachment.',
                'color': '#36a64f',
                'pretext': 'Optional text above the attachment block',
                'author_name': 'Bobby Tables',
                'author_link': 'http://flickr.com/bobby/',
                'author_icon': 'http://flickr.com/icons/bobby.jpg',
                'title': 'Slack API Documentation',
                'title_link': 'https://api.slack.com/',
                'text': 'Optional text that appears within the attachment',
                'fields': [
                    {
                        'title': 'Priority',
                        'value': 'High',
                        'short': False
                    }
                ],
                'image_url': 'http://my-website.com/path/to/image.jpg',
                'thumb_url': 'http://example.com/path/to/thumb.png'
            }
        ]
    })





if __name__ == '__main__':
    app.run()