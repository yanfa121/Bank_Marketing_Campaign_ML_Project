# Bank Marketing Campaign Machine Learning Model Prediction


## **1. Project Overview**

### **Business Understanding**
Sebuah perusahaan perbankan melakukan kampanye pemasaran untuk menawarkan berbagai produk keuangan salah satunya deposito. 
Untuk meningkatkan penjualan produk tersebut Bank melakukan kampanye pemasaran melalui kontak langsung kenasabah via telepon dan pesan, untuk mendapatkan nasabah baru.

Namun upaya upaya tesebut juga harus kita perhatikan untuk cost dan benefitnya, agar lebih efisien dan tepat sasaran maka diperlukan model Machine Learning
untuk memprediksi kandidat nasabah yang kemungkinan akan menggunakan produk ini dan melakukan deposito.

### **Analytical Approach**
Dengan data yang telah dimiliki, dapat digunakan untuk membuat model prediksi kandidat nasabah yang akan menggunakan produk hingga melakukan deposito, dengan membangun model klasifikasi. Dengan tujuan :
- Campaign Program yang lebih efisien dan tepat sasaran
- Meningkatkan efektivitas Campaign Program dengan cara menargetkan nasabah yang memiliki kemungkinan tinggi untuk menggunakan produk hingga melakukan deposito
- Mengoptimalkan budget yang diberikan untuk Campaign Program ini
- Meminimalisir biaya operasional dengan mengurangi jumlah panggilan yang tidak tepat sasaran


## **2. Data**
Data yang digunakan adalah dataset dari UCI Machine Learning Repository
- data_bank_marketing_campaign.csv


## **3. Tools yang Digunakan**
- Microsoft Visual Studio Code, Jupyter Notebook, Google Colab
- Programming Language : Python (Pandas, Numpy, Scikit-learn)
- Visualization        : Seaborn, Matplotlib
- App Builder          : Streamlit [(Bank Deposit Predictor)](https://bankdepositpredictorapp-yanfa121.streamlit.app/)
- Presentation Report  : Canva


## **4. Prerequisites**
Proses pengerjaan project ini menggunakan libraries dengan versi tertentu:
- Python 3.13.5
- NumPy 2.2.0
- Pandas 2.2.3
- Seaborn 0.13.2
- Matplotlib 3.10.0
- Scikit-learn 1.7.0
- Streamlit 1.49.1


## **5. Project Structure**
```
├── README.md                                 <- Guideline and overview of the entire project
├── Models
│   ├── Bank_Marketing_Campaign_ML.ipynb      <- Notebook for building this model
│   ├── bestmodel.mdl                         <- Saved model pipeline
│   ├── data_bank_marketing_campaign.csv      <- Raw data
│   |__ gridsearchtune13.hyp                  <- Saved best tuning for model
│
├── Reports
│   ├── Link_Video.txt                        <- Link video explanation
│   |__ Bank_Marketing_Campaign_PPT.pdf       <- Slide explanation
│
|__ Streamlit
│   ├── bank_deposit_predictor.py             <- Model app main file
│   ├── bestmodel.mdl                         <- Saved model pipeline
│   ├── Link_Streamlit.txt                    <- Streamlit app link
│   |__ requirements.txt                      <- Requierements version of library
```


## **6. Link**
App Deployment Repository : [github.com/yanfa121/Bank_Deposit_Predictor](https://github.com/yanfa121/Bank_Deposit_Predictor_Streamlit_App)

App Link : [Bank Deposit Predictor (Streamlit)](https://bankdepositpredictorapp-yanfa121.streamlit.app/)

Explanation Video : [Video Explanation]()

GDrive : [Link GDrive]()


## **7. Conclusion & Recommendation**
### **Conclusion**
Model akhir yang digunakan adalah LGBM (Light Gradient Boosting Machine) yang telah dilakukan tuning. Berdasarkan hasil akhir model yang dibandingkan dengan model sebelum tuning dan optimasi threshold, model ini dioptimasi untuk memaksimalkan recall kelas 1.

Yang artinya dengan model ini kita lebih memilih tidak melewatkan calon nasabah meskipun dengan resiko False Positive (salah mengontak orang yang akhirnya tidak deposit), karena meski demikian, biaya kehilangan nasabah potensial lebih besar daripada biaya menawarkan ke orang yang tidak tertarik.

Dengan penggunaan model ini, Bank bisa meningkatkan efektivitas karyawan, menghemat waktu, meminimalisir biaya yang dikeluarkan dan juga menambah profit walaupun hanya sedikit lebih baik dari semua prediksi menjadi 1 (semua nasabah ditelepon). Tetapi penggunaan model akan lebih membantu dalam penghematan waktu, tenaga dan juga biaya.

### **Recommendation**
1. Rekomendasi Bisnis
- Fokus untuk melakukan telepon kepada nasabah dengan probabilitas tinggi
- Buat segmentasi perlakuan nasabah, contoh :
    - Probabilitas Tinggi : telepon langsung
    - Probabilitas sedang : hubungi melalui email atau WA (lebih murah)
    - Probabilitas Rendah : bisa dipertimbangkan untuk tidak perlu dihubungi
- Melakukan evaluasi biaya secara berkala untuk memastikan model yang digunakan dapat memberikan keuntungan yang optimal, dengan menyesuaikan threshold berdasarkan perubahan biaya yang ada supaya  

2. Meningkatkan Performa Model
- Untuk meningkatkan performa model agar lebih baik bisa menambah beberapa fitur seperti Gaji, Jumlah Deposit yang sudah ada
- Menjelaskan nilai *unknown* lebih spesifik agar lebih reasonable dan bisa dijadikan treatment yang lebih tepat
- Update model dengan data terbaru di setiap batch Campaign Program, perubahan dalam data bisa mempengaruhi kinerja model. Dengan pemantuan berkala, model lebih bisa menyesuaikan dengan variasi data yang beragam

### **Harapan**
Dengan pembuatan model ini diharapkan Bank dapat mengoptimalkan Campaign Program dengan lebih cepat, efektif dan efisien
- Mengoptimalkan campaign program dengan target nasabah yang lebih terfokus sehingga mengurangi kontak yang tidak efektif
- Meminimalisir waktu dan tenaga tim marketing/telemarketing karena upaya diarahkan pada calon nasabah dengan probabilitas tinggi untuk membuka deposito
- Mengurangi biaya operasional (seperti biaya telepon dan sumber daya lainnya) sehingga anggaran dapat dialokasikan lebih efisien
- Meningkatkan keuntungan jangka pendek maupun jangka panjang, tidak hanya dengan menekan False Positive (nasabah yang ditelepon tapi tidak deposit), tetapi juga dengan mengurangi False Negative (kehilangan nasabah yang potensial)


## **8. Contact**
- Yanfa Anandika
- Email : yanfaanandika21@gmail.com
- LinkedIn : [Yanfa Anandika](https://www.linkedin.com/in/yanfa-anandika-a663bb170/)
- GitHub : [yanfa121](https://github.com/yanfa121)
