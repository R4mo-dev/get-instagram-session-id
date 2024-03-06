# channel t.me/noxyarchive
import requests
import uuid
import telebot
from telebot import types
token = input('✓ Enter Token : ')
bot = telebot.TeleBot(token)
brok = types.InlineKeyboardButton(text='R 4 M O', url='t.me/noxyarchive')

@bot.message_handler(commands=["start"])
def start(message):
    b = types.InlineKeyboardMarkup()
    b.add(brok)
    bot.send_message(
        message.chat.id, 'Welcome to Session ID Bot 😊\nSend Your Username and Password in the Following Format user:pass', reply_markup=b)


@bot.message_handler(content_types=["text"])
def chlogin(message):
    uid = uuid.uuid4()
    text = message.text
    user_pass = text.split(':')
    if len(user_pass) == 2:
        (user, password) = user_pass
        url = 'https://i.instagram.com/api/v1/accounts/login/'
        headers = {
            'Content-Length': '345',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'i.instagram.com',
            'Connection': 'Keep-Alive',
            'User-Agent': 'Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)',
            'Cookie': 'mid=Y-9s1AABAAFWUWzlpPxtinw4eZuq; csrftoken=lBwsSpxhuksvjh6Tg4Hn4enPF2Bg7WNo',
            'Cookie2': '$Version=1',
            'Accept-Language': 'ar-EG, en-US',
            'X-IG-Connection-Type': 'MOBILE(LTE)',
            'X-IG-Capabilities': 'AQ==',
            'Accept-Encoding': 'gzip'}
        data = {
            'username': user,
            'password': password,
            'device_id': uid,
            'guid': uid}
        r = requests.post(url, headers=headers, data=data)
        if 'logged_in_user' in r.text:
            bot.send_message(message.chat.id, 'Succesfull Login ✅')
            session_id = r.cookies.get_dict().get('sessionid')
            bot.send_message(message.chat.id, f'''Session ID: {session_id}''')
            bot.send_message(message.chat.id, 'Please Use /start Command')
        else:
            bot.send_message(message.chat.id, 'Failed Login ⛔')
            bot.send_message(
                message.chat.id, 'Please Try Again Using the /start Command')
    else:
        bot.reply_to(
            message, 'Please write the username and password as user:pass')
        bot.send_message(
            message.chat.id, 'Please Try Again Using the /start Command')

bot.polling()
