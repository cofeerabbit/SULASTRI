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
st.text("Selamat Datang di Dashboard IMDb Milik SULASTRI")
st.text("> NIM  : 2411600303")
st.text("> Nama : SULASTRI")

st.markdown("```")

# Pilihan Menu
menu = st.sidebar.selectbox("Pilih Menu", [
    "Home", 
    "Sub Menu Genre", 
    "Sub Menu Color", 
    "Sub Menu Bahasa", 
    "Sub Menu Negara", 
    "Sub Menu Total Film", 
    "Sub Menu Chart (Rating vs Jumlah Film)"
    "Sub Menu Resume Gross dan Duration"
    "Sub Menu Query (Language dan Genre)"
])


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

#  SUB MENU GENRE
elif "Sub Menu Genre" in menu:
    st.subheader("Jumlah dan Detail per Genre")
    genre_counts = df['Genre'].value_counts().rename_axis("Genre").reset_index(name="Jumlah")
    st.dataframe(genre_counts)

    selected_genre = st.selectbox("Pilih Genre untuk Lihat Detail", genre_counts['Genre'])
    detail_genre = df[df["Genre"] == selected_genre]
    st.write(f"Detail Film dengan Genre: {selected_genre}")
    st.dataframe(detail_genre)

#  SUB MENU COLOR
elif "Sub Menu Color" in menu:
    st.subheader("Jumlah dan Detail per Warna (Color/BW)")

    # Cek kolom yang mirip "Color/BW"
    st.write("Kolom tersedia di dataset:")
    st.write(df.columns.tolist())  # DEBUG: tampilkan semua nama kolom

    # Coba deteksi kolom yang mengandung kata 'color'
    color_col = [col for col in df.columns if 'color' in col.lower() or 'bw' in col.lower()]
    
    if color_col:
        color_column_name = color_col[0]  # Ambil nama kolom yang cocok
        color_counts = df[color_column_name].value_counts().rename_axis("Color").reset_index(name="Jumlah")
        st.write("Tabel Jumlah Film per Color:")
        st.dataframe(color_counts)

        # Dropdown untuk detail
        selected_color = st.selectbox("Pilih Warna untuk Lihat Detail", color_counts['Color'])
        detail_color = df[df[color_column_name] == selected_color]
        st.write(f"Detail Film dengan Warna: {selected_color}")
        st.dataframe(detail_color)
    else:
        st.error("Kolom Color/BW tidak ditemukan di dataset.")


#  SUB MENU GENRE
elif "Sub Menu Genre" in menu:
    st.subheader("Jumlah dan Detail per Genre")

    # Hitung jumlah genre
    genre_counts = df['Genre'].value_counts().rename_axis("Genre").reset_index(name="Jumlah")
    st.write("Tabel Jumlah Film per Genre:")
    st.dataframe(genre_counts)

    # Dropdown untuk detail
    selected_genre = st.selectbox("Pilih Genre untuk Lihat Detail", genre_counts['Genre'])
    detail_genre = df[df["Genre"] == selected_genre]
    st.write(f"Detail Film dengan Genre: {selected_genre}")
    st.dataframe(detail_genre)

#  SUB MENU COLOR
elif "Sub Menu Color" in menu:
    st.subheader("Jumlah dan Detail per Warna (Color/BW)")

    # Hitung jumlah berdasarkan Color
    color_counts = df['Color/BW'].value_counts().rename_axis("Color").reset_index(name="Jumlah")
    st.write("Tabel Jumlah Film per Color:")
    st.dataframe(color_counts)

    # Dropdown untuk detail
    selected_color = st.selectbox("Pilih Warna untuk Lihat Detail", color_counts['Color'])
    detail_color = df[df["Color/BW"] == selected_color]
    st.write(f"Detail Film dengan Warna: {selected_color}")
    st.dataframe(detail_color)

#  SUB MENU BAHASA
elif "Sub Menu Bahasa" in menu:
    st.subheader("Jumlah Bahasa di Dataset")
    
    # Otomatis cari kolom yang mengandung kata "language"
    language_cols = [col for col in df.columns if 'language' in col.lower()]
    
    if language_cols:
        lang_col = language_cols[0]
        num_langs = df[lang_col].nunique()
        st.write(f"Dataset IMDB saat ini terdiri dari **{num_langs} Bahasa**.")
        st.dataframe(df[[lang_col]].drop_duplicates().reset_index(drop=True))
    else:
        st.error("Kolom bahasa tidak ditemukan.")

# SUB MENU NEGARA
elif "Sub Menu Negara" in menu:
    st.subheader("Jumlah Negara di Dataset")

    country_cols = [col for col in df.columns if 'country' in col.lower()]
    
    if country_cols:
        country_col = country_cols[0]
        num_countries = df[country_col].nunique()
        st.write(f"Terdapat **{num_countries} Negara** dalam Dataset IMDB.")
        st.dataframe(df[[country_col]].drop_duplicates().reset_index(drop=True))
    else:
        st.error("Kolom negara tidak ditemukan.")

#  SUB MENU TOTAL FILM
elif "Sub Menu Total Film" in menu:
    st.subheader("Jumlah Total Film di Dataset")
    
    num_films = df.shape[0]
    st.write(f"Dataset IMDB saat ini memiliki **{num_films} Film**.")


#  SUB MENU CHART
elif "Sub Menu Chart" in menu:
    st.subheader("Grafik Jumlah Film per Rating")

    rating_cols = [col for col in df.columns if 'rating' in col.lower()]
    
    if rating_cols:
        rating_col = rating_cols[0]
        rating_counts = df[rating_col].value_counts().reset_index()
        rating_counts.columns = ['Rating', 'Jumlah Film']
        
        st.bar_chart(rating_counts.set_index('Rating'))
    else:
        st.error("Kolom rating tidak ditemukan.")

# SUB MENU RESUME GROSS DAN DURATION
elif "Sub Menu Resume Gross dan Duration" in menu:
    st.subheader("Sub Menu Resume Gross dan Duration")

    st.markdown("### Gross Revenue Resume:")
    total_gross = df["Gross Revenue"].sum()
    rata2_gross = df["Gross Revenue"].mean()
    min_gross = df["Gross Revenue"].min()
    max_gross = df["Gross Revenue"].max()

    st.text(f"Total     : $ {total_gross}")
    st.text(f"Rata-rata : $ {rata2_gross}")
    st.text(f"Terendah  : $ {min_gross}")
    st.text(f"Tertinggi : $ {max_gross}")

    st.markdown("### Duration Resume:")
    total_durasi = df["Duration"].sum()
    rata2_durasi = df["Duration"].mean()
    min_durasi = df["Duration"].min()
    max_durasi = df["Duration"].max()

    st.text(f"Total     : {total_durasi} Menit")
    st.text(f"Rata-rata : {rata2_durasi} Menit")
    st.text(f"Terendah  : {min_durasi} Menit")
    st.text(f"Tertinggi : {max_durasi} Menit")

# SUB MENU QUERY (Language dan Genre)
elif "Sub Menu Query" in menu:
    st.subheader("Sub Menu Query (Language dan Genre)")

    # Input bahasa dan genre
    selected_lang = st.text_input("Masukkan Bahasa (Spasi untuk Kembali):")
    if selected_lang.strip() != "":
        selected_genre = st.text_input("Masukkan Genre (Spasi untuk Kembali):")
        if selected_genre.strip() != "":
            # Filter data
            filtered_df = df[(df["Language"] == selected_lang) & (df["Genre"] == selected_genre)]

            if not filtered_df.empty:
                st.write(f"List 5 Film dengan Genre **{selected_genre}** dan Bahasa **{selected_lang}**")
                st.dataframe(filtered_df[["Title", "Release Date", "Gross Revenue", "Budget"]].head(5))

                # Total Film
                total_film = len(filtered_df)
                st.success(f"Total Film Genre {selected_genre} dan {selected_lang} adalah: {total_film} Film")

                # Resume Durasi
                total_duration = filtered_df["Duration"].sum()
                avg_duration = filtered_df["Duration"].mean()
                min_duration = filtered_df["Duration"].min()
                max_duration = filtered_df["Duration"].max()

                min_durasi_film = filtered_df.loc[filtered_df["Duration"].idxmin(), ["Title", "Lead Actor"]]
                max_durasi_film = filtered_df.loc[filtered_df["Duration"].idxmax(), ["Title", "Lead Actor"]]

                st.markdown("### Durasi Film")
                st.text(f"Total Durasi  : {total_duration} Menit")
                st.text(f"Rata-rata     : {avg_duration} Menit")
                st.text(f"Durasi Terendah: {min_duration} Menit, "
                        f"Lead Actor: {min_durasi_film['Lead Actor']}, Title: [{min_durasi_film['Title']}]")
                st.text(f"Durasi Tertinggi: {max_duration} Menit, "
                        f"Lead Actor: {max_durasi_film['Lead Actor']}, Title: [{max_durasi_film['Title']}]")

                # Resume Gross Revenue
                total_gross = filtered_df["Gross Revenue"].sum()
                avg_gross = filtered_df["Gross Revenue"].mean()
                min_gross = filtered_df["Gross Revenue"].min()
                max_gross = filtered_df["Gross Revenue"].max()

                min_gross_film = filtered_df.loc[filtered_df["Gross Revenue"].idxmin(), ["Title", "Lead Actor"]]
                max_gross_film = filtered_df.loc[filtered_df["Gross Revenue"].idxmax(), ["Title", "Lead Actor"]]

                st.markdown("### Gross Revenue")
                st.text(f"Total Gross Revenue : ${total_gross}")
                st.text(f"Rata-rata Gross     : ${avg_gross}")
                st.text(f"Gross Terendah      : ${min_gross}, "
                        f"Lead Actor: {min_gross_film['Lead Actor']}, Title: [{min_gross_film['Title']}]")
                st.text(f"Gross Tertinggi     : ${max_gross}, "
                        f"Lead Actor: {max_gross_film['Lead Actor']}, Title: [{max_gross_film['Title']}]")

            else:
                st.warning("Data tidak ditemukan untuk bahasa dan genre yang dipilih.")


elif "Exit" in menu:
    st.info("Silakan tutup aplikasi jika ingin keluar.")
