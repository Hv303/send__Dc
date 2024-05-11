url_1 = f"https://discord.com/api/v9/channels/{Channel_1}/messages"
# Fungsi untuk mengirim pesan ke URL dengan delay
def send_message_with_delay(url, payload, headers, delay):
    while True:
        res = requests.post(url, json=payload, headers=headers)
        if res.status_code == 200:
            requests.post(webhook_url, json={"content": "Pesan berhasil dikirim"})
        else:
            requests.post(webhook_url, json={"content": "Gagal mengirim pesan. Kode status: " + str(res.status_code)})
        time.sleep(delay)

# Fungsi untuk menjalankan program
def run_program():
    # Menampilkan pesan selamat datang
    print(Back.BLUE +"Selamat datang!")
    
    # Membuat thread untuk mengirim pesan dengan delay
    thread_1 = threading.Thread(target=send_message_with_delay, args=(url_1, payload, headers, delay_1))
    thread_1.start()

    # Tunggu sampai thread selesai (ini sebenarnya tidak akan pernah terjadi karena thread akan berjalan selamanya)
    thread_1.join()

# Menjalankan program
run_program()
