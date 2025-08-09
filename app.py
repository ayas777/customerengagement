# Save the streamlit app code to a file
streamlit_code = """
import streamlit as st
import pandas as pd
import joblib
import os # Import os to check file existence

# -----------------------------------------------------------
# Pastikan file 'customer_engagement_model_pipeline.pkl'
# berada di direktori yang sama dengan 'app.py' ini.
# -----------------------------------------------------------

# Judul Aplikasi
st.title('Prediksi Customer Engagement')
st.write('Aplikasi ini memprediksi apakah seorang pelanggan akan engaged ("Yes") atau tidak ("No") berdasarkan data input.')

# Menentukan path ke file model
model_path = 'customer_engagement_model_pipeline.pkl'

# Memuat model pipeline yang telah disimpan
try:
    # Cek apakah file model ada sebelum mencoba memuatnya
    if not os.path.exists(model_path):
        st.error(f"❌ File model '{model_path}' tidak ditemukan. Pastikan file tersebut ada di direktori yang sama.")
        st.stop() # Hentikan eksekusi Streamlit jika file tidak ada

    model = joblib.load(model_path)
    st.success("✅ Model berhasil dimuat.")
except Exception as e:
    st.error(f"❌ Terjadi kesalahan saat memuat model: {e}")
    st.stop() # Hentikan eksekusi Streamlit jika terjadi kesalahan

# --- Input Fitur dari Pengguna ---
st.header("Input Data Pelanggan")

# Input fitur numerik
age = st.number_input('Age', min_value=18, max_value=100, value=25)
family_size = st.number_input('Family size', min_value=1, max_value=10, value=3)

# Input fitur kategorikal
gender = st.selectbox('Gender', ['Female', 'Male'])
marital_status = st.selectbox('Marital Status', ['Single', 'Married', 'Divorced'])
occupation = st.selectbox('Occupation', ['Student', 'Employee', 'Self Employed', 'House wife', 'Unemployed'])
monthly_income = st.selectbox('Monthly Income', ['No Income', 'Below Rs.10000', '10001 to 25000', '25001 to 50000', 'More than 50000'])
educational_qualifications = st.selectbox('Educational Qualifications', ['Post Graduate', 'Graduate', 'School'])

# Tombol untuk melakukan prediksi
if st.button('Prediksi'):
    # Membuat DataFrame dari input pengguna
    input_data = pd.DataFrame([{
        'Age': age,
        'Gender': gender,
        'Marital Status': marital_status,
        'Occupation': occupation,
        'Monthly Income': monthly_income,
        'Educational Qualifications': educational_qualifications,
        'Family size': family_size,
    }])

    # Menghilangkan kolom yang tidak relevan (sesuai yang dihapus saat training)
    # Pastikan urutan dan nama kolom sesuai dengan data training
    # Meskipun kolom-kolom ini tidak diinput pengguna, ColumnTransformer mengharapkan struktur kolom yang konsisten.
    # Kita akan membuat placeholder untuk kolom yang dihapus jika diperlukan oleh preprocessor,
    # tapi dalam kasus ini, preprocessor hanya memproses kolom yang ada, jadi tidak perlu.

    # Melakukan prediksi menggunakan model yang sudah dilatih
    # Model pipeline akan menangani pra-pemrosesan secara otomatis
    try:
        prediction = model.predict(input_data)

        # Menerjemahkan hasil prediksi (0 atau 1) ke label aslinya ('No' atau 'Yes')
        # LabelEncoder saat training meng-encode 'No' menjadi 0 dan 'Yes' menjadi 1
        # Kita perlu memastikan urutan mapping ini
        # Jika Anda menggunakan LabelEncoder seperti di sel sebelumnya, 0 -> 'No', 1 -> 'Yes'
        result = "Yes" if prediction[0] == 1 else "No"

        if result == "Yes":
            st.success(f"✅ Prediksi: Pelanggan ini kemungkinan akan engaged ({result}).")
        else:
            st.info(f"🔵 Prediksi: Pelanggan ini kemungkinan tidak akan engaged ({result}).")

        st.write("---")
        st.subheader("Data Input Anda:")
        st.dataframe(input_data)

    except Exception as e:
        st.error(f"❌ Terjadi kesalahan saat melakukan prediksi: {e}")
"""
# Write the code to a file named app.py
with open('app.py', 'w') as f:
    f.write(streamlit_code)

print("✅ Kode Streamlit berhasil disimpan sebagai 'app.py'.")
print("Sekarang Anda bisa menjalankan aplikasi ini.")