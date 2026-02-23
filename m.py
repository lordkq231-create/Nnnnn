
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import asyncio
import os
import datetime
import aiofiles
import sys
import traceback
import time
import random
from pathlib import Path
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton,
    CallbackQuery, Message, ChatMemberUpdated, InputFile
)

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[35m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    BLACK = '\033[30m'
    WHITE = '\033[37m'
    ORANGE = '\033[38;5;214m'
    PINK = '\033[38;5;205m'
    PURPLE = '\033[38;5;141m'
    LIME = '\033[38;5;154m'
    GOLD = '\033[38;5;220m'

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def rainbow_text(text):
    colors = [Colors.RED, Colors.ORANGE, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.PURPLE, Colors.PINK, Colors.MAGENTA, Colors.GOLD, Colors.LIME]
    result = ""
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        result += f"{color}{char}{Colors.END}"
    return result

def gradient_text(text, start_color, end_color):
    result = ""
    colors = [start_color, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.PURPLE, end_color]
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        result += f"{color}{char}{Colors.END}"
    return result

async def fancy_startup():
    clear_console()
    
    frames = ["█", "▓", "▒", "░"]
    for i in range(30):
        bar = ""
        for j in range(40):
            if j < i:
                bar += f"{Colors.GREEN}█{Colors.END}"
            elif j == i:
                bar += f"{Colors.YELLOW}▓{Colors.END}"
            else:
                bar += f"{Colors.RED}░{Colors.END}"
        
        percent = int((i / 30) * 100)
        sys.stdout.write(f"\r{Colors.BOLD}{Colors.CYAN}┌─[ЗАГРУЗКА ПИЗДЕЦА]─┐{Colors.END}\n")
        sys.stdout.write(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.END} {bar} {Colors.BOLD}{Colors.YELLOW}{percent}%{Colors.END} {Colors.MAGENTA}│{Colors.END}\n")
        sys.stdout.write(f"{Colors.BOLD}{Colors.CYAN}└────────────────────┘{Colors.END}")
        sys.stdout.flush()
        await asyncio.sleep(0.05)
    
    print("\n\n")
    
    animation_frames = [
        f"{Colors.RED}╔════════════════════════════════════╗{Colors.END}",
        f"{Colors.ORANGE}║{Colors.END}                                    {Colors.ORANGE}║{Colors.END}",
        f"{Colors.YELLOW}║{Colors.END}         ЗАПУСКАЕМ ПИЗДЕЦ         {Colors.YELLOW}║{Colors.END}",
        f"{Colors.GREEN}║{Colors.END}                                    {Colors.GREEN}║{Colors.END}",
        f"{Colors.CYAN}╚════════════════════════════════════╝{Colors.END}"
    ]
    
    for frame in animation_frames:
        print(frame)
        await asyncio.sleep(0.1)
    
    print("\n")
    
    matrix_chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
    for i in range(10):
        line = ""
        for j in range(60):
            if random.random() > 0.7:
                line += f"{Colors.GREEN}{random.choice(matrix_chars)}{Colors.END}"
            else:
                line += " "
        print(line)
        await asyncio.sleep(0.1)
    
    print("\n")
    
    text1 = "Ебать ты долбаеб, щас снесу тебе телефон"
    colors = [Colors.RED, Colors.ORANGE, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.PURPLE, Colors.PINK, Colors.MAGENTA]
    
    for i, char in enumerate(text1):
        color = colors[i % len(colors)]
        print(f"{color}{char}{Colors.END}", end="", flush=True)
        await asyncio.sleep(0.03)
    print("\n")
    
    spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for i in range(30):
        for frame in spinner:
            sys.stdout.write(f"\r{Colors.MAGENTA}{frame}{Colors.END} {Colors.YELLOW}ПИЗДЕЦ НАБЛИЖАЕТСЯ...{Colors.END} {Colors.CYAN}{frame}{Colors.END}")
            sys.stdout.flush()
            await asyncio.sleep(0.05)
    
    print("\n\n")
    
    text2 = "Чумазий нигирь йоу, ты не шариш за свэг этого скрипта, надо опустить тебя чушкан"
    colors2 = [Colors.PURPLE, Colors.BLUE, Colors.CYAN, Colors.GREEN, Colors.YELLOW, Colors.ORANGE, Colors.RED]
    
    for i, char in enumerate(text2):
        color = colors2[i % len(colors2)]
        print(f"{color}{char}{Colors.END}", end="", flush=True)
        await asyncio.sleep(0.02)
    print("\n")
    
    await asyncio.sleep(1)
    
    explosion_frames = [
        f"{Colors.RED}     *     {Colors.END}",
        f"{Colors.ORANGE}    ***    {Colors.END}",
        f"{Colors.YELLOW}   *****   {Colors.END}",
        f"{Colors.GREEN}  *******  {Colors.END}",
        f"{Colors.CYAN} ********* {Colors.END}",
        f"{Colors.BLUE}***********{Colors.END}",
        f"{Colors.PURPLE} ********* {Colors.END}",
        f"{Colors.PINK}  *******  {Colors.END}",
        f"{Colors.MAGENTA}   *****   {Colors.END}",
        f"{Colors.RED}    ***    {Colors.END}",
        f"{Colors.ORANGE}     *     {Colors.END}",
    ]
    
    for frame in explosion_frames:
        print(frame)
        await asyncio.sleep(0.1)
    
    print("\n")
    
    messages = [
        ("Этот", Colors.RED),
        (" блэт", Colors.ORANGE),
        (" не", Colors.YELLOW),
        (" мой", Colors.GREEN),
        (" блэт", Colors.CYAN),
        (" а", Colors.BLUE),
        (" твой", Colors.PURPLE),
        (" на", Colors.PINK),
        (" хую", Colors.MAGENTA),
        (" верченный", Colors.RED),
        (" омлэт", Colors.ORANGE),
        (",", Colors.YELLOW),
        (" йоу", Colors.GREEN),
        (" детка", Colors.CYAN),
        (" ты", Colors.BLUE),
        (" не", Colors.PURPLE),
        (" шаришь", Colors.PINK),
        (" за", Colors.MAGENTA),
        (" мой", Colors.RED),
        (" свэг", Colors.ORANGE),
        (" и", Colors.YELLOW),
        (" получаешь", Colors.GREEN),
        (" за", Colors.CYAN),
        (" это", Colors.BLUE),
        (" в", Colors.PURPLE),
        (" эблет", Colors.PINK),
        ("!", Colors.MAGENTA),
    ]
    
    line = ""
    for text, color in messages:
        line += f"{color}{text}{Colors.END}"
        print(line, end="\r", flush=True)
        await asyncio.sleep(0.1)
    print()
    
    await asyncio.sleep(0.5)
    
    words = ["БЛЭТ", "БЛЭТ", "БЛЭТ"]
    colors = [Colors.RED, Colors.GREEN, Colors.BLUE, Colors.YELLOW, Colors.PURPLE, Colors.ORANGE, Colors.CYAN, Colors.PINK, Colors.MAGENTA]
    
    for word in words:
        color = random.choice(colors)
        print(f"{color}{word}{Colors.END} ", end="", flush=True)
        await asyncio.sleep(0.3)
    print("\n")
    
    await asyncio.sleep(1)
    
    text3 = "Ладно подарок пощажу тебя и запущусь, ты не вывозишь моего блэта"
    for i, char in enumerate(text3):
        if random.random() > 0.3:
            color = colors[i % len(colors)]
            print(f"{color}{char}{Colors.END}", end="", flush=True)
        else:
            print(char, end="", flush=True)
        await asyncio.sleep(0.03)
    print("\n")
    
    await asyncio.sleep(1)
    
    counter = random.randint(1000, 2000)
    print(f"{Colors.RED}{Colors.BOLD}Отправил(а) вам шахiд⚠️ ({counter}) шт.{Colors.END}\n")
    
    await asyncio.sleep(2)
    
    clear_console()
    
    print(f"{Colors.GREEN}{Colors.BOLD}╔════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.GREEN}{Colors.BOLD}║     БОТ УСПЕШНО ЗАПУЩЕН ЙОУ!     ║{Colors.END}")
    print(f"{Colors.GREEN}{Colors.BOLD}╚════════════════════════════════════╝{Colors.END}\n")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = "8085772389:AAHqDzupoQpsXCrZqpuAKKj_zQ7ffwI68PY"
GROUP_ID = -1003423691334
ADMIN_IDS = [8161340842]
BASE_FILE = "base.txt"
PHOTO_DIR = Path("photo")

user_data_cache = {}
invite_links_cache = {}
admin_action_state = {}
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

def get_main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(text="👤 ПРОФИЛЬ"))
    keyboard.add(KeyboardButton(text="🔗 ССЫЛКА"))
    return keyboard

def get_link_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(text="🔗 СОЗДАТЬ ССЫЛКУ", callback_data="create_link"))
    return keyboard

def get_admin_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="⛔️ Заблокировать", callback_data="admin_block"),
        InlineKeyboardButton(text="✅ Разбанить", callback_data="admin_unblock")
    )
    return keyboard

def safe_int_conversion(value, default=0):
    if value is None or value == 'None' or value == '':
        return default
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

def safe_str_conversion(value, default=''):
    if value is None or value == 'None':
        return default
    return str(value)

async def load_base():
    global user_data_cache
    user_data_cache.clear()
    
    if not os.path.exists(BASE_FILE):
        return
    
    try:
        async with aiofiles.open(BASE_FILE, 'r', encoding='utf-8') as f:
            lines = await f.readlines()
            
            for line_num, line in enumerate(lines, 1):
                try:
                    line = line.strip()
                    if not line:
                        continue
                    
                    parts = line.split('|')
                    if len(parts) < 5:
                        logger.warning(f"Строка {line_num}: недостаточно полей, пропускаем")
                        continue
                    
                    user_id = safe_int_conversion(parts[0])
                    if user_id == 0:
                        logger.warning(f"Строка {line_num}: некорректный user_id, пропускаем")
                        continue
                    
                    user_data_cache[user_id] = {
                        'user_id': user_id,
                        'first_name': safe_str_conversion(parts[1]),
                        'last_name': safe_str_conversion(parts[2] if len(parts) > 2 else ''),
                        'username': safe_str_conversion(parts[3] if len(parts) > 3 else ''),
                        'registered': safe_str_conversion(parts[4] if len(parts) > 4 else datetime.datetime.now().isoformat()),
                        'invite_link': safe_str_conversion(parts[5] if len(parts) > 5 and parts[5] != 'None' else '', None),
                        'referrals': safe_int_conversion(parts[6] if len(parts) > 6 else 0),
                        'blocked': parts[7] == 'True' if len(parts) > 7 else False
                    }
                except Exception as e:
                    logger.error(f"Ошибка обработки строки {line_num}: {e}")
                    continue
        
        logger.info(f"Загружено {len(user_data_cache)} пользователей")
    except Exception as e:
        logger.error(f"Ошибка загрузки базы: {e}")

async def save_base():
    try:
        temp_file = f"{BASE_FILE}.tmp"
        async with aiofiles.open(temp_file, 'w', encoding='utf-8') as f:
            for user_id, data in user_data_cache.items():
                first_name = str(data.get('first_name', '')).replace('|', ' ')
                last_name = str(data.get('last_name', 'None')).replace('|', ' ') if data.get('last_name') else 'None'
                username = str(data.get('username', 'None')).replace('|', ' ') if data.get('username') else 'None'
                registered = str(data.get('registered', datetime.datetime.now().isoformat()))
                invite_link = str(data.get('invite_link', 'None')) if data.get('invite_link') else 'None'
                referrals = str(data.get('referrals', 0))
                blocked = str(data.get('blocked', False))
                
                line = f"{user_id}|{first_name}|{last_name}|{username}|{registered}|{invite_link}|{referrals}|{blocked}\n"
                await f.write(line)
        
        if os.path.exists(BASE_FILE):
            os.remove(BASE_FILE)
        os.rename(temp_file, BASE_FILE)
    except Exception as e:
        logger.error(f"Ошибка сохранения базы: {e}")

async def update_invite_links_cache():
    global invite_links_cache
    invite_links_cache.clear()
    
    for user_id, data in user_data_cache.items():
        if data.get('invite_link') and data.get('invite_link') != 'None' and not data.get('blocked', False):
            invite_links_cache[data['invite_link']] = user_id
    
    logger.info(f"Обновлен кэш ссылок: {len(invite_links_cache)} активных ссылок")

def get_days_since_registered(reg_date_str):
    try:
        if reg_date_str and reg_date_str != 'None':
            reg_date = datetime.datetime.fromisoformat(reg_date_str)
            delta = datetime.datetime.now() - reg_date
            return max(1, delta.days)
    except:
        pass
    return 1

async def is_blocked(user_id):
    user_data = user_data_cache.get(user_id, {})
    return user_data.get('blocked', False)

def generate_link_name(user_data):
    name_part = user_data.get('username') or user_data.get('first_name', 'user')
    clean_name = ''.join(c for c in name_part if c.isalnum() or c in '._-')[:32]
    return f"Ссылка {clean_name}"

def get_display_name(user_data):
    if user_data.get('username'):
        return f"@{user_data['username']}"
    else:
        return user_data.get('first_name', 'Пользователь')

@dp.message_handler(commands=['start'], chat_type=types.ChatType.PRIVATE)
async def cmd_start(message: Message):
    user_id = message.from_user.id
    
    if await is_blocked(user_id):
        return await message.answer("⛔️ Вы заблокированы в этом боте.")
    
    await load_base()
    
    if user_id not in user_data_cache:
        user_data_cache[user_id] = {
            'user_id': user_id,
            'first_name': safe_str_conversion(message.from_user.first_name),
            'last_name': safe_str_conversion(message.from_user.last_name),
            'username': safe_str_conversion(message.from_user.username),
            'registered': datetime.datetime.now().isoformat(),
            'invite_link': None,
            'referrals': 0,
            'blocked': False
        }
        
        await save_base()
        await update_invite_links_cache()
        
        photo_path = PHOTO_DIR / "welcome.png"
        if photo_path.exists():
            photo = InputFile(photo_path)
            display_name = get_display_name(user_data_cache[user_id])
            text = f"✨ <b>Добро пожаловать, {display_name}!</b>\n\nЭто бот проекта <b>GALACTIC LEGACY</b>.\n\nИспользуй кнопки ниже для навигации ⬇️"
            await message.answer_photo(photo=photo, caption=text, parse_mode='HTML', reply_markup=get_main_keyboard())
        else:
            await message.answer("✨ Добро пожаловать! Используй кнопки ниже 👇", reply_markup=get_main_keyboard())
    else:
        await message.answer("С возвращением! Используй кнопки ниже 👇", reply_markup=get_main_keyboard())

@dp.message_handler(Text(equals="👤 ПРОФИЛЬ"), chat_type=types.ChatType.PRIVATE)
async def cmd_profile(message: Message):
    user_id = message.from_user.id
    
    if await is_blocked(user_id):
        return
    
    await load_base()
    
    if user_id not in user_data_cache:
        return await cmd_start(message)
    
    data = user_data_cache[user_id]
    
    first_name = safe_str_conversion(data.get('first_name', ''))
    last_name = safe_str_conversion(data.get('last_name', ''))
    full_name = f"{first_name} {last_name}".strip()
    username = data.get('username')
    days = get_days_since_registered(data.get('registered'))
    
    is_admin = user_id in ADMIN_IDS
    
    if is_admin:
        if username:
            display_name = f"@{username}"
        else:
            display_name = first_name
        
        text = f"👤 <b>Администратор:</b> {full_name}\n"
        text += f"📱 <b>Отображается как:</b> {display_name}\n"
        text += f"🆔 <code>{user_id}</code>\n"
        text += f"ℹ️ Вам доступна команда /admin"
    else:
        if username:
            display_name = f"@{username}"
        else:
            display_name = first_name
        
        text = f"👤 <b>Рекрутер:</b> {full_name}\n"
        text += f"📱 <b>Отображается как:</b> {display_name}\n"
        text += f"🆔 <code>{user_id}</code>\n"
        text += f"⏳ <b>Работает уже:</b> {days} дн."
    
    photo_path = PHOTO_DIR / "profile.png"
    
    if photo_path.exists():
        photo = InputFile(photo_path)
        await message.answer_photo(
            photo=photo,
            caption=text,
            parse_mode='HTML'
        )
    else:
        await message.answer(
            text,
            parse_mode='HTML'
        )

@dp.message_handler(Text(equals="🔗 ССЫЛКА"), chat_type=types.ChatType.PRIVATE)
async def cmd_link(message: Message):
    user_id = message.from_user.id
    
    if await is_blocked(user_id):
        return
    
    await load_base()
    
    if user_id not in user_data_cache:
        return await cmd_start(message)
    
    data = user_data_cache[user_id]
    photo_path = PHOTO_DIR / "menu.png"
    
    if data.get('invite_link') and data['invite_link'] != 'None':
        text = f"🔗 <b>Ваша персональная ссылка:</b>\n\n<code>{data['invite_link']}</code>"
        if photo_path.exists():
            photo = InputFile(photo_path)
            await message.answer_photo(photo=photo, caption=text, parse_mode='HTML')
        else:
            await message.answer(text, parse_mode='HTML')
    else:
        text = "У вас еще нет персональной ссылки. Для создания нажмите кнопку ниже 👇"
        if photo_path.exists():
            photo = InputFile(photo_path)
            await message.answer_photo(photo=photo, caption=text, reply_markup=get_link_keyboard())
        else:
            await message.answer(text, reply_markup=get_link_keyboard())

@dp.callback_query_handler(lambda c: c.data == 'create_link', chat_type=types.ChatType.PRIVATE)
async def create_link(callback: CallbackQuery):
    user_id = callback.from_user.id
    
    if await is_blocked(user_id):
        return await callback.answer("Вы заблокированы", show_alert=True)
    
    await load_base()
    
    if user_id not in user_data_cache:
        return await cmd_start(callback.message)
    
    data = user_data_cache[user_id]
    
    if data.get('invite_link') and data['invite_link'] != 'None':
        return await callback.answer("У вас уже есть ссылка!", show_alert=True)
    
    try:
        link_name = generate_link_name(data)
        link = await bot.create_chat_invite_link(
            chat_id=GROUP_ID,
            name=link_name,
            member_limit=0
        )
        
        user_data_cache[user_id]['invite_link'] = link.invite_link
        await save_base()
        await update_invite_links_cache()
        
        await callback.message.delete()
        
        photo_path = PHOTO_DIR / "menu.png"
        text = f"🔗 <b>Ваша персональная ссылка:</b>\n\n<code>{link.invite_link}</code>"
        
        if photo_path.exists():
            photo = InputFile(photo_path)
            await callback.message.answer_photo(photo=photo, caption=text, parse_mode='HTML')
        else:
            await callback.message.answer(text, parse_mode='HTML')
        
        logger.info(f"Создана ссылка для пользователя {user_id}: {link.invite_link}")
        
    except Exception as e:
        logger.error(f"Ошибка создания ссылки: {e}")
        await callback.answer(f"Ошибка: {str(e)[:50]}", show_alert=True)
    
    await callback.answer()

@dp.chat_member_handler()
async def on_user_join(update: ChatMemberUpdated):
    if update.chat.id != GROUP_ID:
        return
    
    old_status = update.old_chat_member.status
    new_status = update.new_chat_member.status
    
    if old_status in ['left', 'kicked'] and new_status in ['member', 'administrator', 'creator']:
        user_id = update.new_chat_member.user.id
        logger.info(f"Новый участник в группе: {user_id}")
        
        await load_base()
        
        for inviter_id, data in user_data_cache.items():
            if data.get('invite_link') and data['invite_link'] != 'None' and not data.get('blocked', False):
                try:
                    link_info = await bot.get_chat_invite_link(
                        chat_id=GROUP_ID,
                        invite_link=data['invite_link']
                    )
                    
                    if link_info.creator.id == user_id:
                        continue
                    
                    data['referrals'] = data.get('referrals', 0) + 1
                    await save_base()
                    
                    try:
                        photo_path = PHOTO_DIR / "referral.png"
                        text = f"🎉 <b>Отличная работа!</b>\nУ вас новый реферал!\nВсего: {data['referrals']}"
                        
                        if photo_path.exists():
                            photo = InputFile(photo_path)
                            await bot.send_photo(chat_id=inviter_id, photo=photo, caption=text, parse_mode='HTML')
                        else:
                            await bot.send_message(chat_id=inviter_id, text=text, parse_mode='HTML')
                        
                        logger.info(f"Реферал засчитан пользователю {inviter_id}")
                        break
                        
                    except Exception as e:
                        logger.error(f"Ошибка отправки уведомления: {e}")
                        
                except Exception as e:
                    logger.error(f"Ошибка проверки ссылки: {e}")

@dp.message_handler(commands=['admin'], chat_type=types.ChatType.PRIVATE)
async def cmd_admin(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        return await message.answer("❌ Неизвестная команда", reply_markup=get_main_keyboard())
    
    photo_path = PHOTO_DIR / "kolpik.png"
    if photo_path.exists():
        photo = InputFile(photo_path)
        await message.answer_photo(photo=photo, caption="🛠 Панель администратора\nВыберите действие:", parse_mode='HTML', reply_markup=get_admin_keyboard())
    else:
        await message.answer("🛠 Панель администратора\nВыберите действие:", parse_mode='HTML', reply_markup=get_admin_keyboard())

@dp.callback_query_handler(lambda c: c.data in ['admin_block', 'admin_unblock'], chat_type=types.ChatType.PRIVATE)
async def admin_actions(callback: CallbackQuery):
    admin_id = callback.from_user.id
    
    if admin_id not in ADMIN_IDS:
        return await callback.answer("Доступ запрещен", show_alert=True)
    
    if callback.data == "admin_block":
        admin_action_state[admin_id] = "block"
        await callback.message.edit_caption(
            caption="🔹 Введите ID пользователя для блокировки:",
            parse_mode='HTML',
            reply_markup=None
        )
    else:
        admin_action_state[admin_id] = "unblock"
        await callback.message.edit_caption(
            caption="🔹 Введите ID пользователя для разблокировки:",
            parse_mode='HTML',
            reply_markup=None
        )
    
    await callback.answer()

@dp.message_handler(lambda message: message.from_user.id in ADMIN_IDS and message.text and message.text.isdigit(), chat_type=types.ChatType.PRIVATE)
async def process_admin_action(message: Message):
    admin_id = message.from_user.id
    
    if admin_id not in admin_action_state:
        return
    
    action = admin_action_state.pop(admin_id)
    user_id = safe_int_conversion(message.text)
    
    if user_id == admin_id:
        await message.answer("❌ Нельзя заблокировать самого себя!", reply_markup=get_admin_keyboard())
        return
    
    await load_base()
    
    if user_id in user_data_cache:
        if action == "block":
            user_data_cache[user_id]['blocked'] = True
            
            if user_data_cache[user_id].get('invite_link') and user_data_cache[user_id]['invite_link'] != 'None':
                try:
                    await bot.revoke_chat_invite_link(chat_id=GROUP_ID, invite_link=user_data_cache[user_id]['invite_link'])
                    user_data_cache[user_id]['invite_link'] = None
                except:
                    pass
            
            await save_base()
            await update_invite_links_cache()
            
            try:
                await bot.send_message(user_id, "⛔️ Вы были заблокированы в боте GALACTIC LEGACY.")
            except:
                pass
            
            await message.answer(f"✅ Пользователь {user_id} заблокирован", reply_markup=get_admin_keyboard())
            
        elif action == "unblock":
            user_data_cache[user_id]['blocked'] = False
            await save_base()
            await update_invite_links_cache()
            
            try:
                await bot.send_message(user_id, "✅ Вы были разблокированы в боте GALACTIC LEGACY.")
            except:
                pass
            
            await message.answer(f"✅ Пользователь {user_id} разблокирован", reply_markup=get_admin_keyboard())
    else:
        await message.answer(f"❌ Пользователь {user_id} не найден", reply_markup=get_admin_keyboard())

@dp.message_handler(chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def ignore_group_messages(message: Message):
    pass

@dp.message_handler(chat_type=types.ChatType.PRIVATE)
async def handle_unknown_private(message: Message):
    if await is_blocked(message.from_user.id):
        return
    
    if message.text and not message.text.startswith('/'):
        await message.answer("❓ Используйте кнопки ниже", reply_markup=get_main_keyboard())

@dp.errors_handler()
async def errors_handler(update, exception):
    logger.error(f"Ошибка при обработке обновления: {exception}")
    return True

async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()
    await bot.get_session().close()

async def main_loop():
    await fancy_startup()
    
    while True:
        try:
            os.makedirs(PHOTO_DIR, exist_ok=True)
            await load_base()
            await update_invite_links_cache()
            
            try:
                await bot.send_message(chat_id=ADMIN_IDS[0], text="✅ Бот запущен и работает только в личных сообщениях")
            except:
                pass
            
            await dp.start_polling(reset_webhook=True)
        except Exception as e:
            logger.error(f"Критическая ошибка: {e}\n{traceback.format_exc()}")
            await asyncio.sleep(5)
        finally:
            try:
                await shutdown(dp)
            except:
                pass
            await asyncio.sleep(3)

def main():
    while True:
        try:
            asyncio.run(main_loop())
        except KeyboardInterrupt:
            logger.info("Бот остановлен вручную")
            break
        except Exception as e:
            logger.error(f"Фатальная ошибка: {e}\n{traceback.format_exc()}")
            continue

if __name__ == "__main__":
    main()