from re import T
import requests
from bs4 import BeautifulSoup
from pystyle import Colorate, Colors, System, Center, Write, Anime
import os
import time

crackers = """
 ██████ ██████   █████   ██████ ██   ██ ███████ ██████  ███████ 
██      ██   ██ ██   ██ ██      ██  ██  ██      ██   ██ ██      
██      ██████  ███████ ██      █████   █████   ██████  ███████ 
██      ██   ██ ██   ██ ██      ██  ██  ██      ██   ██      ██ 
 ██████ ██   ██ ██   ██  ██████ ██   ██ ███████ ██   ██ ███████
"""

banner = """

                 _____                                             
              .-" .-. "-.                                          
            _/ '=(0.0)=' \_                                        
          /`   .='|m|'=.   `\                                      
          \________________ /                                      
      .--.__///`'-,__~\\\\~`    READY TO SEARCH           
     / /6|__\// a (__)-\\\\      YOUR CRACK !?!?!?!
     \ \/--`((   ._\   ,)))                                        
     /  \\  ))\  -==-  (O)(                                        
    /    )\((((\   .  /)))))                                       
   /  _.' /  __(`~~~~`)__                                          
  //"\\,-'-"`   `~~~~\\~~`"-.                                      
 //  /`"              `      `\                                    
//"""


System.Clear()
System.Size(160, 50)
System.Title("Crackers")

Anime.Fade(Center.Center(banner), Colors.green_to_red,
           Colorate.Diagonal, enter=True)

def imgascii():
    System.Clear()
    print("\n"*2)
    print(Colorate.Diagonal(Colors.green_to_red, Center.XCenter(crackers)))
    print("\n"*5)

def tcrack():
    
    imgascii()
    folder = os.path.isdir('save')

    if str(folder) == 'False':
        os.system('mkdir save')
    elif str(folder) == 'True':
        rien = 0
    
    crack = Write.Input('\nQuelle type de crack veux tu ? (multi ou solo) :',
                    Colors.green_to_red, interval=0.005)

    imgascii()

    if crack == 'multi':
        jeux = Write.Input('Quelle jeux veux-tu en multijoueur ?',
                    Colors.green_to_red, interval=0.005)
        final = ('https://game3rb.com/' + jeux.replace(" ", "-"))
        reponse = requests.get(final)
        validation = (reponse.status_code)
        
        if str(validation) == '200':
            
            requete = requests.get(final)
            page = requete.content
            soup = BeautifulSoup(page, 'lxml')
            for link in soup.find_all("a", {"class": "direct"}):
                lien = (link.get('href'))

            patch = ''

            for patch in soup.find_all("a", {"class": "online"}):
                patch = (patch.get('href'))

            torrent = ''

            for torrent in soup.find_all("a", {"class": "torrent"}):
                torrent = (torrent.get('href'))
            
            savelink = Write.Input('Voulez-vous sauvegarde le lien de telechargement ? (1 = oui/2 = non) :',
                    Colors.green_to_red, interval=0.005)
            
            if savelink == '1':

                imgascii()
                
                fichier = open('save/' + jeux + '.txt', "w")
                fichier.write('Lien direct pour télécharge le jeux: ' + lien)
                if patch == '':
                    rien = 'rien'
                else:
                    fichier.write('\nLien direct pour télécharge le patch multijoueur: ' + patch)
                if torrent == '':
                    rien = '0'
                else:
                    fichier.write('\nLien direct pour le télécharge en torrent: ' + torrent)
                fichier.close()

                Write.Print("Pour retrouve c'est lien sauvegarde vous les trouverés dans le fichier save où se trouve le programme.",
                    Colors.green_to_red, interval=0.005)
                
                acce = Write.Input("\nVoulez-vous y acceder en ecrivant oui le programme vous ouvrira directement l'accés au fichier save au sinon vous pouvez ecrire non.: ",
                    Colors.green_to_red, interval=0.005)

                if acce == 'oui':
                    os.system('start save')
                else:
                    rien = '0'

            else:
                imgascii()

                Write.Print('Lien direct pour télécharge le jeux: ' + lien,
                    Colors.green_to_red, interval=0.005)
                
                if patch == '':
                    rien = 'rien'
                else:
                    Write.Print('\nLien direct pour télécharge le patch multijoueur: ' + patch,
                    Colors.green_to_red, interval=0.005)
                if torrent == '':
                    rien = '0'
                else:
                    Write.Print('\nLien direct pour le télécharge en torrent: ' + torrent,
                    Colors.green_to_red, interval=0.005)
                
                Write.Input('\nQuand vous-aurez finis de copier les liens. Vous avez cas appuyer sur entrée pour fermer le programme',
                    Colors.green_to_red, interval=0.005)

        elif str(validation) == '404':
            Write.Print("Pas de crack de ce jeux trouver.",
                    Colors.green_to_red, interval=0.005)
            time.sleep(1)
            return tcrack()              

    else:
        if crack == 'solo':
            Write.Print('pas encore finis',
                    Colors.green_to_red, interval=0.005)
            time.sleep(1)
            return tcrack()
            
        else:
            Write.Print("Votre réponse n'est pas bonne veuille réessaye.",
                    Colors.red, interval=0.005)
            Write.Print("\nVeuillé réessaye",
                    Colors.red, interval=0.005)
            time.sleep(1)
            return tcrack()

tcrack()
