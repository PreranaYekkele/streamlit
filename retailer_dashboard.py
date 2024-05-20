import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("🗂️Dashboard")
    
    # Load data
    try:
        data = pd.read_csv("data.csv")
    except FileNotFoundError:
        st.error("Data file not found.")
        return
    except pd.errors.EmptyDataError:
        st.error("Data file is empty.")
        return

    # Display Metrics
    # st.subheader("Metrics")
    st.write("Total Inventory:", data['inventory'].sum())
    st.write("Maximum:", data['inventory'].max())
    st.write("Minimum:", data['inventory'].min())
    
    st.subheader("Inventory Charts")

    inventory_chart = px.line(data, x='date', y='inventory', title='Inventory Over Time')
    st.plotly_chart(inventory_chart)

    data['inventory_change'] = data['inventory'].diff()
    inventory_change_chart = px.bar(data, x='date', y='inventory_change', title='Daily Inventory Change')
    st.plotly_chart(inventory_change_chart)

    data['moving_avg'] = data['inventory'].rolling(window=3).mean()
    moving_avg_chart = px.line(data, x='date', y='moving_avg', title='Moving Average of Inventory (3-day window)')
    st.plotly_chart(moving_avg_chart)

if __name__ == "__main__":
    main()
