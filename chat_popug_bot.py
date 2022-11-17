import telebot
from telebot import types
from PIL import Image
from collections import defaultdict
import os, random

TOKEN = '5787323340:AAH6wYVQ2mrguHBOiOm8FhcMkU2cOaNeGLs'
bot = telebot.TeleBot(TOKEN)

ALL_MEMBERS = defaultdict(list)
MEMBERS_TO_UNBAN = defaultdict(list)


@bot.message_handler(commands=['start'])
def starting(message):
    global ALL_MEMBERS, MEMBERS_TO_UNBAN
    user_id = int(message.from_user.id)
    user_name = message.from_user.first_name
    if (user_id, user_name) not in ALL_MEMBERS[message.chat.id]:
        ALL_MEMBERS[message.chat.id].append((user_id, user_name))
    bot.reply_to(message,
                 text=f"Hi!🫰🏻 My name is 🦜 @chat_popug_bot 🦜 and I'm glad that you decided to invite me here. "
                      f"If you want to see, what I can do, print /help or /options, or you can just print / "
                      f"and see the auxiliary menu ⬇️ ‼️ "
                      f"Don't forget to make me the admin or I won't be able to do some commands ‼️")


@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    global ALL_MEMBERS, MEMBERS_TO_UNBAN
    user_name = message.new_chat_members[0].first_name
    user_name2 = message.new_chat_members[0].username
    user_id = int(message.new_chat_members[0].id)
    if (user_id, user_name) not in ALL_MEMBERS[message.chat.id]:
        ALL_MEMBERS[message.chat.id].append((user_id, user_name))
    bot.send_message(message.chat.id, f"🦜 🦜 🦜 Let's welcome a new popug {user_name} of this chat! 🦜 🦜 🦜")
    bot.send_message(message.chat.id, f"😏 What is your favorite popug @{user_name2}? 😏")


@bot.message_handler(commands=['help'])
def help_com(message):
    global ALL_MEMBERS, MEMBERS_TO_UNBAN
    user_id = int(message.from_user.id)
    user_name = message.from_user.first_name
    if (user_id, user_name) not in ALL_MEMBERS[message.chat.id]:
        ALL_MEMBERS[message.chat.id].append((user_id, user_name))
    bot.reply_to(message,
                 text=f'Here are the descriptions of my commands:\n'
                      f'/start - greeting and mini-description about the bot \n'
                      f'/help - the descriptions of bot’s commands \n/options - some commands that user can try\n'
                      f'🦜[@chat_popug_bot should leave] - everyone can ask the bot to leave the chat\n'
                      f'🦜[commands descriptions] - everyone can read the descriptions of bot’s commands\n'
                      f'🦜[count all members] - everyone can find out the number of members in the chat\n'
                      f'🦜[usernames of all administrators] - everyone can look at the usernames of all administrators\n'
                      f'🦜[count all administrators] - everyone can find out the number of administrators in the chat\n'
                      f'🦜[choose someone to ban] - only administrators can choose whom to ban from the list of members, '
                      f'they cannot ban other administrators and themselves\n'
                      f'🦜[choose someone to unban] - only administrators can choose whom to unban from the list of members\n'
                      f'🦜[choose someone to make an admin] - only administrators can choose whom to make an admin from the list of members\n'
                      f'🦜[delete chat photo] - everyone can delete the chat photo\n'
                      f'🦜[set chat photo with popug] - everyone can change the chat photo by the default photo of popug\n'
                      f'/ban - only administrators can ban someone from the reply, they cannot ban other administrators and themselves\n'
                      f'/unban - only administrators can unban someone from the reply\n'
                      f'/admin - only administrators can make someone an admin, they even can unban other administrators besides themselves, '
                      f'all functions will be available as an administrator\n'
                      f'/id - everyone can get an id of someone by the reply\n'
                      f'make_the_chat_photo - everyone can write this command UNDER(not the reply) the photo to make it the chat photo')


@bot.message_handler(commands=['options'])
def options(message):
    global ALL_MEMBERS, MEMBERS_TO_UNBAN
    user_id = int(message.from_user.id)
    user_name = message.from_user.first_name
    if (user_id, user_name) not in ALL_MEMBERS[message.chat.id]:
        ALL_MEMBERS[message.chat.id].append((user_id, user_name))
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
    btn_unban = types.InlineKeyboardButton(text="choose someone to unban", callback_data="choose someone to unban")
    btn_admin = types.InlineKeyboardButton(text="choose someone to make an admin",
                                           callback_data="choose someone to make an admin")
    markup.add(btn_descriptions, btn_leave_bot, btn_count_members, btn_count_admins, btn_name_admins, btn_ban,
               btn_unban, btn_admin,
               btn_delete_chat_photo, btn_set_chat_photo)
    bot.send_message(message.chat.id, "😯 What @chat_popug_bot can do 😯", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "bot leave")
def callback_inline_first(call):
    bot.send_message(call.message.chat.id, text="I'm really sad, that you ask me to leave 😭 Bye...")
    bot.leave_chat(call.message.chat.id)


@bot.callback_query_handler(func=lambda call: call.data == "commands descriptions")
def callback_inline_second(call):
    bot.send_message(call.message.chat.id,
                     text=f'Here are the descriptions of my commands:\n'
                          f'/start - greeting and mini-description about the bot \n'
                          f'/help - the descriptions of bot’s commands \n'
                          f'/options - some commands that user can try\n'
                          f'🦜[@chat_popug_bot should leave] - everyone can ask the bot to leave the chat\n'
                          f'🦜[commands descriptions] - everyone can read the descriptions of bot’s commands\n'
                          f'🦜[count all members] - everyone can find out the number of members in the chat\n'
                          f'🦜[usernames of all administrators] - everyone can look at the usernames of all administrators\n'
                          f'🦜[count all administrators] - everyone can find out the number of administrators in the chat\n'
                          f'🦜[choose someone to ban] - only administrators can choose whom to ban from the list of members, '
                          f'they cannot ban other administrators and themselves\n'
                          f'🦜[choose someone to unban] - only administrators can choose whom to unban from the list of members\n'
                          f'🦜[choose someone to make an admin] - only administrators can choose whom to make an admin from the list of members\n'
                          f'🦜[delete chat photo] - everyone can delete the chat photo\n'
                          f'🦜[set chat photo with popug] - everyone can change the chat photo by the default photo of popug\n'
                          f'/ban - only administrators can ban someone from the reply, they cannot ban other administrators and themselves\n'
                          f'/unban - only administrators can unban someone from the reply\n'
                          f'/admin - only administrators can make someone an admin, they even can unban other administrators besides themselves, '
                          f'all functions will be available as an administrator\n'
                          f'/id - everyone can get an id of someone by the reply\n'
                          f'make_the_chat_photo - everyone can write this command UNDER(not the reply) the photo to make it the chat photo')


@bot.callback_query_handler(func=lambda call: call.data == "count all members")
def callback_inline_third(call):
    try:
        chat = call.message.chat.id
        count = bot.get_chat_members_count(chat)
        bot.send_message(call.message.chat.id, text=f"Here are only {count} popugs 🦜")
    except telebot.apihelper.ApiTelegramException:
        try:
            bot.send_message(call.message.chat.id, "@chat_popug_bot is not the admin")
        except telebot.apihelper.ApiTelegramException:
            pass


@bot.callback_query_handler(func=lambda call: call.data == "usernames of all administrators")
def callback_inline_fourth(call):
    try:
        chat = call.message.chat.id
        chat_admins = bot.get_chat_administrators(chat)
        for admins in chat_admins:
            user_name = admins.user.username
            bot.send_message(call.message.chat.id, text=f"@{user_name}")
    except telebot.apihelper.ApiTelegramException:
        try:
            bot.send_message(call.message.chat.id, "@chat_popug_bot is not the admin")
        except telebot.apihelper.ApiTelegramException:
            pass


@bot.callback_query_handler(func=lambda call: call.data == "count all administrators")
def callback_inline_fifth(call):
    try:
        chat = call.message.chat.id
        chat_admins = bot.get_chat_administrators(chat)
        bot.send_message(call.message.chat.id, text=f"Here are only {len(chat_admins)} admin popugs 🦜")
    except telebot.apihelper.ApiTelegramException:
        try:
            bot.send_message(call.message.chat.id, "@chat_popug_bot is not the admin")
        except telebot.apihelper.ApiTelegramException:
            pass


@bot.callback_query_handler(func=lambda call: call.data == "delete chat photo")
def callback_inline_eighth(call):
    try:
        chat = call.message.chat.id
        user_name = call.from_user.first_name
        bot.delete_chat_photo(chat)
        bot.send_message(call.message.chat.id, text=f"The popug-{user_name} asked me to delete the chat photo 🪣")
    except telebot.apihelper.ApiTelegramException:
        try:
            bot.send_message(call.message.chat.id,
                             text=f"Your chat doesn't have any photo or the bot isn't the admin 🥺")
        except telebot.apihelper.ApiTelegramException:
            pass


@bot.callback_query_handler(func=lambda call: call.data == "set chat photo with popug")
def callback_inline_ninth(call):
    try:
        random_image = random.choice(os.listdir("chat_photos"))
        path = f'chat_photos/{random_image}'
        im = Image.open(path)
        chat = call.message.chat.id
        bot.set_chat_photo(chat, photo=im)
        user_name = call.from_user.first_name
        bot.send_message(call.message.chat.id,
                         text=f"The popug-{user_name} changed photo of the chat by the popug photo 🦜")
    except telebot.apihelper.ApiTelegramException:
        try:
            bot.send_message(call.message.chat.id, "@chat_popug_bot is not the admin")
        except telebot.apihelper.ApiTelegramException:
            pass


@bot.callback_query_handler(func=lambda call: call.data == "choose someone to ban")
def callback_inline_sixth(call):
    try:
        global ALL_MEMBERS, MEMBERS_TO_UNBAN
        chat = call.message.chat.id
        chat_admins = bot.get_chat_administrators(chat)
        user_id = int(call.from_user.id)
        user_name = call.from_user.first_name
        flag = False
        for i in chat_admins:
            if int(i.user.id) == int(user_id):
                flag = True
                break
        if flag:  # проверка, что человек admin
            markup = types.InlineKeyboardMarkup(row_width=1)
            for user in ALL_MEMBERS[call.message.chat.id]:
                btn_username = types.InlineKeyboardButton(text=f"{user[1]}", callback_data=f'ban_{user[0]} {user[1]}')
                markup.add(btn_username)
            bot.send_message(call.message.chat.id, "🦜 All popug-members 🦜", reply_markup=markup)
        else:
            bot.send_message(call.message.chat.id,
                             text=f"The popug-{user_name} isn't the admin and he cannot ban anyone ❌")
            return
    except telebot.apihelper.ApiTelegramException:
        try:
            bot.send_message(call.message.chat.id, "@chat_popug_bot is not the admin")
        except telebot.apihelper.ApiTelegramException:
            pass


@bot.callback_query_handler(func=lambda call: call.data.startswith('ban_'))
def callback_inline_seventh(call):
    try:
        global ALL_MEMBERS, MEMBERS_TO_UNBAN
        chat = call.message.chat.id
        user_id, user_name = call.data.split()
        user_id = user_id[4:]
        user = call.from_user.id
        user_2 = call.from_user.first_name
        chat_admins = bot.get_chat_administrators(chat)
        flag = False
        for i in chat_admins:
            if int(i.user.id) == int(user_id):
                flag = True
                break
        if int(user) == int(user_id):
            bot.send_message(call.message.chat.id, text=f"The {user_name}, you cannot ban yourself ☠️")
            return
        elif flag:
            bot.send_message(call.message.chat.id, text=f"The {user_2}, you cannot ban the admin {user_name} ☠️")
            return
        else:
            try:
                bot.ban_chat_member(call.message.chat.id, user_id)
                MEMBERS_TO_UNBAN[call.message.chat.id].append((int(user_id), user_name))
                if (int(user_id), user_name) in ALL_MEMBERS[call.message.chat.id]:
                    ALL_MEMBERS[call.message.chat.id].remove((int(user_id), user_name))
                bot.send_message(call.message.chat.id, text=f"The {user_name} is banned ☠️")
            except telebot.apihelper.ApiTelegramException:
                try:
                    bot.send_message(call.message.chat.id, "@chat_popug_bot is not the admin")
                except telebot.apihelper.ApiTelegramException:
                    pass
    except telebot.apihelper.ApiTelegramException:
        try:
            bot.send_message(call.message.chat.id, "@chat_popug_bot is not the admin")
        except telebot.apihelper.ApiTelegramException:
            pass


@bot.callback_query_handler(func=lambda call: call.data == "choose someone to unban")
def callback_inline_eighth(call):
    try:
        chat = call.message.chat.id
        chat_admins = bot.get_chat_administrators(chat)
        user_id = int(call.from_user.id)
        user_name = call.from_user.first_name
        flag = False
        for i in chat_admins:
            if int(i.user.id) == int(user_id):
                flag = True
                break
        if flag:
            if len(MEMBERS_TO_UNBAN[call.message.chat.id]) == 0:
                bot.send_message(call.message.chat.id, "No popugs in the black list 🦜")
            else:
                markup = types.InlineKeyboardMarkup(row_width=1)
                for user in MEMBERS_TO_UNBAN[call.message.chat.id]:
                    btn_username = types.InlineKeyboardButton(text=f"{user[1]}",
                                                              callback_data=f'unban_{user[0]} {user[1]}')
                    markup.add(btn_username)
                bot.send_message(call.message.chat.id, "🦜 All popug-members 🦜", reply_markup=markup)
        else:
            bot.send_message(call.message.chat.id,
                             text=f"The popug-{user_name} isn't the admin and he cannot unban anyone ❌")
            return
    except telebot.apihelper.ApiTelegramException:
        try:
            bot.send_message(call.message.chat.id, "@chat_popug_bot is not the admin")
        except telebot.apihelper.ApiTelegramException:
            pass


@bot.callback_query_handler(func=lambda call: call.data.startswith('unban_'))
def callback_inline_nineth(call):
    try:
        global ALL_MEMBERS, MEMBERS_TO_UNBAN
        chat = call.message.chat.id
        user_id, user_name = call.data.split()
        user_id = user_id[6:]
        user = call.from_user.id
        user_2 = call.from_user.first_name
        chat_admins = bot.get_chat_administrators(chat)
        flag = False
        for i in chat_admins:
            if int(i.user.id) == int(user_id):
                flag = True
                break
        if int(user) == int(user_id):
            bot.send_message(call.message.chat.id, text=f"The {user_name}, you cannot unban yourself ☠️")
            return
        elif flag:
            bot.send_message(call.message.chat.id, text=f"The {user_2}, you cannot unban the admin {user_name} ☠️")
            return
        else:
            try:
                bot.unban_chat_member(call.message.chat.id, user_id)
                if (int(user_id), user_name) in ALL_MEMBERS[call.message.chat.id]:
                    ALL_MEMBERS[call.message.chat.id].remove((int(user_id), user_name))
                MEMBERS_TO_UNBAN[call.message.chat.id].remove((int(user_id), user_name))
                bot.send_message(call.message.chat.id, text=f"The {user_name} is unbanned ☠️")
            except telebot.apihelper.ApiTelegramException:
                try:
                    bot.send_message(call.message.chat.id, "@chat_popug_bot is not the admin")
                except telebot.apihelper.ApiTelegramException:
                    pass
    except telebot.apihelper.ApiTelegramException:
        try:
            bot.send_message(call.message.chat.id, "@chat_popug_bot is not the admin")
        except telebot.apihelper.ApiTelegramException:
            pass


@bot.callback_query_handler(func=lambda call: call.data == "choose someone to make an admin")
def callback_inline_tenth(call):
    try:
        global ALL_MEMBERS, MEMBERS_TO_UNBAN
        chat = call.message.chat.id
        chat_admins = bot.get_chat_administrators(chat)
        user_id = int(call.from_user.id)
        user_name = call.from_user.first_name
        flag = False
        for i in chat_admins:
            if int(i.user.id) == int(user_id):
                flag = True
                break
        if flag:
            markup = types.InlineKeyboardMarkup(row_width=1)
            for user in ALL_MEMBERS[call.message.chat.id]:
                btn_username = types.InlineKeyboardButton(text=f"{user[1]}", callback_data=f'admin_{user[0]} {user[1]}')
                markup.add(btn_username)
            bot.send_message(call.message.chat.id, "🦜 All popug-members 🦜", reply_markup=markup)
        else:
            bot.send_message(call.message.chat.id,
                             text=f"The popug-{user_name} isn't the admin and he can't make an admin anyone 🛑")
            return
    except telebot.apihelper.ApiTelegramException:
        try:
            bot.send_message(call.message.chat.id, "@chat_popug_bot is not the admin")
        except telebot.apihelper.ApiTelegramException:
            pass


@bot.callback_query_handler(func=lambda call: call.data.startswith('admin_'))
def callback_inline_eleventh(call):
    try:
        global ALL_MEMBERS, MEMBERS_TO_UNBAN
        chat = call.message.chat.id
        user_id, user_name = call.data.split()
        user_id = user_id[6:]
        user = call.from_user.id
        user_2 = call.from_user.first_name
        chat_admins = bot.get_chat_administrators(chat)
        flag = False
        for i in chat_admins:
            if int(i.user.id) == int(user_id):
                flag = True
                break
        if int(user) == int(user_id):
            bot.send_message(call.message.chat.id, text=f"The {user_name}, you cannot make an admin yourself 🛑️")
            return
        elif flag:
            bot.send_message(call.message.chat.id, text=f"The {user_name} is an admin")
            return
        else:
            try:
                bot.promote_chat_member(call.message.chat.id, int(user_id), can_manage_chat=True,
                                        can_delete_messages=True,
                                        can_manage_video_chats=True, can_restrict_members=True,
                                        can_promote_members=True,
                                        can_change_info=True, can_post_messages=True, can_edit_messages=True,
                                        can_invite_users=True, can_pin_messages=True, is_anonymous=False)
                if (int(user_id), user_name) not in ALL_MEMBERS[call.message.chat.id]:
                    ALL_MEMBERS[call.message.chat.id].append((int(user_id), user_name))
                bot.send_message(call.message.chat.id, text=f"The {user_name} is an admin now too 🎉️")
            except telebot.apihelper.ApiTelegramException:
                try:
                    bot.send_message(call.message.chat.id, "@chat_popug_bot is not the admin")
                except telebot.apihelper.ApiTelegramException:
                    pass
    except telebot.apihelper.ApiTelegramException:
        try:
            bot.send_message(call.message.chat.id, "@chat_popug_bot is not the admin")
        except telebot.apihelper.ApiTelegramException:
            pass


@bot.message_handler(commands=['ban'])
def ban(message):
    try:
        global ALL_MEMBERS, MEMBERS_TO_UNBAN
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
            if message.reply_to_message:
                user_id = message.reply_to_message.from_user.id
                user_name = message.reply_to_message.from_user.first_name
                flag2 = False
                for i in chat_admins:
                    if i.user.id == user_id:
                        flag2 = True
                        break
                if int(user_id1) == int(user_id):
                    bot.send_message(message.chat.id, text=f"The {user_name1}, you cannot ban yourself ☠️")
                    return
                elif flag2:
                    bot.send_message(message.chat.id, text=f"The {user_name1}, you cannot ban the admin {user_name} ☠️")
                    return
            else:
                try:
                    if message.reply_to_message:
                        user_id = message.reply_to_message.from_user.id
                        user_name = message.reply_to_message.from_user.first_name
                        bot.ban_chat_member(message.chat.id, user_id)
                        MEMBERS_TO_UNBAN[message.chat.id].append((int(user_id), user_name))
                        if (int(user_id), user_name) in ALL_MEMBERS[message.chat.id]:
                            ALL_MEMBERS[message.chat.id].remove((int(user_id), user_name))
                        user_name_who = message.from_user.username
                        user_name_whom = message.reply_to_message.from_user.username
                        bot.send_message(message.chat.id,
                                         text=f"The @{user_name_who} asked me to ban the @{user_name_whom} ☠️")
                except telebot.apihelper.ApiTelegramException:
                    try:
                        bot.send_message(message.chat.id, "@chat_popug_bot is not the admin")
                    except telebot.apihelper.ApiTelegramException:
                        pass
        else:
            bot.send_message(message.chat.id, text=f"The popug-{user_name1} isn't the admin and he can't ban anyone ❌")
            return
    except telebot.apihelper.ApiTelegramException:
        try:
            bot.send_message(message.chat.id, "@chat_popug_bot is not the admin")
        except telebot.apihelper.ApiTelegramException:
            pass


@bot.message_handler(commands=['unban'])
def unban(message):
    try:
        global ALL_MEMBERS, MEMBERS_TO_UNBAN
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
            if message.reply_to_message:
                user_id = message.reply_to_message.from_user.id
                user_name = message.reply_to_message.from_user.first_name
                if int(user_id1) == int(user_id):
                    bot.send_message(message.chat.id, text=f"The {user_name1}, you cannot unban yourself ☠️")
                    return
            else:
                try:
                    if message.reply_to_message:
                        user_id = message.reply_to_message.from_user.id
                        user_name = message.reply_to_message.from_user.first_name
                        bot.unban_chat_member(message.chat.id, user_id)
                        if (int(user_id), user_name) in ALL_MEMBERS[message.chat.id]:
                            ALL_MEMBERS[message.chat.id].remove((int(user_id), user_name))
                        MEMBERS_TO_UNBAN[message.chat.id].remove((int(user_id), user_name))
                        user_name_who = message.from_user.username
                        user_name_whom = message.reply_to_message.from_user.username
                        bot.send_message(message.chat.id,
                                         text=f"The @{user_name_who} asked me to unban the @{user_name_whom} ☠️")
                except telebot.apihelper.ApiTelegramException:
                    try:
                        bot.send_message(message.chat.id, "@chat_popug_bot is not the admin")
                    except telebot.apihelper.ApiTelegramException:
                        pass
        else:
            bot.send_message(message.chat.id,
                             text=f"The popug-{user_name1} isn't the admin and he can't unban anyone ❌")
            return
    except telebot.apihelper.ApiTelegramException:
        try:
            bot.send_message(message.chat.id, "@chat_popug_bot is not the admin")
        except telebot.apihelper.ApiTelegramException:
            pass


@bot.message_handler(commands=['admin'])
def unban(message):
    try:
        chat = message.chat.id
        chat_admins = bot.get_chat_administrators(chat)
        user_id1 = message.from_user.id
        user_id2 = message.reply_to_message.from_user.id
        user_name2 = message.reply_to_message.from_user.first_name
        user_name1 = message.from_user.first_name
        flag1 = False
        flag2 = False
        for i in chat_admins:
            if i.user.id == user_id1:
                flag1 = True
                break
        for i in chat_admins:
            if i.user.id == user_id2:
                flag2 = True
                break
        if flag2:
            bot.send_message(message.chat.id, text=f"The {user_name2} is the admin")
            return
        if flag1:
            if message.reply_to_message:
                user_id = message.reply_to_message.from_user.id
                user_name = message.reply_to_message.from_user.first_name
                if int(user_id1) == int(user_id):
                    bot.send_message(message.chat.id, text=f"The {user_name1}, you cannot make an admin yourself 🛑️")
                    return
                else:
                    try:
                        if message.reply_to_message:
                            user_id = message.reply_to_message.from_user.id
                            user_name = message.reply_to_message.from_user.first_name
                            bot.promote_chat_member(message.chat.id, user_id, can_manage_chat=True,
                                                    can_delete_messages=True,
                                                    can_manage_video_chats=True, can_restrict_members=True,
                                                    can_promote_members=True,
                                                    can_change_info=True, can_post_messages=True,
                                                    can_edit_messages=True,
                                                    can_invite_users=True, can_pin_messages=True, is_anonymous=False)
                            if (int(user_id), user_name) not in ALL_MEMBERS[message.chat.id]:
                                ALL_MEMBERS[message.chat.id].append((int(user_id), user_name))
                            user_name_who = message.from_user.username
                            user_name_whom = message.reply_to_message.from_user.username
                            bot.send_message(message.chat.id,
                                             text=f"The @{user_name_who} asked me to make an admin the @{user_name_whom} too 🎉")
                    except telebot.apihelper.ApiTelegramException:
                        try:
                            bot.send_message(message.chat.id, "@chat_popug_bot is not the admin")
                        except telebot.apihelper.ApiTelegramException:
                            pass
        else:
            bot.send_message(message.chat.id,
                             text=f"The popug-{user_name1} isn't the admin and he can't make an admin anyone 🛑")
            return
    except telebot.apihelper.ApiTelegramException:
        try:
            bot.send_message(message.chat.id, "@chat_popug_bot is not the admin")
        except telebot.apihelper.ApiTelegramException:
            pass


@bot.message_handler(commands=['id'])
def ban(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name
        if (int(user_id), user_name) not in ALL_MEMBERS[message.chat.id]:
            ALL_MEMBERS[message.chat.id].append((int(user_id), user_name))
        bot.reply_to(message, text=f"This user_id is: {user_id}")


@bot.message_handler(content_types=['text'])
def text(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    if (int(user_id), user_name) not in ALL_MEMBERS[message.chat.id]:
        ALL_MEMBERS[message.chat.id].append((int(user_id), user_name))


@bot.message_handler(content_types=['photo'])
def after_text(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    if (int(user_id), user_name) not in ALL_MEMBERS[message.chat.id]:
        ALL_MEMBERS[message.chat.id].append((int(user_id), user_name))
    if message.caption:
        if message.caption == 'make_the_chat_photo':
            try:
                file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                chat = message.chat.id
                bot.set_chat_photo(chat, photo=downloaded_file)
                user_name = message.from_user.first_name
                bot.send_message(message.chat.id, text=f"The popug-{user_name} changed photo of the chat  🦜")
            except telebot.apihelper.ApiTelegramException:
                try:
                    bot.send_message(message.chat.id, "@chat_popug_bot is not the admin")
                except telebot.apihelper.ApiTelegramException:
                    pass


bot.polling(none_stop=True, interval=0)
