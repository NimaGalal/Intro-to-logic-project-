from aima.logic import *
from aima.utils import *

people = ['Mummy','Daddy', 'Peter', 'Betty', 'AuntPolly']
desserts = ['Marmalade','Marshmallows', 'NapoleonCake', 'IceCream', 'Waffles']
dreams = ['Paris','SeaTrip', 'SwanLake','CoinAlbum']

# Initialize the First-Order Logic Knowledge Base
kb = FolKB()

# Explicit Facts

# 1. Mummy attends yoga classes on Mondays and Thursdays
kb.tell(expr("AttendsYoga(Mummy, Monday)"))
kb.tell(expr("AttendsYoga(Mummy, Thursday)"))

# 2. A person loving ice cream dreams of visiting Paris.
kb.tell(expr("Likes(x,IceCream) ==> DreamOf(x,Paris)"))

# 3. Betty likes only marmalade
kb.tell(expr("Likes(Betty, Marmalade)"))
for dessert in desserts:
    if dessert != "Marmalade":
        kb.tell(Expr("not", expr("Likes(" + "Betty" + ", " + dessert + ")")))

kb.tell(Expr("not", expr("Likes(Peter, Marmalade)")))
kb.tell(Expr("not", expr("Likes(Daddy, Marmalade)")))
kb.tell(Expr("not", expr("Likes(AuntPolly, Marmalade)")))

# 4. Mummy eats only marshmallows
kb.tell(expr("Eats(Mummy, Marshmallows)"))
kb.tell(expr("Eats(Mummy, Marshmallows) ==> Likes(Mummy, Marshmallows)"))
for dessert in desserts:
    if dessert != "Marshmallows":
        kb.tell(Expr("not", expr("Likes(" + "Mummy" + ", " + dessert + ")")))

kb.tell(Expr("not", expr("Likes(Peter, Marshmallows)")))
kb.tell(Expr("not", expr("Likes(Daddy, Marshmallows)")))
kb.tell(Expr("not", expr("Likes(AuntPolly, Marshmallows)")))

# 5. The Potters have money boxes for their dreams
kb.tell(expr("MoneyBox(SeaTrip)"))
kb.tell(expr("MoneyBox(SwanLake)"))
kb.tell(expr("MoneyBox(CoinAlbum)"))

# 6. Aunt Polly has a sewing machine and a collection of sewing materials at home.
# She made a ballet suit for Betty for her classes.

# Aunt Polly has sewing tools
kb.tell(expr("Has(AuntPolly, SewingTools)"))

# Aunt Polly sews
kb.tell(expr("Has(x, SewingTools) ==> Hobby(x, Sewing)"))

# Aunt Polly made a ballet suit for Betty
kb.tell(expr("Made(AuntPolly, BalletSuit, Betty)"))

# Betty attends ballet classes
kb.tell(expr("Attends(Betty, Ballet)"))
kb.tell(expr("Attends(x, Ballet) ==> Dreams(x,SwanLake)"))


# 7. Peter often goes fishing with his dad, but he quickly becomes bored of it and begins to
# walk down the shore looking for rare coins for his collection.

# Peter goes fishing with his dad
kb.tell(expr("GoesFishing(Peter, Daddy)"))

# Peter looks for rare coins
kb.tell(expr("Collects(Peter, RareCoins)"))

# Peter has a coin collection
kb.tell(expr("Hobby(Peter, CollectingCoins)"))
kb.tell(expr("Hobby(x, CollectingCoins) ==> Dreams(x, CoinAlbum)"))

# 8. Peter dislikes cream
kb.tell(Expr("not", expr("Likes(Peter, NapoleonCake)")))
kb.tell(Expr("not", expr("Likes(Peter, IceCream)")))
kb.tell(expr("Likes(Peter, Waffles)"))

# 9. Peter and Betty’s parents have made the same New Year wish both.
kb.tell(expr("Dreams(Daddy, x) ==> Dreams(Mummy, x)"))
kb.tell(expr("Dreams(Mummy, x) ==> Dreams(Daddy, x)"))


# 10. Mummy prepares the family’s favorite desserts: Napoleon cake, marmalade, and waffles.
kb.tell(expr("Prepares(Mummy, NapoleonCake)"))
kb.tell(expr("Prepares(Mummy, Marmalade)"))
kb.tell(expr("Prepares(Mummy, Waffles)"))


# Desserts prepared on holidays
kb.tell(expr("Dessert(NapoleonCake)"))
kb.tell(expr("Dessert(Marmalade)"))
kb.tell(expr("Dessert(Waffles)"))

# Clarifying the parent relationship for peter and betty
kb.tell(expr("Parent(Daddy, Peter)"))
kb.tell(expr("Parent(Mummy, Peter)"))
kb.tell(expr("Parent(Daddy, Betty)"))
kb.tell(expr("Parent(Mummy, Betty)"))

unassigned_desserts = []

for dessert in desserts:
    if not list(fol_fc_ask(kb, expr(f"Likes(x, {dessert})"))):
        unassigned_desserts.append(dessert)

i = 0
for person in people:
    if not list(fol_fc_ask(kb, expr(f"Likes({person}, x)"))):
        kb.tell((expr(f"Likes({person}, {unassigned_desserts[i]})")))
        i += 1

unassigned_dreams = []

for dream in dreams:
    if not list(fol_fc_ask(kb, expr(f"Dreams(x, {dream})"))):
        unassigned_dreams.append(dream)

i = 0
for person in people:
    for dream in unassigned_dreams:
        if not list(fol_fc_ask(kb, expr(f"Dreams({person}, x)"))):
            if dream == "Paris" and not list(fol_fc_ask(kb, expr(f"Likes({person}, IceCream)"))):
                continue
            kb.tell((expr(f"Dreams({person}, {dream})")))
            break

print(list(fol_fc_ask(kb, expr("Likes(x, NapoleonCake)"))))
print(list(fol_fc_ask(kb, expr("Dreams(x, Paris)"))))