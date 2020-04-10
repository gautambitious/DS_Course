import base64
from io import BytesIO
from tensorflow.keras.models import load_model
from flask import Flask, render_template, request, flash, url_for, redirect
from PIL import Image
import re
import numpy as np

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def paintapp():
    if request.method == 'POST':
        # filename = request.form['save_fname']
        data = request.form
        print(data)
        image_data = re.sub('^data:image/.+;base64,', '', data['img'])
        im = Image.open(BytesIO(base64.b64decode(image_data))).resize(size=(28, 28))
        a = np.mean((np.array(im, dtype=np.uint8) * 255), axis=2)*4
        model = load_model('model.h5')
        res = int(model.predict(np.array([a])).argmax())
        print('res=', res)
        return okay(res)
    return render_template("paint.html")


def okay(res):
    return render_template('result.htm', res=str(res))


if __name__ == '__main__':
    app.run(debug=True, port=3004)
