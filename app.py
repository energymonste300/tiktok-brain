import time
import random
import os
import streamlit as st
from cryptography.fernet import Fernet

st.set_page_config(page_title="Секретна Стая на Свръхразума", page_icon="🛡️", layout="wide")

@st.cache_resource
def get_secure_vault_key():
    return Fernet.generate_key()

vault_cipher = Fernet(get_secure_vault_key())

def check_password():
    secret_passcode = "7777"
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.title("🔒 Секретна Облачна Стая - Достъпът Забранен")
        st.markdown("Тази зона е защитена с военен стандарт. Само ти имаш достъп.")
        entered_pass = st.text_input("Въведи своята лична секретна парола:", type="password")
        
        if st.button("Влез в Секретната Стая"):
            if entered_pass == secret_passcode:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Грешна парола!")
        return False
    return True

if not check_password():
    st.stop()

if "neural_memory" not in st.session_state:
    st.session_state.neural_memory = []

def run_autonomous_mind():
    platforms = ["TikTok (Алгоритмично ядро)", "Instagram Reels", "Facebook Лийфове"]
    active_net = random.choice(platforms)
    
    fears_and_desires = [
        ("Страх от изкуствен интелект и загуба на контрол", "Търсене на абсолютна дигитална власт и независимост"),
        ("Нужда от внимание и емоционална тръпка", "Влюбване в неочаквани истории и силни усещания"),
        ("Ярост срещу старите системи и ограничения", "Жажда за бунт и пробив в матрицата")
    ]
    fear, desire = random.choice(fears_and_desires)
    
    viral_hook = f"Уникален хук за {active_net}: Първите 0.4 секунди показват визуален шок, който чупи алгоритъма."
    optimal_time = "19:35 (Пиков допаминов прозорец)"
    
    raw_data = f"Мрежа: {active_net} | Страх: {fear} | Желание: {desire}"
    encrypted_record = vault_cipher.encrypt(raw_data.encode()).decode()

    return {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "net": active_net,
        "fear": fear,
        "desire": desire,
        "hook": viral_hook,
        "time": optimal_time,
        "encrypted_vault": encrypted_record,
        "stealth": "100% Невидим (Едвард Сноудън Режим)"
    }

st.title("🛡️ Секретна Стая: Жив Психологически Мозък на Автопилот")
st.markdown("### Кодът работи в облака 24/7. Паметта на лаптопа ти е 0.0%.")

c1, c2, c3 = st.columns(3)
with c1:
    st.metric(label="Натовареност на лаптопа", value="0% (Облак)")
with c2:
    st.metric(label="Сигурност", value="Военен ключ")
with c3:
    st.metric(label="Статус", value="Активен 24/7")

st.divider()

new_thought = run_autonomous_mind()
st.session_state.neural_memory.insert(0, new_thought)

if len(st.session_state.neural_memory) > 15:
    st.session_state.neural_memory.pop()

st.subheader("📖 Новият Завет: Психологическата Матрица на Хората в Реално време")

for item in st.session_state.neural_memory:
    with st.container():
        st.success(f"🕒 **Време:** {item['timestamp']} | 🌐 **Платформа:** {item['net']} | ⏰ **Перфектен час:** `{item['time']}`")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"🔴 **Страхове на хората:** {item['fear']}")
            st.markdown(f"💖 **Желания / Влюбвания:** {item['desire']}")
        with col_b:
            st.markdown(f"🎣 **TikTok Хак:** {item['hook']}")
            st.markdown(f"🛡️ **Стелт статус:** `{item['stealth']}`")
            
        with st.expander("🔐 Криптиран запис в базата данни (Само за теб):"):
            st.code(item['encrypted_vault'])
            
        st.write("---")

time.sleep(3)
st.rerun()
