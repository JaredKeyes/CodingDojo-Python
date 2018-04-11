#Assignment: Dictionary in, tuples out
'''
Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the 
key and the second is the value. Here's an example:
# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]
'''

# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def tuples(my_dict):
  newList = []
  for key in my_dict:
    newList.append((key, my_dict[key]))
  return newList

print tuples(my_dict)