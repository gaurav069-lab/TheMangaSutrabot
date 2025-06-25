# bot.py में इन लाइन्स को ऐड करें (सबसे ऊपर)
import os
os.system('pkill -f "python bot.py"')  # सभी पुराने प्रोसेस kill करेगा
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import json
import os
from datetime import datetime, timedelta

# === CONFIGURATION ===
BOT_TOKEN = "7991449866:AAGC7VpX5Gpn8k8ghof7IEVDdcxGbRFdx_I"
ADMIN_ID = 6411610393
MAIN_CHANNEL = 'MANGASUTRAOFFICIAL'
DATA_FILE = 'comics_data.json'
VIP_DATA_FILE = 'vip_data.json'
PAYMENT_DATA_FILE = 'payment_data.json'

# Payment Details
UPI_ID = "mangasutraofficial@ptyes"
ADMIN_NAME = "GAURAV NANDI"

# === CHANNEL LINKS ===
CHANNEL_LINKS = {
    "Indian Comics": {
        "🦸‍♂️ Superhero Comics": "https://t.me/+RKw94L2oijxiOWU1",
        "😂 Comedy Comics": "https://t.me/+LQrqItONYoY1NmVl",
        "🚀 Sci-Fi Comics": "https://t.me/+vWeHWWUxw4sxZWVl",
        "🧙 Fantasy Comics": "https://t.me/+aecO_lbj2ek4MWQ9",
        "🗺️ Adventure Comics": "https://t.me/+EnLzoEEvLZBjMDI1",
        "🔫 Action Comics": "https://t.me/+dosAimsNtKc2MjRl"
    },
    "Korean Manhwa": {
        "🦸‍♂️ Superhero Comics": "https://t.me/+uw-TKzYoeqMzMDA1",
        "😂 Comedy Comics": "https://t.me/+YxH7876PyixlMjE1",
        "🚀 Sci-Fi Comics": "https://t.me/+PrN--UNNBJxkMmE1",
        "🧙 Fantasy Comics": "https://t.me/+xrVR2oJEvxBjNjU1",
        "🗺️ Adventure Comics": "https://t.me/+pA9QwMLpJ7k0ODJl",
        "🔫 Action Comics": "https://t.me/+Kcc59nGNIVM1OWU1"
    },
    "Manga": {
        "Hindi": "https://t.me/+your_manga_hindi_channel",
        "English": "https://t.me/+your_manga_english_channel"
    },
    "🔞 18+ Indian Comics": {
        "Hindi": "https://t.me/+pNqCZCsfFu04ZjVl",
        "English": "https://t.me/+rDfrjuq5iBZmNDll"
    },
    "🔥 18+ Korean Manhwa": {
        "Hindi": "https://t.me/+YNW7wRg29Mc5YjZl",
        "English": "https://t.me/+Ere8IYCDY0M0MDQ1"
    },
    "💎 VIP Zone": {
        "Indian VIP": "https://t.me/+your_indian_vip_channel",
        "Korean VIP": "https://t.me/+your_korean_vip_channel"
    }
}

# VIP Subscription Plans (CORRECTED)
VIP_PLANS = {
    "Indian VIP": {
        "1 Month VIP": {"price": 249, "desc": "50+ comics to Read"},
        "3 Months VIP": {"price": 599, "desc": "100+ comics to read"},
        "6 Months VIP": {"price": 999, "desc": "Unlimited Read + Priority Access"},
        "Lifetime VIP": {"price": 2499, "desc": "Lifetime Access + Bonus Drops"}
    },
    "Korean VIP (Hindi)": {
        "1 Month VIP": {"price": 499, "desc": "50+ Manhwa (Hindi)"},
        "3 Months VIP": {"price": 1299, "desc": "100+ Manhwa, Bonus Drops"},
        "6 Months VIP": {"price": 2499, "desc": "500+ manhwas + Support"},
        "Lifetime VIP": {"price": 5999, "desc": "Lifetime Hindi Manhwa Access"}
    }
}

# Per-Comic Pricing
COMIC_PRICES = {
    "Indian": {
        "30 Chapters": 100,
        "50 Chapters": 200,
        "100+ Chapters": 300
    },
    "Korean": {
        "30 Chapters": 299,
        "60 Chapters": 399,
        "100+ Chapters": 599,
        "Special Premium": 799
    }
}

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='HTML')

# === DATA HANDLING ===
def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        default_data = {cat: {sub: [] for sub in subs} for cat, subs in CHANNEL_LINKS.items()}
        save_data(default_data)
        return default_data

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def load_vip_data():
    try:
        with open(VIP_DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        save_vip_data({"Indian VIP": [], "Korean VIP": []})
        return {"Indian VIP": [], "Korean VIP": []}

def save_vip_data(data):
    with open(VIP_DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def load_payment_data():
    try:
        with open(PAYMENT_DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        save_payment_data({"pending": [], "approved": []})
        return {"pending": [], "approved": []}

def save_payment_data(data):
    with open(PAYMENT_DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# === VIP ZONE IMPLEMENTATION ===
@bot.callback_query_handler(func=lambda call: call.data == "vip_zone")
def vip_zone(call):
    text = """<b>💎 VIP ZONE ACCESS</b>

🔐 <u>Indian 18+ Comics Plans</u>
1 Month VIP - 50+ comics to Read in ₹249
3 Months VIP - 100+ comics to read in ₹599
6 Months VIP - Unlimited Read + Priority Access ₹999
Lifetime VIP - Lifetime Access + Bonus Drops ₹1999-₹2499

<u>Per Comic Purchase (Indian):</u>
30 Chapters → ₹100
50 Chapters → ₹200
100+ Chapters → ₹300

🔐 <u>Korean Manhwa (Hindi) Plans</u>
1 Month VIP - 50+ Manhwa (Hindi) ₹499
3 Months VIP - 100+ Manhwa, Bonus Drops ₹1299
6 Months VIP - 500+ manhwas + Support ₹2499
Lifetime VIP - Lifetime Access + VIP Support ₹4999-₹5999

<u>Per Comic Purchase (Korean):</u>
30 Chapters → ₹299
60 Chapters → ₹399
100+ Chapters → ₹599
Special Premium → ₹799-₹999

<b>10+ Professional Translators Working With Us!</b>"""
    
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("🛒 Subscribe to VIP", callback_data="vip_subscribe"))
    markup.row(InlineKeyboardButton("📖 Buy Single Comic", callback_data="vip_single_comic"))
    markup.row(InlineKeyboardButton("🔙 Back to Main Menu", callback_data="joined"))
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "vip_subscribe")
def vip_subscribe(call):
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("Indian VIP", callback_data="vip_type_Indian"))
    markup.row(InlineKeyboardButton("Korean VIP (Hindi)", callback_data="vip_type_Korean"))
    markup.row(InlineKeyboardButton("🔙 Back", callback_data="vip_zone"))
    bot.edit_message_text("<b>Select VIP Type:</b>", call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("vip_type_"))
def vip_type_selected(call):
    vip_type = call.data.split("_")[-1]
    
    # FIXED: Handle Korean VIP key properly
    plan_key = "Indian VIP" if vip_type == "Indian" else "Korean VIP (Hindi)"
    
    markup = InlineKeyboardMarkup()
    for plan in VIP_PLANS[plan_key]:
        price = VIP_PLANS[plan_key][plan]["price"]
        markup.row(InlineKeyboardButton(
            f"{plan} - ₹{price}", 
            callback_data=f"vip_plan_{vip_type}_{plan.replace(' ', '_')}"
        ))
    
    markup.row(InlineKeyboardButton("🔙 Back", callback_data="vip_subscribe"))
    markup.row(InlineKeyboardButton("🔙 Back to Main Menu", callback_data="joined"))
    bot.edit_message_text(
        f"<b>{vip_type} VIP Plans:</b>\nSelect your subscription:", 
        call.message.chat.id, 
        call.message.message_id, 
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("vip_plan_"))
def vip_payment(call):
    _, _, vip_type, plan = call.data.split("_", 3)
    plan = plan.replace('_', ' ')
    price = VIP_PLANS["Indian VIP" if vip_type == "Indian" else "Korean VIP (Hindi)"][plan]["price"]
    
    text = f"""<b>💳 Payment Details</b>

<b>{plan} - ₹{price}</b>
UPI ID: <code>{UPI_ID}</code>
Name: {ADMIN_NAME}

Please send payment via UPI and upload screenshot below."""
    
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("📤 Upload Payment Proof", callback_data=f"upload_payment_{vip_type}_{plan.replace(' ', '_')}"))
    markup.row(InlineKeyboardButton("🔙 Back", callback_data=f"vip_type_{vip_type}"))
    markup.row(InlineKeyboardButton("🔙 Back to Main Menu", callback_data="joined"))
    
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("upload_payment_"))
def handle_payment_upload(call):
    vip_type, plan = call.data.replace("upload_payment_", "").split("_", 1)
    plan = plan.replace('_', ' ')
    
    msg = bot.send_message(call.message.chat.id, "Please send your payment screenshot now:")
    bot.register_next_step_handler(msg, lambda m: process_payment(m, vip_type, plan))

def process_payment(message, vip_type, plan):
    if not message.photo:
        bot.reply_to(message, "Please send a valid screenshot.")
        return
    
    payment_data = load_payment_data()
    payment_id = f"{message.from_user.id}_{datetime.now().timestamp()}"
    
    payment_data["pending"].append({
        "payment_id": payment_id,
        "user_id": message.from_user.id,
        "vip_type": vip_type,
        "plan": plan,
        "timestamp": str(datetime.now()),
        "screenshot_id": message.photo[-1].file_id
    })
    
    save_payment_data(payment_data)
    
    # Notify admin
    bot.send_photo(
        ADMIN_ID, 
        message.photo[-1].file_id,
        caption=f"New VIP Payment:\nUser: {message.from_user.id}\nType: {vip_type}\nPlan: {plan}\nPayment ID: {payment_id}"
    )
    
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("✅ Confirm", callback_data=f"confirm_{payment_id}"))
    markup.row(InlineKeyboardButton("❌ Reject", callback_data=f"reject_{payment_id}"))
    
    bot.send_message(
        ADMIN_ID,
        "Approve this payment?",
        reply_markup=markup
    )
    
    bot.reply_to(message, "Payment received! We'll verify and activate your VIP access within 20-30 minutes.")

# === ADMIN APPROVAL ===
@bot.callback_query_handler(func=lambda call: call.data.startswith(("confirm_", "reject_")))
def admin_approval(call):
    action, payment_id = call.data.split("_", 1)
    payment_data = load_payment_data()
    
    payment = next((p for p in payment_data["pending"] if p["payment_id"] == payment_id), None)
    if not payment:
        bot.answer_callback_query(call.id, "Payment not found!")
        return
    
    if action == "confirm":
        # Add to approved
        payment_data["approved"].append(payment)
        
        # Calculate expiry date
        plan = payment["plan"]
        if "1 Month" in plan:
            expiry = datetime.now() + timedelta(days=30)
        elif "3 Months" in plan:
            expiry = datetime.now() + timedelta(days=90)
        elif "6 Months" in plan:
            expiry = datetime.now() + timedelta(days=180)
        else:  # Lifetime
            expiry = "Lifetime"
        
        # Update VIP data
        vip_data = load_vip_data()
        vip_data[f"{payment['vip_type']} VIP"].append({
            "user_id": payment["user_id"],
            "plan": payment["plan"],
            "expiry": str(expiry) if isinstance(expiry, datetime) else expiry,
            "payment_id": payment_id
        })
        save_vip_data(vip_data)
        
        # Notify user
        bot.send_message(
            payment["user_id"],
            f"✅ Your {payment['plan']} has been approved!\n"
            f"Expiry: {expiry}\n"
            f"You now have access to the VIP content."
        )
        
        bot.answer_callback_query(call.id, "Payment approved!")
    else:
        bot.send_message(
            payment["user_id"],
            "❌ Your payment was rejected. Please contact admin if you think this is a mistake."
        )
        bot.answer_callback_query(call.id, "Payment rejected!")
    
    # Remove from pending
    payment_data["pending"] = [p for p in payment_data["pending"] if p["payment_id"] != payment_id]
    save_payment_data(payment_data)
    
    # Edit admin message
    bot.edit_message_text(
        f"Payment {action}ed: {payment_id}",
        call.message.chat.id,
        call.message.message_id
    )

# === SINGLE COMIC PURCHASE ===
@bot.callback_query_handler(func=lambda call: call.data == "vip_single_comic")
def single_comic_menu(call):
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("Indian Comic", callback_data="comic_type_Indian"))
    markup.row(InlineKeyboardButton("Korean Manhwa (Hindi)", callback_data="comic_type_Korean"))
    markup.row(InlineKeyboardButton("🔙 Back", callback_data="vip_zone"))
    markup.row(InlineKeyboardButton("🔙 Back to Main Menu", callback_data="joined"))
    bot.edit_message_text("<b>Select Comic Type:</b>", call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("comic_type_"))
def comic_chapter_selection(call):
    comic_type = call.data.split("_")[-1]
    markup = InlineKeyboardMarkup()
    
    for option in COMIC_PRICES[comic_type]:
        price = COMIC_PRICES[comic_type][option]
        markup.row(InlineKeyboardButton(
            f"{option} - ₹{price}", 
            callback_data=f"comic_purchase_{comic_type}_{option.replace(' ', '_')}"
        ))
    
    markup.row(InlineKeyboardButton("🔙 Back", callback_data="vip_single_comic"))
    markup.row(InlineKeyboardButton("🔙 Back to Main Menu", callback_data="joined"))
    bot.edit_message_text(
        f"<b>{comic_type} Comic Chapters:</b>\nSelect chapter range:", 
        call.message.chat.id, 
        call.message.message_id, 
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("comic_purchase_"))
def comic_payment(call):
    _, _, comic_type, chapters = call.data.split("_", 3)
    chapters = chapters.replace('_', ' ')
    price = COMIC_PRICES[comic_type][chapters]
    
    text = f"""<b>💳 Comic Purchase</b>

<b>{comic_type} Comic ({chapters}) - ₹{price}</b>
UPI ID: <code>{UPI_ID}</code>
Name: {ADMIN_NAME}

Please send payment via UPI and upload screenshot below."""
    
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("📤 Upload Payment Proof", callback_data=f"upload_comic_{comic_type}_{chapters.replace(' ', '_')}"))
    markup.row(InlineKeyboardButton("🔙 Back", callback_data=f"comic_type_{comic_type}"))
    markup.row(InlineKeyboardButton("🔙 Back to Main Menu", callback_data="joined"))
    
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("upload_comic_"))
def handle_comic_payment_upload(call):
    comic_type, chapters = call.data.replace("upload_comic_", "").split("_", 1)
    chapters = chapters.replace('_', ' ')
    
    msg = bot.send_message(call.message.chat.id, "Please send your payment screenshot now:")
    bot.register_next_step_handler(msg, lambda m: process_comic_payment(m, comic_type, chapters))

def process_comic_payment(message, comic_type, chapters):
    if not message.photo:
        bot.reply_to(message, "Please send a valid screenshot.")
        return
    
    payment_data = load_payment_data()
    payment_id = f"{message.from_user.id}_{datetime.now().timestamp()}"
    
    payment_data["pending"].append({
        "payment_id": payment_id,
        "user_id": message.from_user.id,
        "comic_type": comic_type,
        "chapters": chapters,
        "price": COMIC_PRICES[comic_type][chapters],
        "timestamp": str(datetime.now()),
        "screenshot_id": message.photo[-1].file_id,
        "is_comic": True
    })
    
    save_payment_data(payment_data)
    
    # Notify admin
    bot.send_photo(
        ADMIN_ID, 
        message.photo[-1].file_id,
        caption=f"New Comic Purchase:\nUser: {message.from_user.id}\nType: {comic_type}\nChapters: {chapters}\nPrice: ₹{COMIC_PRICES[comic_type][chapters]}\nPayment ID: {payment_id}"
    )
    
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("✅ Confirm", callback_data=f"confirm_{payment_id}"))
    markup.row(InlineKeyboardButton("❌ Reject", callback_data=f"reject_{payment_id}"))
    
    bot.send_message(
        ADMIN_ID,
        "Approve this comic purchase?",
        reply_markup=markup
    )
    
    bot.reply_to(message, "Payment received! We'll verify and send your comic within 20-30 minutes.")

# === MAIN MENU ===
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{MAIN_CHANNEL}"),
        InlineKeyboardButton("✅ I've Joined", callback_data="joined")
    )
    bot.send_message(message.chat.id,
                     "📖 <b>Welcome to MangaSutra!</b>\n\nPlease join our channel to access content.",
                     reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "joined")
def joined(call):
    user = bot.get_chat_member(f"@{MAIN_CHANNEL}", call.from_user.id)
    if user.status in ["member", "creator", "administrator"]:
        markup = InlineKeyboardMarkup()
        for cat in CHANNEL_LINKS:
            if cat != "💎 VIP Zone":
                markup.add(InlineKeyboardButton(f"📁 {cat}", callback_data=f"cat_{cat}"))
        markup.add(InlineKeyboardButton("💎 VIP Zone", callback_data="vip_zone"))
        bot.edit_message_text("📚 <b>Main Menu:</b>", call.message.chat.id, call.message.message_id, reply_markup=markup)
    else:
        bot.answer_callback_query(call.id, "🚫 Please join the channel first!", show_alert=True)

# === CATEGORY HANDLER ===
@bot.callback_query_handler(func=lambda call: call.data.startswith("cat_"))
def show_subcategories(call):
    cat = call.data[4:]
    markup = InlineKeyboardMarkup()
    for sub in CHANNEL_LINKS[cat]:
        markup.add(InlineKeyboardButton(sub, url=CHANNEL_LINKS[cat][sub]))
    markup.add(InlineKeyboardButton("🔙 Back to Main Menu", callback_data="joined"))
    bot.edit_message_text(f"<b>{cat} Subcategories:</b>", call.message.chat.id, call.message.message_id, reply_markup=markup)

# === MAIN ===
if __name__ == "__main__":
    if not os.path.exists(DATA_FILE):
        save_data({cat: {sub: [] for sub in subs} for cat, subs in CHANNEL_LINKS.items()})
    if not os.path.exists(VIP_DATA_FILE):
        save_vip_data({"Indian VIP": [], "Korean VIP": []})
    if not os.path.exists(PAYMENT_DATA_FILE):
        save_payment_data({"pending": [], "approved": []})
    
    print("🤖 Bot is running with VIP Zone...")
    bot.infinity_polling()
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # बॉट को अलग थ्रेड में चलाएं
    import threading
    threading.Thread(target=bot.infinity_polling).start()
