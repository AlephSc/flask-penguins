from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model yang sudah dilatih
with open('model_penguin_knn.pickle', 'rb') as file:
    model = pickle.load(file)

# Halaman utama (Menampilkan Form HTML)
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint untuk memproses data dari form
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Mengambil input dari form HTML
        bill_len = float(request.form['bill_length_mm'])
        bill_dep = float(request.form['bill_depth_mm'])
        flip_len = float(request.form['flipper_length_mm'])
        body_mass = float(request.form['body_mass_g'])
        
        # Menyusun data sesuai format yang diminta model (Array 2D)
        input_data = np.array([[bill_len, bill_dep, flip_len, body_mass]])
        
        # Melakukan prediksi
        hasil_prediksi = model.predict(input_data)
        spesies = hasil_prediksi[0] # Mengambil hasil pertama (Adelie, Chinstrap, atau Gentoo)
        
        # Mengembalikan hasil ke halaman HTML
        return render_template('index.html', hasil=spesies)

if __name__ == '__main__':
    # Menjalankan server dalam mode debug
    app.run(debug=True)