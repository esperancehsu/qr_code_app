from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__, template_folder='themes')

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_image = None

    if request.method == 'POST':
        data = request.form['data']
        fill = request.form.get('fill', 'black')
        back = request.form.get('back', 'white')

        qr = qrcode.QRCode(version=3, box_size=8, border=4)
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill, back_color=back)

        # Convertir en image affichable sans sauvegarde
        buf = BytesIO()
        img.save(buf, 'PNG')
        buf.seek(0)

        return send_file(buf, mimetype='image/png')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
