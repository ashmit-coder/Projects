""" In this we will get input fro the client and put into a file 
with the time and all th eimportant data of food and exercise 
and also read the data later """
#  pepole A,B, and C
import datetime as dt
class log(object):
    """ we will use this clas  to make an print to the file as it helps
    to make infinite files """
    def __init__(self, name):
        self.name = name
        # self.food = food
        # self.excersice = excersice
        
    def food_log(self, foods, name_foods):
        """here we will take your food as input and create a file named 
        name_food"""
        na_food = open(name_foods,"w") 
        d_t  = str(dt.datetime.now()) 
        na_food.write(d_t)
        na_food.write("\n")
        na_food.write(foods)
        na_food.write("\n")
        na_food.write("\n")
        na_food.close()
    def excersice_log(self, excercis, name_excersice):
        """here we will take your excersice as input and create a file named 
        name_excersice"""
        na_excersice =  open(name_excersice,"w") 
        d_t = str(dt.datetime.now())
        na_excersice.write(d_t)
        na_excersice.write("\n")
        na_excersice.write(excercis)
        na_excersice.write("\n")
        na_excersice.write("\n")
        na_excersice.close()

task = input("what do you want to do retrive or log the data: ")
if(task.lower() == "log"):
    name = input("give me your name ")
    name_class = log(name)
    task_1 = input("what do you want to log food or excersice ")
    if(task_1.lower() == "food"):
        food = input("what did you have(all at once) ")
        name_food = name + "_food.txt" # we convert your name to file with  extension of the task_1
        name_class.food_log(food, name_food)

    else:
        excersice = input("Tell me your excercise ")
        name_excersice = name + "_excersice.txt" # we convert your name to file with  extension of the task_1
        name_class.excersice_log(excersice, name_excersice)

else:

        # here we just print what we qant and what we  got
    try:   
        name = input("give me your ")
        task_1 = input("what do you want to see ")
        name_food_1 = name + "_food.txt"
        name_excersice_1 = name + "_excersice.txt"
        if(task_1.lower() == "food"):
             with open(name_food_1) as f:
                print(f.read())
        else:
            with open(name_excersice_1) as g:
                print(g.read())        
    except Exception as e:
        print(e)
        print("you dont have a file of ypur name please log first ")