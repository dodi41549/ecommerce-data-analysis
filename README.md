# Ecommerce Data Analysis

Proyek ini bertujuan untuk melakukan analisis menyeluruh terhadap data penjualan dari sebuah platform e-commerce. Fokus utama dari analisis ini adalah memahami pola pembelian pelanggan, performa produk, serta perilaku konsumen berdasarkan data historis penjualan.

EN :
This project aims to conduct a comprehensive analysis of sales data from an e-commerce platform. The main focus of this analysis is to understand customer buying patterns, product performance, and consumer behavior based on historical sales data.

## 📌 Tujuan Proyek (Project Objectives)

- Memberikan **insight berbasis data** terhadap aktivitas bisnis e-commerce.
- Menemukan **pola penjualan** harian, mingguan, dan bulanan.
- Mengidentifikasi **pelanggan paling loyal** dan negara dengan kontribusi penjualan terbesar.
- Memberikan **rekomendasi bisnis** untuk stok produk dan strategi promosi berdasarkan hasil analisis.

EN:
- Provide **data-driven insights** into e-commerce business activities.
- Discover daily, weekly and monthly **sales patterns**.
- Identify **most loyal customers** and countries with the largest sales contribution.
- Provide **business recommendations** for product stock and promotion strategies based on analysis results.


## 🛠 Tools yang Digunakan (Tools to be used)

- Python
- Pandas
- Matplotlib
- Seaborn
- Google Colab
- GitHub

## 🗂 Struktur Direktori (Directory Structure)

project/
├── data/                  # Dataset asli dan hasil pembersihan (Original dataset and cleaning results)
│   └── data.zip
|   └── ecommerce_data_new.zip
├── images/                # Semua gambar plot (PNG, dll.)
|   └── Bar Chart.png
|   └── Bar Plot Top 10 Loyal.png
|   └── Bar Plot.png
|   └── Heatmap.png
|   └── Pie Chart.png
|   └── Plot Line Chart.png
├── notebooks/
│   └── Ecommerce.ipynb
├── src/
│   ├── visualization.py
│   ├── analyst_data.py
│   └── data_cleaning.py
|   └── utils.py
├── requirements.txt       # Daftar library (pandas, matplotlib, seaborn, dll.) (List of libraries (pandas, matplotlib, seaborn, etc.))
└── README.md              # Penjelasan dan insight project (Project explanation and insight)


## ▶️ Cara Menjalankan Proyek (How to Run the Project)

1. **Buka Google Colab**.
2. Upload file notebook `Ecommerce.ipynb` yang ada di folder `notebooks/`.
3. Pastikan file dataset (`ecommerce_data_new.csv`) berada di folder `data/`.
4. Jalankan kode sel demi sel untuk melihat proses data cleaning, analisis, dan visualisasi.
5. Semua gambar/plot yang dihasilkan bisa ditemukan di folder `images/`.

EN:
1. **Open Google Colab**.
2. Upload the `Ecommerce.ipynb` notebook file in the `notebooks/` folder.
3. Make sure the dataset file (`ecommerce_data_new.csv`) is in the `data/` folder.
4. Run the code cell by cell to see the data cleaning, analysis, and visualization process.
5. All generated images/plots can be found in the `images/` folder.

## 📊 Insight Utama dari Analisis (Key Insights from Analysis)

Berikut beberapa insight yang diperoleh dari visualisasi dan analisis data:

- **Produk paling populer**: Produk-produk tertentu memiliki volume pembelian jauh lebih tinggi, cocok untuk prioritas stok.
- **Pola pembelian**: Pembelian meningkat di hari-hari tertentu dalam seminggu dan menunjukkan lonjakan penjualan di bulan tertentu.
- **Negara dengan penjualan tertinggi**: Inggris menyumbang mayoritas pendapatan, disusul negara-negara Eropa lainnya.
- **Pelanggan loyal**: Terdapat pelanggan dengan total pembelian yang jauh di atas rata-rata. Mereka bisa menjadi target promosi eksklusif.
- **Waktu transaksi aktif**: Jam dan hari tertentu menunjukkan volume transaksi yang lebih tinggi.

EN:
Here are some insights gained from data visualization and analysis:

- **Most popular products**: Certain products have a much higher purchase volume, suitable for stock prioritization.
- **Purchase patterns**: Purchases increase on certain days of the week and show spikes in sales in certain months.
- **Highest selling countries**: The UK accounts for the majority of revenue, followed by other European countries.
- **Loyal customers**: There are customers whose total purchases are well above average. They can be targeted for exclusive promotions.
- **Active transaction times**: Certain hours and days show higher transaction volumes.

## ✅ Rekomendasi (Recomendataions)

Berdasarkan hasil analisis, berikut beberapa rekomendasi yang bisa diimplementasikan untuk bisnis:

- **Manajemen Stok**: Fokus pada produk dengan penjualan tertinggi dan minimalkan stok produk dengan demand rendah.
- **Promosi dan Diskon**: Tawarkan diskon khusus di hari atau bulan dengan penjualan rendah untuk meningkatkan konversi.
- **Target Loyal Customer**: Bangun program loyalitas atau membership bagi pelanggan yang sering membeli.
- **Segmentasi Geografis**: Fokus kampanye pemasaran pada negara-negara dengan volume pembelian tinggi.
- **Perencanaan Musiman**: Siapkan strategi berdasarkan pola bulanan untuk menjaga konsistensi pendapatan.

EN:
Based on the analysis, here are some recommendations that can be implemented for businesses:

- **Stock Management**: Focus on products with the highest sales and minimize stock of products with low demand.
- **Promotions and Discounts**: Offer special discounts on days or months with low sales to increase conversions.
- **Target Loyal Customers**: Build a loyalty or membership program for frequent customers.
- **Geographic Segmentation**: Focus marketing campaigns on countries with high purchase volumes.
- **Seasonal Planning**: Set up strategies based on monthly patterns to maintain revenue consistency.

---

📬 **Terima kasih telah melihat proyek ini!**  
Silakan clone repo ini dan eksplorasi lebih lanjut atau gunakan untuk referensi proyek analisis data lainnya.

📬 **Thank you for viewing this project!**  
Please clone this repo and explore further or use it to reference other data analysis projects.





