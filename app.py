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
    st.subheader("🌸 Edukasi Menenangkan - Sesuai Kemenkes & WHO 2026")
    st.caption("Sumber: Buku Pertolongan Pertama Luka Psikologis Kemenkes RI & WHO mhGAP")

    st.info("💜 Ingat ya: 1 dari 3 remaja Indonesia pernah merasa seperti kamu. Kamu tidak sendiri. Ini normal dan bisa dibantu (I-NAMHS 2022)")

    pilihan = st.selectbox("Pilih topik yang ingin kamu baca:",
        ["😥 Cemas & Overthinking", "😞 Sedih Berkepanjangan", "😤 Stres Tugas & Medsos", "😶 Self-Harm & Luka Psikologis", "🤝 Cara Tolong Teman"])

    if "Cemas" in pilihan:
        st.markdown("""
        **### 🌿 FAKTA TENANG - Menurut WHO 2022:**
        Cemas itu alarm tubuh yang normal. Otakmu sedang melindungi kamu, bukan rusak.

        **Yang terjadi di tubuh:** Jantung deg-degan, napas cepat, susah tidur. Itu respon stres yang bisa dilatih kembali.

        **3 Langkah Tenang (WHO Doing What Matters):**
        1. **Grounding 5-4-3-2-1:** Sebut 5 yang kamu lihat, 4 yang kamu sentuh, 3 yang kamu dengar, 2 yang kamu cium, 1 yang kamu rasa. Ini kembalikan otak ke kini.
        2. **Napas Kotak:** Tarik 4 detik - Tahan 4 detik - Hembus 4 detik - Tahan 4 detik. Ulang 4x. Volume 40-60% (Sesuai WHO 60 BPM)
        3. **Batasi Medsos:** WHO bilang, perbandingan di medsos bikin cemas naik 2x lipat. Coba puasa medsos 1 jam sebelum tidur.

        > 🕊️ *Kamu aman saat ini. Cemas ini akan lewat seperti ombak.*
        """)
    elif "Sedih" in pilihan:
        st.markdown("""
        **### 🌧️ FAKTA TENANG - Kemenkes 2026:**
        Sedih berkepanjangan bukan karena kamu lemah. Itu luka psikologis yang tak terlihat, seperti luka jatuh tapi di dalam (Wamenkes Dante Saksono).

        **Tanda yang perlu ditemani:** Tidak minat main/hobi >2 minggu, tidur berantakan, merasa tidak berharga.

        **Self-Care Evidence-Based (Kemenkes):**
        1. **Gerak 15 menit:** Jalan kaki, bukan harus olahraga berat. Riset: gerak 15 menit turunkan sedih 26%
        2. **Jurnal 3 Hal Baik:** Tulis 3 hal baik hari ini, sekecil apapun. Contoh: "Hari ini minum es teh enak"
        3. **Rutinitas Tidur:** WHO anjurkan tidur jam sama tiap hari, 7-9 jam. Matikan HP 30 menit sebelum tidur.

        > 💜 *Tidak apa-apa tidak baik-baik saja hari ini. Besok kita coba lagi pelan-pelan.*
        """)
    elif "Stres" in pilihan:
        st.markdown("""
        **### 📚 FAKTA TENANG - I-NAMHS 2022:**
        9,8% remaja stres karena tugas & medsos. Kamu termasuk banyak teman yang sama, bukan sendirian.

        **Teknik Belajar Anti Stres:**
        1. **Pomodoro:** Belajar 25 menit, istirahat 5 menit. Otak remaja fokus maksimal 25 menit (WHO)
        2. **Aturan 2 Menit:** Jika tugas <2 menit, kerjakan langsung. Jika tidak, tulis di list.
        3. **Kotak Khawatir:** Punya jam khusus khawatir 15 menit sore. Di luar jam itu, bilang "nanti aja dipikirin jam 4"
        """)
    elif "Self-Harm" in pilihan:
        st.markdown("""
        **### 🤲 FAKTA TENANG & AMAN - Kemenkes Sept 2026:**
        Self-harm itu sinyal rasa sakit yang tak terucapkan, BUKAN cari perhatian. 80% remaja melakukannya untuk atasi emosi, bukan akhiri hidup.

        **Pertolongan Pertama Luka Psikologis (Kemenkes: Tanya, Dengarkan, Temani, Hubungkan):**
        1. **TANYA** dengan lembut: "Aku lihat kamu terluka, kamu lagi berat ya?"
        2. **DENGARKAN** tanpa menghakimi. Jangan bilang "lebay". Cukup "Aku di sini dengarin"
        3. **TEMANI:** Jangan tinggalkan sendiri. Ajak aktivitas aman: cuci muka air dingin, remas es, gambar di kertas.
        4. **HUBUNGKAN:** Ajak ke orang terpercaya / Puskesmas / Call Center 119 ext 8 (24 jam Kemenkes)

        > 🌱 *Rasa sakit ini valid. Kamu berhak dapat bantuan yang aman. Kamu berharga.*
        """)
    else: # Tolong Teman
        st.markdown("""
        **### 🤝 Cara Jadi First Aider di Sekolah - Buku Kemenkes 2026:**
        Kamu tidak harus jadi psikolog untuk menolong teman!

        1. Lihat perubahan: teman yang tadinya rame jadi diam >1 minggu
        2. Dekati pelan: "Hai, aku perhatiin kamu beberapa hari ini agak beda, boleh cerita?"
        3. Jika teman bilang ingin menyakiti diri: **Jangan janji rahasiakan.** Temani dan hubungkan ke Guru BK / orang tua / 119 ext 8
        4. Jaga dirimu juga. Setelah menolong, cerita ke orang dewasa yang kamu percaya.
        """)

    st.divider()
    st.success("📞 Jika sangat berat / ada pikiran menyakiti diri: Segera Hubungi **119 ext 8** (Kemenkes 24 Jam GRATIS) atau **Puskesmas terdekat**. Kamu tidak sendiri.")with tab4:
    st.subheader("Musik Terapi Sesuai Anjuran WHO 60-80 BPM")
    st.caption("Tanpa lirik, instrumental lembut, volume 40-60 dB - untuk turunkan cemas")
    
    st.success("🎧 Musik Relaksasi 60 BPM - Piano Lembut (WHO Recommended)")
    st.video("https://www.youtube.com/watch?v=77ZozI0rw7w")
    st.caption("Relaksasi: 60 BPM Piano lembut - detak jantung istirahat - WHO ✅ - 3 jam full lembut")

    st.info("💡 Atur volume HP 40-60% saja ya, jangan keras. Dengarkan 15-30 menit, 2x sehari sesuai anjuran Kemenkes.")
st.divider()
st.subheader("📲 Download / Simpan Aplikasi di HP Seperti APK")
st.caption("Gratis tanpa Play Store - Progressive Web App (PWA)")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **🤖 Android (Chrome):**
    1. Buka link di **Chrome**
    2. Klik **titik 3** kanan atas
    3. Pilih **Tambahkan ke Layar Utama**
    4. Klik **Tambah** -> Ikon muncul!
    """)
with col2:
    st.markdown("""
    **🍎 iPhone (Safari):**
    1. Buka link di **Safari**
    2. Klik **ikon Share** (kotak panah)
    3. Pilih **Add to Home Screen**
    4. Klik **Add**
    """)

st.success("✅ Gratis tanpa Play Store, jadi seperti APK! Buka tanpa ketik link lagi, privasi aman, Didukung Kemenkes & WHO")

st.markdown("**Link Akses:** https://ynxepju7pux.streamlit.app")
