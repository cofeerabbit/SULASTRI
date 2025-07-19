import streamlit as st
import pandas as pd

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
    genre_count = df['Genre'].value_counts().rename_axis('Genre').reset_index(name='Jumlah')
    st.bar_chart(data=genre_count.set_index('Genre'))

# Menu 2 - Bahasa
elif "Bahasa" in menu:
    st.subheader("Jumlah Film per Bahasa")
    lang_count = df['Language'].value_counts().rename_axis('Bahasa').reset_index(name='Jumlah')
    st.bar_chart(data=lang_count.set_index('Bahasa'))

# Menu 3 - Negara
elif "Negara" in menu:
    st.subheader("Jumlah Film per Negara")
    country_count = df['Country'].value_counts().rename_axis('Negara').reset_index(name='Jumlah')
    st.bar_chart(data=country_count.set_index('Negara'))

# Menu 4 - Total Film
elif "Total Film" in menu:
    st.subheader("Total Film dalam Dataset")
    st.success(f"Ada total {len(df)} film dalam dataset.")

# Menu 5 - Chart Rating (pakai line chart)
elif "Chart Rating" in menu:
    st.subheader("Distribusi IMDb Score")
    rating_data = df["IMDb Score (1-10)"].value_counts().sort_index()
    st.line_chart(rating_data)

# Menu 6 - Revenue Gross dan Duration
elif "Revenue" in menu:
    st.subheader("Scatter Chart: Gross Revenue vs Duration")
    scatter_df = df[["Duration (min)", "Gross Revenue"]].dropna()
    st.scatter_chart(scatter_df)

# Menu 7 - Query Berdasarkan Genre dan Language
elif "Query" in menu:
    st.subheader("Filter Berdasarkan Genre dan Bahasa")
    selected_genre = st.selectbox("Pilih Genre", df['Genre'].unique())
    selected_lang = st.selectbox("Pilih Bahasa", df['Language'].unique())
    hasil = df[(df['Genre'] == selected_genre) & (df['Language'] == selected_lang)]
    st.write(f"Ditemukan {len(hasil)} film:")
    st.dataframe(hasil)

# Menu 8 - Exit
elif "Exit" in menu:
    st.info("Silakan tutup aplikasi jika ingin keluar.")
