import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("imdb.csv")

df = load_data()

# Tampilan Awal
st.markdown("```")
st.text("Hello,")
st.text("Selamat Datang di Dashboard IMDb")
st.text("by.")
st.text("> NIM  : 2411600303")
st.text("> Nama : SULASTRI")
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
st.text("[8] Sub Menu Genre")
st.text("[9] Sub Menu Color")
st.text("[10] Exit")
st.markdown("```")

# Pilihan Menu
menu = st.selectbox("Pilih Menu:", (
    "1. Genre", 
    "2. Bahasa", 
    "3. Negara", 
    "4. Total Film", 
    "5. Chart Rating", 
    "6. Revenue Gross dan Duration", 
    "7. Query (Language dan Genre)",
    "8. Sub Menu Genre",
    "9. Sub Menu Color",
    "10. Exit"
))

# Menu Sebelumnya Tetap
if "Genre" in menu and not "Sub" in menu:
    st.subheader("Jumlah Film per Genre")
    genre_count = df['Genre'].value_counts().rename_axis('Genre').reset_index(name='Jumlah')
    st.bar_chart(data=genre_count.set_index('Genre'))

elif "Bahasa" in menu:
    st.subheader("Jumlah Film per Bahasa")
    lang_count = df['Language'].value_counts().rename_axis('Bahasa').reset_index(name='Jumlah')
    st.bar_chart(data=lang_count.set_index('Bahasa'))

elif "Negara" in menu:
    st.subheader("Jumlah Film per Negara")
    country_count = df['Country'].value_counts().rename_axis('Negara').reset_index(name='Jumlah')
    st.bar_chart(data=country_count.set_index('Negara'))

elif "Total Film" in menu:
    st.subheader("Total Film dalam Dataset")
    st.success(f"Ada total {len(df)} film.")

elif "Rating" in menu:
    st.subheader("Distribusi IMDb Score")
    rating_data = df["IMDb Score (1-10)"].value_counts().sort_index()
    st.line_chart(rating_data)

elif "Revenue" in menu:
    st.subheader("Scatter Chart: Gross Revenue vs Duration")
    scatter_df = df[["Duration (min)", "Gross Revenue"]].dropna()
    st.scatter_chart(scatter_df)

elif "Query" in menu:
    st.subheader("Filter Berdasarkan Genre dan Bahasa")
    selected_genre = st.selectbox("Pilih Genre", df['Genre'].unique())
    selected_lang = st.selectbox("Pilih Bahasa", df['Language'].unique())
    hasil = df[(df['Genre'] == selected_genre) & (df['Language'] == selected_lang)]
    st.write(f"Ditemukan {len(hasil)} film:")
    st.dataframe(hasil)

# ✅ SUB MENU GENRE
elif "Sub Menu Genre" in menu:
    st.subheader("Jumlah dan Detail per Genre")
    genre_counts = df['Genre'].value_counts().rename_axis("Genre").reset_index(name="Jumlah")
    st.dataframe(genre_counts)

    selected_genre = st.selectbox("Pilih Genre untuk Lihat Detail", genre_counts['Genre'])
    detail_genre = df[df["Genre"] == selected_genre]
    st.write(f"Detail Film dengan Genre: {selected_genre}")
    st.dataframe(detail_genre)

# ✅ SUB MENU COLOR
elif "Sub Menu Color" in menu:
    st.subheader("Jumlah dan Detail per Warna (Color/BW)")
    color_counts = df['Color/BW'].value_counts().rename_axis("Color").reset_index(name="Jumlah")
    st.dataframe(color_counts)

    selected_color = st.selectbox("Pilih Warna untuk Lihat Detail", color_counts['Color'])
    detail_color = df[df["Color/BW"] == selected_color]
    st.write(f"Detail Film dengan Warna: {selected_color}")
    st.dataframe(detail_color)

elif "Exit" in menu:
    st.info("Silakan tutup aplikasi jika ingin keluar.")
