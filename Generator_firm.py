import streamlit as st
import random


# BIBLIOTEKA

# Ustawienia strony

st.set_page_config(page_title="Generator Nazw")

st.markdown("""
    <style>
    /* wszytsko */
    div.stVerticalBlock { gap: 10px !important; }
    
    /* marginesy linii --- */
    hr { margin: 5px 5px !important; }
    
    /*nagłówki paragrafy */
    h1, p { margin: 5px !important; padding: 0px !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Generator Firm</h1>", unsafe_allow_html=True)
st.write("")

# Baza kolorów
KOLORY = ["#bd3826", "#1e1a18", "#5aa350", "#cc8135", "#3c6498", "#ffcb3c", "#7d7d7d", "#233b7c"]

#baza literek
SAMO = ["a", "o", "e", "u", "i", "y", ]
SPOL = ["ź", "b", 'c', "d", "f", "g", "h", "j", "k", "ł", "m", "n", "p", "R", "s", "t", "w", "z", "ż" ]

# Baza fontów


FONTY = [
    "'Arial Black', san-serif",
    "'Brush Script MT', sans-serif"
    "'Courier New', monospace", 
    "'Georgia', serif", 
    "'Impact', sans-serif", 
    "'Trebuchet MS', sans-serif",
    "'Verdana', sans-serif",
    "'Comic Sans MS', cursive"
]

# 1. INPUTY
imie = st.text_input("Wpisz swoje imię, pseudonim lub nazwisko:")
baza = st.text_input("Twoja branża lub słowo kluczowe:", placeholder="np. Transport, Meble, IT")

st.markdown("---")

# kontrast
def get_text_color(bg_hex):
    if bg_hex.lower() in ["#ffcb3c", "#ffffff"]: 
        return "#000000"
    return "#FFFFFF"

# Inicjalizacja stanu
if 'czesc1' not in st.session_state:
    st.session_state.czesc1 = "TWOJA "
    st.session_state.czesc2 = "FIRMA"
    st.session_state.sep = ""
    st.session_state.kolor1 = "#7d7d7d"
    st.session_state.kolor2 = "#7d7d7d"
    st.session_state.f1 = FONTY[0]
    st.session_state.f2 = FONTY[0]
    st.session_state.s1= 32
    st.session_state.s2= 32
    st.session_state.box1 = False
    st.session_state.box2 = False
    st.session_state.line = False
    st.session_state.outline = False
    st.session_state.kolor_outline1 = "#7d7d7d"
    st.session_state.kolor_outline2 = "#7d7d7d"

# 2. LOGIKA GENEROWANIA
def generuj():
    if len(imie) >= 3 and len(baza) >= 3:
        dl_i, dl_b = random.choice([3, 4]), random.choice([3, 5])
        c_i, c_b = imie[:dl_i].upper(), baza[:dl_b].upper()
        
        opt = ["IMIE", "BAZA", "POL", "MAX", "MEGA"]
        sel = random.choices(opt, weights=[30, 30, 15, 30, 5], k=1)[0]
        
        if sel == "IMIE": p, k = c_i, random.choice(["POL", c_b, "MAX", "EX"])
        elif sel == "BAZA": p, k = c_b, random.choice(["POL", "EX", "MAX", c_i])  
        elif sel == "MEGA": p, k = "MEGA", random.choice(["POL", c_b, "MAX", c_i])
        elif sel == "MAX": p, k = "MAX", random.choice([c_i, c_b])
        else: p, k = "POL", random.choice([c_i, c_b])

        st.session_state.czesc1 = p
        st.session_state.czesc2 = k

        #myslnik
        st.session_state.sep = random.choices(["-", ""], weights=[20, 80])[0]
        
        #dodawanie samiogloski
        if st.session_state.sep == "":
            ostatnia_litera = st.session_state.czesc1[-1].lower()
         
            if ostatnia_litera in [s.lower() for s in SPOL]:
             
                if random.random() < 0.25:
                    lacznik = random.choice(SAMO).upper()
                    st.session_state.czesc1 += lacznik

        #kolory i fonty 
        st.session_state.kolor1 = random.choice(KOLORY)
        st.session_state.kolor2 = random.choice(KOLORY)
        st.session_state.f1 = random.choice(FONTY)
        st.session_state.f2 = random.choice(FONTY)


        # boxy
        if st.session_state.sep == "-":
            st.session_state.box1 = False
            st.session_state.box2 = False
        else:
            st.session_state.box1 = random.random() < 0.40
            st.session_state.box2 = random.random() < 0.40

        #font wielkosc
        st.session_state.s1 = random.randint(35, 50)
        st.session_state.s2 = random.randint(35, 50)

        #linia
        if st.session_state.box1 == False and st.session_state.box2 == False:
            st.session_state.line = random.random() < 0.50
        else: st.session_state.line = False

        #Outline
        st.session_state.outline = random.random() < 0.30
        
        if st.session_state.outline:
            # Kolor 1:
            nowy_kolor1 = random.choice(KOLORY)
            while nowy_kolor1 == st.session_state.kolor1:
                nowy_kolor1 = random.choice(KOLORY)
            st.session_state.kolor_outline1 = nowy_kolor1
            
            # Kolor 2 
            nowy_kolor2 = random.choice(KOLORY)
            while nowy_kolor2 == st.session_state.kolor2:
                nowy_kolor2 = random.choice(KOLORY)
            st.session_state.kolor_outline2 = nowy_kolor2
            
        else:
            # Jeśli outline się nie wylosował 
            st.session_state.kolor_outline1 = st.session_state.kolor1
            st.session_state.kolor_outline2 = st.session_state.kolor2
    else:
        st.error("Wpisz przynajmniej 3 litery!")

       

 
# 3. HTML

#kolor
t1 = get_text_color(st.session_state.kolor1) if st.session_state.box1 else st.session_state.kolor1
t2 = get_text_color(st.session_state.kolor2) if st.session_state.box2 else st.session_state.kolor2
sep_color = st.session_state.kolor1 if not st.session_state.box1 else st.session_state.kolor2

#outline 
if st.session_state.outline:
    s_out1 = (
        f"text-shadow: -1.5px -1.5px 0 {st.session_state.kolor_outline1}, "
        f"1.5px -1.5px 0 {st.session_state.kolor_outline1}, "
        f"-1.5px 1.5px 0 {st.session_state.kolor_outline1}, "
        f"1.5px 1.5px 0 {st.session_state.kolor_outline1};"
    )
    s_out2 = (
        f"text-shadow: -1.5px -1.5px 0 {st.session_state.kolor_outline2}, "
        f"1.5px -1.5px 0 {st.session_state.kolor_outline2}, "
        f"-1.5px 1.5px 0 {st.session_state.kolor_outline2}, "
        f"1.5px 1.5px 0 {st.session_state.kolor_outline2};"
    )
else:
    s_out1 = ""
    s_out2 = ""

# box1 
if st.session_state.box1:
    html_p1 = f'<span style="background-color:{st.session_state.kolor1}; color:{t1}; padding:0.1em 0.3em; border-radius:0px; font-family:{st.session_state.f1}; font-size:{st.session_state.s1}px; display:inline-block; margin:0; white-space: pre-wrap; {s_out1}">{st.session_state.czesc1}</span>'
else:
    html_p1 = f'<span style="color:{t1}; font-family:{st.session_state.f1}; font-size:{st.session_state.s1}px; margin:0; white-space: pre-wrap; {s_out1}">{st.session_state.czesc1}</span>'

# box2 
if st.session_state.box2:
    html_p2 = f'<span style="background-color:{st.session_state.kolor2}; color:{t2}; padding:0.1em 0.3em; border-radius:0px; font-family:{st.session_state.f2}; font-size:{st.session_state.s2}px; display:inline-block; margin:0; white-space: pre-wrap; {s_out2}">{st.session_state.czesc2}</span>'
else:
    html_p2 = f'<span style="color:{t2}; font-family:{st.session_state.f2}; font-size:{st.session_state.s2}px; margin:0; white-space: pre-wrap; {s_out2}">{st.session_state.czesc2}</span>'

#linia
html_line = ""
if st.session_state.line:
    html_line = f'<div style="height: 12px; background-color: {sep_color}; width: 100%; margin-top: 2px; border-radius: 0px;"></div>'

# Final
html_final = (
    f'<div style="text-align: center; padding: 40px 0px;">'  # <--- TUTAJ DODANE PADDING

    f'<div style="display: inline-block; text-align: left;">'
    f'<h1 style="letter-spacing: 0px; line-height: 1.4; display: flex; align-items: center; justify-content: center; margin: 0; padding: 0;">'
    f'{html_p1}<span style="font-size:{st.session_state.s1}px; color:{sep_color};">{st.session_state.sep}</span>{html_p2}'
    f'</h1>{html_line}</div></div>'
)

st.markdown(html_final, unsafe_allow_html=True)

# 4. PRZYCISK
st.markdown("""
    <style>
    /* Styl */
    div.stButton > button {
        background-color: #ffda48 !important; /* Jasny żółty */
        color: #000000 !important;           /* Czarny tekst dla kontrastu */
        border-radius: 10px !important;      /* Zaokrąglone rogi */
        border: 1px solid #fbc02d !important; /* Delikatna obwódka */
        height: 3em !important;
        font-weight: bold !important;
    }
    
    /* hover */
    div.stButton > button:hover {
        background-color: #ffcc00 !important; /* Jeszcze jaśniejszy żółty */
        color: #000000 !important;
        border-color: #fbc02d !important;
    }
    
    /* Efekt po kliknięciu */
    div.stButton > button:active {
        background-color: #fdd835 !important;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.button("Generuj nazwę ✨", on_click=generuj, use_container_width=True)

# --- STOPKA ---
st.markdown("---") 

# Style dla przycisku Donate
st.markdown("""
    <style>
    div.stLinkButton > a {
        background-color: #FF813F !important;
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        font-weight: bold !important;
    }
    div.stLinkButton > a:hover {
        background-color: #ff5f08 !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

d_col1, d_col2, d_col3 = st.columns([1, 1, 1])
with d_col2:
    st.link_button("☕ DONATE", "https://www.buymeacoffee.com/KasiaWorek", use_container_width=True)
    st.caption("<p style='text-align:center;'>Podoba Ci się generator? Wesprzyj moją pracę!</p>", unsafe_allow_html=True)

# Informacja o danych na samym końcu strony
st.markdown("<p style='text-align:center; font-size:10px; color: grey; margin-top: 20px;'>Szanuję Twoją prywatność. Generator nie przechowuje ani nie przesyła wpisywanych przez Ciebie danych.</p>", unsafe_allow_html=True)