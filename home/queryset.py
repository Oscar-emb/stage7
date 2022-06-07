from home.models import People

# Adding a new entry to a list of records
user = People(name="Oscarss")
user.save()

# Getting all the entries in our list of records
all_users = People.objects.all()
print(all_users)  

# Getting the items by primary key
key = People.objects.get(pk=1)
print(key)

# Getting the entry by name
contents = People.objects.get(name = "Oscarss")
print(contents)

# Changing an entry's value in a database
contents.name = "Jeremiah"
contents.save()

