Link: https://roselia-evanny-footballshop.pbp.cs.ui.ac.id/

<details>
<Summary><b>Tugas 2</b></Summary>
Penjelasan mengenai implementasi checklist:
Pertama, saya membuat direktori baru sebagai letak proyek ini. Kemudian, saya melakukan instalasi terhadap dependencies dan membuat proyek Django. Kemudian, saya membuat environment variables untuk menyimpan kredensial database dan pengaturan environment. Kemudian saya menambahkan beberapa konfigurasi di settings.py, seperti menambahkan local host sebagai host yang dapat mengakses web di ALLOWED_HOSTS. Kemudian saya mengubah konfigurasi database, yaitu pada proses production, database yang digunakan adalah PostgreSQL, sedangkan pada proses development, database yang digunakan adalah SQLite. Selanjutnya, saya melakukan migrasi database dan menjalankan servernya. Ini berarti proyek Django berhasil dibuat.

Selanjutnya, saya menghubungkan direktori letak proyek ini ke github. Sebelum itu, saya membuat berkas .gitignore agar berkas yang tercantum di .gitignore, seperti kredensial database atau pengaturan environment, tidak di-push ke github. Selanjutnya, saya menghubungkan proyek ini ke PWS dan menambahkan URL deployment PWS ke ALLOWED_HOSTS di settings.py. Kemudian, saya melakukan add, commit, dan push ke github dan PWS.

Selanjutnya, saya membuat aplikasi main dan mendaftarkannya ke INSTALLED_APPS di settings.py. Selanjutnya, saya membuat berkas .html di aplikasi main, yang berisi informasi nama dan NPM saya. Kemudian, saya membuat model di main, yaitu model Product, saya menambahkan beberapa atribut wajib dan fungsi, lalu melakukan migrasi untuk mengubah struktur tabel basis data sesuai dengan model yang telah dibuat. Kemudian, saya menambahkan fungsi show_main di views.py pada main. Fungsi ini akan menampilkan data yang sesuai ke berkas .html yang sebelumnya telah dibuat.

Tahap selanjutnya adalah melakukan routing dengan membuat berkas urls.py di main. Fungsi show_main perlu di-import ke urls.py, agar fungsi dapat dipanggil ketika URL cocok dengan pola yang ditentukan. Kemudian, saya menambahkan urls.py yang berada di main ke urls.py yang berada di proyek. Sehingga, apabila ditemukan URL yang cocok, maka akan diteruskan ke urls.py di aplikasi. Kemudian saya melakukan add, commit, dan push, agar perubahan yang dilakukan bisa diperbarui.

Secara singkat, saya membuat proyek Django baru, mengubah konfigurasinya, lalu menghubungkannya ke github dan di-deploy di PWS terlebih dahulu. Setelah itu, saya baru membuat aplikasi main, berkas .html, views.py, membuat model, dan routing pada urls.py di main untuk memetakan fungsi yang telah dibuat di views.py.

Penjelasan mengenai bagan request client ke web aplikasi berbasis Django:
Referensi bagan: https://www.google.com/url?sa=i&url=https%3A%2F%2Fagus-hermanto.com%2Fblog%2Fdetail%2Fdjango-flask-framework-python-untuk-web-design-dan-web-development&psig=AOvVaw1GkcxNYxSd5Kl1g29ZGEra&ust=1757432943111000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCLDw84DCyY8DFQAAAAAdAAAAABAK
![Bagan mengenai urls.py, views.py, models.py, dan .html](image.png)
Ketika user melakukan request, request tersebut akan diterima server, lalu akan dibaca urls.py untuk menyocokkan URL yang diminta user ke fungsi yang sesuai di views.py. Jika dibutuhkan data, maka views.py akan memanggil models.py untuk membaca atau menulis data di database. Kemudian, view akan mengirim data ke berkas .html yang dirender menjadi halaman web dan akan ditampilkan ke user.

Penjelasan mengenai settings.py dalam proyek Django:
settings.py dalam proyek Django berfungsi untuk mengatur konfigurasi proyek. Sehingga, pengembang dapat mengatur hal-hal penting hanya dalam satu berkas. settings.py mengatur keamanan proyek, database yang digunakan,  mengatur aplikasi yang digunakan, serta dapat mengatur bahasa dan zona waktu yang digunakan. Dalam tugas ini, beberapa contoh penggunaan settings.py adalah ketika mengubah penggunaan database yang berbeda untuk proses production dan development. Selain itu, ketika membuat aplikasi main, main perlu dicantumkan di INSTALLED_APPS di settings.py. Pada settings.py, terdapat juga pengaturan DEBUG, dimana apabila DEBUG=TRUE, maka akan dimunculkan penjelasan errornya, ini berguna untuk proses development. Sedangkan pada DEBUG=FALSE, tidak akan dimunculkan penjelasan error, ini berguna untuk proses production. Dengan adanya settings.py, ini memudahkan pengembang untuk mengatur semua pengaturan penting.

Penjelasan mengenai cara kerja migrasi database di Django:
Migrasi database di Django adalah proses membuat dan mengubah struktur database berdasarkan definisi model yang berada di berkas models.py. Jadi, setelah membuat model di berkas models.py, perlu dijalankan instruksi python manage.py makemigrations. Instruksi ini akan mempersiapkan file migrasi yang merepresentasikan perubahan pada model. Kemudian, dijalankan instruksi python manage.py migrate. Instruksi ini akan menjalankan semua perubahan yang tercantum pada file migrasi yang sebelumnya telah dibuat, sehingga tabel database akan diperbarui. Sehingga, ini membuat pengelolaan database lebih mudah.
Referensi: 
UNMAHA. (2024). Migrasi Database Django: Langkah-langkah yang Benar untuk Pengembangan Tanpa Masalah. Diambil kembali dari UNMAHA: https://blog.unmaha.ac.id/migrasi-database-django-langkah-langkah-yang-benar-untuk-pengembangan-tanpa-masalah/

Penjelasan mengenai framework Django sebagai permulaan pembelajaran pengembangan perangkat lunak:
Menurut saya, framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena Django menggunakan bahasa pemrograman Python, yaitu salah satu bahasa yang populer di kalangan developer, terutama pemula. Selain itu, banyak fitur bawaan sehingga developer tidak perlu membuatnya sendiri, seperti sistem autentikasi,ORM (Object Relational Mapper) yang menghubungkan Python dengan database, dan berbagai macam lainnya. Sehingga, bisa lebih fokus untuk memahami konsep dasar web development. Selain itu, Django memiliki fleksibilitas tinggi karena dapat dijalankan di berbagai platform. Django juga memiliki keamanan yang baik, framework ini dilengkapi fitur untuk melindungi serangan siber seperti Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), dan SQL injection.
Referensi:
Kvartalnyi, N. (2025, Maret 30). 10 Advantages of Using Django for Web Development. Diambil kembali dari inoxoft: https://djangostars.com/blog/top-14-pros-using-django-web-development/
Ryabtsev, A. (2025, Januari 9). Top 14 Pros of Using Django for Python Web Development. Diambil kembali dari djangostars: https://inoxoft.com/blog/10-advantages-of-using-django-for-web-development/

Feedback untuk asisten dosen tutorial 1:
Saya merasa asisten dosen sangat membantu dalam pengerjaan tutorial, asisten dosen menjelaskan dengan jelas dan tanggap untuk membantu apabila terdapat masalah pada pengerjaannya.
</details>

<details>
<Summary><b>Tugas 3</b></Summary>

</details>