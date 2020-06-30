# --------------
#Step 1
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Toshua Bengio',]
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class = class_1 + class_2
print(new_class)
new_class.append('Peter warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)
#Step 2
courses = {'Math': 65,'English': 70,'History': 80,'French': 70,'Science': 60}
values = courses.values()
total = sum(values)
print(total)
percentage = {"Geoffrey Hinton":total/500*100} 
print(percentage)
#Step 3
mathematics = {'Geoffrey Hinton': 78, 'Andrew Ng':95, 'Sebastian Raschka':65, 'Toshua Bengio':50, 'Hilary Mason': 70,'Corinna Cortes':66, 'Peter warden':75}
print(mathematics)
topper = max(mathematics,key = mathematics.get)
print(topper)

last_name = topper.split()[1]
first_name = topper.split()[0]
full_name = last_name + " " + first_name
certificate_name = full_name.upper()
print(certificate_name)



