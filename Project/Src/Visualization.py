# visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_monthly_revenue(df):
    """
    Menampilkan plot total revenue per bulan.
    """
    monthly_revenue = df.groupby('Month')['Revenue'].sum().reset_index()

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=monthly_revenue, x='Month', y='Revenue', marker='o', color='teal')
    plt.title('Monthly Revenue Trend')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_top_countries(df, top_n=10):
    """
    Menampilkan bar chart negara dengan total revenue tertinggi.
    """
    top_countries = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False).head(top_n)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_countries.values, y=top_countries.index, palette=sns.color_palette('viridis', n_colors=top_n))
    plt.title(f'Top {top_n} Countries by Revenue')
    plt.xlabel('Revenue')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()


def plot_top_loyal_customers(df, top_n=10):
    """
    Menampilkan bar chart pelanggan paling loyal berdasarkan total pembelian.
    """
    loyal_customers = df.groupby('CustomerID')['Revenue'].sum().sort_values(ascending=False).head(top_n)
    df_loyal = loyal_customers.reset_index()
    df_loyal.columns = ['CustomerID', 'TotalPurchases']

    plt.figure(figsize=(12, 6))
    sns.barplot(data=df_loyal, x='CustomerID', y='TotalPurchases', palette=sns.color_palette('coolwarm', n_colors=top_n))
    plt.title(f'Top {top_n} Most Loyal Customers Based on Total Purchases')
    plt.xlabel('Customer ID')
    plt.ylabel('Total Purchases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_day_of_week_distribution(df):
    """
    Menampilkan distribusi revenue berdasarkan hari dalam seminggu.
    """
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    revenue_by_day = df.groupby('DayOfWeek')['Revenue'].sum().reindex(range(7)).reset_index()
    revenue_by_day['Day'] = days

    plt.figure(figsize=(10, 5))
    sns.barplot(data=revenue_by_day, x='Day', y='Revenue', palette='mako')
    plt.title('Revenue by Day of the Week')
    plt.xlabel('Day')
    plt.ylabel('Revenue')
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(df):
    """
    Menampilkan heatmap korelasi antar fitur numerik.
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(df[['Quantity', 'UnitPrice', 'Revenue']].corr(), annot=True, cmap='YlGnBu', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.show()


def plot_country_pie_chart(df, top_n=5):
    """
    Menampilkan pie chart negara dengan revenue tertinggi.
    """
    top_countries = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False).head(top_n)
    others = df['Revenue'].sum() - top_countries.sum()

    labels = list(top_countries.index) + ['Others']
    values = list(top_countries.values) + [others]

    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title(f'Revenue Share by Country (Top {top_n})')
    plt.tight_layout()
    plt.show()
