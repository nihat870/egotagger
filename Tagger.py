import random, os, logging, asyncio 
from telethon import Button 
from telethon import TelegramClient, events 
from telethon.sessions import StringSession 
from telethon.tl.types import ChannelParticipantsAdmins 
 
logging.basicConfig( 
    level=logging.INFO, 
    format='%(name)s - [%(levelname)s] - %(message)s' 
) 
LOGGER = logging.getLogger(name) 
 
api_id = int(os.environ.get("APP_ID")) 
api_hash = os.environ.get("API_HASH") 
bot_token = os.environ.get("TOKEN") 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token) 
 
 
anlik_calisan = [] 
 
tekli_calisan = [] 
 
 
 
@client.on(events.NewMessage(pattern="^/start$")) 
async def start(event): 
      await event.reply("🤖MERYEM TAG Bot Qrupunuzdakı Demək olar ki, Bütün Üzvləri Tağ Edə Bilərəm Yazın =======> / help üçün yardım **", 
                    buttons=( 
                    
        [Button.url('Beni Gruba Ekle ➕', 'https://t.me/meryemtag_bot?startgroup=a')], 
                      [Button.url('Support🛠', 'https://t.me/cosmic_vibes_33')], 
                      [Button.url('Resmi Kanal📣', 'https://t.me/Fake_Love_33')], 
        [Button.url('Developer👨🏻‍💻', 'https://t.me/nihat_33')], 
                    ), 
                    link_preview=False 
                   ) 
@client.on(events.NewMessage(pattern="^/help$")) 
async def help(event): 
  helptext = "🤖 MERYEM TAG Bot Əmrləri \n\n/tag <səbəb> - 5-li Tağ edir\n\n/utag <səbəb> - Emoji ile Tağ edir\n\n/tektag səbəb - Userləri Tək Tək Tağ edir\n\n/admins səbəb - adminləri Tək Tək Tağ Edər\n\n/start - botu başladır" 
  await event.reply(helptext, 
                    buttons=( 
                      [Button.url('Beni Gruba Ekle➕', 'https://t.me/meryemtag_bot?startgroup=a')], 
                      [Button.url('Resmi Grup 👨‍💻', 'https://t.me/cosmic_vibes_33')], 
                      [Button.url('Resmi Kanal🔖', 'https://t.me/Fake_Love_33')], 
        [Button.url('Developer🧑‍🔧', 'https://t.me/nihat_33')], 
                    ), 
                    link_preview=False 
                   ) 
  
@client.on(events.NewMessage(pattern="^/reklam$")) 
async def help(event): 
  helptext = "Çox funksiyalı Qrup Sahibləri @meryemtag_bot Sizin üçün Tağ Botu Tapmağa Çalışır:\n\n📌 5-tağ\n📌 Emoji stikerləri\n📌 Tək Taq\n📌 Yalnız Adminləri Tağlayın\n📌\n\n Cox Funksiyalı Siz @GLOBALTAGGER_Bot -u qrupunuza admin kimi əlavə edə və asanlıqla üzv ola bilərsiniz, tağlar təyin edə bilərsiniz. " 
  await event.reply(helptext, 
                    buttons=( 
                      [Button.url('Botu Gruba Ekle➕', 'https://t.me/meryemtag_bot?startgroup=a')], 
                    ), 
                    link_preview=False 
                   ) 
  
  
 
@client.on(events.NewMessage(pattern='^(?i)/cancel')) 
async def cancel(event): 
  global anlik_calisan 
  anlik_calisan.remove(event.chat_id) 
 
 
emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ") 
 
 
@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def mentionall(event): 
  global anlik_calisan 
  if event.is_private: 
    return await event.respond("Bu əmr qruplar və kanallar üçün etibarlıdır.❗️") 
   
  admins = [] 
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins): 
    admins.append(admin.id) 
  if not event.sender_id in admins: 
    return await event.respond("Bu komutu sadace yoneticiler kullana bilir〽️") 
   
  if event.pattern_match.group(1): 
    mode = "text_on_cmd" 
    msg = event.pattern_match.group(1) 
  elif event.reply_to_msg_id: 
    mode = "text_on_reply" 
    msg = event.reply_to_msg_id 
    if msg == None: 
        return await event.respond("Keçmiş mesajlar üçün necə tag edəcəyimi bilmirəm") 
  elif event.pattern_match.group(1) and event.reply_to_msg_id: 
    return await event.respond("Tag etmək üçün səbəb yoxdur❗️") 
  else: 
    return await event.respond("Etiketdə başlamaq üçün səbəb yazın...!") 
   
  if mode == "text_on_cmd": 
    anlik_calisan.append(event.chat_id) 
    usrnum = 0 
    usrtxt = "" 
    async for usr in client.iter_participants(event.chat_id): 
      usrnum += 1 
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) " 
      if event.chat_id not in anlik_calisan: 
        await event.respond(" Etiket əməliyyatı uğurla dayandırıldı❌") 
        return 
      if usrnum == 5: 
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}") 
        await asyncio.sleep(2) 
        usrnum = 0 
        usrtxt = "" 
         
   
  if mode == "text_on_reply": 
    anlik_calisan.append(event.chat_id) 
  
    usrnum = 0 
    usrtxt = "" 
    async for usr in client.iter_participants(event.chat_id): 
      usrnum += 1 
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) " 
      if event.chat_id not in anlik_calisan: 
        await event.respond("Proses Uğurla dayandırıldı\n\nBurda sizin reklamınız ola bilər. @nihat_33❌") 
        return 
      if usrnum == 5: 
        await client.send_message(event.chat_id, usrtxt, reply_to=msg) 
        await asyncio.sleep(2) 
        usrnum = 0 
        usrtxt = "" 
 
 
@client.on(events.NewMessage(pattern='^(?i)/cancel')) 
async def cancel(event): 
  global anlik_calisan 
  anlik_calisan.remove(event.chat_id) 
 
 
@client.on(events.NewMessage(pattern="^/tag ?(.*)")) 
async def mentionall(event): 
  global anlik_calisan 
  if event.is_private: 
    return await event.respond("Bu əmr qruplar və kanallar üçün etibarlıdır.❗️**") 
   
  admins = [] 
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins): 
    admins.append(admin.id) 
  if not event.sender_id in admins: 
    return await event.respond("Bu əmrdən yalnız idarəçilər istifadə edə bilər.〽️") 
   
  if event.pattern_match.group(1): 
    mode = "text_on_cmd" 
    msg = event.pattern_match.group(1) 
  elif event.reply_to_msg_id: 
    mode = "text_on_reply" 
    msg = event.reply_to_msg_id 
    if msg == None: 
        return await event.respond("Əvvəlki Mesajlara Cavab Verməyin") 
  elif event.pattern_match.group(1) and event.reply_to_msg_id: 
    return await event.respond("Başlamaq üçün heç bir səbəb yoxdur❗️") 
  else: 
    return await event.respond("Başlamaq üçün heç bir səbəb yoxdur") 
   
  if mode == "text_on_cmd": 
    anlik_calisan.append(event.chat_id) 
    usrnum = 0 
    usrtxt = "" 
    async for usr in client.iter_participants(event.chat_id): 
      usrnum += 1 
      usrtxt += f"👥 - [{usr.first_name}](tg://user?id={usr.id}) \n" 
      if event.chat_id not in anlik_calisan: 
        await event.respond("Əməliyyat Uğurla Dayandırıldı\n\nBurda sizin reklamınız ola bilər @nihat_33❌") 
        return 
      if usrnum == 5: 
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
	await asyncio.sleep(2) 
        usrnum = 0 
        usrtxt = "" 
         
   
  if mode == "text_on_reply": 
    anlik_calisan.append(event.chat_id) 
  
    usrnum = 0 
    usrtxt = "" 
    async for usr in client.iter_participants(event.chat_id): 
      usrnum += 1 
      usrtxt += f"👥 - [{usr.first_name}](tg://user?id={usr.id}) \n" 
      if event.chat_id not in anlik_calisan: 
        await event.respond("Əməliyyat Uğurla Dayandırıldı❌") 
        return 
      if usrnum == 5: 
        await client.send_message(event.chat_id, usrtxt, reply_to=msg) 
        await asyncio.sleep(2) 
        usrnum = 0 
        usrtxt = "" 
 
@client.on(events.NewMessage(pattern='^(?i)/cancel')) 
async def cancel(event): 
  global anlik_calisan 
  anlik_calisan.remove(event.chat_id) 
  
 
@client.on(events.NewMessage(pattern="^/tektag ?(.*)")) 
async def mentionall(event): 
  global tekli_calisan 
  if event.is_private: 
    return await event.respond("Bu əmr qruplar və kanallar üçün etibarlıdır.❗️") 
   
  admins = [] 
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins): 
    admins.append(admin.id) 
  if not event.sender_id in admins: 
    return await event.respond("Bu əmrdən yalnız idarəçilər istifadə edə bilər〽️") 
   
  if event.pattern_match.group(1): 
    mode = "text_on_cmd" 
    msg = event.pattern_match.group(1) 
  elif event.reply_to_msg_id: 
    mode = "text_on_reply" 
    msg = event.reply_to_msg_id 
    if msg == None: 
        return await event.respond("**Əvvəlki mesajı etiketləyə bilmirəm*") 
  elif event.pattern_match.group(1) and event.reply_to_msg_id: 
    return await event.respond("Başlamaq üçün Səbəb Yazın❗️") 
  else: 
    return await event.respond("Əməliyyata başlamağın səbəbini yazın..") 
   
  if mode == "text_on_cmd": 
    tekli_calisan.append(event.chat_id) 
    usrnum = 0 
    usrtxt = "" 
    async for usr in client.iter_participants(event.chat_id): 
      usrnum += 1 
      usrtxt += f"👤 - [{usr.first_name}](tg://user?id={usr.id}) \n" 
      if event.chat_id not in tekli_calisan: 
        await event.respond("Əməliyyat Uğurla Dayandırıldı\n\nBurda sizin reklamınız ola bilər @nihat_33❌**") 
        return 
      if usrnum == 1: 
        await client.send_message(event.chat_id, f"{usrtxt} {msg}") 
        await asyncio.sleep(2) 
        usrnum = 0 
        usrtxt = "" 
         
   
  if mode == "text_on_reply": 
    tekli_calisan.append(event.chat_id) 
  
    usrnum = 0 
    usrtxt = "" 
    async for usr in client.iter_participants(event.chat_id): 
      usrnum += 1 
      usrtxt += f"👤 - [{usr.first_name}](tg://user?id={usr.id}) \n" 
      if event.chat_id not in tekli_calisan: 
        await event.respond("Əməliyat uğurla dayandırıldı\n\nBurda sizin reklamınız ola bilər @nihat_33❌**") 
        return 
      if usrnum == 1: 
        await client.send_message(event.chat_id, usrtxt, reply_to=msg) 
        await asyncio.sleep(2) 
        usrnum = 0 
        usrtxt = "" 
 
@client.on(events.NewMessage(pattern='^(?i)/cancel')) 
async def cancel(event): 
  global tekli_calisan 
  tekli_calisan.remove(event.chat_id) 
  
 
 
@client.on(events.NewMessage(pattern="^/admins ?(.*)")) 
async def mentionall(tagadmin): 
 
 if tagadmin.pattern_match.group(1): 
  seasons = tagadmin.pattern_match.group(1) 
 else: 
  seasons = "" 
 
 chat = await tagadmin.get_input_chat() 
 a_=0 
 await tagadmin.delete() 
 async for i in client.iter_participants(chat, filter=cp): 
  if a_ == 500: 
   break 
  a_+=5 
  await tagadmin.client.send_message(tagadmin.chat_id, "[{}](tg://user?id={}) {}".format(i.first_name, i.id, seasons)) 
  sleep(0.5) 
 
 
print(">> Bot işləyir narahat olmayın 🚀 @nihat_33 Məlumat ala bilərsiniz <<") 
client.run_until_disconnected()
