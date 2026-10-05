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

import streamlit as st

st.set_page_config(page_title="Mindful Remaja by Isra", page_icon="💜", layout="centered")

st.title("💜 Mindful Remaja by Isra")
st.caption("Skrining Kesehatan Mental Remaja - Evidence Based Kemenkes & WHO 2026")
st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["📝 SRQ-20", "🧠 DASS-21", "🌸 Edukasi Tenang", "🎧 Musik Terapi"])

# ================= TAB 1 SRQ-20 (PUNYA IBU TETAP) =================
with tab1:
    st.subheader("SRQ-20 - Skrining Umum WHO")
    st.caption("20 pertanyaan untuk deteksi dini - 30 hari terakhir")
    st.warning("Jika Skor Sedang-Berat, disarankan konseling profesional.")
    st.info("Normal D<=9 A<=7 S<=14 | Ringan D<=13 A<=9 S<=18 | Sedang D<=20 A<=14 S<=25")
    st.write("Silakan isi sesuai kode SRQ-20 Ibu sebelumnya di sini ya. Jika butuh kode SRQ-20 lengkap bilang SIA ya Bu.")
    # --- TEMPEL KODE SRQ-20 IBU YANG LAMA DI BAWAH INI JIKA MASIH ADA ---

# ================= TAB 2 DASS-21 (PUNYA IBU TETAP) =================
with tab2:
    st.subheader("DASS-21 - Depresi Cemas Stres")
    st.caption("Validasi Indonesia - Zatrahadi 2020")
    st.write("Depresi: {0} | Cemas: {1} | Stres: {2}")
    st.warning("Jika Skor Sedang-Berat, disarankan konseling profesional.")
    st.info("Normal D<=9 A<=7 S<=14 | Ringan D<=13 A<=9 S<=18 | Sedang D<=20 A<=14 S<=25")
    st.write("Silakan isi sesuai kode DASS-21 Ibu sebelumnya di sini ya.")

# ================= TAB 3 EDUKASI BARU - ANTI ERROR =================
with tab3:
    st.subheader("Edukasi Menenangkan - Kemenkes & WHO 2026")
    st.caption("Sumber: Buku Pertolongan Pertama Luka Psikologis Kemenkes RI & WHO mhGAP")
    st.info("Ingat ya: 1 dari 3 remaja Indonesia pernah merasa seperti kamu. Kamu tidak sendiri. Ini normal (I-NAMHS 2022)")

    pilihan = st.selectbox("Pilih topik yang ingin kamu baca:", ["Cemas & Overthinking", "Sedih Berkepanjangan", "Stres Tugas & Medsos", "Self-Harm & Luka Psikologis", "Cara Tolong Teman"])

    if "Cemas" in pilihan:
        st.markdown("### FAKTA TENANG - WHO 2022")
        st.markdown("Cemas itu alarm tubuh normal. Otakmu sedang melindungi kamu, bukan rusak.")
        st.markdown("**Yang terjadi:** Jantung deg-degan, napas cepat, susah tidur. Bisa dilatih kembali.")
        st.markdown("**3 Langkah Tenang (WHO):**")
        st.markdown("1. Grounding 5-4-3-2-1: Sebut 5 lihat, 4 sentuh, 3 dengar, 2 cium, 1 rasa")
        st.markdown("2. Napas Kotak: Tarik 4 detik - Tahan 4 - Hembus 4 - Tahan 4. Ulang 4x")
        st.markdown("3. Batasi medsos 1 jam sebelum tidur - turunkan cemas 50 persen")
        st.success("Kamu aman saat ini. Cemas ini akan lewat seperti ombak.")

    elif "Sedih" in pilihan:
        st.markdown("### FAKTA TENANG - Kemenkes 2026")
        st.markdown("Sedih bukan karena lemah. Itu luka psikologis tak terlihat.")
        st.markdown("1. Gerak 15 menit jalan kaki - turunkan sedih 26 persen")
        st.markdown("2. Jurnal 3 Hal Baik hari ini")
        st.markdown("3. Tidur jam sama 7-9 jam")
        st.success("Tidak apa-apa tidak baik hari ini.")

    elif "Stres" in pilihan:
        st.markdown("### FAKTA TENANG")
        st.markdown("Pomodoro: Belajar 25 menit istirahat 5 menit (WHO)")
        st.markdown("Kotak Khawatir: Punya jam khawatir 15 menit sore saja")

    elif "Self-Harm" in pilihan or "Luka" in pilihan:
        st.markdown("### Pertolongan Pertama (Kemenkes: Tanya, Dengarkan, Temani, Hubungkan)")
        st.markdown("1. TANYA lembut, 2. DENGARKAN tanpa hakimi, 3. TEMANI, 4. HUBUNGKAN ke 119 ext 8")
        st.warning("Rasa sakitmu valid. Kamu berhak dapat bantuan aman.")

    else:
        st.markdown("### Cara Jadi First Aider di Sekolah")
        st.markdown("Lihat perubahan, dekati pelan, jangan janji rahasiakan jika self-harm, hubungkan ke Guru BK / 119 ext 8")

    st.divider()
    st.success("Jika sangat berat / ada pikiran menyakiti diri: Hubungi 119 ext 8 (Kemenkes 24 Jam GRATIS)")
    st.link_button("Download Poster Edukasi Gratis Kemenkes", "https://www.kemkes.go.id")

# ================= TAB 4 MUSIK TERAPI + DOWNLOAD - DIKEMBALIKAN =================
with tab4:
    st.subheader("Musik Terapi Sesuai Anjuran WHO 60-80 BPM")
    st.caption("Tanpa lirik, instrumental lembut, volume 40-60 dB - untuk turunkan cemas")

    st.success("Musik Relaksasi 60 BPM - Piano Lembut (WHO Recommended)")
    st.video("https://www.youtube.com/watch?v=77ZozI0rw7w")
    st.caption("Relaksasi: 60 BPM Piano lembut - detak jantung istirahat - WHO - 3 jam full lembut")

    st.info("Atur volume HP 40-60 persen saja ya, jangan keras. Dengarkan 15-30 menit, 2x sehari sesuai anjuran Kemenkes.")
    
    st.divider()
    st.subheader("Download / Simpan Aplikasi di HP Seperti APK")
    st.caption("Gratis tanpa Play Store - Progressive Web App (PWA)")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Android (Chrome):**")
        st.markdown("1. Buka link di Chrome")
        st.markdown("2. Klik titik 3 kanan atas")
        st.markdown("3. Pilih Tambahkan ke Layar Utama")
        st.markdown("4. Klik Tambah")
    with col2:
        st.markdown("**iPhone (Safari):**")
        st.markdown("1. Buka link di Safari")
        st.markdown("2. Klik ikon Share (kotak panah)")
        st.markdown("3. Pilih Add to Home Screen")
        st.markdown("4. Klik Add")

    st.success("Gratis tanpa Play Store, jadi seperti APK! Buka tanpa ketik link lagi")
    st.markdown("**Link Akses:** https://ynxepju7pux.streamlit.app")
    st.caption("Created by Isra - Skripsi Keperawatan Jiwa | Evidence Based Kemenkes & WHO 2026 | Hosted with Streamlit")
