import telebot
from telebot import types
import os
bot=telebot.TeleBot('Your bot token')

list=['87.232.49.136', '218.102.181.63', '49.159.134.140', '36.64.247.206', '101.195.139.169', '119.196.102.177', '101.42.182.112', '168.70.52.129', '3.46.61.190', '198.224.185.130']

@bot.message_handler(commands=[('buy'),('getDnsPq'),('getDnsxp'),('getDnsmb'),('getDnsFp'),('getDnsjN'),('getDnsbx'),('getDnsZD'),('getDnsiJ'),('buy')])
def send_dns(message):


    
      try:
            if message.text=='/buy':
                  markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                  super_button=types.KeyboardButton('🚀سوپر DNS')
                  normal_button=types.KeyboardButton('👽اDNS اقتصادی')
                  support_button=types.KeyboardButton('پشتیبانی☎️')
                  markup.add(super_button,normal_button, support_button)
                  bot.send_message(message.chat.id,'اDNS خود را انتخاب کنید',reply_markup=markup)

            if message.text=='/getDnsPq':
                  if '49.159.134.140' in list:
                        bot.reply_to(message,f"Primary: {list[0]} Secondary: 10.202.10.10")
                        list.remove('49.159.134.140')
                  else:
                        bot.reply_to(message,"این dns قبلا خریده شده برای خرید dns از دستور /buy استفده کنید" )

            if message.text=='/getDnsxp':
                  if '36.64.247.206' in list:
                        bot.reply_to(message,f"Primary: {list[0]} Secondary: 10.202.10.10")
                        list.remove('36.64.247.206')
                  else:
                        bot.reply_to(message,"این dns قبلا خریده شده برای خرید dns از دستور /buy استفده کنید" )


            if message.text=='/getDnsmb':
                  if '101.195.139.169' in list:
                        bot.reply_to(message,f"Primary: {list[0]} Secondary: 10.202.10.10")
                        list.remove('101.195.139.169')
                  else:
                        bot.reply_to(message,"این dns قبلا خریده شده برای خرید dns از دستور /buy استفده کنید" )


            if message.text=='/getDnsFp':
                  if '119.196.102.177' in list:
                        bot.reply_to(message,f" Primary: {list[0]} Secondary: 10.202.10.10")
                        list.remove('119.196.102.177')
                  else:
                        bot.reply_to(message,"این dns قبلا خریده شده برای خرید dns از دستور /buy استفده کنید" )


            if message.text=='/getDnsjN':
                  if '101.42.182.112' in list:
                        bot.reply_to(message,f"Primary: {list[0]} Secondary: 10.202.10.10")
                        list.remove('101.42.182.112')
                  else:
                        bot.reply_to(message,"این dns قبلا خریده شده برای خرید dns از دستور /buy استفده کنید" )


            if message.text=='/c':
                  if '168.70.52.129' in list:
                        bot.reply_to(message,f" Primary: {list[0]} Secondary: 10.202.10.10")
                        list.remove('168.70.52.129')
                  else:
                        bot.reply_to(message,"این dns قبلا خریده شده برای خرید dns از دستور /buy استفده کنید" )


            if message.text=='/getDnsZD':
                  if '3.46.61.190' in list:
                        bot.reply_to(message,f"Primary: {list[0]} Secondary: 10.202.10.10")
                        list.remove('3.46.61.190')
                  else:
                        bot.reply_to(message,"این dns قبلا خریده شده برای خرید dns از دستور /buy استفده کنید" )


            if message.text=='/getDnsiJ':
                  if '198.224.185.130' in list:
                        bot.reply_to(message,f"Primary: {list[0]} Secondary: 10.202.10.10")
                        list.remove('198.224.185.130')
                  else:
                        bot.reply_to(message,"این dns قبلا خریده شده برای خرید dns از دستور /buy استفده کنید" )
            
      except Exception as e:
            print(f'error{e}')
@bot.message_handler(commands=['start'])
def send_welcome(message):
      chat_id = message.chat.id
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      buy_button = types.KeyboardButton('خرید DNS اختصاصی🪐')
      markup.add(buy_button)
      bot.send_message(message.chat.id,'به بات شاپ بزرگ 🪐DLshop خوش امدی',reply_markup=markup)

      if os.path.exists('chat_id.text'):
                with open('chat_id.text', 'r') as f:
                    existing_ids = f.read().splitlines()
      else:
                existing_ids = []

            # Write the chat_id to the file if it does not already exist
      if str(chat_id) not in existing_ids:
                with open("chat_id.text", 'a') as f:  # Changed from 'chat_id.text' to 'chat_id'
                    f.write(f"{chat_id}\n") 

@bot.message_handler(func= lambda message:message.text=='خرید DNS اختصاصی🪐' )

def buy_button(message):
      markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
      super_button=types.KeyboardButton('🚀سوپر DNS')
      normal_button=types.KeyboardButton('👽اDNS اقتصادی')
      support_button=types.KeyboardButton('پشتیبانی☎️')
      markup.add(super_button,normal_button, support_button)
      bot.send_message(message.chat.id,'اDNS خود را انتخاب کنید',reply_markup=markup)



@bot.message_handler(func= lambda message:message.text=='پشتیبانی☎️' )

def buy_button(message):
      markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
      back_button=types.KeyboardButton('🔙باز گشت')
      markup.add(back_button,)
      bot.send_message(message.chat.id,"جهت داشتن هرگونه مشکل به ایدی @Danims39 پیام دهید",reply_markup=markup)



                  
@bot.message_handler(func=lambda message: message.text=='👽اDNS اقتصادی')
def payment(message):
      markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
      back_button=types.KeyboardButton('🔙باز گشت')
      markup.add(back_button)
      bot.send_message(message.chat.id,"""برای خرید DNS اختصاصی مبلغ 39,000  تومان  را به شماره‌ی حساب زیر واریز کنید 👇🏻
            
        
        ==================== 
        6219861975009787
        سعید مسعودی فرد 
        ====================

‼️حتما فیش رسید خود را همینجا ارسال کنید

‼️توجه داشته باشید بعد از تحویل DNS  هیچ پولی برگشت داده نمیشود""",reply_markup=markup)
      


@bot.message_handler(func=lambda message: message.text=='🚀سوپر DNS')

def payment_2(message):
      markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
      back_button=types.KeyboardButton('🔙باز گشت')
      markup.add(back_button)
      bot.send_message(message.chat.id,"""برای خرید DNS اختصاصی مبلغ 59,000  تومان  را به شماره‌ی حساب زیر واریز کنید 👇🏻
        
        ==================== 
        6219861975009787
        سعید مسعودی فرد 
        ====================

‼️حتما فیش رسید خود را همینجا ارسال کنید

‼️توجه داشته باشید بعد از تحویل DNS  هیچ پولی برگشت داده نمیشود""",reply_markup=markup)




@bot.message_handler(func=lambda message: message.text=='🔙باز گشت')

def back_button(message):
      markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
      super_button=types.KeyboardButton('🚀سوپر DNS')
      normal_button=types.KeyboardButton('👽اDNS اقتصادی')
      support_button=types.KeyboardButton('پشتیبانی☎️')
      markup.add(super_button,normal_button,support_button)
      bot.send_message(message.chat.id,'اDNS خود را انتخاب کنید',reply_markup=markup)

   


@bot.message_handler(content_types='photo')
def loding(message):
      bot.reply_to(message,"""✅✅درخواست شما با موفقیت ارسال شد
بعد بررسی و تایید فیش, DNS برای شما فرستاده میشود""")

bot.polling()
