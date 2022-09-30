#Full Name: Kartikey Pandey
#Team Members: Kartikey Pandey(kfp5411), Riya Rawal(rzr5540), Aviral Bansal(akb6824)
#ID:939970318
#Date:28th September 2022
#Filename:A1_Team21_Pandey_Kartikey_kfp5411
#Purpose: Code for A1 for Team 21



#Problem 1 
#Create a function that, given a list of unknown size, returns its most repeated element and its least repeated element 
#as a list of the two elements in that order. Assign the returned list to a variable and then print the variable on another line. 
#You can test the function by giving it [ 10, 30, 60, 88, 10, 30, 10, 60, 3, 88 ], the returned list for which should be [ 10, 3 ].
def count_l(count,l,word):
    for j in range(len(l)): 
        if l[j] == word: 
            count += 1
    return count 

def ml(l): 
    #Counting Max
    counter = 0
    count = 0
    word = ""
    word_max= ""

     
    for i in range(len(l)): 
        word = l[i]

        count = count_l(count,l,word)

        if count >= counter: 
            counter = count 
            word_max= l[i]

        count = 0

    counter_2 = 1
    count_2 = 0
    word_2 = ""
    word_min = ""

     
    for i in range(len(l)): 
        word_2 = l[i]
        for j in range(len(l)): 
            if l[j] == word_2: 
                count_2 += 1

        if count_2 <= counter_2: 
            counter_2 = count_2 
            word_min= l[i]
        count_2 = 0
    
    return word_max,word_min



#Problem 2
#Consider a list and another variable called window size(w). Let us define a sliding window as a part of the list of size w. 
#This window keeps sliding one element at a time from the very left.
#Your task is to create a resulting array that contains the maximum of each of the sliding windows.

def max(l): 
    word_max= l[0]
     
    for i in range(len(l)): 
        if l[i] >= word_max: 
            word_max = l[i]

        
    return word_max


def new_list(ls,i,w): 
    nl = []
    for i in range(i,w+i):
        nl = nl + [ls[i]]
        i = i + 1

    return nl


def sliding_window(ls, w): 
    for i in range(0,len(ls)-w+1): 

        k = new_list(ls,i,w)
        g = max(k)
        ls[i] = g 


    final = []
    for d in range(0,len(ls)-w+1): 
        final = final + [ls[d]]


    return final 



#Main function
def main(): 
    #Problem 1
    l = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,1,2,3,4,5,6,1,2,3,4,5,1,2,3,4,1,2,3,1,2,1]
    prob_1 = ml(l)
    print("Most occuring element =",prob_1[0])
    print("Least occuring element =",prob_1[1])

    #Problem 2 
    l = [1,3,5,1,2,4,7,8]
    w = 4
    prob_2 = sliding_window(l,w)
    print("Output for Problem 2 =",prob_2)


#Call for main function
main()


