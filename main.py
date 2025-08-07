import os
# 我们不再需要正则表达式库 re，可以将其移除
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)

# --- 在这里替换成您的链接 ---
URL_FOR_BUTTON_1 = 'https://www.your-first-link.com'      # 第一个按钮的链接
URL_FOR_BUTTON_2 = 'https://t.me/your_second_link_group' # 第二个按钮的链接

# 从环境变量中获取您的机器人令牌
BOT_TOKEN = os.environ.get('BOT_TOKEN') # 强烈建议将令牌存储为环境变量

# 处理文本消息的函数
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """当接收到特定关键词'中文'时，发送带链接按钮的回复。"""
    
    # 核心修改：直接判断消息内容是否为'中文'
    if update.message.text == '中文':
        
        # 创建内联键盘按钮
        keyboard = [
            [
                InlineKeyboardButton("官方网站", url=URL_FOR_BUTTON_1),
                InlineKeyboardButton("官方群组", url=URL_FOR_BUTTON_2),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # 回复原始消息，并附上我们创建的键盘
        await update.message.reply_text('检测到关键词，请选择一个入口：', reply_markup=reply_markup)

def main() -> None:
    """启动并运行机器人。"""
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # 添加一个消息处理器来处理文本消息
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # 开始轮询
    print("机器人已启动，正在轮询...")
    application.run_polling()

if __name__ == '__main__':
    main()
