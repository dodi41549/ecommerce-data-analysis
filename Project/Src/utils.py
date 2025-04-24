# utils.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

# === DATA CLEANING ===

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath, encoding='ISO-8859-1')
    df.dropna(subset=['CustomerID'], inplace=True)
    df = df[df['Quantity'] > 0]
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    return df


# === VISUALISASI PRODUK TERLARIS ===

def plot_top_products(df, n=10, save_path=None):
    top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(n)
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_products.values, y=top_products.index, palette='viridis')
    plt.title(f'Top {n} Best-Selling Products')
    plt.xlabel('Total Quantity Sold')
    plt.ylabel('Product')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()


# === PENJUALAN PER BULAN ===

def plot_monthly_revenue(df, save_path=None):
    df['Month'] = df['InvoiceDate'].dt.to_period('M').astype(str)
    monthly_revenue = df.groupby('Month')['Revenue'].sum()
    
    plt.figure(figsize=(14, 6))
    monthly_revenue.plot(marker='o', color='blue')
    plt.title('Monthly Revenue')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()


# === HEATMAP ORDER ===

def plot_order_heatmaps(df, save_path=None):
    df['DayOfWeek'] = df['InvoiceDate'].dt.dayofweek
    df['Week'] = df['InvoiceDate'].dt.isocalendar().week
    
    order_counts = df.groupby(['Week', 'DayOfWeek'])['InvoiceNo'].count().unstack()
    order_counts.columns = [calendar.day_name[d] for d in order_counts.columns]
    
    plt.figure(figsize=(14, 7))
    sns.heatmap(order_counts, cmap='YlGnBu', linewidths=0.5)
    plt.title('Order Count Heatmap (Weekly vs Day of Week)')
    plt.xlabel('Day of Week')
    plt.ylabel('Week Number')
    if save_path:
        plt.savefig(save_path)
    plt.show()


# === NEGARA DENGAN PEMBELIAN TERBANYAK ===

def plot_top_countries(df, n=10, save_path=None):
    top_countries = df.groupby('Country')['InvoiceNo'].nunique().sort_values(ascending=False).head(n)
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_countries.values, y=top_countries.index, hue=top_countries.index, legend=False, palette='viridis')
    plt.title(f'Top {n} Countries by Number of Purchases')
    plt.xlabel('Number of Unique Invoices')
    plt.ylabel('Country')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()


# === PELANGGAN PALING LOYAL ===

def plot_top_loyal_customers(df, n=10, save_path=None):
    loyal_customers = df.groupby('CustomerID')['Revenue'].sum().sort_values(ascending=False).head(n)
    df_loyal = loyal_customers.reset_index()
    df_loyal.columns = ['CustomerID', 'TotalPurchases']
    
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df_loyal, x='CustomerID', y='TotalPurchases', hue='CustomerID', legend=False, palette='coolwarm')
    plt.title('Top 10 Most Loyal Customers')
    plt.xlabel('Customer ID')
    plt.ylabel('Total Purchases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()
