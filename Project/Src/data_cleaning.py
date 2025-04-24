# data_cleaning.py

import pandas as pd

def load_data(filepath, encoding='ISO-8859-1'):
    """
    Membaca file CSV dari path dan mengembalikan DataFrame.

    Parameters:
        filepath (str): Lokasi file dataset.
        encoding (str): Tipe encoding file.

    Returns:
        pd.DataFrame: DataFrame hasil pembacaan file.
    """
    try:
        df = pd.read_csv(filepath, encoding=encoding)
        return df
    except Exception as e:
        print(f"Gagal memuat data: {e}")
        return None


def clean_data(df):
    """
    Membersihkan data dengan menghapus nilai kosong penting, 
    menghapus kuantitas negatif, dan menghitung kolom revenue.

    Parameters:
        df (pd.DataFrame): Dataset awal.

    Returns:
        pd.DataFrame: Dataset yang telah dibersihkan.
    """
    df = df.copy()

    # Hapus baris tanpa CustomerID
    df.dropna(subset=['CustomerID'], inplace=True)

    # Hapus transaksi dengan Quantity <= 0
    df = df[df['Quantity'] > 0]

    # Konversi InvoiceDate menjadi datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # kolom Revenue
    df['Revenue'] = df['Quantity'] * df['UnitPrice']

    return df


def preprocess_datetime(df):
    """
    Menambahkan fitur waktu tambahan untuk analisis.

    Parameters:
        df (pd.DataFrame): Dataset setelah pembersihan.

    Returns:
        pd.DataFrame: Dataset dengan fitur waktu tambahan.
    """
    df = df.copy()

    df['Month'] = df['InvoiceDate'].dt.to_period('M').astype(str)
    df['DayOfWeek'] = df['InvoiceDate'].dt.dayofweek
    df['Week'] = df['InvoiceDate'].dt.isocalendar().week

    return df
