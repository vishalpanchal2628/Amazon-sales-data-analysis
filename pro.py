import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """
    Load the CSV file into a pandas DataFrame.
    """
    return pd.read_csv(file_path)

def clean_data(df):
    """
    Clean the data by handling missing values, converting date columns, etc.
    """
    # Convert date columns to datetime
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    
    # Handle missing values if any
    # df = df.dropna()  # or use appropriate imputation method
    
    return df

def calculate_sales_trends(df):
    """
    Calculate monthly, yearly, and yearly-monthly sales trends.
    """
    # Monthly trends
    monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Total Revenue'].sum()
    
    # Yearly trends
    yearly_sales = df.groupby(df['Order Date'].dt.year)['Total Revenue'].sum()
    
    # Yearly-monthly trends
    yearly_monthly_sales = df.groupby([df['Order Date'].dt.year, df['Order Date'].dt.month])['Total Revenue'].sum()
    
    return monthly_sales, yearly_sales, yearly_monthly_sales

def analyze_key_metrics(df):
    """
    Analyze key metrics and relationships between attributes.
    """
    # Calculate profit margin
    df['Profit Margin'] = df['Total Profit'] / df['Total Revenue']
    
    # Analyze sales channel vs total revenue
    channel_revenue = df.groupby('Sales Channel')['Total Revenue'].sum()
    
    # Analyze region vs total revenue
    region_revenue = df.groupby('Region')['Total Revenue'].sum()
    
    # Analyze item type vs total profit
    item_profit = df.groupby('Item Type')['Total Profit'].sum()
    
    return channel_revenue, region_revenue, item_profit

def visualize_trends(monthly_sales, yearly_sales, yearly_monthly_sales):
    """
    Create visualizations for sales trends.
    """
    # Plot monthly sales trend
    plt.figure(figsize=(12, 6))
    monthly_sales.plot()
    plt.title('Monthly Sales Trend')
    plt.xlabel('Date')
    plt.ylabel('Total Revenue')
    plt.show()
    
    # Add more visualizations for yearly and yearly-monthly trends

def main():
    # Load data
    df = load_data('Amazon Sales data.csv')
    
    # Clean data
    df = clean_data(df)
    
    # Calculate sales trends
    monthly_sales, yearly_sales, yearly_monthly_sales = calculate_sales_trends(df)
    
    # Analyze key metrics
    channel_revenue, region_revenue, item_profit = analyze_key_metrics(df)
    
    # Visualize trends
    visualize_trends(monthly_sales, yearly_sales, yearly_monthly_sales)
    
    # Add more analysis and visualizations as needed

if __name__ == "__main__":
    main()