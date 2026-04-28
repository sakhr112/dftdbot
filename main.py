from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import yt_dlp

TOKEN = "8622664181:AAGiqqLK2HMYbfGQ8Uy21cM6rJPb4etXx3k"

def start(update, context):
    update.message.reply_text("ارسل رابط الفيديو")

def handle(update, context):
    url = update.message.text

    if "http" in url:
        update.message.reply_text("جاري التحميل...")

        ydl_opts = {'outtmpl': 'video.mp4', 'format': 'best'}

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            update.message.reply_video(open("video.mp4", "rb"))

        except Exception as e:
            update.message.reply_text(str(e))
    else:
        update.message.reply_text("ارسل رابط صحيح")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, handle))

updater.start_polling()
updater.idle()