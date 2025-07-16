import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")
st.title("📊 Supermarket Sales Dashboard - India")

# ✅ Logout Button
if st.button("Logout"):
    st.session_state.logged_in = False
    st.switch_page("pages/1_Login.py")

# Load Data
df = pd.read_csv("india_supermarket_sales.csv")
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.strftime('%b')

# Sidebar Filters
st.sidebar.header("🔍 Filters")
state = st.sidebar.selectbox("Select State", sorted(df['state'].unique()))
city = st.sidebar.selectbox("Select City", sorted(df[df['state'] == state]['city'].unique()))
year = st.sidebar.selectbox("Select Year", sorted(df['year'].unique()))
date_range = st.sidebar.date_input("Date Range", [df['date'].min(), df['date'].max()])

# Filter Data
filtered_df = df[(df['state'] == state) & (df['city'] == city) & (df['year'] == year) &
                 (df['date'] >= pd.to_datetime(date_range[0])) &
                 (df['date'] <= pd.to_datetime(date_range[1]))]

# ✅ KPIs
total_sales = filtered_df['sales'].sum()
total_orders = len(filtered_df)
avg_rating = filtered_df['rating'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"₹{total_sales:,.2f}")
col2.metric("Total Orders", f"{total_orders}")
col3.metric("Avg Rating", f"{avg_rating:.2f}")

# ✅ Monthly Trend Chart
st.subheader("📈 Monthly Sales Trend")
monthly_sales = filtered_df.groupby('month')['sales'].sum().reset_index()
fig1 = px.line(monthly_sales, x='month', y='sales', markers=True, title="Monthly Sales", template="plotly_white")
st.plotly_chart(fig1, use_container_width=True)

# ✅ Top Products
st.subheader("🏆 Top 5 Products")
top_products = filtered_df.groupby('product line')['sales'].sum().sort_values(ascending=False).head(5).reset_index()
fig2 = px.bar(top_products, x='product line', y='sales', color='product line', title="Top Products", template="plotly_white")
st.plotly_chart(fig2, use_container_width=True)

# ✅ Payment Method Pie
st.subheader("💳 Payment Method Distribution")
fig3 = px.pie(filtered_df, names='payment', values='sales', title="Payment Methods", template="plotly_white")
st.plotly_chart(fig3, use_container_width=True)

# ✅ Download Data
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("📥 Download Filtered Data", csv, "filtered_sales.csv", "text/csv")
