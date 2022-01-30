import streamlit as st
import streamlit.components.v1 as components
from streamlit_player import st_player

def show_presentation():
    st.title("Notre proposition")

    """
    ## 🎮 Dead Cells, un jeu :
     * **jouissif** - le contrôle du personnage et l'utilisation des armes ont été spécialement conçus pour donner un plaisir imémdiat aux joueurs
     * **populaire** - Plus de 5 millions de ventes et un incroyable succès critique (Meilleur jeu d'action 2018)
    """

    components.html("""<iframe src="https://streamable.com/e/i7lykp?loop=0" width="560" height="315" frameborder="0" allowfullscreen></iframe>""",height=315)

    """
    ## 🏃 Fresh File, une catégorie :
     * **palpitante** - de part la nature aléatoire du jeu, les retournements de situations lors d'une race peuvent être nombreux
     * **intense** - autour de 18 minutes RTA, la run est très dense et ne laisse pas le public s'ennuyer
     * **reconnue** - montrée au Stunfest, à la GDQ et sur IGN
    """

    """
    ## 🧑🏾🧑🏼 Deux runners :
    
    * **Evian** :
      - speedrunner depuis 3 ans, dont 2 ans sur Dead Cells
      - ancien **recordman mondial** dans de multiples catégories, actuellement 3ème en Fresh File
      - a participé au **BSG, au Stunfest et à Interglitches**
      - **1,2 millions de vues** sur sa chaîne Youtube
    """
    st.image('https://cdn.discordapp.com/attachments/513701275305639947/936910088420077608/Sans_titre_2_cleanup.png')
    
    """
    * **Matash** :
      - speedrunner depuis 1 an, dont 3 mois sur Dead Cells
      - **2ème en Fresh File**
      - Etoile montante du speedrun de Dead Cells
    """

    st.image("https://images.everyeye.it/img-articoli/g-t-o-great-teacher-onizuka-recensione-dell-anime-amazon-prime-video-recensione-v4-37844-720x720.jpg")

    """
    ## ⚔️ De l'enjeu :
    Officiellement retraité de Dead Cells, Evian ne le présente plus qu'aux marathons. 
    A-t-il encore le niveau pour être compétitif ou est-il dépassé par la nouvelle génération de runners dont fait partie Matash ?
    """

def show_intro():
    st.title("Merci d’avoir cliqué sur cet autre lien 😊")
    """Salut les reviewers ! 👋"""
    """Vous recherchez une autre run qui permettra à Speedons 2 d’élargir son public et de lui en mettre plein la vue pour récolter un maximum de dons pour Médecins du Monde ?"""
     
    """Vous lisez la bonne candidature !"""
     
    """👈 Utilisez le menu pour découvrir la run et ses deux runners."""

    st.image('https://j.gifs.com/57KRnA.gif')


def show_VODs():
    st.subheader("Evian au Stunfest 👀")
    st_player("https://youtu.be/UZzN0F4hApQ")


def show_doc():
    st.subheader("Assault Boost")
    components.html("""<iframe src="https://streamable.com/e/vzw18k?loop=0" width="560" height="315" frameborder="0" allowfullscreen></iframe>""",height=315)
    st.write("Attaquez avec le bouclier d'assault et faire une roulade juste après pour vous déplacer plus rapidement.")

    st.subheader("Vine Rune Skip")
    components.html("""<iframe src="https://streamable.com/e/qht1f2?loop=0" width="560" height="315" frameborder="0" allowfullscreen></iframe>""",height=315)
    st.write("En sautant au dernier moment tout en attaquant pour gagner de la hauteur, on peut skipper un mini-boss (dur 😤)")

    st.subheader("Ledge climbing animation cancel")
    components.html("""<iframe src="https://streamable.com/e/zx7hrt?loop=0" width="560" height="315" frameborder="0" allowfullscreen></iframe>""",height=315)
    st.write("En attaquant pendant que l'on grimpe sur certaines plateformes et en annulant l'attaque la frame suivante, on peut annuler l'animation d'accrochage (très très très dur 😤). Hypnotisant !")

    st.subheader("Boss skip")
    components.html("""<iframe src="https://streamable.com/e/dlvqfj?loop=0" width="560" height="315" frameborder="0" allowfullscreen></iframe>""",height=315)
    st.write("En utilisant deux fois la compétence Assault près d'un mur, on peut casser la physique du jeu et skipper le dernier boss.")




PAGES = ["Intro","Présentation","GIFs cools","VOD commentée"]
st.sidebar.title('Menu :bulb:')
choix_page = st.sidebar.radio(label="", options=PAGES)

if choix_page == "Intro":
    show_intro()
elif choix_page == "Présentation":
    show_presentation()
elif choix_page == "VOD commentée":
    show_VODs()
elif choix_page == "GIFs cools":
    show_doc()