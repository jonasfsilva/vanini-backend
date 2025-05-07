import os
from chat.models import ChatInfo
from openai import OpenAI

# Carrega a chave da API do OpenAI a partir das variáveis de ambiente
OPENAI_API_KEY = os.getenv("CHATGPT_KEY")
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Cria o cliente OpenAI com a chave da API
openai_client = OpenAI(api_key=OPENAI_API_KEY)


def get_previous_context(chat):
    from chat.models import ChatMessage
    chat_messages = ChatMessage.objects.filter(chat=chat).values('text', 'type')

    messages = ['Respostas Anteriores: ']
    for msg in chat_messages:
        messages.append((f"{msg.get('type')}: {msg.get('text')}"))

    return str(messages)


def chatgpt_send_message(question, messages_context):
    """
    Envia uma mensagem para o ChatGPT e retorna a resposta.
    """
    # Contexto para o ChatGPT
    context = ChatInfo.objects.last().context
    # Realiza o pedido de completamento de texto para o OpenAI
    completion = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context + messages_context},
            {"role": "user", "content": question},
        ],
    )
    # Retorna a resposta do assistente
    return completion.choices[0].message.content
