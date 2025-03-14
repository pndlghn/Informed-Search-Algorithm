# INFORMED SEARCH ALGORITHM

## 📌 Greedy Best-First
Kode ini mengimplementasikan **Greedy Best-First Search (GBFS)**, sebuah algoritma pencarian yang menggunakan heuristik untuk memilih jalur terbaik menuju tujuan. Algoritma ini selalu memilih simpul dengan nilai heuristik terendah, tanpa mempertimbangkan biaya sebenarnya.

## Bagaimana Algoritma ini bekerja?
Berikut adalah langkah-langkah eksekusi berdasarkan heuristik:
1.  Mulai dari **'S'** (heuristik = 7), masukan ke frontier.
2.  Ambil simpul dengan heuristik terkecil dari frontier:
     - **‘E’** (heuristik = 3) dipilih karena lebih kecil dari **‘A’** (heuristik = 9).
3.  Dari **‘E’** → **‘D’** (heuristik = 5) dimasukkan ke frontier.
4.  Dari **‘D’** → **‘G’** (heuristik = 0), pencarian selesai.

**Urutan Kunjungan Simpul**:<br>
```S → E → D → G```

## Kesimpulan
Kode ini mengimplementasikan Greedy Best-First Search menggunakan PriorityQueue untuk memilih simpul dengan heuristik terendah. Meskipun cepat, algoritma ini tidak selalu optimal karena hanya mempertimbangkan heuristik tanpa menghitung total biaya perjalanan.
<br><br>
## 📌 A-Star Tree
