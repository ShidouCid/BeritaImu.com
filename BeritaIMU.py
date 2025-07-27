from flask import Flask, render_template_string

app = Flask(name)

@app.route("/") def home(): html = """ <!DOCTYPE html> <html lang="id"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Breaking News Imu</title> <style> * { box-sizing: border-box; transition: all 0.3s ease; } body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; margin: 0; padding: 20px; color: #333; } .container { max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); opacity: 0; transform: translateY(20px); animation: fadeInUp 0.6s ease-out forwards; } img { width: 100%; border-radius: 10px; margin-top: 20px; transition: transform 0.3s ease; } img:hover { transform: scale(1.03); } h1 { color: #c0392b; font-size: 26px; } .source { font-style: italic; color: #888; margin-top: 12px; font-size: 14px; } .content { margin-top: 25px; line-height: 1.8; white-space: pre-wrap; font-size: 16px; } @keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } } </style> </head> <body> <div class="container"> <h1>Riyan dan Idlan ketahuan selingkuh dan berduaan di kamar 😱</h1> <img src="https://i.postimg.cc/bJsrxh5b/Screenshot-20250727-191130.png" alt="Bukti Foto"> <div class="source">Source by Mr.士道</div> <div class="content"> Skandal Perselingkuhan Sesama Jenis Terungkap: Riyan dan Idlan Diduga Selingkuh dari Pasangan Sah Mereka, Kasus Diserahkan ke Pihak Berwajib

Kota Purwajati, 27 Juli 2025 — Sebuah kasus perselingkuhan yang melibatkan dua pria berinisial R (Riyan) dan I (Idlan) mengejutkan warga Kota Purwajati. Skandal ini menjadi pusat perhatian publik setelah keduanya diduga kuat menjalin hubungan sesama jenis secara diam-diam, meski masing-masing telah memiliki pasangan sah: Dinda (pasangan Riyan) dan Dea (pasangan Idlan).

Kabar ini pertama kali mencuat ke publik setelah Dinda mencurigai perubahan sikap Riyan yang dalam dua bulan terakhir sering pulang larut malam dan enggan bersentuhan fisik. Sementara itu, Dea juga menyampaikan kepada rekan dekatnya bahwa Idlan kerap memberikan alasan yang tidak masuk akal saat diajak bertemu atau sekadar berkabar.

Temuan Bukti dan Percakapan Mencurigakan

Kecurigaan keduanya terkonfirmasi setelah Dinda berhasil mengakses galeri dan pesan dalam aplikasi chatting pribadi milik Riyan. Ditemukan sejumlah foto dan pesan yang menunjukkan kedekatan antara Riyan dan Idlan, mulai dari foto berpelukan di tempat umum hingga pesan bernuansa romantis dan sensual. Salah satu pesan yang menjadi bukti paling mengejutkan berbunyi:

“Kamu tuh satu-satunya yang bikin aku ngerasa hidup, bukan Dinda, bukan siapa pun. Hanya kamu, Lan…”

Tak berselang lama, Dea pun melakukan langkah serupa dan menemukan rekaman suara serta pesan bernada serupa dalam ponsel Idlan. Setelah itu, keduanya—Dinda dan Dea—memutuskan untuk bertemu dan menyusun langkah hukum bersama.

Konfrontasi Terbuka dan Pengakuan di Hadapan Warga

Pada tanggal 23 Juli 2025, sebuah konfrontasi terbuka dilakukan di rumah kontrakan yang disewa Riyan di kawasan Cipulir Baru. Dalam konfrontasi yang disaksikan oleh tetangga sekitar dan beberapa perangkat RT, Riyan dan Idlan akhirnya mengakui hubungan mereka secara emosional dan fisik yang telah berlangsung selama lebih dari lima bulan.

“Kami enggak pernah maksud nyakitin siapa-siapa… tapi perasaan ini muncul begitu aja…,” ujar Riyan dengan suara bergetar, sementara Idlan tampak tertunduk dan enggan berbicara.

Pernyataan tersebut memicu amarah warga, terutama dari keluarga Dinda dan Dea yang merasa dikhianati. Warga pun menuntut agar keduanya diproses secara hukum sesuai peraturan yang berlaku.

Langkah Hukum dan Penyerahan Kasus

Menanggapi tekanan masyarakat dan demi menjaga ketertiban umum, permasalahan ini langsung diserahkan kepada Mas Agus, selaku tokoh masyarakat sekaligus ketua RW setempat, untuk dilakukan mediasi awal. Namun, karena menyangkut unsur dugaan penipuan emosional, pemalsuan hubungan, dan potensi pelanggaran norma sosial, Mas Agus memutuskan untuk menyerahkan kasus ini secara resmi ke pihak kepolisian.

“Kami sudah kumpulkan bukti-bukti dari pihak pelapor dan juga saksi. Karena ini menyangkut nama baik lingkungan serta potensi tindak penipuan dalam hubungan sah, kami percayakan kasus ini kepada pihak yang berwenang,” ujar Mas Agus dalam konferensi pers terbatas.

Setelah proses pelaporan dilakukan, kasus ini kini ditangani langsung oleh Kapolres Purwajati, Kompol Hendrawan Surya. Dalam keterangannya kepada media, Kapolres menyampaikan:

“Kami akan menyelidiki lebih lanjut aspek hukum dari kasus ini. Meskipun hubungan sesama jenis tidak dikriminalisasi secara eksplisit dalam KUHP, namun ada dugaan manipulasi dan kerugian emosional yang bisa ditindaklanjuti. Jika terbukti ada pelanggaran hukum lain seperti kekerasan psikis atau pemalsuan data, tentu akan kami proses secara adil.”

Kesimpulan dan Proses Selanjutnya

Hingga saat ini, Riyan dan Idlan masih berstatus sebagai saksi terlapor. Mereka telah diminta untuk kooperatif selama proses penyelidikan berlangsung. Dinda dan Dea, didampingi oleh kuasa hukum masing-masing, akan terus mengawal kasus ini demi mendapatkan keadilan atas pengkhianatan yang mereka alami.

Masyarakat diimbau untuk tidak melakukan tindakan main hakim sendiri dan menyerahkan proses sepenuhnya kepada penegak hukum.

Kasus ini menjadi cerminan bahwa pengkhianatan dalam hubungan, apapun bentuknya, bukan hanya soal moralitas, namun juga soal tanggung jawab dan kejujuran antarindividu dalam sebuah ikatan yang sah. </div> </div> </body> </html> """ return render_template_string(html)

if name == "main": app.run(debug=True)

