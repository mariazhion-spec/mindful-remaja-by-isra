import streamlit as st
import datetime

try:
    st.set_page_config(page_title="Mindful Remaja by Isra - FINAL LENGKAP", page_icon="logo.png", layout="wide")
except:
    st.set_page_config(page_title="Mindful Remaja by Isra - FINAL LENGKAP", page_icon="💜", layout="wide")

if "jurnal" not in st.session_state:
    st.session_state.jurnal = []
if "skor_srq" not in st.session_state:
    st.session_state.skor_srq = 0
    st.session_state.dass_d = 0
    st.session_state.dass_a = 0
    st.session_state.dass_s = 0

try:
    st.image("logo.png", width=90)
except:
    pass
st.title("Mindful by Isra - Bidan NTT 2026")
st.caption("Skrining Lengkap SRQ-20 + DASS-21 | Edukasi Personal | Jurnal Pintar | Musik | Darurat")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔍 1. Skrining SRQ & DASS", "📚 2. Edukasi & Napas", "📝 3. Jurnal Pintar", "🎧 4. Musik Relaksasi", "🚨 5. Bantuan Darurat"])

# ================= TAB 1 SRQ + DASS =================
with tab1:
    st.subheader("🔍 Skrining Lengkap")
    st.write("Isi 2 kuesioner ini, nanti Tab 2 akan keluar saran sesuai hasilmu otomatis.")

    with st.expander("📋 A. SRQ-20 (Kesehatan Mental Umum) - WAJIB", expanded=True):
        srq_q = ["Sering sakit kepala?","Tidak nafsu makan?","Tidur tidak nyenyak?","Mudah takut?","Tangan gemetar?","Merasa gugup?","Pencernaan buruk?","Sulit berpikir jernih?","Merasa tidak bahagia?","Banyak menangis?","Sulit menikmati kegiatan?","Sulit ambil keputusan?","Pekerjaan terganggu?","Tidak mampu berperan?","Kehilangan minat?","Merasa tidak berharga?","Pikiran mengakhiri hidup?","Merasa lelah?","Perut tidak enak?","Mudah lelah?"]
        skor_srq=0
        for i,q in enumerate(srq_q):
            if st.radio(f"{i+1}. {q}", ["Tidak","Ya"], key=f"srq{i}", horizontal=True)=="Ya":
                skor_srq+=1
        st.session_state.skor_srq = skor_srq
        if skor_srq < 6:
            st.success(f"Skor SRQ {skor_srq}/20 = Ringan")
        elif skor_srq < 10:
            st.warning(f"Skor SRQ {skor_srq}/20 = Sedang")
        else:
            st.error(f"Skor SRQ {skor_srq}/20 = Tinggi")

    with st.expander("📋 B. DASS-21 (Depresi, Cemas, Stres) - WAJIB", expanded=True):
        st.caption("0=Tidak pernah, 1=Kadang, 2=Sering, 3=Sangat sering (dalam 1 minggu terakhir)")
        dass_q = [
            ("D", "Sulit merasa senang"),
            ("S", "Sulit beristirahat / tidak bisa santai"),
            ("A", "Mulut terasa kering"),
            ("A", "Sulit bernapas / napas pendek"),
            ("D", "Sulit melakukan inisiatif"),
            ("S", "Cenderung bereaksi berlebihan"),
            ("A", "Tubuh gemetar"),
            ("S", "Merasa sangat gugup"),
            ("A", "Khawatir akan dipermalukan"),
            ("D", "Merasa tidak ada harapan"),
            ("S", "Merasa gelisah"),
            ("S", "Sulit rileks"),
            ("D", "Merasa sedih & tertekan"),
            ("S", "Tidak toleran / mudah marah"),
            ("A", "Merasa mau pingsan"),
            ("D", "Tidak antusias"),
            ("D", "Merasa tidak berharga"),
            ("S", "Mudah tersinggung"),
            ("A", "Jantung berdebar tanpa aktivitas"),
            ("A", "Takut tanpa alasan"),
            ("D", "Hidup terasa tidak berarti"),
        ]
        d,a,s = 0,0,0
        for i,(kat,q) in enumerate(dass_q):
            nilai = st.selectbox(f"{i+1}. {q}", [0,1,2,3], key=f"dass{i}", horizontal=True, format_func=lambda x: ["Tidak Pernah (0)","Kadang (1)","Sering (2)","Sangat Sering (3)"][x])
            if kat=="D": d+=nilai
            elif kat=="A": a+=nilai
            else: s+=nilai
        st.session_state.dass_d = d*2
        st.session_state.dass_a = a*2
        st.session_state.dass_s = s*2
        col1,col2,col3 = st.columns(3)
        with col1:
            st.metric("Depresi", f"{d*2}", "Normal<9" if d*2<10 else "Sedang" if d*2<21 else "Berat")
        with col2:
            st.metric("Cemas", f"{a*2}", "Normal<7" if a*2<8 else "Sedang" if a*2<15 else "Berat")
        with col3:
            st.metric("Stres", f"{s*2}", "Normal<14" if s*2<15 else "Sedang" if s*2<26 else "Berat")

    if st.button("💾 Simpan Semua Skor & Lihat Saran di Tab 2", type="primary"):
        st.balloons()
        st.success("Tersimpan! Buka Tab 2 Edukasi & Napas ya")

# ================= TAB 2 EDUKASI + NAPAS FLOWCHART =================
with tab2:
    st.subheader("📚 Edukasi Personal Sesuai Hasil SRQ + DASS")
    srq = st.session_state.skor_srq
    dep = st.session_state.dass_d
    anx = st.session_state.dass_a
    str_ = st.session_state.dass_s

    if srq==0 and dep==0:
        st.info("Isi skrining di Tab 1 dulu ya")
    else:
        st.write(f"**Hasilmu:** SRQ {srq}/20 | Depresi {dep} | Cemas {anx} | Stres {str_}")

        # LOGIKA SARAN
        if anx >= 8 or str_ >= 15 or srq >= 6:
            st.warning("**🔴 Hasilmu menunjukkan Cemas/Stres - Saran Utama: Atur Napas 4-7-8**")
            st.markdown("""
            **Kenapa napas?** Saat cemas, napas jadi pendek, jantung berdebar. Napas 4-7-8 membuat otak tenang.
            """)

            # === FLOWCHART / CARA NAPAS BIAR USER PAHAM ===
            st.markdown("### 🌬️ CONTOH ALIR CARA MENGATUR NAPAS 4-7-8 (Ikuti ini)")
            c1,c2,c3,c4 = st.columns(4)
            with c1:
                st.markdown("**LANGKAH 1**\n\n😮‍💨\n\n**DUDUK NYAMAN**\n\nPunggung tegak, tangan di paha, tutup mata")
            with c2:
                st.markdown("**LANGKAH 2**\n\n👃 **TARIK 4 DETIK**\n\nTarik napas lewat hidung hitung 1-2-3-4\nPerut mengembang")
            with c3:
                st.markdown("**LANGKAH 3**\n\n😶‍🌫️ **TAHAN 7 DETIK**\n\nTahan napas hitung 1-2-3-4-5-6-7\nJangan tegang")
            with c4:
                st.markdown("**LANGKAH 4**\n\n😮‍💨 **BUANG 8 DETIK**\n\nBuang lewat mulut pelan 1-2-3-4-5-6-7-8\nUlangi 4x")

            st.divider()
            st.markdown("#### 📊 Alur Sederhana:")
            st.code("""
            START -> Duduk nyaman -> Tarik 4 detik -> Tahan 7 detik -> Buang 8 detik
                  -> Sudah 4x? -> TIDAK -> Ulangi lagi
                                -> YA -> SELESAI, rasakan tenang 1 menit
            """, language="text")

            st.info("💡 **Tips:** Lakukan 2x sehari (pagi sebelum sekolah & malam sebelum tidur) sambil dengar musik di Tab 4")

        if dep >= 10:
            st.error(f"**Hasil Depresi {dep} - Saran:**")
            st.markdown("""
            - Tulis 3 hal bersyukur tiap hari di Tab 3
            - Jalan 10 menit pagi, mandi teratur
            - Cerita ke 1 orang terpercaya (Guru BK/Orang tua)
            - Jika >2 minggu, buka Tab 5 Bantuan Darurat
            """)

        if srq < 6 and dep < 10 and anx < 8 and str_ < 15:
            st.success("**Hasilmu dalam batas Wajar - Fokus Pencegahan:** Tidur 8 jam, kurangi HP sebelum tidur, jurnal syukur")

# ================= TAB 3,4,5 TETAP =================
with tab3:
    st.subheader("📝 Jurnal Pintar")
    refleksi = st.text_area("Tulis perasaan:")
    if st.button("💾 Simpan & Saran", type="primary"):
        if refleksi.strip()!="":
            st.session_state.jurnal.append({"waktu": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), "isi": refleksi})
            st.success("Tersimpan! Jika cemas/sedih, lihat cara napas di Tab 2 ya")
            if any(k in refleksi.lower() for k in ["bunuh","mati aja","sayat"]):
                st.error("🚨 Kamu berharga! Buka TAB 5 SEJIWA 119 ext 8 SEKARANG")

with tab4:
    st.subheader("🎧 Musik Relaksasi Pilihan Isra")
    st.video("https://www.youtube.com/watch?v=77ZozI0rw7w")
    st.link_button("🔗 Buka di YouTube (Jika hitam)", "https://youtu.be/77ZozI0rw7w?si=4kCd8W9YwVV3Qoky", type="primary", use_container_width=True)
    st.audio("https://cdn.pixabay.com/audio/2022/06/07/audio_b9bd4170e8.mp3")
    st.caption("Pakai musik ini sambil latihan napas 4-7-8 di Tab 2")

with tab5:
    st.subheader("🚨 Bantuan Darurat")
    st.error("Jangan sendiri, klik:")
    st.link_button("📞 SEJIWA 119 ext 8 - WA GRATIS", "https://wa.me/62811881119", type="primary", use_container_width=True)
    st.link_button("📞 HALO KEMENKES 1500-567", "tel:1500567", use_container_width=True)
    st.link_button("📍 PUSKESMAS TERDEKAT", "https://www.google.com/maps/search/puskesmas+terdekat/", use_container_width=True)
