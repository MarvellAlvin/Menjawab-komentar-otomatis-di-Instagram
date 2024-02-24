import instagram_private_api

# Masukkan kredensial Instagram Anda
username = "username_anda"
password = "password_anda"

# Buat objek API Instagram
api = instagram_private_api.Client(username, password)

# Dapatkan komentar terbaru untuk postingan
post_id = "1234567890"
comments = api.get_post_comments(post_id)

# Buat dictionary untuk menyimpan kata kunci dan balasan
keywords = {
    "ai": "https://chat.openai.com/",
    "halo": "Halo Juga",
    "keren": "Terima kasih!"
}

# Loop melalui komentar dan balas komentar yang mengandung kata kunci
for comment in comments:
    for keyword, reply in keywords.items():
        if keyword in comment["text"]:
            api.reply_comment(comment["id"], reply)

# Tutup koneksi API
api.end_session()
