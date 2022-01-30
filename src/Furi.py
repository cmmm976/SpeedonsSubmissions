import streamlit as st
import streamlit.components.v1 as components
from streamlit_player import st_player

def show_presentation():
    st.title("Notre proposition")

    """
    ## 🎮 Furi, un jeu :
     * **visuel** - un boss rush centré sur l’apprentissage de patterns, la quintessence du jeu d’action exigeant
     * **apprécié** - après un début difficile, s’est écoulé à 700 000 exemplaires (+2,7 millions de téléchargements à travers l’abonnement PS Plus) fin 2020 grâce à son succès d’estime
     * **auditivement orgasmique (oui)** - la bande son cumule plus de 45 millions de vues sur Youtube
    """

    st.video("https://j.gifs.com/qQLZ80.mp4")

    """
    ## 🏃 Speedrun Mode, une catégorie :
     * **skillée** - très peu de glitches, principalement un très haut niveau de jeu
     * **dense** - autour de 35 minutes RTA, la run n'est ni trop courte ni trop longue
     * **reconnue** - montré à Interglitches, à l’ESA et à la GDQ
    """

    """
    ## 👨🧑🏾🧑🏻 Trois runners :
    
    * **AEtienne** :
      - speedrunner depuis 4 ans et demi, dont 2 ans sur Furi
      - 11ème en mode normal, 3ème en mode difficile
      - vétéran des marathons, dont l'**ESA, Interglitches et Speedons**
      - **commentateur de légende**
    """
    st.image("https://cdn.discordapp.com/attachments/513701275305639947/936905684153434132/Sans_titre_1.jpg")
    """
    * **Evian** :
      - speedrunner depuis 3 ans, dont 1 an sur Furi
      - 10ème en mode normal, 5ème en mode difficile
      - a participé au **BSG, au Stunfest et à Interglitches**
      - **1,2 millions de vues** sur sa chaîne Youtube
    """
    st.image('https://cdn.discordapp.com/attachments/513701275305639947/936910088420077608/Sans_titre_2_cleanup.png')
    
    """
    * **Jeremichto** :
      - speedrunner depuis 1 an
      - 3ème en mode normal, **recordman de France**
      - point faible : trop fort
    """

    """
    ## ⚔️ De belles rivalités :
      - AEtienne a appris Evian à runner le jeu… pour se faire battre par l’élève lors d’une race à Interglitches. 
        Le maître réussira-t-il à prendre sa revanche ou le jeune Padawan achèvera-t-il de prendre son envol ?
    """
    st.image("https://cdn.discordapp.com/attachments/931247875776729202/937288570669006898/wholesome_cleanup.png")

def show_intro():
    st.title("Merci d’avoir cliqué sur ce lien 😊")
    """Salut les reviewers ! 👋"""
    """Vous recherchez une run qui permettra à Speedons 2 d’élargir son public et de lui en mettre plein la vue pour récolter un maximum de dons pour Médecins du Monde ?"""
     
    """Vous lisez la bonne candidature !"""
     
    """👈 Utilisez le menu pour découvrir la run et ses trois runners."""

    st.image('https://j.gifs.com/57KRnA.gif')


def show_VODs():
    st.subheader("Evian et AEtienne à Interglitches 👀")
    st_player("https://www.youtube.com/watch?v=665ol_aRo84")

    st.subheader("Si vous en voulez encore... 👇")
    
    with st.expander("Furi [Speedrun Mode (Furier)] par AEtienne à l'ESASummerOnline"):
        st_player("https://www.youtube.com/watch?v=hzF0lJEmaI0")

    with st.expander("Furi [Speedrun Mode] par AEtienne à l'ESAWinter20"):
        st_player("https://www.youtube.com/watch?v=3hHiDANADg4")

    with st.expander("Furi [Speedrun Mode] par Evian et Jeremichto à The Octogone Saison 1"):
        st_player("https://youtu.be/zOh6Cs0-m6Y?t=698")

    with st.expander("Furi [Speedrun Mode] par Evian à l'ODJV 2021"):
        st_player("https://www.twitch.tv/videos/1041171873?t=00h05m56s")

def show_doc():
    st.subheader("Le combo 7-8")
    components.html("""<iframe src="https://streamable.com/e/co7udx?loop=0" width="560" height="315" frameborder="0" allowfullscreen></iframe>""",height=315)
    st.write("La manière la plus rapide de vaincre la plupart des bosses au corps à corps.")

    st.subheader("Boss stunlock")
    components.html("""<iframe src="https://streamable.com/e/fiv244?loop=0" width="560" height="315" frameborder="0" allowfullscreen></iframe>""",height=315)
    st.write("En annulant le recul du pistolet par un enchaînement de dashs, on peut stunlock La Sangle à l'infini.")

    st.subheader("The best sniper in the world")
    components.html("""<iframe src="https://streamable.com/e/x88050?loop=0" width="560" height="315" frameborder="0" allowfullscreen></iframe>""",height=315)
    st.write("On peut gagner beaucoup de temps en tirant juste après avoir cassé le dernier panneau de La Ligne (très dur 😤)")

    st.subheader("Hmmm... You okay dude ?")
    components.html("""<iframe src="https://streamable.com/e/i8yn5x?loop=0" width="560" height="315" frameborder="0" allowfullscreen></iframe>""",height=315)
    st.write("On peut casser l'IA de La Main en se plaçant correctement face à lui.")

    st.subheader("Le boss le plus technique")
    components.html("""<iframe src="https://streamable.com/e/8ookt2?loop=0" width="560" height="315" frameborder="0" allowfullscreen></iframe>""",height=315)
    st.write("Il faut alterner entre tirs normaux et tirs chargés pour maximiser les dégâts durant sa 2ème phase.")

    components.html("""<iframe src="https://streamable.com/e/xbdiui?loop=0" width="560" height="315" frameborder="0" allowfullscreen></iframe>""",height=315)
    st.write("8 tirs chargés très précis tout en évitant les vagues pour ne voir qu'une seule attaque de sa 3ème phase.")

    components.html("""<iframe src="https://streamable.com/e/xh9y1t?loop=0" width="560" height="315" frameborder="0" allowfullscreen></iframe>""",height=315)
    st.write("Attaquer immédiatement après avoir cassé son pilier de protection pour skipper une cinématique.")

    st.subheader("Now you're mine")
    components.html("""<iframe src="https://streamable.com/e/ueyk7s?loop=0" width="560" height="315" frameborder="0" allowfullscreen></iframe>""",height=315)
    st.write("Dasher à un timing extrêmement précis pour toucher l'Eclat pendant qu'elle est invisible dans ses trois premières phases (dur 😤)")

    st.subheader("Damage boost")
    components.html("""<iframe src="https://streamable.com/e/aef6lo?loop=0" width="560" height="315" frameborder="0" allowfullscreen></iframe>""",height=315)
    st.write("Tanker la vague pour enchaîner deux combos et battre La Pointe plus vite (trop souvent run-killer 😒)")

    st.subheader("That's a lot of damage !")
    components.html("""<iframe src="https://streamable.com/e/4v58zw?loop=0" width="560" height="315" frameborder="0" allowfullscreen></iframe>""",height=315)
    st.write("Coller les mains de l'Etoile lors de sa phase 4 pour lui infliger 1 dégâts par frame et la skipper omplètement.")





PAGES = ["Intro","Présentation","GIFs cools","VODs commentées"]
st.sidebar.title('Menu :bulb:')
choix_page = st.sidebar.radio(label="", options=PAGES)

if choix_page == "Intro":
    show_intro()
elif choix_page == "Présentation":
    show_presentation()
elif choix_page == "VODs commentées":
    show_VODs()
elif choix_page == "GIFs cools":
    show_doc()