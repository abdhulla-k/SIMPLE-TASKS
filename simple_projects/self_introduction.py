# string concatenation (how to put string together)

youtouber = "freeCodeCamp"

# a few ways to add this to 

print("subscribe to " + youtouber)
print("subscribe to {}".format(youtouber))
print(f"subscribe to {youtouber}")


# an another task to complete a self introduction demo.

name = input("what is your name?")
place = input("where are you from?")
education = input("Enter your education")
collage_name = input("what is your collage neme?")
collage_place = input("where is your collage?")
percentage = input("How many percentage marks did you have in the exam?")
family_members = input("how many members are there in your family?")
job_of_father = input("what is your father's job?")
job_of_mother = input("what is your mother's job?")


self_introduction = f"I am {name} from {place}.I have completed my {education} from {collage_name} {collage_place},\
 with an aggregate of {percentage}%. we are {family_members} in my family.my father is a {job_of_father} and my mother\
 is a {job_of_mother}.Thats all about me"

print(self_introduction)