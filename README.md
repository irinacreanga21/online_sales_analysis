
# online_sales_analysis
#Acest proiect este un exercițiu practic pentru lucrul cu Python și Git
Am creat:

product.py – clasa Product cu atributele name, price, quantity, plus metode pentru afișare și actualizarea cantității.
product_manager.py – clasa ProductManager cu o listă de produse, metode pentru adăugare, afișare și calculul valorii totale a inventarului.
main.py – unde creez un ProductManager, adaug câteva produse, afișez produsele și valoarea totală.

Am folosit Git:

Am făcut primul commit cu funcționalitatea de bază.
Am creat ramura add-product-removal și am adăugat o metodă în ProductManager pentru ștergerea produselor după nume, apoi am făcut commit și merge în ramura principală.


Am creat ramura add-cart-functionality.
Am creat cart.py cu clasa Cart (listă de produse în coș, metode pentru adăugare, afișare și calculul valorii totale).
În main.py am creat un Cart, am adăugat câteva produse în coș din ProductManager și am afișat conținutul și valoarea totală.
Am făcut commit pe această ramură.

Am exersat conflicte și merge:

Pe ramura principală am modificat produse în main.py și am șters afișarea inventarului.
Am făcut merge cu add-cart-functionality și am rezolvat conflictele în main.py.

Am configurat .gitignore:

Am creat config.json cu date de test
Am adăugat în .gitignore ca Git să ignore config.json