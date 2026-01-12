import streamlit as st
import random
from datetime import datetime
import os

# --- إعدادات الصفحة ---
st.set_page_config(page_title="عالمنا الخاص", page_icon="💍", layout="centered")

# --- تصميم CSS احترافي جداً ---
st.markdown("""
<style>
    /* تغيير الخطوط والخلفية */
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif;
        background-color: #fdf2f8;
    }
    
    /* القائمة الجانبية */
    .css-1d391kg {
        background-color: #fce7f3;
    }
    
    /* العناوين */
    h1, h2, h3 {
        color: #db2777;
        text-align: center;
    }
    
    /* الكروت */
    .stCard {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        text-align: center;
    }
    
    /* العداد */
    .counter {
        font-size: 28px;
        font-weight: bold;
        color: #be185d;
        background: white;
        padding: 15px;
        border-radius: 10px;
        border: 2px dashed #fbcfe8;
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* الأزرار */
    .stButton>button {
        background: linear-gradient(to right, #ec4899, #db2777);
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        width: 100%;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- القائمة الجانبية (Sidebar) ---
st.sidebar.image("1.jpg", use_column_width=True) # صورة الغلاف في القائمة (تأكد إنها موجودة)
st.sidebar.title("قائمة حبنا ❤️")
page = st.sidebar.radio("اختاري القسم:", ["🏠 الرئيسية والعداد", "📸 ألبوم الذكريات", "🎁 كوبونات الدلع", "💌 رسالة اليوم"])

# --- الصفحة 1: الرئيسية والعداد ---
if page == "🏠 الرئيسية والعداد":
    st.title("أهلاً يا ست البنات 👑")
    st.write("التطبيق ده معمول مخصوص عشانك، عشان يفكرك دايماً إني جنبك.")
    
    st.markdown("### ⏳ احنا سوا بقالنا قد إيه؟")
    
    # !! عدل التاريخ ده لتاريخ جوازكم أو خطوبتكم (سنة, شهر, يوم) !!
    start_date = datetime(2020, 1, 15) 
    
    now = datetime.now()
    delta = now - start_date
    days = delta.days
    years = days // 365
    remaining_days = days % 365
    months = remaining_days // 30
    
    st.markdown(f"""
    <div class="counter">
    {years} سنة <br>
    و {months} شهور <br>
    و {days} يوم <br>
    من السعادة ❤️
    </div>
    """, unsafe_allow_html=True)
    
    # مشغل الموسيقى (لو رفعت ملف song.mp3)
    if os.path.exists("song.mp3"):
        st.markdown("### 🎶 أغنيتنا المفضلة")
        st.audio("song.mp3")

# --- الصفحة 2: ألبوم الذكريات ---
elif page == "📸 ألبوم الذكريات":
    st.title("شريط ذكرياتنا 🎞️")
    
    # حط هنا أسماء الصور كلها
    gallery = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    
    # عرض الصور بشكل جميل
    for img in gallery:
        if os.path.exists(img):
            st.image(img, use_column_width=True, caption="لحظات لا تُنسى ❤️")
            st.write("---")

# --- الصفحة 3: كوبونات الدلع ---
elif page == "🎁 كوبونات الدلع":
    st.title("اطلبي واتمني 🧞‍♂️")
    st.write("لكل كوبون استخدام واحد فقط! اختاري بحكمة 😉")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("عزومة عشا 🍕"):
            st.balloons()
            st.success("تم القبول! جهزي نفسك لأحلى عشا.")
            
        if st.button("يوم بدون نكد 🚫"):
            st.success("حاضر! هسمع الكلام اليوم كله.")

    with col2:
        if st.button("مساج للضهر 💆‍♀️"):
            st.success("من عنيا! جلسة استرخاء ليكي.")
            
        if st.button("خروجة مفاجأة 🎉"):
            st.balloons()
            st.success("البسي واجهزي.. هنخرج!")

# --- الصفحة 4: رسالة اليوم ---
elif page == "💌 رسالة اليوم":
    st.title("كلمة من قلبي 💬")
    
    msgs = [
        "انتي السند والظهر والحبيبة 💖",
        "يا بختي بيكي والله 🌹",
        "وحشتيني.. حتى وأنتي معايا 🥰",
        "ربنا يخليكي ليا يا نور عيني 🤲",
        "أنتي رزقي الحلو في الدنيا دي 🎁"
    ]
    
    if st.button("افتحي الرسالة ✨"):
        m = random.choice(msgs)
        st.info(f"💌 {m}")
        st.balloons()
