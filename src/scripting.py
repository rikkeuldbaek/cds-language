import argparse

#initialise the parser
parser = argparse.ArgumentParser()
#add arguments
parser.add_argument("--name", type=str) #this gives the reciever options for the function ?
# parse the arguments from the command line 
args = parser.parse_args()

#print argument
#print(args)
#print(args.name)


#### Turn the above steps into a function:
# this function takes no input, just input from the command line in terminal
def input_parse():
    parser = argparse.ArgumentParser()
    #add arguments
    parser.add_argument("--name", type=str) #this gives the reciever options for the function ?
    # parse the arguments from the command line 
    args = parser.parse_args()
    #get the name
    name = args.name

    #define a return value
    return name



#create simple function
def hello(name):
    print("hello my name is " + name + "!!")

#hello(args.name)


#### define a main function (KEY)
def main():
    # run the input parse to get name
    name = input_parse()
    # pass name to hello()
    hello(name)

main()

### for the recipient being able to run your code, 
### DOCUMENT either in a readme or print it terminal