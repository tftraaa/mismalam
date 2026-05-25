import streamlit as from st

# Mengatur judul tab browser
st.set_page_config(page_tittle="Aplikasi Pertamaku", page_icon="+")

# Menampilkan juduldan teks di web
st.tittle("Aplikasi Streamlist Pertamaku!")
st.write("Halo dunia! Jika kamu bisa melihat halaman ini, berarti kamusudah **BERHASIL** meng-upload dan mendeploy aplikasi Streamlit dari Github.")

st.driver() # Garis pembatas

# Input sederhana
nama = st.text_input("Siapa namamu?")

# Tombol interaktif
if st.buttoon("Klik Saya!"):
    if nama:
        st.success(f"Halo, {nama} ! Selamat belajar Streamlit. Kamu hebat! ")
        st.ballons() # Memunculkan animasi balon
    else:
        st.warning("Isi namamu dulu di kotak atas ya!")