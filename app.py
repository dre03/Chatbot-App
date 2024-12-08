import streamlit as st
from Model import ChatbotModel

# Inisialisasi model chatbot
chatbot = ChatbotModel()

# Konfigurasi antarmuka sidebar untuk percakapan
with st.sidebar:
    st.image('https://nurulfikri.ac.id/wp-content/uploads/2019/12/logo-sttnf-brand.png')
    st.title(""":blue[Chatbot STTNF]""")

    # Inisialisasi percakapan
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Kontainer untuk menampilkan riwayat percakapan
    messages_container = st.container()

    # Input pengguna
    if prompt := st.chat_input("Tulis pesan di sini:"):
        # Tambahkan pesan pengguna ke riwayat
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Dapatkan respons dari chatbot
        response = chatbot.predict_response(prompt)
        # Tambahkan respons bot ke riwayat
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Tampilkan semua pesan dalam riwayat
    with messages_container:
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.chat_message("user").write(message["content"])
            elif message["role"] == "assistant":
                st.chat_message("assistant").write(message["content"])


st.image('https://nurulfikri.ac.id/wp-content/uploads/2019/12/logo-sttnf-brand.png')
col1, col2 = st.columns([5, 4])

with col1:
    st.subheader("Sekolah Tinggi Teknologi Berfokus Membangun Talenta IT")
    st.write("STT Terpadu Nurul Fikri hadir dengan kurikulum berbasis project based-learning dan up-to-date yang menawarkan pembelajaran real industri untuk membentuk talenta digital masa depan.")

with col2:
    st.image('https://nurulfikri.ac.id/wp-content/uploads/2024/11/foto-mahasiswa.png')


st.header(":blue[Mitra Kerjasama STT Terpadu Nurul Fikri]")
st.image('https://nurulfikri.ac.id/wp-content/uploads/2023/12/Update-Kerjasama1-1536x327.png')
st.write(''':blue[Copyright © Sekolah Tinggi Teknologi Terpadu Nurul Fikri]''')