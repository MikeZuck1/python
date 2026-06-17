def product():
  name = "pen"
  price = 2.5
  quantity = 100
  return name, price, quantity
name, price, quantity = product()
print(f"Le produit {name} coûte {price}€ et il en reste {quantity} en stock.")
