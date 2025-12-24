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
