import os
import base64
from io import BytesIO
from flask import Flask, render_template, request, redirect, url_for
from flask_httpauth import HTTPBasicAuth
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

app = Flask(__name__)
APP_SETTINGS = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
app.config.from_object(APP_SETTINGS)

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    u = os.getenv('BASICAUTH_USERNAME', 'novelapp')
    p = os.getenv('BASICAUTH_PASSWORD', 'novels')
    return username == u and password == p


@app.route('/')
@auth.login_required
def index():
    # local = {}
    # return render_template('./index.html', local=local)
    return redirect(url_for('category'))


@app.route('/category', methods=['GET', 'POST'])
def category():
    local = {
        'predicted': False
    }

    if request.files.get('image'):
        file = request.files['image']
        local['file'] = file

        content = file.read()
        local['file_base64'] = str(base64.b64encode(content), 'utf-8')

        model = load_model('etc/model/category-2.h5', compile=False)

        img = Image.open(BytesIO(content))
        img_resize = img.resize((229, 229))
        img_np = np.asarray(img_resize) / 255.0
        img_reshape = img_np.reshape(1, 229, 229, 3)

        x = img_reshape
        y = np.argmax(model.predict(x))
        y_proba = model.predict_proba(x)
        y_proba = np.round((y_proba[0] * 100), 5)

        local['predicted'] = True
        local['y'] = y
        local['y_proba'] = y_proba

        print(y, y_proba)

    return render_template('./category.html', local=local)


if __name__ == '__main__':
    print('Config:', APP_SETTINGS)
    app.run()

