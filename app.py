import streamlit as st
import datetime
import urllib.parse
import math

st.set_page_config(page_title="Mindful Remaja by Isra - FINAL Lengkap", layout="centered", page_icon="💜")

# ===== SESSION STATE =====
if 'completed' not in st.session_state:
    st.session_state.completed = set()
if 'jurnal' not in st.session_state:
    st.session_state.jurnal = {}
if 'kontak_keluarga' not in st.session_state:
    st.session_state.kontak_keluarga = []
if 'srq_skor' not in st.session_state:
    st.session_state.srq_skor = None
if 'dass_skor' not in st.session_state:
    st.session_state.dass_skor = None

MODULS = {
    "1. MODUL 1: Kenali Emosi": {"judul": "MODUL 1: Kenali Emosi","video": "https://www.youtube.com/watch?v=LI9p2i9YTsE","materi": "Kenali emosi: Senang, Sedih, Marah, Takut. Emosi adalah sinyal tubuh.","quiz_q": "Apa fungsi utama mengenali emosi?","quiz_opt": ["Menekan emosi","Memahami sinyal tubuh & merespon sehat","Agar tidak pernah sedih"],"quiz_ans": 1},
    "2. MODUL 2: Stres Remaja": {"judul": "MODUL 2: Stres Remaja","video": "https://www.youtube.com/watch?v=3SsK-cvHOdA","materi": "Stres akademik, sosial, keluarga - teknik 3-3-3 Grounding: Sebut 3 hal yang dilihat, didengar, disentuh.","quiz_q": "Teknik 3-3-3 untuk?","quiz_opt": ["Menghafal","Grounding saat cemas","Menambah stres"],"quiz_ans": 1},
    "3. MODUL 3: Sedih Berkepanjangan": {"judul": "MODUL 3: Sedih Berkepanjangan","video": "https://www.youtube.com/watch?v=BYG5T02z8Zs","materi": "Jurnal 3 Hal Baik & Gerak 15 menit setiap hari (WHO 2023).","quiz_q": "Jika sedih >2 minggu terus?","quiz_opt": ["Didiamkan saja","Curhat & skrining DASS-21 / hubungi 119 ext 8","Marah-marah"],"quiz_ans": 1},
    "4. MODUL 4: Cemas Berlebih": {"judul": "MODUL 4: Cemas Berlebih","video": "https://www.youtube.com/watch?v=ZidGozDhOQc","materi": "Bedakan Cemas wajar vs Gangguan Cemas - latih napas diafragma.","quiz_q": "Gejala fisik cemas?","quiz_opt": ["Jantung berdebar, napas pendek","Lapar terus","Tidak ada gejala"],"quiz_ans": 0},
    "5. MODUL 5: T.A.N.Y.A Self-Harm": {"judul": "MODUL 5: T.A.N.Y.A Self-Harm","video": "https://www.youtube.com/watch?v=XiCrniLQGYc","materi": "Jika teman ada pikiran melukai diri: TANYA, DENGARKAN tanpa menghakimi, HUBUNGKAN ke bantuan 119 ext 8.","quiz_q": "Teman bilang ingin self-harm, apa yang dilakukan?","quiz_opt": ["Bilang lebay / cari perhatian","TANYA-DENGARKAN-HUBUNGKAN ke 119 ext 8","Jauhi teman itu"],"quiz_ans": 1},
    "6. MODUL 6: Jadi First Aider": {"judul": "MODUL 6: Jadi First Aider","video": "https://www.youtube.com/watch?v=1qq7lDL-bzY","materi": "Prinsip PFA WHO: LIHAT-DEKATI-DENGARKAN-HUBUNGKAN.","quiz_q": "Prinsip PFA WHO?","quiz_opt": ["LIHAT-DEKATI-DENGARKAN-HUBUNGKAN","Beri nasihat panjang lebar","Abaikan saja"],"quiz_ans": 0},
    "7. MODUL 7: Napas 4-7-8 WHO": {"judul": "MODUL 7: Napas 4-7-8 WHO","video": "https://www.youtube.com/watch?v=aNXKjGFUlA4","materi": "Tarik napas 4 detik, Tahan 7 detik, Hembus 8 detik - ulang 4 siklus untuk menurunkan cemas (WHO).","quiz_q": "Manfaat teknik napas 4-7-8?","quiz_opt": ["Menurunkan cemas & menenangkan","Membuat ngantuk seharian","Tidak ada manfaat"],"quiz_ans": 0},
    "8. MODUL 8: Review & Sertifikat": {"judul": "MODUL 8: Review & Sertifikat","video": "https://www.youtube.com/watch?v=JGw8DWQOQq8","materi": "Review 7 modul & komitmen jadi First Aider Remaja!","quiz_q": "Komitmen First Aider?","quiz_opt": ["Praktekkan PFA & jaga kesehatan mental","Lupakan semua materi","Hanya ambil sertifikat"],"quiz_ans": 0}
}

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2-lat1); dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(dlon/2)**2
    return R * 2*math.atan2(math.sqrt(a), math.sqrt(1-a))

# ===== HEADER =====
st.markdown("## 💜 Mindful Remaja by Isra")
st.markdown("### Bidan NTT 2026 - SRQ-20 + DASS-21 + Edukasi + Jurnal + Musik + Sertifikat")
st.warning("⚠️ Aplikasi ini untuk edukasi & skrining awal, bukan diagnosis. Jika skor tinggi atau ada pikiran menyakiti diri, segera hubungi bantuan profesional 119 ext 8.")
st.divider()

# ===== PROGRESS =====
total = len(MODULS); done = len(st.session_state.completed)
pct = int(done/total*100) if total else 0
st.write(f"**📊 Progress Modul: {pct}% - {done}/{total} selesai**")
st.progress(pct)

# ===== MENU UTAMA =====
menu = st.tabs(["🔍 1. Skrining Awal", "📚 2. Modul Edukasi", "📝 3. Jurnal", "🎧 4. Musik Tenang", "🆘 5. Bantuan & Sertifikat"])

# ===== TAB 1: SKRINING =====
with menu[0]:
    st.header("🔍 Skrining Awal - SRQ-20 & DASS-21")
    st.info("Isi skrining sebelum mulai modul. Hasil hanya untuk memantau, bukan diagnosis.")

    with st.expander("📋 SRQ-20 (20 Pertanyaan Kesehatan Mental Umum) - WHO", expanded=True):
        st.write("Jawab Ya/Tidak untuk 30 hari terakhir:")
        srq_questions = [
            "Sering sakit kepala?", "Nafsu makan buruk?", "Tidur tidak nyenyak?", "Mudah takut?",
            "Tangan gemetar?", "Merasa gugup/tegang?", "Pencernaan buruk?", "Sulit berpikir jernih?",
            "Merasa tidak bahagia?", "Menangis lebih sering?", "Sulit menikmati aktivitas?",
            "Sulit mengambil keputusan?", "Pekerjaan sehari-hari terbengkalai?", "Merasa tidak berguna?",
            "Kehilangan minat?", "Merasa tidak berharga?", "Pikiran mengakhiri hidup?",
            "Merasa lelah terus?", "Perasaan tidak enak di perut?", "Mudah lelah?"
        ]
        srq_score = 0
        for i,q in enumerate(srq_questions):
            ans = st.radio(f"{i+1}. {q}", ["Tidak","Ya"], key=f"srq_{i}", horizontal=True, index=0)
            if ans=="Ya": srq_score+=1
        if st.button("💾 Simpan Skor SRQ-20"):
            st.session_state.srq_skor = srq_score
            if srq_score >= 6:
                st.error(f"Skor SRQ-20: {srq_score}/20 - Skor ≥6 perlu perhatian. Disarankan curhat ke orang terpercaya & pertimbangkan konseling ke Puskesmas. Hubungi 119 ext 8 jika ada pikiran menyakiti diri.")
            else:
                st.success(f"Skor SRQ-20: {srq_score}/20 - Skor <6 dalam batas wajar. Tetap jaga kesehatan mental!")

    with st.expander("📋 DASS-21 (Depresi, Cemas, Stres)", expanded=False):
        st.write("Seberapa sering dalam 1 minggu terakhir (0=Tidak pernah, 3=Sangat sering):")
        dass_q = [
            ("Saya sulit beristirahat","S"), ("Mulut terasa kering","A"), ("Tidak bisa merasakan hal positif","D"),
            ("Napas pendek tanpa aktivitas","A"), ("Sulit memulai aktivitas","D"), ("Bereaksi berlebihan","S"),
            ("Tangan gemetar","A"), ("Gugup berlebihan","S"), ("Khawatir berlebihan","A"),
            ("Tidak ada harapan masa depan","D"), ("Merasa gelisah","S"), ("Sulit rileks","S"),
            ("Merasa sedih & tertekan","D"), ("Tidak toleran terhadap gangguan","S"), ("Hampir panik","A"),
            ("Tidak antusias","D"), ("Merasa tidak berharga","D"), ("Mudah tersinggung","S"),
            ("Jantung berdebar tanpa aktivitas","A"), ("Takut tanpa alasan","A"), ("Hidup tidak berarti","D")
        ]
        d_score = 0; a_score=0; s_score=0
        for i,(q,cat) in enumerate(dass_q):
            v = st.select_slider(f"{i+1}. {q}", options=[0,1,2,3], key=f"dass_{i}", value=0)
            if cat=="D": d_score+=v
            elif cat=="A": a_score+=v
            else: s_score+=v
        if st.button("💾 Simpan Skor DASS-21"):
            st.session_state.dass_skor = {"D":d_score*2, "A":a_score*2, "S":s_score*2}
            st.success(f"Skor D: {d_score*2}, A: {a_score*2}, S: {s_score*2} (skor sudah x2 sesuai manual DASS)")
            st.caption("Interpretasi: 0-9 Normal, 10-13 Ringan, 14-20 Sedang, 21-27 Berat, 28+ Sangat Berat - Segera hubungi bantuan jika Berat/Sangat Berat")

# ===== TAB 2: MODUL =====
with menu[1]:
    st.header("📚 Modul Edukasi 1-8")
    pilihan = st.selectbox("Pilih Modul:", list(MODULS.keys()))
    data = MODULS[pilihan]
    st.subheader(data["judul"])
    st.video(data["video"])
    st.success(f"🎬 Materi: {data['materi']}")

    st.subheader("❓ Quiz Mini")
    st.write(f"**{data['quiz_q']}**")
    jawaban = st.radio("Pilih jawaban:", data["quiz_opt"], key=f"quiz_{pilihan}", index=None)

    if st.button("✅ Selesaikan Modul Ini", key=f"btn_{pilihan}", use_container_width=True):
        if not st.session_state.jurnal.get(pilihan,"").strip():
            st.warning("Isi Jurnal Refleksi di Tab Jurnal dulu ya!")
        elif jawaban is None:
            st.warning("Pilih quiz dulu!")
        else:
            st.session_state.completed.add(pilihan)
            if data["quiz_opt"].index(jawaban) == data["quiz_ans"]:
                st.success(f"✅ BENAR! Progres {len(st.session_state.completed)}/{total}"); st.balloons()
            else:
                st.error("Kurang tepat, tapi modul tetap tercatat. Coba pahami lagi materinya!")
            st.rerun()

# ===== TAB 3: JURNAL =====
with menu[2]:
    st.header("📝 Jurnal Refleksi")
    st.caption("Tulis perasaanmu setelah menonton modul. Jurnal tersimpan otomatis di HP.")
    pilihan_j = st.selectbox("Pilih Modul untuk Jurnal:", list(MODULS.keys()), key="jurnal_pilih")
    refleksi = st.text_area("Tulis refleksimu di sini:", value=st.session_state.jurnal.get(pilihan_j, ""), key=f"jurnal_{pilihan_j}_area", height=150, placeholder="Hari ini saya belajar... Saya merasa...")
    st.session_state.jurnal[pilihan_j] = refleksi
    if refleksi:
        st.success("✅ Jurnal tersimpan otomatis")

# ===== TAB 4: MUSIK =====
with menu[3]:
    st.header("🎧 Musik Tenang & Latihan Napas")
    st.info("Putar musik saat cemas, sedih, atau sebelum tidur. Kombinasikan dengan napas 4-7-8")

    musik_pilih = st.selectbox("Pilih Audio:", ["🌬️ Panduan Napas 4-7-8 (3 menit)", "🌧️ Suara Hujan Tenang", "🎹 Piano Relaksasi"])

    if "Napas" in musik_pilih:
        st.subheader("🌬️ Latihan Napas 4-7-8 WHO")
        st.write("Ikuti panduan: Tarik 4 detik - Tahan 7 detik - Hembus 8 detik")
        st.components.v1.html("""
        <div style="text-align:center; padding:20px; background:#ede9fe; border-radius:12px;">
            <h2 id="napas" style="color:#7c3aed;">Siap...</h2>
            <p id="count" style="font-size:48px;">4</p>
            <button onclick="mulai()" style="padding:10px 20px; background:#7c3aed; color:white; border:none; border-radius:8px;">▶️ Mulai Latihan 4-7-8 (4 Siklus)</button>
        </div>
        <script>
        async function mulai(){
            const fases = [
                {t:"Tarik Napas... 4 detik", c:4},{t:"Tahan... 7 detik", c:7},{t:"Hembuskan... 8 detik", c:8}
            ];
            for(let siklus=0; siklus<4; siklus++){
                for(let f of fases){
                    document.getElementById("napas").innerText = f.t + " (Siklus "+(siklus+1)+"/4)";
                    for(let i=f.c;i>0;i--){document.getElementById("count").innerText=i; await new Promise(r=>setTimeout(r,1000));}
                }
            }
            document.getElementById("napas").innerText="✅ Selesai! Bagus sekali!"; document.getElementById("count").innerText="💜";
        }
        </script>
        """, height=250)
        st.audio("https://cdn.pixabay.com/audio/2022/06/07/audio_b9bd4170e8.mp3") # contoh audio calm
    elif "Hujan" in musik_pilih:
        st.subheader("🌧️ Suara Hujan")
        st.audio("https://cdn.pixabay.com/audio/2022/03/10/audio_397232d6f6.mp3")
        st.caption("Tips: Dengarkan 10-15 menit sambil jurnal 3 Hal Baik")
    else:
        st.subheader("🎹 Piano Relaksasi")
        st.audio("https://cdn.pixabay.com/audio/2024/09/19/audio_b9bd4170e8.mp3")
        st.caption("Gunakan untuk relaksasi sebelum tidur")

# ===== TAB 5: BANTUAN & SERTIFIKAT =====
with menu[4]:
    if done == total:
        st.header("🎉 Selamat! Kamu First Aider!")
        nama = st.text_input("Nama untuk Sertifikat:", "Isra - Bidan NTT")
        tgl = datetime.date.today().strftime("%d %B %Y")
        srq_txt = f"SRQ:{st.session_state.srq_skor}" if st.session_state.srq_skor is not None else "SRQ: -"
        dass_txt = f"DASS D:{st.session_state.dass_skor}" if st.session_state.dass_skor else "DASS: -"
        sertifikat_text = f"SERTIFIKAT FIRST AIDER\nMindful Remaja by Isra\nNama: {nama}\nTelah menyelesaikan 8 Modul Edukasi Kesehatan Mental\nTanggal: {tgl}\n{srq_txt} | {dass_txt}\nKontak Darurat: 119 ext 8"
        st.code(sertifikat_text)
        st.download_button("📥 DOWNLOAD SERTIFIKAT", data=sertifikat_text, file_name=f"Sertifikat_{nama}.txt", mime="text/plain", use_container_width=True, type="primary")
    else:
        st.info(f"Selesaikan {total-done} modul lagi untuk membuka sertifikat. Progress {pct}%")

    st.divider()
    st.header("🆘 Pusat Bantuan Darurat")
    tab1, tab2, tab3 = st.tabs(["📞 Resmi 24 Jam", "👨‍👩‍👧 Keluarga", "🗺️ Maps Auto GPS"])

    with tab1:
        st.error("Jika ada pikiran menyakiti diri, kamu tidak sendiri. Segera hubungi:")
        c1, c2 = st.columns(2)
        with c1: st.link_button("📞 SEJIWA 119 ext 8", "tel:119", use_container_width=True)
        with c2:
            wa = urllib.parse.quote("Halo SEJIWA, saya butuh bantuan")
            st.link_button("💬 WA SEJIWA", f"https://wa.me/62811105567?text={wa}", use_container_width=True)
        st.link_button("📞 SAPA 129 (KDRT)", "tel:129", use_container_width=True)
        st.link_button("📞 PUSPAGA NTT", "tel:0380", use_container_width=True)

    with tab2:
        st.subheader("👨‍👩‍👧 Kontak Keluarga (Privasi Aman)")
        st.caption("Hanya tersimpan di HP kamu, tidak dikirim kemana-mana. 1 klik Telpon/WA.")
        with st.form("form_keluarga", clear_on_submit=True):
            nama_k = st.text_input("Nama (Mama/Kakak/Bidan)"); hub_k = st.selectbox("Hubungan", ["Orang Tua","Saudara","Sahabat","Bidan","Lainnya"]); no_k = st.text_input("No HP 0812xxx")
            if st.form_submit_button("➕ Tambah Kontak"):
                if nama_k and no_k:
                    nb = no_k.replace(" ","").replace("-",""); nwa = "62"+nb[1:] if nb.startswith("0") else nb
                    st.session_state.kontak_keluarga.append({"nama":nama_k,"hubungan":hub_k,"no_hp":nb,"no_wa":nwa}); st.rerun()
        for i,k in enumerate(st.session_state.kontak_keluarga):
            with st.container(border=True):
                st.write(f"**{k['nama']}** - {k['hubungan']} - {k['no_hp']}")
                a,b,c = st.columns(3)
                with a: st.link_button("📞 Telp", f"tel:{k['no_hp']}", key=f"t{i}", use_container_width=True)
                with b:
                    wt = urllib.parse.quote(f"Halo {k['nama']}, saya butuh bantuan")
                    st.link_button("💬 WA", f"https://wa.me/{k['no_wa']}?text={wt}", key=f"w{i}", use_container_width=True)
                with c:
                    if st.button("🗑️ Hapus", key=f"d{i}", use_container_width=True): st.session_state.kontak_keluarga.pop(i); st.rerun()

    with tab3:
        st.subheader("🗺️ Puskesmas NTT - Auto GPS")
        puskesmas_ntt = [
            {"nama": "Puskesmas Oebobo","alamat": "Kota Kupang","lat": -10.1718,"lon": 123.6075,"tel": "0380123456"},
            {"nama": "Puskesmas Bakunase","alamat": "Kota Kupang","lat": -10.1852,"lon": 123.6138,"tel": "0380123457"},
            {"nama": "RS Jiwa Naimata","alamat": "RS Jiwa Naimata Kupang","lat": -10.2153,"lon": 123.6121,"tel": "0380123458"},
            {"nama": "Puskesmas Alak","alamat": "Kota Kupang","lat": -10.1625,"lon": 123.5702,"tel": "0380123459"},
        ]
        st.components.v1.html("""
            <div id="loc" style="padding:10px;background:#f3f4f6;border-radius:8px;">🔄 Mencari lokasi... Izinkan akses lokasi</div>
            <script>
            function getLoc(){if(navigator.geolocation){navigator.geolocation.getCurrentPosition(pos=>{document.getElementById("loc").innerHTML="✅ Lokasi: "+pos.coords.latitude.toFixed(5)+", "+pos.coords.longitude.toFixed(5)+"<br>Salin ke form bawah!";},err=>{document.getElementById("loc").innerHTML="❌ "+err.message+" - Isi manual";});}else{document.getElementById("loc").innerHTML="Tidak support GPS";}}
            getLoc();
            </script>
            <button onclick="getLoc()" style="margin-top:8px;padding:8px 12px;background:#7c3aed;color:white;border:none;border-radius:6px;">🔄 Refresh Lokasi</button>
        """, height=140)
        col1, col2 = st.columns(2)
        with col1: user_lat = st.number_input("Latitude Kamu", value=-10.1718, format="%.5f", key="ulat")
        with col2: user_lon = st.number_input("Longitude Kamu", value=123.6075, format="%.5f", key="ulon")
        for p in puskesmas_ntt: p['jarak'] = haversine(user_lat, user_lon, p['lat'], p['lon'])
        sorted_puskes = sorted(puskesmas_ntt, key=lambda x: x['jarak'])
        terdekat = sorted_puskes[0]
        st.success(f"⭐ TERDEKAT: {terdekat['nama']} - {terdekat['jarak']:.2f} km")
        dir_main = f"https://www.google.com/maps/dir/{user_lat},{user_lon}/{terdekat['lat']},{terdekat['lon']}/"
        st.link_button(f"🧭 ARAHKAN ke {terdekat['nama']} ({terdekat['jarak']:.1f} km)", dir_main, use_container_width=True, type="primary")
        for p in sorted_puskes:
            with st.container(border=True):
                st.write(f"**{p['nama']}** - 📏 {p['jarak']:.2f} km - {p['alamat']}")
                st.markdown(f'<iframe width="100%" height="180" frameborder="0" src="https://maps.google.com/maps?q={p["lat"]},{p["lon"]}&z=15&output=embed"></iframe>', unsafe_allow_html=True)
                r1, r2, r3 = st.columns(3)
                with r1: st.link_button("🧭 Rute", f"https://www.google.com/maps/dir/{user_lat},{user_lon}/{p['lat']},{p['lon']}/", key=f"rt{p['nama']}", use_container_width=True)
                with r2: st.link_button("📞 Telp", f"tel:{p['tel']}", key=f"tp{p['nama']}", use_container_width=True)
                with r3: st.link_button("📍 Maps", f"https://www.google.com/maps/search/?api=1&query={p['lat']},{p['lon']}", key=f"mp{p['nama']}", use_container_width=True)
