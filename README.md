                                 Process_Scraping_BookToScrap
----------------------------------------------------------------------------------------------


## Contexte 
La fonction process du fichier Process_Scraping permet d’extraire des données du site http://books.toscrape.com/. 

Sont concernées les informations suivantes : 
- product_page_url
- universal_ product_code (upc)
- title
- price_including_tax
- price_excluding_tax
- number_available
- product_description
- category
- review_rating
- image_url 

Les données sont regroupées par catégorie de livre et écrites dans un fichier .csv
Un fichier Images est également crée avec l'ensemble des images des livres présent sur le site. les images sont nommées par leur titre.  

## Installation 

Tout d'abord, créer un dossier via la commande mkdirv(ici nommé projet2) dans lequel se trouvera l'environnement virtuel et l'ensemble des données extraites. Puis y accéder via la commande cd.

```python
mkdir projet2
cd projet2
```
Déplacer Process_Scraping.py et requierements.txt  dans le dossier 
Ensuite, créer un environnement virtuel dans le dossier (ici nommé env): 

```python
python3 -m venv env
```
Puis activer le via : 

```python
source env/bin/activate #MacOS ou Unix
ou
env/Scripts/activate.bat #Sur Windows
```
Importer les packages nécessaire avec la commande : 

```python 
pip install -r requirements.txt
``` 

## Résultat

Vous pouvez désormais lancer le script ! 
vous devriez obtenir un dossier par catégorie avec le fichier .csv correspondant détenant les datas des livres référencés dans cette catégorie. 
Vous obtenez également un fichier "Images" avec l'ensemble des covers des livres du site, nommé par leur titre.
