import json

class Bookcollection: # class ek blue print hota hai object ko creat karne ka object k andar data hota he ya method hota hai
    """A class to manage a collection of books, allowing users to store and organize their reading materials """

    def __init__(self):
        """Initialize a new book collection with an empty list and set up file storage """
        self.book_list=[]
        self.storage_file= "books_data_json"
        self.read_from_file()

    def read_from_file(self):
        """Load saved books from a json file into memory.
        if the file dosen't exist or is corrupted, start with an empty collection."""

        try:
            with open(self.storage_file, "r") as file:
                self.book_list=json.load(file) # hold kra empty list ko
        except (FileNotFoundError,json.JSONDecodeError):
            self.book_list=[]

    def save_to_file(self):
        """ Store the current book collection to a JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent= 4 )

    def create_new_book(self):
        """Add a new book to the collection by gathering information from the user. """
        book_title = input("Enter a book title: ")
        book_author = input("Enter author: ")
        publicaton_year = input("Enter publication year: ")
        book_genre = input("Enter genre: ")
        is_book_read = input("Have you read this book? (yes/no): ").strip().lower()


        new_book={
            "title"   : book_title,
            "author"  : book_author,
            "year"    : publicaton_year,
            "genre"   : book_genre,
            "read"    : is_book_read,
        }
        self.book_list.append(new_book)
        self.save_to_file()
        print("Book aded successfully!\n")

    def delete_book(self):
     """Remove a book from the collection using its title. """
     book_title = input("Enter the title of book you want to remove: ")

     for book in self.book_list:
         if book["title"].lower() == book_title.lower():
             self.book_list.remove(book)
             self.save_to_file()
             print("Book removed successfully!\n")
             return

     print("Book not found! \n")


    def find_book(self):
        """Search for books in collection by title or author name."""
        search_type =input("Search by:\n1. Title\n2.Author\nEnter your choice: ")
        search_text =input("Enter search term: ").lower()

        found_books = [
          book
          for book in self.book_list
          if search_text in book["title"].lower()
          or search_text in book["author"].lower()
      ]

        if found_books:
         print("Matching books:" )
         for index, book in enumerate(found_books,1):
            reading_status= "Read" if book["read"] else "Unread"
            print(f"{index}.{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}\n")

        else:
         print("No matching books found\n")

    def update_book(self):
     """Modify the detail of an existing book in the collection. """
     book_title= input("Enter the title of the book you want to edit: ")
     for book in self.book_list:
       if book["title"].lower() == book_title.lower():
          print("Leave blank to keep existing value.")
          book["title"] = input (f"New title ({book['title']}):  ") or book['title']

          book["author"] = (
             input(f"New author ({book['author']}): ") or book ["author"]
          )

          book["year"]= input(f"New year ({book['year']}): ") or book["year"]
          book["genre"]= input(f"New genre ({book['genre']}): ") or book["genre"]
          book["read"]=( input("Have you read this book? (yes/no)") .strip() .lower() == "yes")
          self.save_to_file()
          print("Book updated successfully ")

          return
    print("Book not found \n")

    def show_all_books(self):
       """Display all books in the collection with their details."""
       if not self.book_list:
          print("Your collection is empty.\n")
          return
       
       print("Your book collection:  ")

       for index, book in enumerate(self.book_list,1):
          reading_status = "Read" if book["read"] else "Unread"
          print(f"{index}. {book['title']} by {book['author']} - {book['year']} - {book['genre']} - {reading_status}")
       print()

    def show_reading_progress(self):
       """Calculate and display statistics about your reading progress."""
       total_books = len(self.book_list)
       completed_books = sum(1 for book in self.book_list if book['is_read'])
       compltion_rate=(
          (completed_books / total_books * 100) if total_books> 0 else 0
       )

       print(f"Total books is collection: {total_books}")
       print(f"Reading progress: {compltion_rate: .2f}%\n")

    def start_application(self):
     """Run the main application loop with a user _friendly menu interface. """

     while True:

        print("📚 Welcome to your Book Collection Manager!📚\n")
        print("1.Add a new book")
        print("2. Remove a book")
        print("3. Search a book")
        print("4. Update book details")
        print("5. View all books")
        print("6. Vies reading progress")
        print("7. Exit")
        try:
              
            user_choice= int(input("Please choose an option (1-7): "))

            if user_choice == 1:
              self.create_new_book()

            elif user_choice == 2:
                 self.delete_book()

            elif user_choice == 3:
                  self.find_book()

            elif user_choice == 4:
                 self.update_book()

            elif user_choice == 5:
                self.show_all_books()

            elif user_choice == 6:
                 self.show_reading_progress()

            elif user_choice == 7:
                 self.save_to_file()
                 print("Thankyou for using Book collection Manager. Goodbye!")
                 break
        except  ValueError:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
   book_manager= Bookcollection()
   book_manager.start_application()                     

             





                 





