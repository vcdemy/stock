import streamlit as st
import yfinance as yf

st.sidebar.write("Sidebar")
ticker = st.sidebar.text_input("請輸入股票代號")
st.write("顯示股票資料")

df = yf.download(ticker)

st.write(df.tail(50))