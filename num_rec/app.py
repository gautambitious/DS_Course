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
        a = np.mean((np.array(im, dtype=np.uint8) * 255), axis=2)
        model = load_model('model.h5')
        res = int(model.predict(np.array([a])).argmax())
        # conn = psycopg2.connect(database="paintmyown", user = "nidhin") cur = conn.cursor() cur.execute("INSERT
        # INTO files (name, data, canvas_image) VALUES (%s, %s, %s)", [filename, data, canvas_image]) conn.commit()
        # conn.close()
        return render_template('result.htm', res=str(res))
    return render_template("paint.html")


if __name__ == '__main__':
    app.run(debug=True, port=3004)
