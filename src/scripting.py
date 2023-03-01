## importing stuff
import argparse

#### Turn the above steps into a function:
# this function takes no input, just input from the command line in terminal
def input_parse():
    #initialise the parser
    parser = argparse.ArgumentParser()
    #add arguments
    parser.add_argument("--name", type=str, default= "Kevin") #this gives the reciever options for the function ?
    parser.add_argument("--age", type= int) #age argument 
    # parse the arguments from the command line 
    args = parser.parse_args()
    
    #define a return value
    return args #returning all arguments (age and name)



#create simple function
def hello(name, age):
    print("hello my name is " + name + "!!")
    print("I am "+ str(age) + " years old") #we're trying to do string concatenating, but we have integers as age, so we wrap it in a str()

#hello(args.name)


#### define a main function (KEY)
def main():
    # run the input parse to get name
    args = input_parse()
    # pass name to hello()
    hello(args.name, args.age) #there is nothing in these until they are specified in terminal

main()

### for the recipient being able to run your code, 
### DOCUMENT either in a readme or print it terminal