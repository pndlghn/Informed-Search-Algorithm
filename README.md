# INFORMED SEARCH ALGORITHM

## 📌 Greedy Best-First
Kode ini mengimplementasikan **Greedy Best-First Search (GBFS)**, sebuah algoritma pencarian yang menggunakan heuristik untuk memilih jalur terbaik menuju tujuan. Algoritma ini selalu memilih simpul dengan nilai heuristik terendah, tanpa mempertimbangkan biaya sebenarnya.

##  🚀 Bagaimana Algoritma ini bekerja?
Berikut adalah langkah-langkah eksekusi berdasarkan heuristik:
1.  Mulai dari **'S'** (heuristik = 7), masukan ke frontier.
2.  Ambil simpul dengan heuristik terkecil dari frontier:
     - **‘E’** (heuristik = 3) dipilih karena lebih kecil dari **‘A’** (heuristik = 9).
3.  Dari **‘E’** → **‘D’** (heuristik = 5) dimasukkan ke frontier.
4.  Dari **‘D’** → **‘G’** (heuristik = 0), pencarian selesai.

**Urutan Kunjungan Simpul**:<br>
```S → E → D → G```

## Kesimpulan
Kode ini mengimplementasikan *Greedy Best-First Search* menggunakan `PriorityQueue` untuk memilih simpul dengan heuristik terendah. Meskipun cepat, algoritma ini tidak selalu optimal karena hanya mempertimbangkan heuristik tanpa menghitung total biaya perjalanan.
<br><br>

## 📌 A-Star Tree
Kode ini mengimplementasikan algoritma **A Tree Search**, yang digunakan untuk mencari jalur optimal dari simpul awal ke simpul tujuan dalam graf berbobot menggunakan fungsi evaluasi:

𝑓
(
𝑛
)
`=`
𝑔
(
𝑛
)
+
ℎ
(
𝑛
)
=

di mana:

`g(n)` adalah biaya sebenarnya dari simpul awal ke simpul n.
`h(n)` adalah estimasi biaya dari simpul n ke tujuan berdasarkan heuristik.

##  🚀 Bagaimana Algoritma ini Bekerja?
1. Mulai dari S (biaya awal = 0).
2. Dari S, pilih simpul dengan f(n) terendah:
     - `A` dengan f(A) = 3 + 9 = 12.
     - `E` dengan f(E) = 2 + 3 = 5 (lebih kecil, jadi dipilih).
3. Dari E, pilih simpul dengan f(n) terendah:
     - `D` dengan f(D) = (2 + 6) + 5 = 11.
4. Dari D, ke G dengan f(G) = (2 + 6 + 3) + 0 = 11.
5. Sampai tujuan G dengan total biaya 11.

## Kesimpulan
*A Tree Search* bekerja dengan memilih jalur berdasarkan biaya total `f(n) = g(n) + h(n)` terkecil tanpa menghindari eksplorasi ulang. Perbedaan utama antara *A Tree Search* dan *A Graph Search* terletak pada tidak adanya explored set dalam Tree Search, sehingga simpul dapat dikunjungi lebih dari sekali dalam proses pencarian. Hal ini membuat *A Tree Search* lebih cocok untuk pencarian dalam struktur pohon, di mana tidak ada kemungkinan siklus. Namun, dalam graf yang memiliki siklus, metode ini bisa menjadi kurang efisien karena memungkinkan eksplorasi ulang terhadap simpul yang sama berkali-kali, sehingga dapat meningkatkan waktu komputasi dan penggunaan memori.
<br><br>

## 📌 A-Star Graph
Kode ini mengimplementasikan algoritma *A Graph Search*, yang digunakan untuk menemukan jalur optimal dari simpul awal ke simpul tujuan dalam graf berbobot. Algoritma ini menggunakan fungsi evaluasi:

𝑓
(
𝑛
)
`=`
𝑔
(
𝑛
)
+
ℎ
(
𝑛
)
=

di mana:<br>
- `g(n)` = biaya aktual dari simpul awal ke simpul saat ini.
- `h(n)` = perkiraan biaya dari simpul saat ini ke tujuan (heuristik).

Perbedaan utama antara *A Graph Search* dan *A Tree Search* adalah penggunaan dictionary explored, yang memastikan bahwa setiap simpul hanya dieksplorasi sekali dan hanya diperbarui jika ditemukan jalur dengan biaya lebih rendah.

##  🚀 Bagaimana Algoritma ini Bekerja?
1. Mulai dari S (biaya awal = 0).
2. Dari S, pilih simpul dengan f(n) terendah:
     - `A` dengan f(A) = 3 + 9 = 12.
     - `E` dengan f(E) = 2 + 3 = 5 (lebih kecil, jadi dipilih).
3. Dari E, pilih simpul dengan f(n) terendah:
     - `D` dengan f(D) = (2 + 6) + 5 = 11.
4. Dari D, ke G dengan f(G) = (2 + 6 + 3) + 0 = 11.
5. Sampai tujuan G dengan total biaya 11.

## Kesimpulan
*A Graph Search* memilih jalur dengan biaya f(n) terkecil sambil menghindari eksplorasi ulang simpul yang telah ditemukan dengan biaya lebih rendah. Berbeda dengan *A Tree Search*, algoritma ini menggunakan explored set sehingga hanya mengeksplorasi simpul jika jalur baru lebih optimal. Keunggulannya adalah lebih efisien dalam graf dengan siklus, karena tidak mengunjungi simpul yang sama berulang kali. Namun, kekurangannya adalah membutuhkan lebih banyak memori untuk menyimpan simpul yang telah dieksplorasi.
