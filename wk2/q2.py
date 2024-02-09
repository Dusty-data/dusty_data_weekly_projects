
import json

# Create a dictionary to store the film collection


film_collection = {}

# Add a new film
def add_film():
    film_name = input("Enter the film name: ")
    director = input("Enter the director: ")
    release_year = input("Enter the release year: ")
    genre = input("Enter the genre: ")

    film = {
        'Film Name': film_name,
        'Director': director,
        'Release Year': release_year,
        'Genre': genre
    }

    film_collection[film_name] = film
    print(f"{film_name} added to the collection.")

# Edit a film
def edit_film(film_name):
    if film_name in film_collection:
        print(f"Editing {film_name}...")
        new_data = {}
        new_data['Film Name'] = input(f"New film name ({film_collection[film_name]['Film Name']}): ")
        new_data['Director'] = input(f"New director ({film_collection[film_name]['Director']}): ")
        new_data['Release Year'] = input(f"New release year ({film_collection[film_name]['Release Year']}): ")
        new_data['Genre'] = input(f"New genre ({film_collection[film_name]['Genre']}): ")

        film_collection[film_name] = new_data
        print(f"{film_name} updated.")
    else:
        print(f"{film_name} not found in the collection.")

# Delete a film
def delete_film(film_name):
    if film_name in film_collection:
        del film_collection[film_name]
        print(f"{film_name} deleted from the collection.")
    else:
        print(f"{film_name} not found in the collection.")

# View the collection
def view_collection():
    print("\nFilm Collection:")
    for film_name, data in film_collection.items():
        print(f"Film Name: {data['Film Name']}")
        print(f"Director: {data['Director']}")
        print(f"Release Year: {data['Release Year']}")
        print(f"Genre: {data['Genre']}")
        print("-" * 30)



# Function to load data
def load_data():
    try:
        with open("film_library.json", "r") as file:
            film_collection.update(json.load(file))
    except FileNotFoundError:
        pass

# Function to save data
def save_data():
    with open("film_library.json", "w") as file:
        json.dump(film_collection, file)


while True:
    print("\nFilm Collection Management")
    print("1. Add Film")
    print("2. Edit Film")
    print("3. Delete Film")
    print("4. View Collection")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_film()
        
    elif choice == '2':
        film_name = input("Enter the film name to edit: ")
        edit_film(film_name)
       
    elif choice == '3':
        film_name = input("Enter the film name to delete: ")
        delete_film(film_name)
        
    elif choice == '4':
        
        # Load the saved film collection
        load_data() 
        view_collection()
        
    elif choice == '5':
        # Save the film collection when exiting the program
        save_data()
        print("Exiting the program...")
        break
    else:
        print("Invalid option! Please try again.")

