from home.models import People, Product

# Adding a new entry to a list of records
user = Product(brand="Toyota", price = "$50,000")
user.save()

# Getting all the entries in our list of records
all_products = Product.objects.all()
print(all_products)  

# Getting the items by primary key
key = Product.objects.get(pk=1)
print(key)

# Getting the entry by name
contents = Product.objects.get(brand = "Toyota")
print(contents)

# Changing an entry's value in a database
contents.price = "$200,000"
contents.save()

