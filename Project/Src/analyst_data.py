# analyst_data.py

import pandas as pd

def basic_statistics(df):
    """
    Menampilkan statistik deskriptif dasar dari dataset.
    """
    return df.describe()


def top_products_by_revenue(df, top_n=10):
    """
    Mengembalikan produk dengan total revenue tertinggi.
    """
    top_products = df.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(top_n)
    return top_products.reset_index().rename(columns={'Revenue': 'TotalRevenue'})


def top_products_by_quantity(df, top_n=10):
    """
    Mengembalikan produk yang paling banyak terjual berdasarkan quantity.
    """
    top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(top_n)
    return top_products.reset_index().rename(columns={'Quantity': 'TotalQuantity'})


def revenue_by_country(df):
    """
    Mengembalikan total revenue berdasarkan negara.
    """
    return df.groupby('Country')['Revenue'].sum().sort_values(ascending=False).reset_index()


def revenue_by_month(df):
    """
    Mengembalikan total revenue berdasarkan bulan.
    """
    return df.groupby('Month')['Revenue'].sum().reset_index().sort_values('Month')


def customer_segmentation(df):
    """
    Mengembalikan total pembelian dan jumlah transaksi per pelanggan.
    """
    segment = df.groupby('CustomerID').agg({
        'Revenue': 'sum',
        'InvoiceNo': pd.Series.nunique
    }).reset_index()

    segment.columns = ['CustomerID', 'TotalRevenue', 'TotalTransactions']
    return segment.sort_values(by='TotalRevenue', ascending=False)


def average_order_value(df):
    """
    Menghitung rata-rata nilai pesanan (AOV).
    """
    order_value = df.groupby('InvoiceNo')['Revenue'].sum()
    return order_value.mean()


def conversion_rate(df):
    """
    Menghitung conversion rate berdasarkan total customer dan total transaksi.
    (asumsi: satu transaksi per invoice)
    """
    total_customers = df['CustomerID'].nunique()
    total_transactions = df['InvoiceNo'].nunique()
    return (total_transactions / total_customers) * 100 if total_customers != 0 else 0


def most_active_days(df):
    """
    Mengembalikan hari dalam seminggu dengan revenue tertinggi.
    """
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['DayOfWeek'] = df['InvoiceDate'].dt.dayofweek
    revenue_by_day = df.groupby('DayOfWeek')['Revenue'].sum().reset_index()
    revenue_by_day['Day'] = revenue_by_day['DayOfWeek'].map(lambda x: days[x])
    return revenue_by_day.sort_values('Revenue', ascending=False).reset_index(drop=True)
