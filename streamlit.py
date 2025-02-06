# Streamlit-ը Python-ով վեբ հավելվածներ ստեղծելու պարզ և արագ գործիք է, 
# որը հատկապես հարմար է մեքենայական ուսուցման մոդելների, տվյալների վիզուալիզացիայի 
# և ինտերակտիվ գրաֆիկների համար։

# Ինչո՞ւ օգտագործել Streamlit
# 1. Պարզ և արագ – Չպետք է գրել HTML, CSS կամ 
#   JavaScript (Ցանկացած web կայքի հիմքում ընկած ֆայլեր)

# 2. Կոդերը գրվում են .py ֆայլում, հետևաբար ուղիղ կապ python-ի հետ, 
#   պետք չէ հաղորդակցվելու համար այլընտրանքներ մտածել* 

# 3. Գոյություն ունեն բազմաթիվ ֆունկցիաներ, համարյա բոլոր 
#   ցանկությունները իրականացնելու համար

import streamlit as st
import datetime # datetime.date

st.title("Բարև, Streamlit!")
st.write("Սա իմ առաջին Streamlit հավելվածն է")

st.markdown("""
- Կետիկով նշումներ
""")

a = st.date_input("Օր ներմուծիր") # datetime

print(a)
st.checkbox(a.strftime("%d.%m.%Y"))

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue() # ստանալ բայթերով

    print(bytes_data)
    print(type(bytes_data))
    with open("example.png", "wb") as f:
        f.write(bytes_data)

    st.image(uploaded_file)

name = st.text_input("Քո անունը:")
if name:
    st.write(f"Ողջույն, {name}!")