import streamlit as st

st.set_page_config(page_title="MIDFULL Remaja", layout="centered")

st.title("MIDFULL Remaja")
st.subheader("Aplikasi Edukasi Kesehatan Mental Remaja")
st.caption("Edukasi & skrining awal saja, bukan diagnosis medis. Jika butuh bantuan, hubungi tenaga profesional.")

if 'srq_score' not in st.session_state:
    st.session_state.srq_score = 0
if 'dass' not in st.session_state:
    st.session_state.dass = {"D":0, "A":0, "S":0}

srq_q = ["Sering sakit kepala?","Nafsu makan buruk?","Tidur tidak nyenyak?","Mudah takut?","Tangan gemetar?","Merasa cemas/tegang?","Pencernaan buruk?","Sulit berpikir jernih?","Merasa tidak bahagia?","Lebih banyak menangis?","Sulit menikmati kegiatan?","Sulit mengambil keputusan?","Pekerjaan terbengkalai?","Tidak mampu berperan?","Kehilangan minat?","Merasa tidak berharga?","Pikiran mengakhiri hidup?","Lelah sepanjang waktu?","Tidak enak di perut?","Mudah lelah?"]

dass_q = [("Sulit untuk tenang","S"),("Mulut kering","A"),("Tidak ada hal positif","D"),("Sesak napas","A"),("Sulit inisiatif","D"),("Reaksi berlebihan","S"),("Gemetar","A"),("Gugup","S"),("Khawatir berlebihan","A"),("Tidak ada harapan","D"),("Mudah gelisah","S"),("Sulit santai","S"),("Sedih tertekan","D"),("Tidak toleran","S"),("Hampir panik","A"),("Tidak antusias","D"),("Tidak berharga","D"),("Mudah tersinggung","S"),("Jantung berdebar","A"),("Takut tanpa alasan","A"),("Hidup tidak berarti","D")]

tab1, tab2, tab3, tab4, tab5 = st.tabs(["1. SRQ-20", "2. DASS-21", "3. Hasil", "4. Relaksasi", "5. Bantuan"])

with tab1:
    st.write("Jawab Ya / Tidak (1 bulan terakhir)")
    skor=0
    for i,q in enumerate(srq_q):
        if st.radio(f"{i+1}. {q}", ["Tidak","Ya"], key=f"srq{i}", horizontal=True)=="Ya":
            skor+=1
    if st.button("Simpan Skor SRQ"):
        st.session_state.srq_score=skor
        st.success(f"Skor SRQ tersimpan: {skor}")

with tab2:
    st.write("0=Tidak pernah, 1=Kadang, 2=Sering, 3=Sangat sering")
    d=a=s=0
    for i,(q,k) in enumerate(dass_q):
        v=st.radio(f"{i+1}. {q}", [0,1,2,3], key=f"dass{i}", horizontal=True)
        if k=="D": d+=v
        elif k=="A": a+=v
        else: s+=v
    if st.button("Simpan Skor DASS"):
        st.session_state.dass={"D":d*2,"A":a*2,"S":s*2}
        st.success(f"Tersimpan - D:{d*2} A:{a*2} S:{s*2}")

with tab3:
    srq=st.session_state.srq_score
    dass=st.session_state.dass
    st.metric("Skor SRQ-20", srq)
    st.metric("Depresi / Cemas / Stres", f"{dass['D']} / {dass['A']} / {dass['S']}")
    if srq>=6:
        st.warning("Skor SRQ >=6 menunjukkan perlu perhatian lebih. Diskusikan dengan guru BK / bidan / psikolog ya. Ini bukan diagnosis.")
    else:
        st.info("Skor SRQ dalam batas umum, tetap jaga kesehatan mental ya!")
    st.divider()
    if dass['A']>9: st.write("- Cemas tinggi: coba napas 4-7-8, kurangi kafein, journaling.")
    if dass['D']>9: st.write("- Mood rendah: olahraga ringan, cerita ke orang terpercaya, tidur teratur.")
    if dass['S']>14: st.write("- Stres tinggi: atur waktu, istirahat, relaksasi.")

with tab4:
    st.subheader("Flowchart Latihan Napas 4-7-8")
    st.graphviz_chart('digraph{ rankdir=TB; A[label="START"]; B[label="Tarik Napas 4 detik"]; C[label="Tahan 7 detik"]; D[label="Hembus 8 detik"]; E[label="Ulangi 4x"]; F[label="END - Lebih Tenang"]; A->B->C->D->E->F; }')
    st.write("Musik Relaksasi:")
    st.link_button("▶️ Buka Musik Tenang di YouTube", "https://www.youtube.com/watch?v=77ZozI0rw7w")

with tab5:
    st.subheader("Bantuan")
    st.error("Jika ada pikiran menyakiti diri, kamu tidak sendiri. Segera hubungi bantuan profesional.")
    st.write("- SEJIWA 119 ext 8 (Kemenkes)")
    st.write("- Guru BK / Puskesmas terdekat")
    st.link_button("Chat SEJIWA", "https://wa.me/628119385353")

st.caption("MIDFULL Remaja v8.3 FIX - Untuk Edukasi")
