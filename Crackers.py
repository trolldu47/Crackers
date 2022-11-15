import requests, time, re, os, tkinter
from bs4 import BeautifulSoup
from pystyle import Colorate, Colors, System, Center, Write, Anime

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

def oui():
    os.system('msg * Starting update')
    app.destroy()
    os.system('start updater.exe')
    
def non():
    app.destroy()
    tcrack() 
    
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)

def imgascii():
    System.Clear()
    print("\n"*2)
    print(Colorate.Diagonal(Colors.green_to_red, Center.XCenter(crackers)))
    print("\n"*5)

def tcrack():
    System.Clear()
    System.Size(160, 50)
    System.Title("Crackers")
    
    Anime.Fade(Center.Center(banner), Colors.green_to_red,
           Colorate.Diagonal, enter=True)
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

            update = ''
            result = ''
            for update in soup.find_all("time", {"class": "entry-date"}):
                update = (update.get('title'))
            update2 = str(update)
            update2, result = update2[:-1], update2[-1]
            update2, result = update2[:-1], update2[-1]
            update2 = update2.replace(":", "")
            update2, result = update2[:-1], update2[-1]
            update2, result = update2[:-1], update2[-1]
            update2 = change_date_format(update2)

            imgascii()
            
            Write.Print("Voici les informations sur le cracks:",
                    Colors.green_to_red, interval=0.005)

            Write.Print("\nDate de la dernire mise à jour du crack: " + str(update2),
                    Colors.green_to_red, interval=0.005)            
            
            savelink = Write.Input('\n\nVoulez-vous sauvegarde le lien de telechargement ? (1 = oui/2 = non) :',
                    Colors.green_to_red, interval=0.005)
            
            if savelink == '1':

                imgascii()
                
                jeux = jeux.replace(" ", "-")
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

                Write.Print("\nPour fermer le programme il vous suffit juste de ferme le bloc-notes",
                    Colors.green_to_red, interval=0.005)               

                repertoire = (jeux + '.txt')
                os.system('start /w save/' + repertoire)

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

fichier = open('version.txt', "r")
test = fichier.read()
fichier.close
    
requete = requests.get("https://github.com/trolldu47/Crackers/blob/main/version.txt")
page = requete.content
soup = BeautifulSoup(page, 'lxml')
link = soup.find("td", {"class": "blob-code blob-code-inner js-file-line"})
test2 = (link.get_text())
    
if test == test2:   
    tcrack()
    
else:
    app = tkinter.Tk()
    app.title("")
    app.geometry('150x100')

    text = tkinter.Label(app, text="Update Crackers ?", font=(40))
    ouib = tkinter.Button(app, text="OUI", bg="green", command=oui)
    nonb = tkinter.Button(app, text="NON", bg="red", command=non)

    text.pack()
    ouib.pack(side="left", ipadx="21")
    nonb.pack(side="right", ipadx="21")
    app.mainloop()

