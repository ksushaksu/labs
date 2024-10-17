# TODO Найдите количество книг, которое можно разместить на дискете

info_of_disk = 1.44

pages_count = 100
number_of_line_per_page = 50
symb_count_in_line = 25
one_symb_in_bytes = 4

book_size = (one_symb_in_bytes * symb_count_in_line * number_of_line_per_page * pages_count) / (2 ** 20)

count_books = info_of_disk / book_size

print("Количество книг, помещающихся на дискету:", round(count_books))
