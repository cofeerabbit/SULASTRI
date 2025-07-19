import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("imdb.csv")

df = load_data()

# Tampilan Awal
st.markdown("```")
st.text("Hello,")
st.text("Selamat Datang di Dashboard IMDb")
st.text("by.")
st.text("> NIM  : 1911600123")
st.text("> Nama : Budi Luhur")
st.text("-----------------------------")
st.text("        M  E  N  U           ")
st.text("-----------------------------")
st.text("[1] Genre")
st.text("[2] Bahasa")
st.text("[3] Negara")
st.text("[4] Total Film")
st.text("[5] Chart Rating")
st.text("[6] Revenue Gross dan Duration")
st.text("[7] Query (Language dan Genre)")
st.text("[8] Exit")
st.markdown("```")

# Menu Pilihan
menu = st.selectbox("Input Pilihan Menu:", (
    "1. Genre", 
    "2. Bahasa", 
    "3. Negara", 
    "4. Total Film", 
    "5. Chart Rating", 
    "6. Revenue Gross dan Duration", 
    "7. Query (Language dan Genre)", 
    "8. Exit"
))

# Menu 1 - Genre
if "Genre" in menu:
    st.subheader("Jumlah Film per Genre")
    st.bar_chart(df['Genre'].value_counts())

# Menu 2 - Bahasa
elif "Bahasa" in menu:
    st.subheader("Jumlah Film per Bahasa")
    st.bar_chart(df['Language'].value_counts())

# Menu 3 - Negara
elif "Negara" in menu:
    st.subheader("Jumlah Film per Negara")
    st.bar_chart(df['Country'].value_counts())

# Menu 4 - Total Film
elif "Total Film" in menu:
    st.subheader("Total Film dalam Dataset")
    st.success(f"Ada total {len(df)} film.")

# Menu 5 - Chart Rating
elif "Chart Rating" in menu:
    st.subheader("Distribusi IMDb Score")
    fig, ax = plt.subplots()
    ax.hist(df["IMDb Score (1-10)"], bins=10, color='skyblue', edgecolor='black')
    ax.set_xlabel("IMDb Score")
    ax.set_ylabel("Jumlah Film")
    st.pyplot(fig)

# Menu 6 - Revenue dan Duration
elif "Revenue" in menu:
    st.subheader("Scatter Plot: Gross Revenue vs Duration")
    fig, ax = plt.subplots()
    ax.scatter(df["Duration (min)"], df["Gross Revenue"], color="orange")
    ax.set_xlabel("Durasi (menit)")
    ax.set_ylabel("Pendapatan Kotor (Gross)")
    st.pyplot(fig)

# Menu 7 - Query
elif "Query" in menu:
    st.subheader("Filter Berdasarkan Genre dan Bahasa")
    genre = st.selectbox("Pilih Genre", df['Genre'].unique())
    language = st.selectbox("Pilih Bahasa", df['Language'].unique())
    hasil = df[(df['Genre'] == genre) & (df['Language'] == language)]
    st.write(f"Ditemukan {len(hasil)} film")
    st.dataframe(hasil)

# Menu 8 - Exit
elif "Exit" in menu:
    st.info("Silakan tutup aplikasi jika ingin keluar.")
