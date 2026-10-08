import streamlit as st
import datetime

# === V5.1 FIX STABIL - KONSEP ASLI TETAP - Mindful Remaja by Isra ===
try:
    st.set_page_config(page_title="Mindful Remaja by Isra", page_icon="💜", layout="wide")
except:
    pass

if "jurnal" not in st.session_state:
    st.session_state.jurnal = []
if "skor_srq" not in st.session_state:
    st.session_state.skor_srq = 0

# Logo aman
try:
    st.image("logo.png", width=90)
except:
    st.write("💜")

st.title("Mindful by Isra - Bidan NTT 2026")
st.caption("Edukasi Personal sesuai Hasil Skrining | Musik Relaksasi | Bantuan Darurat")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔍 1. Skrining", "📚 2. Edukasi Personal", "📝 3. Jurnal Pintar", "🎧 4. Musik Relaksasi", "🚨 5. Bantuan Darurat"])

# TAB 1 SKRINING
with tab1:
    st.subheader("Skrining SRQ-20")
    st.write("Jawab Ya/Tidak, nanti edukasi di Tab 2 akan menyesuaikan skor kamu otomatis.")
    srq_q = ["Sering sakit kepala?","Tidak nafsu makan?","Tidur tidak nyenyak?","Mudah takut?","Tangan gemetar?","Merasa gugup?","Pencernaan buruk?","Sulit berpikir jernih?","Merasa tidak bahagia?","Banyak menangis?","Sulit menikmati kegiatan?","Sulit ambil keputusan?","Pekerjaan terganggu?","Tidak mampu berperan?","Kehilangan minat?","Merasa tidak berharga?","Pikiran mengakhiri hidup?","Merasa lelah?","Perut tidak enak?","Mudah lelah?"]
    skor=0
    for i,q in enumerate(srq_q):
        if st.radio(f"{i+1}. {q}", ["Tidak","Ya"], key=f"srq{i}", horizontal=True)=="Ya":
            skor+=1
    st.session_state.skor_srq=skor
    st.divider()
    if skor < 6:
        st.success(f"Skor {skor}/20 - Wajar. Edukasi pencegahan ada di Tab 2.")
    elif skor < 10:
        st.warning(f"Skor {skor}/20 - Sedang. Kamu butuh latihan mindfulness rutin, buka Tab 2.")
    else:
        st.error(f"Skor {skor}/20 - Tinggi. Sangat disarankan konseling & lihat Tab 5 Bantuan Darurat.")
    if st.button("💾 Simpan Skor & Lihat Edukasi Personal di Tab 2"):
        st.balloons()
        st.info("Skor tersimpan! Buka Tab 2 Edukasi Personal ya.")

# TAB 2 EDUKASI PERSONAL
with tab2:
    st.subheader("📚 Edukasi Personal Sesuai Hasil Skriningmu")
    skor = st.session_state.skor_srq
    if skor == 0:
        st.info("Kamu belum skrining. Isi di Tab 1 dulu ya.")
    elif skor < 6:
        st.success(f"Hasilmu {skor}/20 (Ringan) - Fokus Pencegahan:")
        st.markdown("""
        **MODUL 1: Kenali Emosi:** Semua emosi normal. Tulis 3 emosimu tiap hari.
        **MODUL 2: Tidur Sehat:** Remaja butuh 8-9 jam. Matikan HP 30 menit sebelum tidur.
        **MODUL 3: Napas 4-7-8:** Tarik 4 detik, Tahan 7 detik, Buang 8 detik. 3x sehari.
        **Tugas:** Buat jadwal tidur & jurnal syukur di Tab 3.
        """)
    elif skor < 10:
        st.warning(f"Hasilmu {skor}/20 (Sedang) - Kamu butuh coping skill:")
        st.markdown("""
        **MODUL 1: Stres & Cemas:** Grounding 5-4-3-2-1: Sebut 5 hal dilihat, 4 disentuh, 3 didengar.
        **MODUL 2: Mindfulness:** Saat pikiran ramai, fokus ke napas 1 menit.
        **MODUL 3: Komunikasi:** Cari 1 orang dewasa terpercaya untuk cerita.
        **Tugas Wajib:** Dengarkan musik relaksasi di Tab 4 selama 5 menit.
        """)
    else:
        st.error(f"Hasilmu {skor}/20 (Tinggi) - Butuh Perhatian Lebih:")
        st.markdown("""
        **Kamu tidak sendiri.** Skor tinggi bukan berarti lemah, tapi butuh support lebih.
        **MODUL 1:** Jika >2 minggu tidak semangat, cerita ke Guru BK.
        **MODUL 2:** Jangan pendam sendiri.
        **MODUL 3: Rencana Aman:** Tulis 3 orang yang bisa dihubungi, 3 tempat tenang, 3 hal disukai.
        **TUGAS PENTING: Buka Tab 5 Bantuan Darurat & simpan nomor SEJIWA 119 ext 8.**
        """)
    with st.expander("Buka Semua 8 Modul Tulisan"):
        st.write("1. Kenali Emosi | 2. Kenali Stres | 3. Atasi Cemas | 4. Atasi Sedih | 5. Napas 4-7-8 | 6. Tidur Sehat | 7. Komunikasi Asertif | 8. Rencana Sehat Mental")

# TAB 3 JURNAL PINTAR
with tab3:
    st.subheader("📝 Jurnal Pintar - Auto Saran")
    refleksi = st.text_area("Tulis perasaanmu hari ini:", placeholder="Contoh: hari ini saya cemas ujian...", height=150)
    if st.button("💾 Simpan & Dapat Saran Otomatis", type="primary"):
        if refleksi.strip()=="":
            st.warning("Tulis dulu ya")
        else:
            st.session_state.jurnal.append({"waktu": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), "isi": refleksi})
            teks=refleksi.lower()
            st.success("Tersimpan!")
            if any(k in teks for k in ["bunuh","mati aja","pengen mati","sayat","lukai"]):
                st.error("🚨 Kamu berharga! Segera buka TAB 5 & hubungi SEJIWA 119 ext 8 GRATIS 24 jam.")
            elif any(k in teks for k in ["sedih","nangis","hampa","sendiri"]):
                st.info("💜 Untuk sedihmu: Coba Tab 4 musik 5 menit + tulis 3 hal bersyukur.")
            elif any(k in teks for k in ["cemas","takut","khawatir","panik"]):
                st.info("🌿 Untuk cemasmu: Lakukan Grounding 5-4-3-2-1 & napas 4-7-8 di Tab 4.")
            elif any(k in teks for k in ["stres","capek","pusing","tugas"]):
                st.info("✨ Untuk stresmu: Istirahat 5 menit, minum air, jalan sebentar. Buka edukasi Tab 2.")
            else:
                st.info("🌈 Keren sudah jujur! Lanjutkan jurnal tiap hari ya.")
    if st.session_state.jurnal:
        st.divider()
        for j in reversed(st.session_state.jurnal):
            st.write(f"_{j['waktu']}_")
            st.write(f"> {j['isi']}")
            st.write("---")

# TAB 4 MUSIK YOUTUBE
with tab4:
    st.subheader("🎧 Musik Relaksasi - YouTube (Pasti Bunyi)")
    st.write("Pilih musik, pakai headset, tarik napas 4-7-8")
    pilihan = st.selectbox("Pilih Musik:", ["Relaksasi Napas 4-7-8", "Musik Tidur Tenang", "Suara Hujan Tenang", "Musik Meditasi 5 Menit"])
    # Link stabil
    links = {
        "Relaksasi Napas 4-7-8": "https://www.youtube.com/watch?v=QKkxl1Z1i1o",
        "Musik Tidur Tenang": "https://www.youtube.com/watch?v=77ZozI0rw7w",
        "Suara Hujan Tenang": "https://www.youtube.com/watch?v=mPZkdNFkNps",
        "Musik Meditasi 5 Menit": "https://www.youtube.com/watch?v=5Y76XIgwVyI"
    }
    st.video(links[pilihan])
    st.link_button("🔗 Buka di YouTube (jika tidak bunyi)", "https://www.youtube.com/results?search_query=musik+relaksasi+tidur")
    st.info("**Cara:** Tarik 4 detik - Tahan 7 detik - Buang 8 detik sambil dengar musik.")

# TAB 5 BANTUAN DARURAT
with tab5:
    st.subheader("🚨 Bantuan Darurat - Tombol Langsung Klik")
    st.error("Jika kamu atau temanmu ada pikiran menyakiti diri, JANGAN SENDIRI. Klik di bawah ini SEKARANG:")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("📞 SEJIWA 119 ext 8 - GRATIS 24 JAM", "https://wa.me/62811881119", type="primary", use_container_width=True)
        st.link_button("📍 PUSKESMAS TERDEKAT", "https://www.google.com/maps/search/puskesmas+terdekat/", use_container_width=True)
    with col2:
        st.link_button("💬 HALO KEMENKES 1500-567", "https://wa.me/628111500567", use_container_width=True)
        st.link_button("👩‍🏫 HUBUNGI GURU BK", "https://wa.me/", use_container_width=True)
    st.divider()
    st.write(f"**Ringkasanmu:** Skor {st.session_state.skor_srq}/20 | Jurnal {len(st.session_state.jurnal)} entri")
    st.success("Simpan nomor SEJIWA di HP: **119 ext 8**")
    if st.button("🎓 Download Sertifikat Penyelesaian"):
        st.balloons()
        st.success(f"SERTIFIKAT: Telah menyelesaikan Mindful by Isra - Skor {st.session_state.skor_srq} - {datetime.datetime.now().strftime('%d %B %Y')}")
