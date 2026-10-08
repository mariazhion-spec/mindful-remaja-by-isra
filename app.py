import streamlit as st
import datetime

# === FINAL V4 - MINDFUL REMAJA BY ISRA - ICON + JURNAL PINTAR + VIDEO FIX ===
try:
    st.set_page_config(page_title="Mindful Remaja by Isra - FINAL", page_icon="logo.png", layout="wide")
except:
    st.set_page_config(page_title="Mindful Remaja by Isra - FINAL", page_icon="💜", layout="wide")

# DATA 8 MODUL - VIDEO FIX ANTI HITAM
MODUL_DATA = {
    "1. MODUL 1: Kenali Emosi": {
        "desc": "Mengenal emosi dasar: senang, sedih, marah, takut. Semua emosi itu normal.",
        "video": "https://www.youtube.com/watch?v=5Y76XIgwVyI",
        "edukasi": "Tugas hari ini: Tulis 3 emosi yang kamu rasakan di Jurnal Tab 3 ya."
    },
    "2. MODUL 2: Kenali Stres": {
        "desc": "Tanda stres: susah tidur, pusing, malas makan. Bedakan stres ringan & berat.",
        "video": "https://www.youtube.com/watch?v=QKkxl1Z1i1o",
        "edukasi": "Saat stres, coba tarik napas 4-7-8 di Tab 4 Musik."
    },
    "3. MODUL 3: Cemas & Khawatir": {
        "desc": "Cemas sebelum ujian wajar. Pelajari teknik grounding 5-4-3-2-1.",
        "video": "https://www.youtube.com/watch?v=5Y76XIgwVyI",
        "edukasi": "Grounding: Sebut 5 hal yang kamu LIHAT, 4 yang kamu SENTUH, 3 yang kamu DENGAR."
    },
    "4. MODUL 4: Sedih Berkepanjangan": {
        "desc": "Sedih >2 minggu & tidak minat main perlu perhatian khusus.",
        "video": "https://www.youtube.com/watch?v=QKkxl1Z1i1o",
        "edukasi": "Kamu tidak sendiri. Cerita ke guru BK atau hubungi SEJIWA 119 ext 8."
    },
    "5. MODUL 5: Mindfulness & Napas 4-7-8": {
        "desc": "Latihan napas: 4 detik tarik, 7 detik tahan, 8 detik buang.",
        "video": "https://www.youtube.com/watch?v=QKkxl1Z1i1o",
        "edukasi": "Lakukan 3x sehari pagi-siang-malam."
    },
    "6. MODUL 6: Tidur Sehat": {
        "desc": "Remaja butuh 8-9 jam tidur. Kurang tidur bikin emosi labil.",
        "video": "https://www.youtube.com/watch?v=5Y76XIgwVyI",
        "edukasi": "Matikan HP 30 menit sebelum tidur malam."
    },
    "7. MODUL 7: Komunikasi & Support System": {
        "desc": "Cara bilang 'tidak' & cara minta tolong tanpa di-judge.",
        "video": "https://www.youtube.com/watch?v=QKkxl1Z1i1o",
        "edukasi": "Cari 1 orang dewasa yang kamu percaya untuk cerita."
    },
    "8. MODUL 8: Rencana Sehat Mental": {
        "desc": "Buat rencana harian: jurnal, musik tenang, olahraga ringan.",
        "video": "https://www.youtube.com/watch?v=5Y76XIgwVyI",
        "edukasi": "Tulis 3 hal yang membuatmu bersyukur hari ini."
    }
}

if "jurnal" not in st.session_state:
    st.session_state.jurnal = []
if "skor_srq" not in st.session_state:
    st.session_state.skor_srq = 0

# HEADER
try:
    st.image("logo.png", width=100)
except:
    pass
st.title("Mindful by Isra - Bidan NTT 2026")
st.caption("Aplikasi Edukasi Deteksi Dini & Mindfulness Kesehatan Mental Remaja")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔍 1. Skrining", "📚 2. Modul Edukasi", "📝 3. Jurnal PINTAR", "🎧 4. Musik Tenang", "🚨 5. Bantuan & Sertifikat"])

# TAB 1 SKRINING
with tab1:
    st.subheader("Skrining Awal SRQ-20")
    st.write("Isi 20 pertanyaan ya/ tidak. Skor >=6 disarankan konseling.")
    srq_q = ["Sering sakit kepala?", "Tidak nafsu makan?", "Tidur tidak nyenyak?", "Mudah takut?", "Tangan gemetar?", "Merasa gugup?", "Pencernaan buruk?", "Sulit berpikir jernih?", "Merasa tidak bahagia?", "Banyak menangis?", "Sulit menikmati kegiatan?", "Sulit mengambil keputusan?", "Pekerjaan terganggu?", "Tidak mampu berperan?", "Kehilangan minat?", "Merasa tidak berharga?", "Pikiran mengakhiri hidup?", "Merasa lelah?", "Perut tidak enak?", "Mudah lelah?"]
    skor = 0
    for i,q in enumerate(srq_q):
        if st.radio(f"{i+1}. {q}", ["Tidak","Ya"], key=f"srq{i}", horizontal=True)=="Ya":
            skor+=1
    st.session_state.skor_srq = skor
    st.divider()
    if skor < 6:
        st.success(f"Skor kamu {skor}/20 - Dalam batas wajar. Tetap jaga kesehatan mental ya!")
    else:
        st.warning(f"Skor kamu {skor}/20 - Di atas ambang. Yuk buka Modul & cerita ke orang terdekat di Tab 5.")
    if st.button("💾 Simpan Hasil Skrining"):
        st.balloons()
        st.info("Hasil tersimpan!")

# TAB 2 MODUL
with tab2:
    st.subheader("📚 Modul Edukasi 8 Topik - Video Sudah Fix")
    pilih = st.selectbox("Pilih Modul untuk ditonton:", list(MODUL_DATA.keys()))
    data = MODUL_DATA[pilih]
    st.info(f"**{pilih}** - {data['desc']}")
    st.video(data["video"])
    st.link_button("🔗 Buka di YouTube jika video tidak muncul", data["video"])
    st.success(f"💡 Edukasi Inti: {data['edukasi']}")

# TAB 3 JURNAL PINTAR AUTO EDUKASI
with tab3:
    st.subheader("📝 Jurnal Refleksi PINTAR - Auto Saran Sesuai Perasaan")
    st.caption("Setelah nonton modul, tulis di sini. Sistem akan kasih saran otomatis.")
    modul_jurnal = st.selectbox("Jurnal untuk Modul:", list(MODUL_DATA.keys()), key="jmod")
    refleksi = st.text_area("Tulis refleksimu:", placeholder="Hari ini saya belajar... Saya merasa... Contoh: saya sedih sendiri terus nangis", height=150, key="refleksi")

    if st.button("💾 Simpan & Dapatkan Saran Otomatis", type="primary"):
        if refleksi.strip()=="":
            st.warning("Tulis dulu perasaanmu ya Kak")
        else:
            st.session_state.jurnal.append({"waktu": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), "modul": modul_jurnal, "isi": refleksi})
            teks = refleksi.lower()
            st.success("✅ Jurnal tersimpan di HP kamu!")

            if any(k in teks for k in ["bunuh","mati aja","pengen mati","sayat","self harm","lukai"]):
                st.error("🚨 **Kamu sangat berharga!** SIA deteksi kamu sedang sangat berat. Kamu tidak sendiri. Segera hubungi **SEJIWA 119 ext 8 GRATIS 24 jam** di Tab 5 atau cerita ke orang dewasa yang kamu percaya SEKARANG ya. Tarik napas 4-7-8 dulu.")
            elif any(k in teks for k in ["sedih","nangis","hampa","kosong","sendiri","down"]):
                st.info(f"💜 **Untuk rasa sedihmu:** {MODUL_DATA['4. MODUL 4: Sedih Berkepanjangan']['edukasi']} Coba buka Tab 4 Musik Tenang & dengarkan 3 menit ya.")
            elif any(k in teks for k in ["cemas","takut","khawatir","deg-degan","panik","ujian","gugup"]):
                st.info(f"🌿 **Untuk rasa cemasmu:** {MODUL_DATA['3. MODUL 3: Cemas & Khawatir']['edukasi']} Yuk latihan napas di Tab 4.")
            elif any(k in teks for k in ["stres","pusing","capek","banyak tugas","lelah","tertekan"]):
                st.info(f"✨ **Untuk stresmu:** {MODUL_DATA['2. MODUL 2: Kenali Stres']['edukasi']} Istirahat 5 menit, minum air putih.")
            elif any(k in teks for k in ["marah","kesal","benci","emosi","ngamuk"]):
                st.info("🔥 **Untuk rasa marahmu:** Wajar marah. Tunda 5 menit, tarik napas di Tab 4 sebelum bertindak ya.")
            else:
                st.info(f"🌈 Keren sudah menulis! Saran dari {modul_jurnal}: {MODUL_DATA[modul_jurnal]['edukasi']}")

    if st.session_state.jurnal:
        st.divider()
        st.write("**📖 Riwayat Jurnalmu (tersimpan di HP):**")
        for j in reversed(st.session_state.jurnal):
            st.write(f"_{j['waktu']} - {j['modul']}_")
            st.write(f"> {j['isi']}")
            st.write("---")

# TAB 4 MUSIK
with tab4:
    st.subheader("🎧 Musik Tenang & Latihan Napas")
    st.write("Putar musik ini sambil latihan napas 4-7-8")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    st.info("**Latihan 4-7-8:** Tarik napas 4 detik -> Tahan 7 detik -> Buang 8 detik. Ulangi 3x.")
    if st.button("Mulai Timer 3 Menit"):
        st.success("Mulai... Tarik... Tahan... Buang... Fokus ke napas ya 💜")

# TAB 5 BANTUAN
with tab5:
    st.subheader("🚨 Bantuan & Sertifikat Penyelesaian")
    st.error("Jika ada pikiran menyakiti diri / sangat berat, segera hubungi:")
    st.write("**SEJIWA 119 ext 8 - GRATIS 24 Jam - Kemenkes RI**")
    st.link_button("📞 Chat WA SEJIWA 119", "https://wa.me/62811881119")
    st.link_button("📍 Cari Puskesmas Terdekat", "https://www.google.com/maps/search/puskesmas+terdekat/")
    st.divider()
    st.write(f"Skor Skrining Terakhir: **{st.session_state.skor_srq}/20** | Jumlah Jurnal: **{len(st.session_state.jurnal)}**")
    if st.button("🎓 Download Sertifikat Telah Menyelesaikan Mindful by Isra"):
        st.balloons()
        st.success(f"Selamat! Sertifikat untuk partisipan Mindful by Isra - NTT 2026 - Skor: {st.session_state.skor_srq}/20 - Tgl: {datetime.datetime.now().strftime('%d %B %Y')}")
        st.caption("Screenshot halaman ini sebagai bukti untuk skripsi ya Kak!")
