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

tab1, tab2, tab3, tab4, tab5 = st.tabs(["😟 SRQ-20", "🧠 DASS-21", "📚 Edukasi", "🎵 Musik Terapi", "🎓 8 Modul + Sertifikat"])
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
    pertanyaan_srq = [
        "Sering sakit kepala?", "Nafsu makan buruk?", "Tidur tidak nyenyak?",
        "Mudah takut?", "Tangan gemetar?", "Merasa gugup?",
        "Pencernaan buruk?", "Sulit berpikir jernih?", "Merasa tidak bahagia?",
        "Lebih banyak menangis?", "Sulit menikmati aktivitas?", "Sulit mengambil keputusan?",
        "Pekerjaan terganggu?", "Tidak mampu berperan?", "Kehilangan minat?",
        "Merasa tidak berharga?", "Pikiran mengakhiri hidup?", "Selalu merasa lelah?",
        "Perasaan tidak nyaman di perut?", "Mudah lelah?"
    ]
    skor_srq = 0
    for i, q in enumerate(pertanyaan_srq):
        jawab = st.radio(f"{i+1}. {q}", ["Tidak", "Ya"], key=f"srq{i}", horizontal=True)
        if jawab == "Ya": skor_srq += 1
    st.divider()
    if skor_srq >= 6:
        st.error(f"Skor SRQ-20 kamu: {skor_srq} / 20 - Terdeteksi gejala, disarankan konseling")
    else:
        st.success(f"Skor SRQ-20 kamu: {skor_srq} / 20 - Normal")
    st.info("Normal <6 | Butuh perhatian >=6 (WHO)")

with tab2:
    st.subheader("DASS-21 - Depresi Cemas Stres")
    st.caption("Validasi Indonesia - Zatrahadi 2020")
    dass_q = [
        ("Saya sulit beristirahat", "S"), ("Saya sadar mulut saya kering", "A"), ("Saya tidak bisa merasakan hal positif", "D"),
        ("Saya sesak napas", "A"), ("Sulit memulai sesuatu", "D"), ("Saya bereaksi berlebihan", "S"),
        ("Tangan gemetar", "A"), ("Saya cemas berlebihan", "S"), ("Khawatir situasi memalukan", "A"),
        ("Merasa tidak ada harapan", "D"), ("Merasa gelisah", "S"), ("Sulit rileks", "S"),
        ("Sedih & tertekan", "D"), ("Tidak toleran gangguan", "S"), ("Hampir panik", "A"),
        ("Tidak antusias", "D"), ("Merasa tidak berharga", "D"), ("Mudah tersinggung", "S"),
        ("Denyut jantung keras", "A"), ("Takut tanpa alasan", "A"), ("Merasa hidup tak berarti", "D")
    ]
    skor_d = skor_a = skor_s = 0
    for i, (tanya, kode) in enumerate(dass_q):
        nilai = st.selectbox(f"{i+1}. {tanya}", [0,1,2,3], format_func=lambda x: f"{x} - {'Tidak pernah' if x==0 else 'Kadang' if x==1 else 'Sering' if x==2 else 'Sangat sering'}", key=f"dass{i}")
        if kode=="D": skor_d+=nilai
        elif kode=="A": skor_a+=nilai
        else: skor_s+=nilai
    D,A,S = skor_d*2, skor_a*2, skor_s*2
    st.divider()
    st.write(f"**Depresi: {D} | Cemas: {A} | Stres: {S}**")
    st.warning("Jika Skor Sedang-Berat, disarankan konseling profesional.")
    st.info("Normal D<=9 A<=7 S<=14 | Ringan D<=13 A<=9 S<=18 | Sedang D<=20 A<=14 S<=25")
with tab3:
    st.subheader("Edukasi Kesehatan Mental Remaja")
    st.caption("Sumber: Buku Pertolongan Pertama Luka Psikologis Kemenkes RI & WHO mhGAP")
    
    st.info("Ingat ya: 1 dari 3 remaja Indonesia pernah merasa seperti kamu. Kamu tidak sendiri. Ini normal (I-NAMHS 2022)")
    
    topik = st.selectbox("Pilih topik yang ingin kamu baca:", 
        ["Cara Tolong Teman", "Grounding 5-4-3-2-1", "Napas Kotak", "Cara Jadi First Aider di Sekolah"])
    
    if topik == "Cara Tolong Teman":
        st.markdown("### Cara Tolong Teman")
        st.write("1. Dengarkan tanpa menghakimi\n2. Katakan 'Aku di sini buat kamu'\n3. Jangan janji rahasiakan kalau ada bahaya\n4. Ajak ke Guru BK / orang dewasa yang dipercaya")
    elif topik == "Grounding 5-4-3-2-1":
        st.markdown("### Teknik Grounding 5-4-3-2-1")
        st.write("Saat cemas: Sebut 5 hal dilihat, 4 hal disentuh, 3 hal didengar, 2 hal dicium, 1 hal dirasa")
    elif topik == "Napas Kotak":
        st.markdown("### Napas Kotak (Box Breathing)")
        st.write("Tarik napas 4 detik - Tahan 4 detik - Hembus 4 detik - Tahan 4 detik. Ulangi 4x")
    else:
        st.markdown("### Cara Jadi First Aider di Sekolah")
        st.write("Lihat perubahan, dekati pelan, jangan janji rahasiakan jika self-harm, hubungkan ke Guru BK / 119 ext 8")
    
    st.divider()
    st.success("Jika sangat berat / ada pikiran menyakiti diri: Hubungi 119 ext 8 (Kemenkes 24 Jam GRATIS)")
    
    # INI TOMBOL DOWNLOAD POSTER NYA BU - SUDAH JADI
    st.markdown("### 📥 Download Poster Edukasi")
    poster_content = """
    POSTER EDUKASI KESEHATAN MENTAL REMAJA
    KEMENKES RI x WHO mhGAP
    
    CARA JADI FIRST AIDER DI SEKOLAH:
    1. LIHAT - Lihat perubahan perilaku teman
    2. DEKATI - Dekati pelan dengan empati
    3. DENGARKAN - Dengarkan tanpa menghakimi
    4. HUBUNGKAN - Hubungkan ke Guru BK / 119 ext 8
    
    Ingat: 1 dari 3 remaja pernah merasa seperti kamu.
    Kamu Tidak Sendiri!
    
    Hotline: 119 ext 8 - GRATIS 24 Jam
    """
    st.download_button(
        label="📥 Download Poster Edukasi Gratis Kemenkes",
        data=poster_content,
        file_name="Poster_Edukasi_Kesehatan_Mental_Remaja.txt",
        mime="text/plain"
    )
    st.caption("Bisa di-download dan di-print untuk ditempel di sekolah Bu!")# ================= TAB 4 MUSIK TERAPI + DOWNLOAD - DIKEMBALIKAN =================
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
with tab5:
    st.subheader("📚 Edukasi Lengkap 8 Modul - Video, Jurnal, Quiz & Sertifikat")
    st.caption("Ini yang ada di poster promosi Ibu yang dilingkari hijau!")
    st.info("Selesaikan 8 modul untuk dapat Sertifikat First Aider!")

    if 'modul_selesai' not in st.session_state:
        st.session_state.modul_selesai = [False]*8
        st.session_state.jurnal = [""]*8

    modul_list = [
        {"judul": "MODUL 1: Kenali Emosi", "video": "https://www.youtube.com/watch?v=5qap5aO4i9A", "materi": "Kenali emosi: Senang, Sedih, Marah, Takut."},
        {"judul": "MODUL 2: Cemas & Overthinking", "video": "https://www.youtube.com/watch?v=O-6f5wQXSu8", "materi": "Grounding 5-4-3-2-1 + Napas Kotak"},
        {"judul": "MODUL 3: Sedih Berkepanjangan", "video": "https://www.youtube.com/watch?v=3-s0UIYc7o4", "materi": "Jurnal 3 Hal Baik & Gerak 15 menit"},
        {"judul": "MODUL 4: Stres Tugas", "video": "https://www.youtube.com/watch?v=ZToicYcHIOU", "materi": "Pomodoro 25-5"},
        {"judul": "MODUL 5: T.A.N.Y.A Self-Harm", "video": "https://www.youtube.com/watch?v=5D2E6z0m6cA", "materi": "TANYA, DENGARKAN, HUBUNGKAN 119 ext 8"},
        {"judul": "MODUL 6: Jadi First Aider", "video": "https://www.youtube.com/watch?v=Db9yrH8N9c8", "materi": "LIHAT-DEKATI-DENGARKAN-HUBUNGKAN"},
        {"judul": "MODUL 7: Napas 4-7-8 WHO", "video": "https://www.youtube.com/watch?v=YRPhh4Ybb_g", "materi": "Tarik 4 Tahan 7 Hembus 8"},
        {"judul": "MODUL 8: Sertifikat", "video": "https://www.youtube.com/watch?v=ZbZSe6N_BXs", "materi": "Review & Ambil Sertifikat!"}
    ]

    progress = sum(st.session_state.modul_selesai) / 8
    st.progress(progress, text=f"Progress: {int(progress*100)}% - {sum(st.session_state.modul_selesai)}/8 Modul")

    pilih = st.selectbox("Pilih Modul:", [f"{i+1}. {m['judul']}" for i,m in enumerate(modul_list)], key="pilih_modul5")
    idx = int(pilih.split(".")[0]) - 1
    m = modul_list[idx]

    st.markdown(f"### {m['judul']}")
    st.video(m['video'])
    st.info(m['materi'])

    st.markdown("#### 📝 Jurnal Refleksi")
    st.session_state.jurnal[idx] = st.text_area("Tulis refleksimu:", value=st.session_state.jurnal[idx], key=f"jurnal5_{idx}")

    st.markdown("#### ❓ Quiz Mini")
    q = st.radio("Sudah paham & akan praktek?", ["Sudah paham & Ya", "Belum"], key=f"quiz5_{idx}")

    if st.button(f"✅ Selesaikan {m['judul']}", key=f"btn5_{idx}"):
        if st.session_state.jurnal[idx].strip()!="" and q=="Sudah paham & Ya":
            st.session_state.modul_selesai[idx]=True
            st.success("Modul selesai!")
            st.balloons()
        else:
            st.warning("Isi Jurnal dulu & pilih Sudah paham ya!")

    if sum(st.session_state.modul_selesai)==8:
        st.divider()
        st.success("🎉 SELAMAT 8 MODUL SELESAI!")
        nama = st.text_input("Nama untuk Sertifikat:", "Isra - First Aider", key="nama_cert5")
        if st.button("🎓 Download Sertifikat", key="dl_cert5"):
            cert = f"SERTIFIKAT First Aider - {nama} - Telah menyelesaikan 8 Modul Mindful Remaja by Isra - Kemenkes x WHO 2026"
            st.download_button("📜 Download Sertifikat", data=cert, file_name=f"Sertifikat_{nama}.txt", key="dl_btn5")
            st.balloons()
