from flask import Flask, request
from handleImage import handle
from flask_cors import CORS
from PIL import Image
from datetime import datetime
import base64
import collections
from io import BytesIO
app = Flask(__name__)
CORS(app)

@app.route('/')
def catch_all():
    return app.send_static_file("main.html")


@app.route('/api/image', methods=['POST'])
def handle_image():
    # if datetime.now().hour > 22 or datetime.now().hour < 7:
    #     return None
    content = request.get_json().get('body')
    thickness = content.get('width')
    colors = content.get('colors')
    image = content.get('image')
    shadow_size = content.get('shadowSize')

    textpadder = image[:image.find(',') + 1]
    image = image[image.find(',')+1:]
    image = Image.open(BytesIO(base64.b64decode(image)))

    colors = {float(k):v for k,v in colors.items()}
    colors = collections.OrderedDict(sorted(colors.items())) # order the dict by the key

    result = handle(image, colors, thickness, shadow_size)

    buffer = BytesIO()
    image_format = textpadder[textpadder.find('/')+1:textpadder.find(';')]
    result.save(buffer, format=image_format)  # Enregistre l'image dans le buffer
    myimage = buffer.getvalue()
    result = textpadder + base64.b64encode(myimage).decode("utf-8")
    return result


def start_server():
    app.run(port=5001, host='0.0.0.0')


if __name__ == "__main__":
    start_server()
