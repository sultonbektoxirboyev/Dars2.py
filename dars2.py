 class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Band" if self.is_borrowed else "Mavjud"
        return f"{self.title} - {self.author} ({status})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"'{title}' kitobi qo‘shildi.")

    def show_books(self):
        if not self.books:
            print("Kutubxonada kitob yo‘q.")
        else:
            print("\n📚 Kitoblar ro‘yxati:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"Siz '{title}' kitobini oldingiz.")
                else:
                    print("Bu kitob allaqachon band.")
                return
        print("Bunday kitob topilmadi.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"Siz '{title}' kitobini qaytardingiz.")
                else:
                    print("Bu kitob olinmagan.")
                return
        print("Bunday kitob topilmadi.")


#Dastur ishlashi 
library = Library()

while True:
    print("\n1. Kitob qo‘shish")
    print("2. Kitoblarni ko‘rish")
    print("3. Kitob olish")
    print("4. Kitob qaytarish")
    print("5. Chiqish")

    choice = input("Tanlang: ")

    if choice == "1":
        title = input("Kitob nomi: ")
        author = input("Muallif: ")
        library.add_book(title, author)

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        title = input("Qaysi kitobni olmoqchisiz: ")
        library.borrow_book(title)

    elif choice == "4":
        title = input("Qaysi kitobni qaytarmoqchisiz: ")
        library.return_book(title)

    elif choice == "5":
        print("Dastur tugadi.")
        break

    else:
        print("Noto‘g‘ri tanlov!")



   ---2-o'yin vaqtli---

import random
import time


class GuessGame:
    def __init__(self, min_num=1, max_num=100, time_limit=30):
        self.min_num = min_num
        self.max_num = max_num
        self.secret_number = random.randint(min_num, max_num)
        self.attempts = 0
        self.time_limit = time_limit

    def check_guess(self, guess):
        self.attempts += 1

        if guess < self.secret_number:
            return "Kattaroq son kiriting 📈"
        elif guess > self.secret_number:
            return "Kichikroq son kiriting 📉"
        else:
            return "To‘g‘ri topdingiz 🎉"

    def play(self):
        print(f"\nMen {self.min_num} dan {self.max_num} gacha son o‘yladim.")
        print(f"Sizda {self.time_limit} soniya vaqt bor ⏱")

        start_time = time.time()

        while True:
            # vaqtni tekshirish
            current_time = time.time()
            if current_time - start_time > self.time_limit:
                print("\n⏰ Vaqt tugadi!")
                print(f"To‘g‘ri javob: {self.secret_number}")
                break

            try:
                guess = int(input("Taxminingiz: "))
                result = self.check_guess(guess)
                print(result)

                if guess == self.secret_number:
                    print(f"Urinishlar soni: {self.attempts}")
                    break

            except ValueError:
                print("Iltimos, faqat son kiriting!")


# --- O‘yin boshlash ---
game = GuessGame(time_limit=30)
game.play()

