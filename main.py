from datetime import datetime
import time
import keyboards
import configs
import logs
import errors

client = configs.bot
openai = configs.open_ai_key
time_now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")


@client.message_handler(content_types=['text'])
def get_text(message):
    username = message.from_user.first_name
    lastname = message.from_user.last_name
    us_id = message.from_user.id
    if '/start' == message.text:
        client.send_chat_action(message.chat.id, 'typing')
        time.sleep(1.5)
        client.send_message(message.chat.id, f"Приветсвую, {username}!\n"
                                             "Данный бот создан для облегчения использования ChatGPT",
                            reply_markup=keyboards.main_keyboard())
        logs.logging_bot(message, 'вход в бота')
        return


@client.callback_query_handler(func=lambda message: True)
def logic_inline(call):
    if 'Начать диалог с GPT' in call.data:
        client.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(0.5)
        client.send_message(call.message.chat.id, 'Введите свой запрос')
        return


while True:
    try:
        print(f'{time_now} Запуск {configs.telegram["name"]} успешен')
        client.polling(non_stop=True, interval=0)
    except Exception as error:
        errors.error_save(error, client)
