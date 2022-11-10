import telebot
from telebot import types
from PIL import Image

TOKEN = '5787323340:AAH6wYVQ2mrguHBOiOm8FhcMkU2cOaNeGLs'
bot = telebot.TeleBot(TOKEN)

members = set()
flag_photo_chat = False


@bot.message_handler(commands=['start'])
def starting(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    if (user_id, user_name) not in members:
        members.add((user_id, user_name))
    bot.reply_to(message,
                 text=f"Hi!🫰🏻 My name is 🦜 @chat_popug_bot 🦜 and I'm glad that you decided to invite me here. If you want to see, what I can do, print /help or /options, or you can just print / and see the auxiliary menu ⬇️ ‼️ Don't forget to make me the admin or I won't be able to do some commands ‼️")


@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    user_name = message.new_chat_members[0].first_name
    user_name2 = message.new_chat_members[0].username
    user_id = message.new_chat_members[0].id
    if (user_id, user_name) not in members:
        members.add((user_id, user_name))
    bot.send_message(message.chat.id, f"🦜 🦜 🦜 Let's welcome a new popug {user_name} of this chat! 🦜 🦜 🦜")
    bot.send_message(message.chat.id, f"😏 What is your favorite popug @{user_name2}? 😏")


@bot.message_handler(commands=['help'])
def help_com(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    if (user_id, user_name) not in members:
        members.add((user_id, user_name))
    bot.reply_to(message,
                 text=f'Here are the descriptions of my commands:\n/start - greeting and mini-description about the bot \n'
                      f'/help - the descriptions of bot’s commands \n/options - some commands that user can try\n🦜[@chat_popug_bot should leave] - everyone can ask the bot to leave the chat\n'
                      f'🦜[commands descriptions] - everyone can read the descriptions of bot’s commands\n'
                      f'🦜[count all members] - everyone can find out the number of members in the chat\n'
                      f'🦜[usernames of all administrators] - everyone can look at the usernames of all administrators\n'
                      f'🦜[count all administrators] - everyone can find out the number of administrators in the chat\n'
                      f'🦜[choose someone to ban] - only administrators can choose whom to ban from the list of members, they even can ban other administrators besides themselves\n'
                      f'🦜[delete chat photo] - everyone can delete the chat photo\n'
                      f'🦜[set chat photo with popug] - everyone can change the chat photo by the default photo of popug\n'
                      f'/ban - only administrators can ban someone from the reply, they even can ban other administrators besides themselves\n'
                      f'/unban - only administrators can unban someone from the reply, they even can unban other administrators besides themselves\n'
                      f'/admin - only administrators can make someone an admin, they even can unban other administrators besides themselves, all functions will be available as an administrator\n'
                      f'/id - everyone can get an id of someone by the reply')


@bot.message_handler(commands=['options'])
def options(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    if (user_id, user_name) not in members:
        members.add((user_id, user_name))
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_leave_bot = types.InlineKeyboardButton(text="@chat_popug_bot should leave", callback_data="bot leave")
    btn_count_members = types.InlineKeyboardButton(text="count all members", callback_data="count all members")
    btn_name_admins = types.InlineKeyboardButton(text="usernames of all administrators",
                                                 callback_data="usernames of all administrators")
    btn_ban = types.InlineKeyboardButton(text="choose someone to ban", callback_data="choose someone to ban")
    btn_count_admins = types.InlineKeyboardButton(text="count all administrators",
                                                  callback_data="count all administrators")
    btn_descriptions = types.InlineKeyboardButton(text="commands descriptions", callback_data="commands descriptions")
    btn_delete_chat_photo = types.InlineKeyboardButton(text="delete chat photo", callback_data="delete chat photo")
    btn_set_chat_photo = types.InlineKeyboardButton(text="set chat photo with popug",
                                                    callback_data="set chat photo with popug")
    markup.add(btn_descriptions, btn_leave_bot, btn_count_members, btn_count_admins, btn_name_admins, btn_ban,
               btn_delete_chat_photo, btn_set_chat_photo)
    bot.send_message(message.chat.id, "😯 What @chat_popug_bot can do 😯", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "bot leave")
def callback_inline_first(call):
    bot.send_message(call.message.chat.id, text="I'm really sad, that you ask me to leave 😭 Bye...")
    bot.leave_chat(call.message.chat.id)


@bot.callback_query_handler(func=lambda call: call.data == "commands descriptions")
def callback_inline_second(call):
    bot.send_message(call.message.chat.id,
                     text=f'Here are the descriptions of my commands:\n/start - greeting and mini-description about the bot \n'
                          f'/help - the descriptions of bot’s commands \n/options - some commands that user can try\n🦜[@chat_popug_bot should leave] - everyone can ask the bot to leave the chat\n'
                          f'🦜[commands descriptions] - everyone can read the descriptions of bot’s commands\n'
                          f'🦜[count all members] - everyone can find out the number of members in the chat\n'
                          f'🦜[usernames of all administrators] - everyone can look at the usernames of all administrators\n'
                          f'🦜[count all administrators] - everyone can find out the number of administrators in the chat\n'
                          f'🦜[choose someone to ban] - only administrators can choose whom to ban from the list of members, they even can ban other administrators besides themselves\n'
                          f'🦜[delete chat photo] - everyone can delete the chat photo\n'
                          f'🦜[set chat photo with popug] - everyone can change the chat photo by the default photo of popug\n'
                          f'/ban - only administrators can ban someone from the reply, they even can ban other administrators besides themselves\n'
                          f'/unban - only administrators can unban someone from the reply, they even can unban other administrators besides themselves\n'
                          f'/admin - only administrators can make someone an admin, they even can unban other administrators besides themselves, all functions will be available as an administrator\n'
                          f'/id - everyone can get an id of someone by the reply')


@bot.callback_query_handler(func=lambda call: call.data == "count all members")
def callback_inline_third(call):
    chat = call.message.chat.id
    count = bot.get_chat_members_count(chat)
    bot.send_message(call.message.chat.id, text=f"Here are only {count} popugs 🦜")


@bot.callback_query_handler(func=lambda call: call.data == "usernames of all administrators")
def callback_inline_fourth(call):
    chat = call.message.chat.id
    chat_admins = bot.get_chat_administrators(chat)
    for admins in chat_admins:
        user_name = admins.user.username
        bot.send_message(call.message.chat.id, text=f"@{user_name}")


@bot.callback_query_handler(func=lambda call: call.data == "count all administrators")
def callback_inline_fifth(call):
    chat = call.message.chat.id
    chat_admins = bot.get_chat_administrators(chat)
    bot.send_message(call.message.chat.id, text=f"Here are only {len(chat_admins)} admin popugs 🦜")


@bot.callback_query_handler(func=lambda call: call.data == "delete chat photo")
def callback_inline_eighth(call):
    chat = call.message.chat.id
    try:
        user_name = call.from_user.first_name
        bot.delete_chat_photo(chat)
        bot.send_message(call.message.chat.id, text=f"The popug-{user_name} asked me to delete the chat photo 🪣")
    except:
        bot.send_message(call.message.chat.id, text=f"Your chat doesn't have any photo 🥺")


@bot.callback_query_handler(func=lambda call: call.data == "set chat photo with popug")
def callback_inline_ninth(call):
    im = Image.open('popug.jpg')
    chat = call.message.chat.id
    bot.set_chat_photo(chat, photo=im)
    user_name = call.from_user.first_name
    bot.send_message(call.message.chat.id,
                     text=f"The popug-{user_name} changed photo of the chat by the popug photo 🦜")


@bot.callback_query_handler(func=lambda call: call.data == "choose someone to ban")
def callback_inline_sixth(call):
    chat = call.message.chat.id
    chat_admins = bot.get_chat_administrators(chat)
    user_id = call.from_user.id
    user_name = call.from_user.first_name
    flag = False
    for i in chat_admins:
        if int(i.user.id) == int(user_id):
            flag = True
            break
    if flag:
        markup = types.InlineKeyboardMarkup(row_width=1)
        for user in members:
            btn_username = types.InlineKeyboardButton(text=f"{user[1]}", callback_data=f"{user[0]} {user[1]}")
            markup.add(btn_username)
        bot.send_message(call.message.chat.id, "🦜 All popug-members 🦜", reply_markup=markup)
    else:
        bot.send_message(call.message.chat.id, text=f"The popug-{user_name} isn't the admin and he cannot ban anyone ❌")
        return


@bot.callback_query_handler(func=lambda call: True)
def callback_inline_seventh(call):
    user_id, user_name = call.data.split()
    user = call.from_user.id
    if int(user) == int(user_id):
        bot.send_message(call.message.chat.id, text=f"The {user_name}, you cannot ban yourself ☠️")
        return
    else:
        if (user_id, user_name) in members:
            members.remove((user_id, user_name))
        bot.send_message(call.message.chat.id, text=f"The {user_name} is banned ☠️")
        bot.ban_chat_member(call.message.chat.id, user_id)


@bot.message_handler(commands=['ban'])
def ban(message):
    chat = message.chat.id
    chat_admins = bot.get_chat_administrators(chat)
    user_id1 = message.from_user.id
    user_name1 = message.from_user.first_name
    flag = False
    for i in chat_admins:
        if i.user.id == user_id1:
            flag = True
            break
    if flag:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name
        if int(user_id1) == int(user_id):
            bot.send_message(message.chat.id, text=f"The {user_name1}, you cannot ban yourself ☠️")
            return
        else:
            if message.reply_to_message:
                if (user_id, user_name) in members:
                    members.remove((user_id, user_name))
                user_name_who = message.from_user.username
                user_name_whom = message.reply_to_message.from_user.username
                bot.send_message(message.chat.id, text=f"The @{user_name_who} asked me to ban the @{user_name_whom} ☠️")
                bot.ban_chat_member(message.chat.id, user_id)
    else:
        bot.send_message(message.chat.id, text=f"The popug-{user_name1} isn't the admin and he can't ban anyone ❌")
        return


@bot.message_handler(commands=['unban'])
def unban(message):
    chat = message.chat.id
    chat_admins = bot.get_chat_administrators(chat)
    user_id1 = message.from_user.id
    user_name1 = message.from_user.first_name
    flag = False
    for i in chat_admins:
        if i.user.id == user_id1:
            flag = True
            break
    if flag:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name
        if int(user_id1) == int(user_id):
            bot.send_message(message.chat.id, text=f"The {user_name1}, you cannot unban yourself ☠️")
            return
        else:
            if message.reply_to_message:
                if (user_id, user_name) in members:
                    members.remove((user_id, user_name))
                user_name_who = message.from_user.username
                user_name_whom = message.reply_to_message.from_user.username
                bot.send_message(message.chat.id,
                                 text=f"The @{user_name_who} asked me to unban the @{user_name_whom} ☠️")
                bot.unban_chat_member(message.chat.id, user_id)
    else:
        bot.send_message(message.chat.id, text=f"The popug-{user_name1} isn't the admin and he can't unban anyone ❌")
        return


@bot.message_handler(commands=['admin'])
def unban(message):
    chat = message.chat.id
    chat_admins = bot.get_chat_administrators(chat)
    user_id1 = message.from_user.id
    user_name1 = message.from_user.first_name
    flag = False
    for i in chat_admins:
        if i.user.id == user_id1:
            flag = True
            break
    if flag:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name
        if int(user_id1) == int(user_id):
            bot.send_message(message.chat.id, text=f"The {user_name1}, you cannot make an admin yourself 🛑️")
            return
        else:
            if message.reply_to_message:
                if (user_id, user_name) not in members:
                    members.add((user_id, user_name))
                user_name_who = message.from_user.username
                user_name_whom = message.reply_to_message.from_user.username
                bot.send_message(message.chat.id,
                                 text=f"The @{user_name_who} asked me to make an admin the @{user_name_whom} too 🎉")
                bot.promote_chat_member(message.chat.id, user_id, can_manage_chat=True, can_delete_messages=True,
                                        can_manage_video_chats=True, can_restrict_members=True,
                                        can_promote_members=True,
                                        can_change_info=True, can_post_messages=True, can_edit_messages=True,
                                        can_invite_users=True, can_pin_messages=True, is_anonymous=True)
    else:
        bot.send_message(message.chat.id,
                         text=f"The popug-{user_name1} isn't the admin and he can't make an admin anyone 🛑")
        return


@bot.message_handler(commands=['id'])
def ban(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name
        if (user_id, user_name) not in members:
            members.add((user_id, user_name))
        bot.reply_to(message, text=f"This user_id is: {user_id}")


@bot.message_handler(content_types=['text'])
def after_text(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    if (user_id, user_name) not in members:
        members.add((user_id, user_name))


bot.polling(none_stop=True, interval=0)
