import requests
import os

def send_sms(phone_number, message):
    try:
        apiUrl = 'https://arman83939.000webhostapp.com/customsms.php'
        payload = {'number': phone_number, 'msg': message}
        response = requests.get(apiUrl, params=payload)
        
        if response.status_code == 200:
            print("\033[92mSMS sent successfully!\033[0m")  # Green color for success message
        else:
            print("Failed to send SMS.")
    except Exception as e:
        print("An error occurred:", e)

def clear_screen():
    os.system('clear')

if __name__ == "__main__":
    while True:
        clear_screen()
        print("\033[92m╔═══════════════════════════╗")
        print("║  _______ _____  _____     ║")
        print("║  |__   __/ ____|/ ____|   ║")
        print("║     | | | |    | (___     ║")
        print("║     | | | |     \___ \    ║")
        print("║     | | | |____ ____) |   ║")
        print("║     |_|  \_____|_____/    ║")  # Green color for logo
        print("║  T𝙀𝙍𝙈𝙐𝙓 𝘾𝙊𝙈𝙈𝘼𝙉𝘿 𝙎𝙏𝙊𝙍𝙀 ║")  # Green color for highlighted text
        print("╚═══════════════════════════╝")
        print("\033[0mTCS")
        print("FOLLOW US ON TELEGRAM: 𝙏𝙀𝙍𝙈𝙐𝙓 𝘾𝙊𝙈𝙈𝘼𝙉𝘿 𝙎𝙏𝙊𝙍𝙀 ")
        print("FOLLOW US ON FACEBOOK: 𝙏𝙀𝙍𝙈𝙐𝙓 𝘾𝙊𝙈𝙈𝘼𝙉𝘿 𝙎𝙏𝙊𝙍𝙀 ")
        
        phone_number = input("\n\n💕Enter phone number: ")  # Two line gaps between "FOLLOW US ON FACEBOOK" and "Enter phone number"
        message = input("💕Enter message: ")
        
        send_sms(phone_number, message)
        input("Press Enter to send another message...")
