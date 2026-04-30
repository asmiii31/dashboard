import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Dashboard", layout="wide")
st.title("📊 Simple Data Dashboard")
st.markdown("Upload your Excel file to generate instant charts.")

# File Uploader
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file:
    # Read Data
    df = pd.read_excel(uploaded_file)
    st.write("### Data Preview", df.head())

    # Sidebar Settings
    st.sidebar.header("Chart Settings")
    columns = df.columns.tolist()
    
    chart_type = st.sidebar.selectbox("Select Chart Type", 
                                    ["Bar Chart", "Line Chart", "Scatter Plot", "Pie Chart"])
    
    x_axis = st.sidebar.selectbox("Select X-axis (Category)", columns)
    y_axis = st.sidebar.selectbox("Select Y-axis (Values)", columns)

    # Generate Charts
    st.subheader(f"{chart_type}: {y_axis} by {x_axis}")
    
    if chart_type == "Bar Chart":
        fig = px.bar(df, x=x_axis, y=y_axis, color=x_axis)
    elif chart_type == "Line Chart":
        fig = px.line(df, x=x_axis, y=y_axis)
    elif chart_type == "Scatter Plot":
        fig = px.scatter(df, x=x_axis, y=y_axis, color=x_axis)
    elif chart_type == "Pie Chart":
        fig = px.pie(df, names=x_axis, values=y_axis)

    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Please upload an Excel file to begin.")
