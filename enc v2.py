# Fungsi untuk mengenkripsi string dengan rotasi karakter
def encrypt_string(s, shift):
    encrypted_string = ""
    for char in s:
        if char.isalpha():
            shifted_char = chr((ord(char) + shift - 65) % 26 + 65) if char.isupper() else chr((ord(char) + shift - 97) % 26 + 97)
            encrypted_string += shifted_char
        else:
            encrypted_string += char
    return encrypted_string

# Kode yang akan dienkripsi
code_to_encrypt = """
# code area
url_1 = f"https://discord.com/api/v9/channels/{Channel_1}/messages"

# get cpu and ram
def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def get_ram_usage():
    
    ram = psutil.virtual_memory()
    ram_total = ram.total
    ram_used = ram.total - ram.available
    ram_percent_used = (ram_used / ram_total) * 100
    return ram_percent_used

if __name__ == "__main__":
  
    cpu_usage = get_cpu_usage()
    ram_usage = get_ram_usage()

# webhok true
# create embed object for webhook

embed = DiscordEmbed(title="AUTO SEND LOG", description=f"**Pesan berhasil dikirim ke id {Channel_1}**", color="03b2f8")
# set image
embed.set_image(url="https://media.discordapp.net/attachments/1224687667338547310/1224689594046349386/standard_5.gif?ex=664157d0&is=66400650&hm=da3f8715b1ed6a24e2aad577d7bb9f1abb52a4118129c662ba34fba41a8d8fe0&")
# set thumbnail
embed.set_thumbnail(url="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRdglAS7d9GYDXsTkkRguKXyVoCZjM3-vL35sPVlra1iRRC0i2OR1CqVhI9jqyY9ri_i8Hq")
# set footer
embed.set_footer(text="Embed Footer Text", icon_url="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRdglAS7d9GYDXsTkkRguKXyVoCZjM3-vL35sPVlra1iRRC0i2OR1CqVhI9jqyY9ri_i8Hq")
# set timestamp (default is now) accepted types are int, float and datetime
embed.set_timestamp()
# add fields to embed
embed.add_embed_field(name="Coming soon", value=f"CPU Usage: {cpu_usage}%")
embed.add_embed_field(name="Coming soon", value=f"RAM Usage: {ram_usage}%")
# add embed object to webhook
webhook.add_embed(embed)

# Fungsi untuk mengirim pesan ke URL dengan delay
def send_message_with_delay(url, payload, headers, delay):
    while True:
        res = requests.post(url, json=payload, headers=headers)
        if res.status_code == 200:
            response = webhook.execute()
        else:
            print("lol")
        time.sleep(delay)

# Fungsi untuk menjalankan program
def run_program():
    print(Back.BLUE +"Selamat datang!")
    
    thread_1 = threading.Thread(target=send_message_with_delay, args=(url_1, payload, headers, delay_1))
    thread_1.start()
    thread_1.join()

run_program()
"""

# Enkripsi kode dengan pergeseran karakter 3
encrypted_code = encrypt_string(code_to_encrypt, 3)
print("Kode yang dienkripsi:")
print(encrypted_code)
