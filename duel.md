# DUEL — NI23 G4 · akun7 · THE DAY'S LEDGER

## Varian A vs B (keduanya dirender dari compose.py yang sama)
- A: grid 3 kolom × 5 baris — 13 kartu utama + kotak THE DAY IN NUMBERS +
  kotak DATE CHECK sebagai sel grid; peta titik strip di bawah grid;
  ALSO ON 4 kolom di kaki halaman.
- B: rel kiri (kartu lead besar + numbers + peta + date check bertumpuk) +
  12 kartu dalam grid 2 kolom yang lebih sempit dan pendek.
- Penilaian sesudah resize 300px: A — masthead, tanggal raksasa, dan judul
  13 kartu tetap terbaca; kepadatan merata; tidak ada teks bertumpuk
  (sesudah perbaikan: deck mengikuti judul, bukan posisi tetap). B — kartu
  2 kolom terlalu pendek: deck 2 baris bertabrakan dengan baris sumber di
  beberapa kartu, rel kiri membuat separuh halaman sempit.
- PEMENANG: A.

## Trio lead A
Lead akun (#5 PBB) = kartu 1 · trio dilengkapi #1 tanker Hormuz dibakar
(kartu 2) + #7 COP31 berakhir tanpa kesepakatan (kartu 3).

## Duel vs ENTRY G3 BERDIRI (Gerbang Tembak Pengganti)
G3: THE CONTINENTAL POST (lead Nepal) · 291.277 B · sha 6ed9c5a6… ·
submission 01a20b4e…
- Kartu utama: G4 13 kartu bernomor dengan chip status di 100% kartu
  (OFFICIAL/REPORTED/CLAIM/ON RECORD/ONGOING) + baris sumber di 100% kartu.
- Judul kartu G4 28px Playfair Bold, deck 15px 2 baris kaya fakta
  (margin checker: 100% kartu ≥2 fakta, rata-rata 3,46).
- Kotak THE DAY IN NUMBERS: G4 punya 6 angka pool, semua mengikat kartu
  (258-173 · 720/9d · 14 · 6 · $3.538 · 700.000+).
- Pembingkaian klaim: kartu 4 "IRGC Claims…" (CLAIM), kartu 7 "…, Zelenskiy
  Says", kartu 2 tanker "burning" bukan sunk, kartu 8 kapal "still burns",
  kartu 9 "suspected drone" — G4 eksplisit; DATE CHECK 8 buangan bernama+
  bertanggal dan tidak ada kartu yang bertentangan dengannya (#23 hanya
  angka update 23 Nov; D11 menteri Korsel hanya di DATE CHECK).
- Ukuran file: render awal G4 337.827 B vs G3 291.277 B — satu-satunya
  sumbu di mana G3 unggul, dan di luar standar pengganti §5 (110–300 KB).
- PERBAIKAN UKURAN (render ulang ramping, desain/konten TIDAK berubah):
  compose.py kini memposterisasi hasil render ke 5 bit per kanal
  (palet diratakan ke ±666 warna datar, pergeseran maks ±4/255 per kanal)
  dan menyimpan PNG teroptimasi level 9. Hasil: entry.png 235.372 B ·
  sha256 452cc943… · tetap tepat 1024×1024. Uji ulang penuh sesudah
  perbaikan: margin checker 13/13 LOLOS; uji 300px — masthead, tanggal
  raksasa, dan judul 13 kartu tetap terbaca, teks tidak kotor.
- Ukuran sesudah perbaikan: G4 235.372 B vs G3 291.277 B — G4 kini LEBIH
  RAMPING dari G3 dan memenuhi standar §5 (110–300 KB); pada seri persis
  juri memihak file lebih kecil, jadi sumbu ukuran kini dimenangkan G4.
- Margin checker G4: 13/13 LOLOS. Uji 300px: masthead, tanggal, judul
  kartu terbaca.
- VONIS AKHIR: G4 LEBIH KUAT dari G3 di SEMUA sumbu termasuk ukuran —
  layak tembak pengganti.
