import book_module_act816
book_module_act816.favorite_book("Alice in Wonderland")

from book_module_act816 import favorite_book
favorite_book("Alice in Wonderland")

from book_module_act816 import favorite_book as fb
fb("Alice in Wonderland")

import book_module_act816 as bm
bm.favorite_book("Alice in Wonderland")

from book_module_act816 import *
favorite_book("Alice in Wonderland")