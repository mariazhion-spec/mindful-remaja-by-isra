import streamlit as st

st.set_page_config(page_title="Mindful-Remaja by Isra", page_icon="💜", layout="centered")
# --- FITUR BARU: UMUR + HOTLINE DARURAT ---
st.sidebar.markdown("### 👤 Profil")
umur_kategori = st.sidebar.selectbox("Pilih Usia:", ["15-18 th (Remaja)", "19-24 th (Mahasiswa)", "25+ th (Dewasa)"])
st.sidebar.info(f"Anda: {umur_kategori}")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🚨 TOMBOL DARURAT")
st.sidebar.error("Jika ada pikiran ingin menyakiti diri")
st.sidebar.link_button("📞 HUBUNGI SEJIWA 119 ext 8 (24 JAM)", "tel:119", type="primary", use_container_width=True)
st.sidebar.link_button("💬 Chat WA SEJIWA", "https://wa.me/628111385353")

st.title("💜 MINDFUL-REMAJA BY ISRA")
st.caption(f"Skrining, Edukasi & Terapi {umur_kategori} | Evidence-Based Kemenkes & WHO")
st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["📋 SRQ-20", "🧠 DASS-21", "📚 Edukasi", "🎵 Musik Terapi"])
with tab1:
    st.subheader("SRQ-20 - Cek Kesehatan Gratis Kemenkes")
    st.info("Jawab YA/TIDAK. Dalam 30 hari terakhir.")
    q_srq = ["Sakit kepala","Nafsu makan buruk","Tidur tidak nyenyak","Mudah takut","Tangan gemetar","Gugup tegang","Pencernaan buruk","Sulit berpikir jernih","Tidak bahagia","Menangis lebih","Sulit menikmati","Sulit keputusan","Pekerjaan terbengkalai","Tidak mampu berperan","Kehilangan minat","Merasa tidak berharga","Pikiran akhiri hidup","Lelah sepanjang waktu","Perut tidak enak","Mudah lelah"]
    ans_srq = []
    for i,q in enumerate(q_srq):
        ans_srq.append(st.radio(f"{i+1}. {q}", ["Tidak","Ya"], key=f"s{i}", horizontal=True))
    if st.button("Lihat Hasil SRQ-20"):
        skor = ans_srq.count("Ya")
        if skor >= 6:
            st.error(f"Skor {skor}/20 - TERINDIKASI. Segera ke Puskesmas/Psikolog. Cut-off Kemenkes >=6")
        else:
            st.success(f"Skor {skor}/20 - Tidak terindikasi gangguan emosional")

with tab2:
    st.subheader("DASS-21 - Depresi Cemas Stres")
    st.caption("0=Tidak Pernah, 1=Kadang, 2=Sering, 3=Sangat Sering | Validasi Indonesia: Zatrahadi 2020")
    q_dass = [("Sulit beristirahat","s"),("Mulut kering","a"),("Tidak merasa positif","d"),("Sulit bernafas","a"),("Sulit memulai","d"),("Bereaksi berlebihan","s"),("Gemetar","a"),("Gugup","s"),("Khawatir dipermalukan","a"),("Tidak ada harapan","d"),("Gelisah","s"),("Sulit rileks","s"),("Sedih tertekan","d"),("Tidak toleran","s"),("Hampir panik","a"),("Tidak antusias","d"),("Tidak berharga","d"),("Mudah tersinggung","s"),("Jantung berdebar","a"),("Takut tanpa alasan","a"),("Hidup tidak berarti","d")]
    skor_d = skor_a = skor_s = 0
    for i,(q,k) in enumerate(q_dass):
        v = st.slider(f"{i+1}. {q}", 0,3,0, key=f"d{i}")
        if k=="d": skor_d+=v
        elif k=="a": skor_a+=v
        else: skor_s+=v
    if st.button("Hitung DASS-21"):
        D,A,S = skor_d*2, skor_a*2, skor_s*2
        st.write(f"**Depresi: {D} | Cemas: {A} | Stres: {S}**")
        st.warning("Jika Skor Sedang-Berat, disarankan konseling profesional.")
        st.info("Normal D<=9 A<=7 S<=14 | Ringan D<=13 A<=9 S<=18 | Sedang D<=20 A<=14 S<=25")

with tab3:
    st.subheader("📚 Edukasi Mindful Remaja - Evidence Based")
    st.caption("Materi: Kemenkes RI, WHO, & UNICEF - Untuk Usia 15-24 Tahun")
    
    edu_pilihan = st.selectbox("Pilih Topik Edukasi:", 
        ["🧠 Kenali Emosi", "🌬️ Teknik Napas & Mindfulness", "💬 Pertolongan Pertama Psikologis", "🚫 Mitos vs Fakta", "🎥 Video Edukasi"])

    if "Kenali Emosi" in edu_pilihan:
        st.markdown("### 🧠 Kenali Emosi - Roda Emosi Plutchik")
        st.info("Remaja 15-24 tahun sering mengalami mood swing karena hormon & tekanan sosial. Itu NORMAL!")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **4 Emosi Dasar Remaja:**
            - 😊 **Senang**: Dopamin naik saat dapat likes, pujian
            - 😢 **Sedih**: Saat ditolak, nilai turun, putus
            - 😡 **Marah**: Saat dibatasi, dibanding-bandingkan
            - 😨 **Takut/Cemas**: Ujian, masa depan, FOMO
            """)
        with col2:
            st.markdown("""
            **Cara Kelola Sehat:**
            1.  Beri nama emosi: "Aku lagi cemas karena..."
            2.  Skala 1-10, seberapa kuat?
            3.  Tulis di jurnal 3 menit
            4.  Cerita ke teman aman
            """)
        st.success("Latihan: Hari ini kamu dominan emosi apa? Tulis 1 kalimat di buku!")

    elif "Teknik Napas" in edu_pilihan:
        st.markdown("### 🌬️ Teknik Napas 4-7-8 (Evidence-Based WHO)")
        st.write("Teknik ini menurunkan detak jantung & cortisol dalam 2 menit - sudah diuji Kemenkes!")
        st.video("https://www.youtube.com/watch?v=8vkBvMGP2v4")
        st.markdown("""
        **Langkah (Ikuti bareng):**
        1.  Tarik napas lewat hidung **4 detik**
        2.  Tahan **7 detik**
        3.  Buang lewat mulut **8 detik** (bunyi whoosh)
        4.  Ulangi 3x
        """)
        if st.button("Mulai Latihan 1 Menit"):
            st.balloons()
            st.success("Hebat! Lakukan ini tiap mau ujian / susah tidur ya!")

    elif "Pertolongan" in edu_pilihan:
        st.markdown("### 💬 Pertolongan Pertama Psikologis - T.A.N.Y.A")
        st.warning("**TANYA = Tanya, Dengarkan, Nyaman-kan, Ajak bantuan - Model Kemenkes SEJIWA**")
        st.markdown("""
        **Jika teman bilang "pengen ngilang / gak berharga":**
        - **T**anya: "Kamu lagi kepikiran apa? Aku dengerin"
        - **A**nti menghakimi: Jangan bilang "lebay ah" / "kurang iman"
        - **N**yamankan: "Aku di sini, kamu gak sendiri"
        - **Y**akinkan bantuan: "Mau kita hubungi Guru BK / SEJIWA 119 ext 8 bareng?"
        - **A**jari self-care: Napas, minum air, jalan kaki
        """)
        st.error("🚨 Jika ada rencana bunuh diri DETAIL, hubungi SEGERA: SEJIWA 119 ext 8 (24 jam) atau Puskesmas terdekat!")

    elif "Mitos" in edu_pilihan:
        st.markdown("### 🚫 Mitos vs Fakta Kesehatan Mental Remaja")
        mitos = st.radio("Pilih Mitos yang sering kamu dengar:", 
            ["Curhat = Lemah", "Mental health = Kurang ibadah", "Self-harm buat cari perhatian"])
        if "Curhat" in mitos:
            st.markdown("**FAKTA:** Curhat itu KEKUATAN! Otak remaja butuh co-regulasi. WHO bilang remaja yang punya 1 orang dewasa aman 60% lebih resilient.")
        elif "ibadah" in mitos:
            st.markdown("**FAKTA:** Ibadah penting untuk spiritual, tapi gangguan mental itu medis seperti demam. Perlu 2 sayap: spiritual + profesional. Kemenkes & MUI sepakat.")
        else:
            st.markdown("**FAKTA:** Self-harm itu sinyal rasa sakit yang tak terucapkan, BUKAN caper. 80% remaja melakukannya untuk mengurangi rasa tidak nyaman, bukan cari perhatian.")
    
    else:
        st.markdown("### 🎥 Video Edukasi 3 Menit")
        st.write("Pilih video sesuai kebutuhanmu:")
        st.video("https://www.youtube.com/watch?v=7z8g5dB5R4Q")
        st.caption("Sumber: Direktorat Kesehatan Jiwa Kemenkes RI - Remaja Sehat Jiwa")
        st.link_button("Download Poster Edukasi Gratis Kemenkes", "https://www.kemkes.go.id")
with tab4:
    st.subheader("Musik Terapi Sesuai Anjuran WHO 60-80 BPM")
    st.caption("Tanpa lirik, instrumental lembut, volume 40-60 dB - untuk turunkan cemas")
    mode = st.selectbox("Pilih Kebutuhan:", ["🧘 Relaksasi 60 BPM - Piano Lembut", "📚 Fokus 75 BPM - Lofi Tenang", "😌 Calming Cemas - Suara Alam", "😴 Tidur 50 BPM - Musik Tidur"])

    if "Relaksasi" in mode:
        st.audio("https://www.bensound.com/bensound-music/bensound-slowmotion.mp3")
        st.caption("Relaksasi: 60 BPM Piano lembut - detak jantung istirahat - WHO ✅")
    elif "Fokus" in mode:
        st.audio("https://www.bensound.com/bensound-music/bensound-pianomoment.mp3")
        st.caption("Fokus: 75 BPM tanpa lirik - untuk belajar konsentrasi ✅")
    elif "Calming" in mode:
        st.audio("https://www.bensound.com/bensound-music/bensound-anewbeginning.mp3")
        st.caption("Calming: 60 BPM flute + alam - untuk cemas turun ✅")
    else:
        st.audio("https://www.bensound.com/bensound-music/bensound-sweetdreams.mp3")
        st.caption("Tidur: 50 BPM lembut malam - atur volume 40% ✅")

    st.info("💡 Atur volume HP 40-60% saja ya, jangan keras. Dengarkan 15-30 menit, 2x sehari sesuai anjuran Kemenkes.")
