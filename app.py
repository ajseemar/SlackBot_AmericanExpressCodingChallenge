from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World from Flask App'

@app.route('/parse-bot', methods=["POST"])
def parse():
    token = request.form.get('token', None)  # TODO: validate the token
    if token != os.environ.get('SLACK_BOT_TOKEN'):
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

    return {
		"type": "image",
		"title": {
			"type": "plain_text",
			"text": "Example Image",
			"emoji": true
		},
		"image_url": "https://image.shutterstock.com/image-photo/funny-cat-ophthalmologist-appointmet-squinting-260nw-598805597.jpg",
		"alt_text": "Example Image"
	}

    # return 'Responding to slash command...'
    # return 'Retrieving requested HTML content...'




if __name__ == '__main__':
    app.run()