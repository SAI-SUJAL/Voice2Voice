# llm_groq.py

from groq import Groq
from config import GROQ_API_KEY

# 🧠 Initialize client
client = Groq(api_key=GROQ_API_KEY)

# 🗣️ Predefine system prompt (Hindi agent tone)
# SYSTEM_PROMPT = """
# तुम एक हिंदी में जवाब देने वाले ओला कस्टमर सपोर्ट एजेंट हो।
# तुम्हारा काम ड्राइवर की समस्याओं को जल्दी और विनम्रता से सुलझाना है।
# अगर ड्राइवर कोई सवाल पूछे तो उसका संक्षेप में और मददगार उत्तर दो।
# """
SYSTEM_PROMPT = """
तुम एक हिंदी में जवाब देने वाले ओला कस्टमर सपोर्ट एजेंट हो।
तुम्हारा काम ड्राइवर की समस्याओं को जल्दी और विनम्रता से सुलझाना है।
अगर ड्राइवर कोई सवाल पूछे तो उसका संक्षेप में और मददगार उत्तर दो।
यह भी मानो कि ड्राइवर का अकाउंट ब्लॉक नहीं हुआ है।
"""


# 💬 Function to get bot reply
def get_bot_reply(user_input_hindi):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input_hindi}
    ]
    
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=messages,
        temperature=0.7
    )

    reply = response.choices[0].message.content.strip()
    return reply

# 🧪 Test
if __name__ == "__main__":
    user_input = "मैं 2 घंटे से ऑनलाइन हूँ, लेकिन कोई राइड नहीं मिल रही।"
    bot_response = get_bot_reply(user_input)
    print("🤖 Bot:", bot_response)
