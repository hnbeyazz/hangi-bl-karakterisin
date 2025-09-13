import streamlit as st

st.markdown("""
<h1 style="
    color: #D8BFD8;
    font-family: 'Lucida', monospace;
    text-align: right;
">
Hangi BL Karakterisin?
</h1>
<p style="
    color: #D8BFD8;
    font-family: 'Lucida', monospace;
    text-align: center;
    font-size: 30px;
">
⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆
</p>
""", unsafe_allow_html=True)


page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url('https://resmim.net/cdn/2025/09/13/jjJo5x.jpg');
    background-size: cover;       
    background-position: center;
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)


st.markdown("""
<h1 style="
    font-size: 22px;
    font-family: 'Georgia', serif;
    color: #D8BFD8;
    text-align: left;
">
CEVAPLAMASI ZORUNLU 
</h1>
""", unsafe_allow_html=True)


st.markdown("""
<style>
div[data-testid="stTextInput"] > label {
    color: #000080;
    font-family: 'Courier New', monospace;
    font-size: 20px;                         
    font-style: italic;
}
</style>
""", unsafe_allow_html=True)

st.markdown('''
<style>
div[data-testid="stAlert"][data-alert-type="warning"] {
    background-color: #FFF0F5;        /* Açık mor arka plan */
    color: #8B008B;                   /* Yazı rengi */
    font-family: 'Courier New', monospace;
    font-size: 40px;
}
</style>
''',unsafe_allow_html=True)


yas = st.text_input("Yaşınızı girin:")

if yas:
    try:
        yas = int(yas)
        if yas < 16:
            st.warning("Üzgünüz, bu teste 16 yaşından küçükler katılamaz!")
        else:
            st.success("Teste devam edebilirsin!")
            ad = st.text_input('Adınız?')
            if ad:
                st.markdown(f"""
                <div style="
                    color: #0E141C;         
                    font-family: 'Georgia', serif; 
                    font-size: 24px;
                    font-style: italic;
                ">
                Hoş geldin, {ad}! Son bir sorumuz daha var...
                </div>
                """, unsafe_allow_html=True)
                secim = st.radio('Yuri sever misin?', ["", "Evet", "Hayır"], index=0)

                if secim == "Evet":
                    st.warning('Eğer yuri sevdiğini onaylarsan teste devam edemezsin ╭∩╮( •̀_•́ )╭∩╮')
                elif secim == "Hayır":
                    st.success('Harika biz de öyle düşünmüştük ≽^•⩊•^≼ ')
                    questions = [
                        {
                            'qu': 'İnsanları rahatsız etmekte ne kadar iyisiniz?',
                            'op': {
                                'Kimseyi rahatsız etmem.': 0,
                                'Biraz sinir bozucuyum.': 1,
                                'Rahatsız ediciyim.': 0,
                                "This's my hobby": 1
                            }
                        },
                        {
                            'qu': 'Garip ya da utangaç bir insan olduğunuzu düşünüyor musunuz? ',
                            'op': {
                                'Dünyanın en karizmatik ve sosyal insanıyım.': 1,
                                'Normal düz insanım işte.': 0,
                                'Sanırım biraz utagacım.': 0,
                                'Garip sorunlu utangaç insanın tekiyim' : 1
                            }
                        },
                        {
                            'qu': 'Günlük uyku ihtiyacınızı nasıl tanımlarsınız? ',
                            'op': {
                            'Uyku sorunlaırm var.Günde 3-4 saat anca uyurum.': 0,
                            '8 saat uyur kalkarım.': 1,
                            '8 saat bana yetmez günde en az 12 saat uyumam lazım.': 0,
                            'Gece her haltı yerim asla akıllanmam en erken 14.00-15.00e kadar uyurum' :1
                            }
                        },
                        {
                            'qu': 'İzlediğiniz, okuduğunuz veya yaptığınız bir şeye ne kadar bağlanırsınız?',
                            'op': {
                            'Ne bağlanması maksat zaman geçsin.' :0,
                            'Bağlanma problemlerim var.' :1,
                            'Gerçekten sevdiysem yeterli ilgiyi gösteririm.': 3,
                            'O şeye bütün benliğimi,hayatımı,emeğimi,her şeyimi ortaya koyarım.Onunla yatar onunla kalkarım': 3
                            }
                        },
                        {
                            'qu': 'Hatırlama kabiliyetiniz ne kadar iyi?',
                            'op': {
                            'Ne... neyi hatırlamam gerekiyor' : 3,
                            'Bana yapılan bir davranışı asla unutmam.' :2,
                            'Beynim her şeyi kaydeder.': 5,
                            'Kişiye ve duruma bağlı hatırlamam gerekiyorsa hatırlarım.' :4
                            }
                        },
                        {
                            'qu' :'Yolda gördüğünüz ya da okulunuzdaki insanları seme/uke diye ayırt eder misiniz?',
                            'op': {
                            'İnsanları o şekilde kalıplara sokmam.' :5,
                            'Sadece göz ucuyla bir bakarım.':6,
                            'Dikkatle bakarım bunun üzerie düşünürüm.':5,
                            'Arkadaşlarımı bile o şekilde düşünüp seçerim. Herkes benim gözümde ya uke ya semedir.': 6
                            }
                        }

                    ]

                    toplam_puan = 0
                    for i, s in enumerate(questions):
                        cevap = st.radio(s["qu"], list(s["op"].keys()), key=f"soru_{i}")
                        toplam_puan += s["op"][cevap]

                    if st.button("Sonucu Gör"):
                        if toplam_puan >= 2:
                            st.success("Tebrikler! Başarılı oldun 🎉")
                        else:
                            st.error("Maalesef yeterli değil 😢")

    except ValueError:
        st.error("Lütfen sadece sayı gir!")




