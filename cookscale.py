recipes = {
    "Biryani": (2, {"Rice": 200, "Chicken": 300, "Onion": 2}),
    "Pulao": (2, {"Rice": 150, "Carrot": 2, "Onion": 1})
}
units = {"Rice": "g", "Chicken": "g", "Onion": "piece", "Carrot": "piece"}
prices = {"Rice": 60, "Chicken": 250, "Onion": 40, "Carrot": 50}
weekly_plan = []
def get_servings(prompt):
    try: n = int(input(prompt))
    except ValueError: n = 0
    if n <= 0: print("Enter positive whole servings!")
    return max(n, 0)
while True:
    print("\n===== COOKSCALE =====")
    print("1.View Recipes  2.Scale Recipe  3.Plan Week")
    print("4.Grocery List  5.Estimate Cost  6.Exit")
    choice = input("Enter choice: ").strip()
    if choice == "1":
        for name, (base, items) in recipes.items():
            print(name, "serves", base, ":", items)
    elif choice == "2":
        name = input("Recipe name: ").strip().title()
        people = get_servings("Required servings: ")
        if name in recipes and people:
            base, items = recipes[name]
            for item, qty in items.items():
                print(item, qty * people / base, units[item])
        else:
            print("Recipe not found or servings invalid!")
    elif choice == "3":
        weekly_plan = []
        for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
            name = input(day + " recipe: ").strip().title()
            people = get_servings("Servings: ")
            if name in recipes and people:
                weekly_plan.append((name, people))
            else:
                print("Invalid entry; day skipped.")
    elif choice in ("4", "5"):
        if not weekly_plan:
            print("Please plan meals first!")
            continue
        grocery = {}
        for name, people in weekly_plan:
            base, items = recipes[name]
            for item, qty in items.items():
                grocery[item] = grocery.get(item, 0) + qty * people / base
        if choice == "4":
            for item, qty in grocery.items():
                print(item, round(qty, 2), units[item])
        else:
            total = sum(qty * prices[item] / (1000 if units[item] == "g" else 1) for item, qty in grocery.items() if item in prices)
            print("Estimated cost: Rs.", round(total, 2))
            for item in grocery:
                if item not in prices: print(item, "- Price unavailable")
    elif choice == "6":
        print("Thank you for using CookScale!")
        break
    else:
        print("Invalid choice! Select 1-6.")
