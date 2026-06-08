⁡⁢⁣⁢# --------------------------------------------------------------------------------------------------------------------------------- #
#                          ​‌‌‌ 𝙎𝙞𝙢𝙥𝙡𝙚 𝙙𝙖𝙩𝙖 𝙩𝙮𝙥𝙚𝙨     ​​                                                                                  #
# --------------------------------------------------------------------------------------------------------------------------------- #⁡
    ⁡⁢⁢⁢# --------------------------------- ​‌‍‌𝙄𝙣𝙩𝙚𝙧𝙜𝙚𝙧​ ------------------------------------------------------------=============------- #⁡⁡
    ⁡⁢⁢⁢# An int type variable is used to represent the nuber without floating point                                                    #
    #                                                                                                                               #
    # Ex: 1, 2, 3;                                                                                                                  #
    #                                                                                                                               #
    # -----------------------------------------------------------------------------------------------=============----------------- #⁡
    ⁡⁣⁣⁢# --------------------------------- ​‌‍‌𝙛𝙡𝙤𝙖𝙩​ -----------------------------------------------==============------------------------#
    # A float type variable is used to represent the nuber with floating point (better precision)
    #
    # Ex: 1.0, 2.0, 3.0;
    #
    # -------------------------------------------------------------------------===============--------------------------------------#⁡
    ⁡⁣⁣⁡⁢⁣⁣# --------------------------------- ​‌‍‌𝙎𝙩𝙧𝙞𝙣𝙜​ ----------------------------------------------------------------------------------- #
    # A string type variable is used to represent an array of characters (used for text)
    #  always between ' or "
    #
    # Ex: "Hello world";
    #
    # ----------------------------------------------------------------------------------------------------------------------------- #⁡
    ⁡⁣⁣⁡⁢⁣⁡⁣⁢⁣# --------------------------------- ​‌‍‌𝘽𝙤𝙤𝙡𝙚𝙖𝙣​ --------------------------------------------------------------------------------- #
    # A bool type variable is used to represent the truth value of something, it can be False or True (0 or 1)
    #  
    #
    # Ex: False, True;
    #
    # ------------------------------------------------------------------------------------------------------------------------------ #⁡
⁡⁢⁣⁢# ---------------------------------------------------------------------------------------------------------------------------------- #
#                               ​‌‌‌ ‍𝙂𝙧𝙤𝙪𝙥 𝙙𝙖𝙩𝙖 𝙩𝙮𝙥𝙚𝙨​  ​​                    #
# ---------------------------------------------------------------------------------------------------------------------------------- #
    ⁡⁢⁢⁢# --------------------------------- ​‌‍‌‍𝙇𝙞𝙨𝙩​ --------------------------------------------------------------------------------------- #
    # a List type variable can contain more than one item, List items are ordered, changeable, and allow duplicate values.
    #  List items are bracketed [] 
    #  # --------------------------- 𝙖𝙙𝙙 𝙚𝙡𝙚𝙢𝙚𝙣𝙩𝙨 ---------------------------------------------------------------------------------- #
    # Ex: thislist = ["apple", "banana", "cherry", "apple", "cherry";
    #   to add items to the end of a list use thislist.𝗮͟𝗽͟𝗽͟𝗲͟𝗻͟𝗱͟("orange")
    #
    #   output: thislist = ["apple", "banana", "cherry", "apple", "cherry", "orange"];
    #
    #   to add elements in a specific position use thislist.insert(index,"orange")
    #       ex: thislist.insert(1,"orange")
    #           output: thislist = ["apple", "orange", "banana", "cherry", "apple", "cherry"];
    #
    #
    # # --------------------------𝙧𝙚𝙢𝙤𝙫𝙚 𝙚𝙡𝙚𝙢𝙚𝙣𝙩𝙨 ---------------------------------------------------------------------------------- #
    #
    #  to remove the first occurence of an item use thislist.remove("apple")
    #   
    #  output: thislist = ["banana", "cherry", "apple", "cherry"];
    #
    #  to remove elements in a specific position use thislist.pop(index,"apple")
    #   ex: thislist.insert(3,"apple")
    #       output: thislist = ["apple", "banana", "cherry", "cherry"];
    #
    # # --------------------------𝙇𝙞𝙨𝙩 𝙢𝙚𝙩𝙝𝙤𝙙𝙨 ------------------------------------------------------------------------------------- #
    #   Method:	 |   Description:
    # ------------------------------------------------------------------------------------------------------------------------------ #
    #   append()	Adds an element at the end of the list
    #   clear()	    Removes all the elements from the list
    #   copy()	    Returns a copy of the list
    #   count()	    Returns the number of elements with the specified value
    #   extend()	Add the elements of a list (or any iterable), to the end of the current list
    #   index()	    Returns the index of the first element with the specified value
    #   insert()	Adds an element at the specified position
    #   pop()	    Removes the element at the specified position
    #   remove()	Removes the first item with the specified value
    #   reverse()	Reverses the order of the list
    #   sort()	    Sorts the list
    # ------------------------------------------------------------------------------------------------------------------------------- #
    ⁡⁣⁣⁢# # --------------------------------- ​‌‍‌𝙏𝙪𝙥𝙡𝙚​ ------------------------------------------------------------------------------------- #
    # a Tuple type variable can contain more than one item,
    #  tuple is a collection which is ordered and unchangeable.(ordered != sorted)
    #  Tuple items are round bracketed () 
    #
    # ex: thistuple= ("apple", "banana", "cherry")
    #
    #  # --------------------------- 𝙚𝙙𝙞𝙩 𝙚𝙡𝙚𝙢𝙚𝙣𝙩𝙨 ---------------------------------------------------------------------------------- #
    # to add tuple items you need to convert to a list using var_name = list(thistuple)
    #
    #  you can add a tuple to another using sum operatos between the tuples
    # 
    #   ex: tuple_A = tuple_A + tuple_B
    #                or
    #       tuple_A += tuple_B
    # --------------------------- 𝙪𝙣𝙥𝙖𝙘𝙠𝙞𝙣𝙜 𝙚𝙡𝙚𝙢𝙚𝙣𝙩𝙨 ------------------------------------------------------------------------------- #
    #
    # you can extract the values into variables like this
    #
    #   (a,b,c)=thistuple
    #
    #   output:
    #       a = "apple"
    #       b = "banana"
    #       c = "cherry"
    #
    # # --------------------------𝙏𝙪𝙥𝙡𝙚 𝙢𝙚𝙩𝙝𝙤𝙙𝙨 ------------------------------------------------------------------------------------ #
    #   Method:	 |   Description:
    # ------------------------------------------------------------------------------------------------------------------------------ #
    #   count()		Returns the number of times a specified value occurs in a tuple
    #   index()	    Searches the tuple for a specified value and returns the position of where it was found
    # ------------------------------------------------------------------------------------------------------------------------------ #⁡
   ⁡⁢⁣⁣ # # --------------------------------- ​‌‍‌𝙎𝙚𝙩​ -------------------------------------------------------------------------------------- #
    # a Set type variable can contain more than one item, A set is a collection which is unordered, unchangeable,
    #  unindexed and don't allow duplicates. (ordered != sorted)
    #
    # U͟n͟o͟r͟d͟e͟r͟e͟d͟:
    #      • Unordered means that the items in a set do not have a defined order.
    #      • Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
    #
    # U͟n͟c͟h͟a͟n͟g͟e͟a͟b͟l͟e:
    #       • Set items are unchangeable, meaning that we cannot change the items after the set has been created.
    #
    # U͟n͟i͟n͟d͟e͟x͟e͟d:
    #       • does not support accessing elements by position
    #
    #  Set items are curly bracketed {} 
    #
    # ex: thisset= {"apple", "banana", "cherry"}
    #
    #  # --------------------------- 𝙖𝙙𝙙 𝙚𝙡𝙚𝙢𝙚𝙣𝙩𝙨 ---------------------------------------------------------------------------------- #
    # to add items to a set use thisset.add(" ")
    #
    #  you can add a set to another variable and vice versa using set_a.update(variable_b) 
    # 
    #   added elements from variable_b to set_a   
    #
    # --------------------------- 𝙧𝙚𝙢𝙤𝙫𝙚 𝙚𝙡𝙚𝙢𝙚𝙣𝙩𝙨 ---------------------------------------------------------------------------------- #
    #
    # you can remove items from a set like this:
    #
    #   to remove an item from a set use thisset.remove(" ")
    #                       or
    #   use thisset.discard(" ") so that it wont raise an error if the item doesn't exist
    #
    #   ps: using .pop() a random item will be removed
    #
    # # --------------------------- 𝙟𝙤𝙞𝙣 𝙨𝙚𝙩𝙨 ---------------------------------------------------------------------------------------- #
    #   union()                 methods joins all items from both sets.
    #   intersection()          method keeps ONLY the duplicates.
    #   difference()            method keeps the items from the first set that are not in the other set(s).
    #   symmetric_difference()  method keeps all items EXCEPT the duplicates.
    #
    ## --------------------------𝙁𝙧𝙤𝙯𝙚𝙣𝙨𝙚𝙩 -------------------------------------------------------------------------------------------- #
    #
    # a frozenset as the name suggests is an immutable set
    ### ---------------------Frozenset methods----------------------------------------------------------------------------------------- #
    #       Method            | Shortcut| 	Description	
    # --------------------------------------------------------------------------------------------------------------------------------- #
    #   copy()	 	          |         |   Returns a shallow copy	
    #   difference()	      |    -    |   Returns a new frozenset with the difference	
    #   intersection()	      |    &    |   Returns a new frozenset with the intersection	
    #   isdisjoint()	 	  |         |   Returns True if there is NO intersection between two frozensets	
    #   issubset()	          |  <= / < |   Returns True if this frozenset is a (proper) subset of another	
    #   issuperset()	      | >= / >  | 	Returns True if this frozenset is a (proper) superset of another	
    #   symmetric_difference()|	   ^    | 	Returns a new frozenset with the symmetric differences	
    #   union()	|	          |         |   Returns a new frozenset containing the union	
    #
    #
    # # --------------------------------------𝙎𝙚𝙩 𝙢𝙚𝙩𝙝𝙤𝙙𝙨 ------------------------------------------------------------------------------ #
    #
    #       Method                      | Shortcut | 	Description
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    #   add()	 	                    |          |     Adds an element to the set
    #   clear()	 	                    |          |     Removes all the elements from the set
    #   copy()	 	                    |          |     Returns a copy of the set
    #   difference()	                |    -	   |     Returns a set containing the difference between two or more sets
    #   difference_update()             |  	 -=	   |     Removes the items in this set that are also included in another, specified set
    #   discard()	 	                |          |     Remove the specified item
    #   intersection()	                |     &	   |     Returns a set, that is the intersection of two other sets
    #   intersection_update()           |     &=   |     Removes the items in this set that are not present in other, specified set(s)
    #   isdisjoint()	 	            |          |     Returns True if NO items of this set is present in another set
    #   issubset()	                    |     <=   |     Returns True if all items of this set is present in another set
    #       	                        |     <	   |     Returns True if all items of this set is present in another, larger set
    #   issuperset()	                |     >=   |     Returns True if all items of another set is present in this set
    #    	                            |     >	   |     Returns True if all items of another, smaller set is present in this set
    #   pop()	 	                    |          |     Removes an element from the set
    #   remove()	 	                |          |     Removes the specified element
    #   symmetric_difference()          |	  ^    |     Returns a set with the symmetric differences of two sets
    #   symmetric_difference_update()   |	  ^=   |     Inserts the symmetric differences from this set and another
    #   union()	                        |     |    |     Return a set containing the union of sets
    #   update()	                    |     |=   |     Update the set with the union of this set and others
    #
    #
    # ------------------------------------------------------------------------------------------------------------------------------------ #⁡
    ⁡⁣⁢⁣# --------------------------------- ​‌‍‌𝘿𝙞𝙘𝙩𝙞𝙤𝙣𝙖𝙧𝙞𝙚𝙨​ ----------------------------------------------------------------------------------- #
    #
    #a dict type variable can contain more than one item, a dictionary is a collection which is ordered*,
    #  changeable and do not allow duplicates.(ordered != sorted)
    #
    # dictionaries can be nested
    #
    #  dict items are curly bracketed {} and have a key value :
    #
    # # -----------------------𝘿𝙞𝙘𝙩𝙞𝙤𝙣𝙖𝙧𝙮 𝙢𝙚𝙩𝙝𝙤𝙙𝙨 ------------------------------------------------------------------------------------- #
    #                  | 
    #       Method     |	Description
    # --------------------------------------------------------------------------------------------------------------------------------- #
    #   clear()	       |     Removes all the elements from the dictionary
    #   copy()	       |     Returns a copy of the dictionary
    #   fromkeys()	   |     Returns a dictionary with the specified keys and value
    #   get()	       |     Returns the value of the specified key
    #   items()	       |     Returns a list containing a tuple for each key value pair
    #   keys()	       |     Returns a list containing the dictionary's keys
    #   pop()	       |     Removes the element with the specified key
    #   popitem()	   |     Removes the last inserted key-value pair
    #   setdefault()   |    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
    #   update()	   |     Updates the dictionary with the specified key-value pairs
    #   values()	   |     Returns a list of all the values in the dictionary
    # ---------------------------------------------------------------------------------------------------------------------------------- #
⁡⁢⁣⁢# -------------------------------------------------------------------------------------------------------------------------------------- #
#                               ​‌​‌‌‌𝙥𝙖𝙨𝙨 𝙨𝙩𝙖𝙩𝙚𝙢𝙚𝙣𝙩​ ​                                                                             #
# -------------------------------------------------------------------------------------------------------------------------------------- #
# The "pass statement" serves as a placeholder for code, 
# meaning that its basically creating an empty statement in a way that python can process
# -------------------------------------------------------------------------------------------------------------------------------------- #⁡
⁡⁢⁣⁢# -------------------------------------------------------------------------------------------------------------------------------------- #
#                               ​‌​‌‌‌𝙁𝙪𝙣𝙘𝙩𝙞𝙤𝙣𝙨​ ​                                                                                       #
# -------------------------------------------------------------------------------------------------------------------------------------- #
# 
#   def teste(parameter): a parameter is a variable listed in a function declaration
#
#   teste(argument): a value that is used in the main fuction
#   
#       basically parameter is a placeholder for the argument
#
#   both types of *arg can be unpacked
#
## --------------------------------------------*𝙖𝙧𝙜 ------------------------------------------------------------------------------------- #
#
#   the *arg parameter is used to accept any positional value in the argument camp
#   arg becomes a tuple
#
#   def my_function(*args):
#
#       print("First argument:", args[0])
#       print("Second argument:", args[1])
#       print("All arguments:", args)
#
#   my_function("Emil", "Tobias", "Linus")
## --------------------------------------------**𝗸𝘄𝗮𝗿𝗴 ------------------------------------------------------------------------------------- #
#   
#   the **kwarg parameter follows the same logic but for keywords/strings
#   '**'kwarg becomes a dict
#
#
# -------------------------------------------------------------------------------------------------------------------------------------- #⁡
⁡⁢⁣⁢# -------------------------------------------------------------------------------------------------------------------------------------- #
#                            ​‌‌‌ 𝙄𝙩𝙚𝙧𝙖𝙩𝙤𝙧 𝙫𝙨 𝙄𝙩𝙚𝙧𝙖𝙗𝙡𝙚 ​ ​                                                                   #
# -------------------------------------------------------------------------------------------------------------------------------------- #
#
#  an iterable is an object that can be itered (percorrido com um loop)
#  ex: lists, tuples, strings, etc.
#
#  an iterator is an object that procuced the next element in a sequence using next() (Usually created from an iterable using iter())
#  basically a marker
#   
#  numbers = [1, 2, 3] ----> iterable
#
#  it = iter(numbers)  ----> iterator
#
#  print(next(it))  ----> 1
#  print(next(it))  ----> 2
#  print(next(it))  ----> 3
#
# -------------------------------------------------------------------------------------------------------------------------------------- #⁡
⁡⁢⁣⁢# -------------------------------------------------------------------------------------------------------------------------------------- #
#                            ​‌‌‌ ​‌‌‌𝙈𝙤𝙙𝙪𝙡𝙚​                                                                                             #
# -------------------------------------------------------------------------------------------------------------------------------------- #
#
#  A module is basically a group of functions in a file format
#
#  to use just save a code as code.py, and now just call it using import
#
#  to rename a module you can use "as" to add an alias
#
#
#  to find all functions names in a module use dir() function
# -------------------------------------------------------------------------------------------------------------------------------------- #⁡
⁡⁢⁣⁢# -------------------------------------------------------------------------------------------------------------------------------------- #
#                            ​‌‌‌ ​‌‌‌𝙅𝙎𝙊𝙉​                                                                                                 #
# -------------------------------------------------------------------------------------------------------------------------------------- #
#
#  A JSON is text written in JavaScript object notation
#
#  to use first import json module
#  a json has the format of a python dictionary
#  to parse to python use json.loads(json_name)
#
#  to convert from python to json use json.dump(dict_name)
#
#  You can convert Python objects of the following types, into JSON strings:
#
#   • dict   == object
#   • list   == array
#   • tuple  == array
#   • string == string
#   • int    == number
#   • float  == number
#   • True   == true
#   • False  == false
#   • None   == null
# -------------------------------------------------------------------------------------------------------------------------------------- #⁡
⁡⁢⁣⁢# -------------------------------------------------------------------------------------------------------------------------------------- #
#                            ​‌‌‌ ​‌‌‌𝙍𝙚𝙜𝙀𝙭​                                                                                               #
# -------------------------------------------------------------------------------------------------------------------------------------- #
#
#  A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#
#  to use first import re module
#
#  RegEx functions:
#--------------------------------------------------------------------------------------------------------------------------------------- #
#   Function    |	Description
#--------------------------------------------------------------------------------------------------------------------------------------- #
#    findall	|    Returns a list containing all matches
#     search	|    Returns a Match object if there is a match anywhere in the string
#     split	    |    Returns a list where the string has been split at each match
#     sub	    |    Replaces one or many matches with a string
# -------------------------------------------------------------------------------------------------------------------------------------- #⁡
⁡⁢⁣⁢# -------------------------------------------------------------------------------------------------------------------------------------- #
#                            ​‌‌‌ ​‌‌‌𝙏𝙧𝙮 𝙀𝙭𝙘𝙚𝙥𝙩  ​                                                                                  #
# -------------------------------------------------------------------------------------------------------------------------------------- #
#
#  Try is used to test a block of code for error, so it must be used with Except for when the error occurs
#
#  Except is used to present a error handling block of code  
#
#  else is used to process after the except block ran
#
#  Finally is used to run regardless of the try, except blocks
#
#  you can use "raise" to raise a wich kind of error ocurred 
# -------------------------------------------------------------------------------------------------------------------------------------- #⁡
⁡⁢⁣⁢# -------------------------------------------------------------------------------------------------------------------------------------- #
#                           ‌ ​‌‌‌𝙑𝙞𝙧𝙩𝙪𝙖𝙡 𝙚𝙣𝙫𝙞𝙧𝙤𝙢𝙚𝙣𝙩           ​                                                   #
# -------------------------------------------------------------------------------------------------------------------------------------- #
#
#  python has a built in venv module, to create it use:
#
#   • Windows:  C:\Users\Your Name> python -m venv myfirstproject
#   
#   • Linux:    $ python -m venv myfirstproject
#
#   to activate the env use:
#       
#       • Windows: C:\Users\Your Name> myfirstproject\Scripts\activate
#   
#       • Linux:   $ source myfirstproject/bin/activate
#
#   use pip to install packages
#       the packages will be installed only inside the env
#
#   to use the package create a file in the same location as the env folder but not inside it
#   place the code inside the new file
#   inside the env run: 
#
#   • Windows: (myfirstproject) C:\Users\Your Name> python test.py
#   
#   • Linux:   (myfirstproject) ... $ python test.py
#
#
#   to deactivate it write deactivate in the terminal
#
#   to delete the env use:
#   
#   • Windows: C:\Users\Your Name> rmdir /s /q myfirstproject
#   
#   • Linux:   $ rm -rf myfirstproject
#
# -------------------------------------------------------------------------------------------------------------------------------------- #⁡
⁡⁢⁣⁢# -------------------------------------------------------------------------------------------------------------------------------------- #
#                           ​‌‌‌           ​‌‌‌𝙊𝙊𝙋  ​        ​                                                                   #
# -------------------------------------------------------------------------------------------------------------------------------------- #
#
#  python is an object oriented programing language
# -------------------------------------------------------------------------------------------------------------------------------------- #⁡
     ⁡⁣⁢⁣# ---------------------------------------- ​‌‍‌‍Class​ --------------------------------------------------------------------------------- #
