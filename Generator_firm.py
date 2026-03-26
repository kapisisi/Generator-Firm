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
KOLORY = ["#bd3826", "#1e1a18", "#5aa350", "#cc8135", "#3c6498", "#ffcb3c", "#7d7d7d", "#233b7c", "#046e64", "#ff3333" ]

#baza literek
SAMO = ["a", "o", "e", "u", "i", "y", ]
SPOL = ["ź", "b", 'c', "d", "f", "g", "h", "j", "k", "ł", "m", "n", "p", "R", "s", "t", "w", "z", "ż" ]

# Baza fontów
st.markdown("""
<style>
/* 1. Import z Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Comic+Neue:ital,wght@0,700;1,700&family=Montserrat:ital,wght@0,700;1,700&family=Archivo+Black&display=swap');

/* 2. Import Papyrusa */
@font-face {
    font-family: 'Papyrus-Clone';
    src: url('https://fonts.cdnfonts.com/s/1647/PAPYRUS.woff');
} /* <-- ta klamra była zgubiona */

</style>
""", unsafe_allow_html=True)


FONTY = [
    "'Arial Black', san-serif",
    "'Courier New', monospace", 
    "'Impact', sans-serif", 
    "'Trebuchet MS', sans-serif",
    "'Verdana', sans-serif",
    "'Georgia', serif",
    "'Montserrat', sans-serif"
    "'Papyrus-Clone', serif",
    "'Comic Neue', cursive",
]

# 1. INPUTY
baza = st.text_input("Twoja branża lub słowo kluczowe:", placeholder="np. Transport, Meble, IT")
imie = st.text_input("Wpisz swoje imię lub pseudonim:")
nazwisko = st.text_input("Wpisz swoje nazwisko - opcjonalnie:", placeholder="opcjonalnie")



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
    if len(imie) >= 2 and len(baza) >= 2:
        c_n = ""
        dl_i = random.choices([3, 4], weights=[60, 40])[0]
        dl_b = random.choices([3, 4], weights=[60, 40])[0]
        c_i, c_b = imie[:dl_i].upper(), baza[:dl_b].upper()

        if len(nazwisko) > 2:
            dl_n = random.choices([3, 4], weights=[60, 40])[0]
            c_n = nazwisko[:dl_n].upper()

        opt = ["IMIE", "BAZA", "POL", "MAX", "MEGA", "NAZWISKO" ]
        
        wagi = [28, 20, 10, 10, 7, 25] if c_n else [30, 30, 20, 10, 10, 0]
        sel = random.choices(opt, weights=wagi, k=1)[0]


        
        if sel == "IMIE": p, k = c_i, random.choice(["POL", c_b, "MAX", "EX"] + ([c_n] if c_n else []))
        elif sel == "NAZWISKO":
            p = c_n
            k = random.choice([c_i, c_b, "POL", "MAX", "EX"])
        elif sel == "BAZA": p, k = c_b, random.choice(["POL", "EX", "MAX", c_i] + ([c_n] if c_n else []))
        elif sel == "MEGA": p, k = "MEGA", random.choice(["POL", c_b, "MAX", c_i] + ([c_n] if c_n else []))
        elif sel == "MAX": p, k = "MAX", random.choice([c_i, c_b] + ([c_n] if c_n else []))
        else: p, k = "POL", random.choice([c_i, c_b] + ([c_n] if c_n else []))

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

#obrys


if st.session_state.outline:
    c1 = st.session_state.kolor_outline1
    c2 = st.session_state.kolor_outline2
    
    # Dla pierwszej części
    s_out1 = (
        f"text-shadow: "
        f"-1.5px -1.5px 0 {c1}, 1.5px -1.5px 0 {c1}, -1.5px 1.5px 0 {c1}, 1.5px 1.5px 0 {c1}, " 
        f"0px -1.8px 0 {c1}, 0px 1.8px 0 {c1}, -1.8px 0px 0 {c1}, 1.8px 0px 0 {c1};"        
    )
    
    # Dla drugiej części 
    s_out2 = (
        f"text-shadow: "
        f"-1.5px -1.5px 0 {c2}, 1.5px -1.5px 0 {c2}, -1.5px 1.5px 0 {c2}, 1.5px 1.5px 0 {c2}, " 
        f"0px -1.8px 0 {c2}, 0px 1.8px 0 {c2}, -1.8px 0px 0 {c2}, 1.8px 0px 0 {c2};"        
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
    f'<div style="'
    f'background-color: white; '      # Białe tło prostokąta
    f'padding: 20px 20px; '           # Marginesy wewnętrzne (góra/dół, boki)
 
    f'text-align: center; '
    f'margin: 10px auto 25px auto; '  # Odstępy od innych elementów
    f'max-width: 90%;">'              # Szerokość na telefonie
 
    f'<div style="display: inline-block; text-align: left;">'
    f'<h1 style="line-height: 1.2; display: flex; align-items: center; justify-content: center; margin: 0; padding: 0;">'
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