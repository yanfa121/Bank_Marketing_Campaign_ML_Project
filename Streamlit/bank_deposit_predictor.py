import streamlit as st
import pandas as pd
import joblib
import numpy as np
from datetime import datetime

# Konfigurasi halaman
st.set_page_config(
    page_title="Prediksi Deposito Bank",
    page_icon="🏦",
    layout="wide"
)

# Load model
@st.cache_resource
def load_model():
    try:
        model = joblib.load('bestmodel.mdl')
        return model
    except FileNotFoundError:
        st.error("Model file 'bestmodel.mdl' tidak ditemukan. Pastikan file berada dalam direktori yang sama.")
        return None
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

# Definisi nilai-nilai kategorikal berdasarkan gambar
JOB_OPTIONS = ['admin.', 'self-employed', 'services', 'housemaid', 'technician', 
               'management', 'student', 'blue-collar', 'entrepreneur', 'retired', 
               'unemployed']

HOUSING_OPTIONS = ['no', 'yes']
LOAN_OPTIONS = ['no', 'yes']
CONTACT_OPTIONS = ['cellular', 'telephone']
MONTH_OPTIONS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

def main():
    st.title("🏦 Prediksi Deposito Bank")
    st.markdown("---")
    st.markdown("### Aplikasi untuk memprediksi kemungkinan nasabah membuka deposito")
    
    # Load model
    model = load_model()
    if model is None:
        return
    
    # Layout dalam kolom
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🧑🏻‍🤝‍🧑🏻 Data Demografi")
        
        # Age input
        age = st.slider(
            "Usia", 
            min_value=18, 
            max_value=95, 
            value=41, 
            help="Rentang usia: 18-95 tahun"
        )
        
        # Job selection
        job = st.selectbox(
            "Pekerjaan",
            options=JOB_OPTIONS,
            index=0,
            help="Pilih jenis pekerjaan nasabah"
        )
        
        # Housing loan
        housing = st.selectbox(
            "Kredit Rumah",
            options=HOUSING_OPTIONS,
            index=0,
            help="Apakah memiliki kredit rumah?"
        )
        
        # Personal loan
        loan = st.selectbox(
            "Pinjaman Personal",
            options=LOAN_OPTIONS,
            index=0,
            help="Apakah memiliki pinjaman personal?"
        )
    
    with col2:
        st.subheader("📞 Data Campaign")
        
        # Contact method
        contact = st.selectbox(
            "Metode Kontak",
            options=CONTACT_OPTIONS,
            index=0,
            help="Metode komunikasi yang digunakan"
        )
        
        # Month
        month = st.selectbox(
            "Bulan Kontak",
            options=MONTH_OPTIONS,
            index=0,
            help="Bulan terakhir dihubungi"
        )
        
        # Balance
        balance = st.number_input(
            "Saldo Rekening",
            min_value=-6847.0,
            max_value=29340.0,
            value=1457.0,
            step=100.0,
            help="Saldo rata-rata tahunan (dalam euro)"
        )
        
        # Campaign
        campaign = st.number_input(
            "Jumlah Kontak Campaign",
            min_value=1,
            max_value=30,
            value=3,
            step=1,
            help="Jumlah kontak yang dilakukan selama campaign ini"
        )
        
        # Previous days
        pdays = st.number_input(
            "Hari Sejak Kontak Terakhir",
            min_value=-1,
            max_value=450,
            value=48,
            step=1,
            help="Jumlah hari yang berlalu setelah klien terakhir dihubungi (-1 = belum pernah dihubungi)"
        )
    
    st.markdown("---")
    
    # Predict button
    if st.button("🔎 Prediksi Kemungkinan Deposito", type="primary"):
        try:
            # Prepare data for prediction
            input_data = pd.DataFrame({
                'age': [age],
                'job': [job],
                'housing': [housing],
                'loan': [loan],
                'contact': [contact],
                'month': [month],
                'balance': [balance],
                'campaign': [campaign],
                'pdays': [pdays]
            })
            
            # Make prediction
            prediction = model.predict(input_data)
            prediction_proba = model.predict_proba(input_data)
            
            # Display results
            st.markdown("## 📈 Hasil Prediksi")
            
            col3, col4 = st.columns(2)
            
            with col3:
                if prediction[0] == 1:
                    st.success("### ✅ AKAN MEMBUKA DEPOSITO")
                    st.balloons()
                else:
                    st.error("### ❌ TIDAK AKAN MEMBUKA DEPOSITO")
            
            with col4:
                prob_no = prediction_proba[0][0] * 100
                prob_yes = prediction_proba[0][1] * 100
                
                st.metric("Probabilitas TIDAK", f"{prob_no:.1f}%")
                st.metric("Probabilitas YA", f"{prob_yes:.1f}%")
            
            # Progress bar untuk visualisasi probabilitas
            st.markdown("### 📊 Tingkat Kepercayaan")
            st.progress(prob_yes/100, text=f"Kemungkinan membuka deposito: {prob_yes:.1f}%")
            
            # Interpretasi hasil
            st.markdown("### 💡 Interpretasi")
            if prob_yes >= 70:
                st.info("🎯 **Prioritas Tinggi**: Nasabah ini sangat potensial untuk membuka deposito!")
            elif prob_yes >= 50:
                st.warning("⚡ **Prioritas Sedang**: Nasabah ini cukup potensial, perlu pendekatan yang tepat.")
            else:
                st.error("📋 **Prioritas Rendah**: Nasabah ini kurang potensial untuk membuka deposito.")
                
        except Exception as e:
            st.error(f"Error dalam prediksi: {str(e)}")
            st.info("Pastikan model telah dilatih dengan kolom yang sesuai.")
    
    # Informasi tambahan
    with st.expander("ℹ️ Informasi Model"):
        st.markdown("""
        **Model**: LightGBM Classifier
        
        **Target Prediksi**:
        - Nasabah kemungkinan akan membuka deposito
        - Nasabah kemungkinan tidak akan membuka deposito
        
        **Fitur yang Digunakan**:
        - Age: Usia nasabah
        - Job: Jenis pekerjaan
        - Housing: Status kredit rumah
        - Loan: Status pinjaman personal
        - Contact: Metode kontak
        - Month: Bulan kontak terakhir
        - Balance: Saldo rekening rata-rata
        - Campaign: Jumlah kontak campaign
        - Pdays: Hari sejak kontak terakhir
        """)

if __name__ == "__main__":
    main()