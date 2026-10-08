import streamlit as st
import pandas as pd

st.set_page_config(page_title="KOTA SIA - Cek Kesehatan", layout="centered")

st.title("KOTA SIA - Aplikasi Edukasi Kesehatan Mental")
st.caption("Aplikasi ini untuk tujuan edukasi & skrining awal saja, bukan diagnosis medis. Jika merasa tidak nyaman, segera hubungi tenaga profesional.")

# --- Data SRQ-20 ---
srq_q = [
    "Sering sakit kepala?", "Nafsu makan buruk?", "Tidur tidak nyenyak?", "Mudah takut?",
    "Tangan gemetar?", "Merasa cemas/tegang?", "Pencernaan buruk?", "Sulit berpikir jernih?",
    "Merasa tidak bahagia?", "Lebih banyak menangis?", "Sulit menikmati kegiatan sehari-hari?",
    "Sulit mengambil keputusan?", "Pekerjaan sehari-hari terbengkalai?", "Merasa tidak mampu berperan?",
    "Kehilangan minat?", "Merasa tidak berharga?", "Pikiran untuk mengakhiri hidup?",
    "Merasa lelah sepanjang waktu?", "Perasaan tidak enak di perut?", "Mudah lelah?"
]

# --- Data DASS-21 ---
dass_q = [
    ("Saya merasa sulit untuk tenang", "S"), ("Mulut terasa kering", "A"), ("Seakan tidak ada hal positif", "D"),
    ("Sesak napas", "A"), ("Sulit memulai inisiatif", "D"), ("Cenderung bereaksi berlebihan", "S"),
    ("Gemetar", "A"), ("Merasa gugup", "S"), ("Khawatir berlebihan", "A"),
    ("Merasa tidak ada harapan", "D"), ("Mudah gelisah", "S"), ("Sulit santai", "S"),
    ("Merasa sedih & tertekan", "D"), ("Tidak toleran terhadap gangguan", "S"), ("Hampir panik", "A"),
    ("Tidak antusias", "D"), ("Merasa tidak berharga", "D"), ("Mudah tersinggung", "S"),
    ("Detak jantung keras", "A"), ("Takut tanpa alasan", "A"), ("Hidup tidak berarti", "D")
]

tab1, tab2, tab3, tab4, tab5 = st.tabs(["1. SRQ-20", "2. DASS-21", "3. Hasil & Edukasi", "4. Relaksasi", "5. Bantuan"])

if 'srq_score' not in st.session_state: st.session_state.srq_score = 0
if 'dass' not in st.session_state: st.session_state.dass = {"D":0, "A":0, "S":0}

with tab1:
    st.subheader("Skrining SRQ-20")
    st.write("Jawab Ya / Tidak untuk 20 pertanyaan ini (1 bulan terakhir)")
    skor = 0
    for i, q in enumerate(srq_q):
        ans = st.radio(f"{i+1}. {q}", ["Tidak", "Ya"], key=f"srq_{i}", horizontal=True)
        if ans == "Ya": skor += 1
    if st.button("Simpan Skor SRQ"):
        st.session_state.srq_score = skor
        st.success(f"Skor SRQ tersimpan: {skor}")

with tab2:
    st.subheader("Skrining DASS-21")
    st.write("0=Tidak pernah, 1=Kadang, 2=Sering, 3=Sangat sering")
    d,a,s = 0,0,0
    for i, (q, kode) in enumerate(dass_q):
        val = st.radio(f"{i+1}. {q}", [0,1,2,3], key=f"dass_{i}", horizontal=True)
        if kode=="D": d+=val
        elif kode=="A": a+=val
        else: s+=val
    if st.button("Simpan Skor DASS"):
        st.session_state.dass = {"D":d*2, "A":a*2, "S":s*2}
        st.success(f"Tersimpan - D:{d*2} A:{a*2} S:{s*2}")

with tab3:
    st.subheader("Hasil & Edukasi Personal")
    srq = st.session_state.srq_score
    dass = st.session_state.dass
    st.metric("Skor SRQ-20", srq)
    st.metric("DASS - Depresi / Cemas / Stres", f"{dass['D']} / {dass['A']} / {dass['S']}")
    
    if srq >= 6:
        st.warning("Skor SRQ >=6 menunjukkan perlu perhatian lebih. Ini bukan diagnosis, silakan diskusikan dengan bidan/nakes atau psikolog.")
    else:
        st.info("Skor SRQ <6 dalam batas umum, tetap jaga kesehatan mental ya.")
    
    st.divider()
    st.write("**Edukasi:**")
    if dass['A'] > 10:
        st.write("- Untuk rasa cemas: coba teknik napas 4-7-8, batasi kafein, journaling.")
    if dass['D'] > 10:
        st.write("- Untuk mood rendah: aktivitas fisik ringan, cerita ke orang terpercaya, rutinitas tidur teratur.")
    if dass['S'] > 15:
        st.write("- Untuk stres: manajemen waktu, teknik relaksasi, istirahat cukup.")

with tab4:
    st.subheader("Latihan Relaksasi - Flowchart Napas")
    st.write("Ikuti alur: Tarik 4 detik -> Tahan 7 detik -> Hembus 8 detik")
    st.code("START -> Tarik Napas 4s -> Tahan 7s -> Hembus 8s -> Ulangi 4x -> END", language="text")
    
    st.write("**Musik Relaksasi:**")
    st.link_button("Buka Musik Tenang di YouTube", "https://www.youtube.com/watch?v=77ZozI0rw7w")
    st.video("https://www.youtube.com/watch?v=77ZozI0rw7w")

with tab5:
    st.subheader("Bantuan Darurat")
    st.error("Jika Anda atau orang terdekat memiliki pikiran untuk menyakiti diri, segera hubungi bantuan profesional. Anda tidak sendiri.")
    st.write("- **SEJIWA 119 ext 8** - Kemenkes RI")
    st.write("- **Puskesmas / Bidan terdekat**")
    st.write("- Hubungi keluarga / orang terpercaya")
    st.link_button("Chat WhatsApp Sejiwa 119", "https://wa.me/628119385353")

st.divider()
st.caption("KOTA SIA v8.1 | Dibuat untuk edukasi masyarakat")
