import streamlit as st

st.set_page_config(page_title="Mindful-Remaja by Isra", page_icon="💜", layout="centered")

st.title("💜 MINDFUL-REMAJA BY ISRA")
st.caption("Skrining, Edukasi & Terapi Remaja 15-24 Tahun | Evidence-Based Kemenkes & WHO")
st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["📝 SRQ-20", "🧠 DASS-21", "📚 Edukasi", "🎵 Musik Terapi"])

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
    st.subheader("Edukasi Kesehatan Mental")
    st.markdown("""
    **I-NAMHS 2022: 1 dari 3 remaja Indonesia bermasalah mental.**
    **Tanda bahaya >2 minggu:** Menutup diri, nilai anjlok, bicara ingin mati.
    **T.D.T.H (Kemenkes):** Tanya - Dengarkan tanpa hakimi - Temani - Hubungkan ke bantuan.
    **Hubungi SEGERA: SEJIWA 119 ext 8 (24 jam)**
    """)

with tab4:
    st.subheader("Musik Terapi 60-80 BPM")
    st.write("Referensi: de Witte 2022, WHO 2023. Menurunkan kortisol.")
    pilihan = st.selectbox("Pilih:", ["Relaksasi","Fokus Belajar","Tidur","Calming"])
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    st.success(f"Mode {pilihan} aktif - Putar 15 menit dengan napas 4-7-8")

st.markdown("---")
st.caption("© 2026 Mindful-Remaja by Isra | Berbasis Evidence Kemenkes, WHO, I-NAMHS | Bukan diagnosis")
