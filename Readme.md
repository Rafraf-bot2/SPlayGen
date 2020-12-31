# Spotify PlayGen
Un générateur de **playlist spotify** qui vous concocte une **playlist** sur-mesure !
L'application analyse vos écoutes, détermine les artistes que vous avez **le plus écouté** durant les 4 dernières semaines, et vous créé une playlist contenant 5 sons aléatoire de chacun de ces artiste ! (Et en prime il génère **topArtist.txt** dans lequel est repertorié vos artistes les plus streamés)

Pour faire fonctionner le script il faut :
* Installer le module **spotipy** : ```pip install spotipy```
* Se faire un compte développeur Spotify
* Créer une app spotify 
* Paramétrer l'app de sorte a ce qu'elle ai un URI de redirection
* Récuperer le Client ID et le Client Secret
* Définir les variables d'environement :
   * SPOTIPY_CLIENT_SECRET
   * SPOTIPY_CLIENT_ID
   * SPOTIPY_REDIRECT_URI
* Mettre votre nom d'utilisateur dans **username.txt**

