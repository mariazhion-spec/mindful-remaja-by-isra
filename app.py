import streamlit as st
import datetime

try:
    st.set_page_config(page_title="Mindful Remaja by Isra - FINAL", page_icon="logo.png", layout="wide")
except:
    st.set_page_config(page_title="Mindful Remaja by Isra - FINAL", page_icon="💜", layout="wide")

if "jurnal" not in st.session_state:
    st.session_state.jurnal = []
if "skor_srq" not in st.session_state:
    st.session_state.skor_srq = 0

try:
    st.image("logo.png", width=90)
except:
    pass
st.title("Mindful by Isra - Bidan NTT 2026")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔍 1. Skrining", "📚 2. Edukasi Personal", "📝 3. Jurnal Pintar", "🎧 4. Musik Relaksasi", "🚨 5. Bantuan Darurat"])

# TAB 1
with tab1:
    st.subheader("Skrining SRQ-20")
    srq_q = ["Sering sakit kepala?","Tidak nafsu makan?","Tidur tidak nyenyak?","Mudah takut?","Tangan gemetar?","Merasa gugup?","Pencernaan buruk?","Sulit berpikir jernih?","Merasa tidak bahagia?","Banyak menangis?","Sulit menikmati kegiatan?","Sulit ambil keputusan?","Pekerjaan terganggu?","Tidak mampu berperan?","Kehilangan minat?","Merasa tidak berharga?","Pikiran mengakhiri hidup?","Merasa lelah?","Perut tidak enak?","Mudah lelah?"]
    skor=0
    for i,q in enumerate(srq_q):
        if st.radio(f"{i+1}. {q}", ["Tidak","Ya"], key=f"srq{i}", horizontal=True)=="Ya":
            skor+=1
    st.session_state.skor_srq=skor
    if skor < 6:
        st.success(f"Skor {skor}/20 - Wajar")
    elif skor < 10:
        st.warning(f"Skor {skor}/20 - Sedang")
    else:
        st.error(f"Skor {skor}/20 - Tinggi, buka Tab 5")
    if st.button("💾 Simpan Skor"):
        st.balloons()

# TAB 2
with tab2:
    st.subheader("📚 Edukasi Personal Sesuai Skor")
    skor = st.session_state.skor_srq
    if skor == 0:
        st.info("Isi skrining dulu")
    elif skor < 6:
        st.success(f"Skor {skor}/20 - Ringan: Tidur 8 jam, jurnal syukur, napas 4-7-8")
    elif skor < 10:
        st.warning(f"Skor {skor}/20 - Sedang: Grounding 5-4-3-2-1, cerita ke orang terpercaya")
    else:
        st.error(f"Skor {skor}/20 - Tinggi: Kamu tidak sendiri. Buka Tab 5 simpan nomor SEJIWA")
    with st.expander("Lihat 8 Modul Tulisan"):
        st.write("1. Kenali Emosi 2. Stres 3. Cemas 4. Sedih 5. Napas 4-7-8 6. Tidur Sehat 7. Komunikasi 8. Rencana Sehat Mental")

# TAB 3
with tab3:
    st.subheader("📝 Jurnal Pintar")
    refleksi = st.text_area("Tulis perasaan:")
    if st.button("💾 Simpan & Saran", type="primary"):
        if refleksi.strip()!="":
            st.session_state.jurnal.append({"waktu": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), "isi": refleksi})
            teks=refleksi.lower()
            st.success("Tersimpan!")
            if any(k in teks for k in ["bunuh","mati aja","sayat"]):
                st.error("🚨 Kamu berharga! Buka TAB 5 hubungi SEJIWA 119 ext 8 SEKARANG")
            elif "sedih" in teks or "nangis" in teks:
                st.info("💜 Sedihmu wajar. Dengarkan musik di Tab 4")
            elif "cemas" in teks or "takut" in teks:
                st.info("🌿 Cemasmu wajar. Napas 4-7-8 di Tab 4 ya")
            else:
                st.info("🌈 Keren sudah menulis!")

# TAB 4 - PAKAI LINK KAKAK
with tab4:
    st.subheader("🎧 Musik Relaksasi Pilihan Isra")
    st.write("Musik ini Kakak pilih sendiri - Link: https://youtu.be/77ZozI0rw7w")
    
    # Video utama pakai link Kakak
    st.markdown("#### ▶️ Musik Utama - Pilihan Kak Isra")
    st.video("https://www.youtube.com/watch?v=77ZozI0rw7w")
    
    st.link_button("🔗 Buka di YouTube Langsung (Jika hitam, klik ini pasti bunyi)", "https://youtu.be/77ZozI0rw7w?si=4kCd8W9YwVV3Qoky", type="primary", use_container_width=True)
    
    st.divider()
    st.markdown("#### 🎵 Audio Cadangan (Pasti Bunyi Tanpa YouTube)")
    st.audio("https://cdn.pixabay.com/audio/2022/06/07/audio_b9bd4170e8.mp3")
    st.caption("Jika YouTube hitam, pakai audio ini untuk latihan napas")
    
    st.divider()
    st.info("**Latihan 4-7-8 sambil dengar musik:** Tarik 4 detik - Tahan 7 detik - Buang 8 detik")
    if st.button("Mulai Latihan"):
        st.success("Tarik... Tahan... Buang... Fokus ke musik ya 💜")

# TAB 5
with tab5:
    st.subheader("🚨 Bantuan Darurat")
    st.error("Jangan sendiri. Klik tombol di bawah:")
    st.link_button("📞 SEJIWA 119 ext 8 - WA GRATIS 24 JAM", "https://wa.me/62811881119", type="primary", use_container_width=True)
    st.link_button("📞 HALO KEMENKES 1500-567", "tel:1500567", use_container_width=True)
    st.link_button("📍 PUSKESMAS TERDEKAT", "https://www.google.com/maps/search/puskesmas+terdekat/", use_container_width=True)
    if st.button("🎓 Sertifikat"):
        st.balloons()
        st.success(f"SERTIFIKAT Mindful by Isra - Skor {st.session_state.skor_srq} - {datetime.datetime.now().strftime('%d %B %Y')}")
