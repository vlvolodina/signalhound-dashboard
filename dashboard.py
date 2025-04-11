import streamlit as st
import pandas as pd

st.set_page_config(page_title="SignalHound Dashboard", layout="wide")

st.title("📈 SignalHound Dashboard")
st.markdown("Добро пожаловать в аналитику по сигналам Telegram-бота!")

try:
    df = pd.read_csv("signals.csv")
    st.dataframe(df)
except:
    st.warning("📁 Файл signals.csv пока не найден или пуст.")