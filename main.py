from aima.logic import *

print("="*80)
print("Potter Family Puzzle Analysis")
print("="*80)

people = ['Mummy','Daddy', 'Peter', 'Betty', 'AuntPolly']
desserts = ['Marmalade','Marshmallows', 'Napoleon', 'IceCream', 'Waffles']
dreams = ['Paris','Sea', 'SwanLake','CoinCollection']

print("\n People in the puzzle (Constants) ")
for person in people:
    print(f"  • {person}")

print("\n Desserts (5 total) ")
for dessert in desserts:
    print(f"  • {dessert}")

print("\n- Dreams (4 total) -")
for dream in dreams:
    print(f"  • {dream}")

print("\n" + "="*80)
print(" Puzzle Conditions Analysis ")
print("="*80)

print("\nCondition 1 ")
print("Text: Mummy Potter attends yoga classes on Mondays and Thursdays")
print("Type: Direct Fact")
print("FOL: Attends(Mummy,Yoga,Monday)")
print("FOL: Attends(Mummy,Yoga,Thursday)")

print("\n Condition 2 ")
print("Text: A person loving ice cream dreams of visiting Paris")
print("Type: Inference Rule")
print("FOL: Likes(x,IceCream)--> Dreams(x, Paris)")

print("\nCondition 3 ")
print("Text:Betty likes only marmalade")
print("Type: Direct Fact")
print("FOL:Likes(Betty,Marmalade)")

print("\nCondititon 4 ")
print("Text: Mummy eats only marshmallows")
print("Type:Direct Fact")
print("FOL: Likes(Mummy, Marshmallows)")

print("\nCondition 5 ")
print("Text: Three money boxes for dreams")
print("Type: Direct Fact")
print("FOL:HasMoneyBox(PotterFamily,TripToSea)")
print("FOL: HasMoneyBox(PotterFamily, SwanLakeBallet)")
print("FOL: HasMoneyBox(PotterFamily,CoinAlbum)")

print("\nCondtion 6 ")
print("Text: Aunt Polly has sewing materials and made ballet suit for Betty")
print("Type: Direct Fact + Deduction")
print("FOL: HasHobby(AuntPolly, Sewing)")
print("FOL: Attends(Betty,BalletClasses)")
print("FOL: Dreams(Betty, SwanLake) [Deduced]")

print("\nCondition 7")
print("Text: Peter goes fishing with dad and collects rare coins")
print("Type: Direct Fact + Deduction")
print("FOL: HasHobby(Peter, CoinCollecting)")
print("FOL: Dreams(Peter,CoinCollection) [Deduced]")

print("\n Condition 8")
print("Text: Peter doesn't like anything with cream")
print("Type: Direct Fact (Negative)")
print("FOL: ~Likes(Peter,Napoleon)")
print("FOL: ~Likes(Peter, IceCream)")

print("\nCondition 9 ")
print("Text: Peter and Betty's parents made the same New Year wish")
print("Type: Inference Rule")
print("FOL: Dreams(Mummy, x) --> Dreams(Daddy, x)")

print("\nCondition 10 ")
print("Text: Mummy prepares Napoleon cake,marmalade,and waffles")
print("Type: Direct Fact")
print("FOL: Prepares(Mummy, Napoleon)")
print("FOL: Prepares(Mummy, Marmalade)")
print("FOL: Prepares(Mummy,Waffles)")

print("\n" + "="*80)
print("Logical deduction")
print("="*80)

print("\nStep 1: Assign Dreams ")
print("1. Betty does ballet -> Dreams(Betty, SwanLake)")
print("2. Peter collects coins -> Dreams(Peter, CoinCollection)")
print("3. Parents share same dream -> Both dream of Sea")
print("4. AuntPolly likes ice cream -> Dreams(AuntPolly, Paris)")

print("\nStep 2: Assign Desserts ")
print("1. Betty likes Marmalade (given)")
print("2. Mummy likes Marshmallows (given)")
print("3. Peter doesn't like cream -> Peter likes Waffles")
print("4. AuntPolly dreams of Paris -> AuntPolly likes IceCream")
print("5. Daddy gets the remaining -> Daddy likes Napoleon")

print("\n" + "="*80)
print("Fnal solution")
print("="*80)

print("\n{:<12} {:<15} {:<20}".format("Person","Dessert", "Dream"))
print("-" * 50)
print("{:<12} {:<15} {:<20}".format("Mummy","Marshmallows", "Sea"))
print("{:<12} {:<15} {:<20}".format("Daddy", "Napoleon", "Sea"))
print("{:<12} {:<15} {:<20}".format("Peter", "Waffles", "CoinCollection"))
print("{:<12} {:<15} {:<20}".format("Betty", "Marmalade", "SwanLake"))
print("{:<12} {:<15} {:<20}".format("AuntPolly","IceCream", "Paris"))

print("\n" + "="*80)
print("Answers to the questions in the puzzle : ")
print("="*80)
print("\n Question 1: Who likes the Napoleon cake?")
print("Answer: Daddy")
print("\nQuestion 2: Who dreams of going to Paris?")
print("Answer: AuntPolly")


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