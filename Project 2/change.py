#!/usr/bin/env python

import sys
import csv
import random
import time


if (len(sys.argv) != 2):
	print "\n"
	print "Error! Incorrect number of arguments supplied.\nUsage: python change.py [inputfile]"
	quit()
	
	
inputfile = sys.argv[1]


#takes as input array V where V[i] is the value of the coin of the ith denomination and value A which is the amount of change we are asked to make

def changeslow(coins, total):
    minCoins = float("inf")         #Number of coins will always be less than this
    coinCounts = [0] * len(coins)   #Keep track of the number of coins in each spot in the array

    if total in coins:      #If the total is equal to a coin, increment that place in the coin array and return the array and 1 (for 1 coin)
        coinCounts[coins.index(total)] = 1
        return coinCounts, 1
    elif total == 0:        #No change means no coins are needed
        return coinCounts, 0

    for i in range(0, len(coins)):  #Keep iterating and keeping track of the total number of coins
        if (coins[i] <= total):
            coinHolder, coinsUsed = changeslow(coins, total - coins[i])
            coinsUsed += 1
            coinHolder[i] = coinHolder[i] + 1

            if coinsUsed < minCoins:
                minCoins = coinsUsed
                coinCounts = coinHolder

    return coinCounts, minCoins
    
    
#takes as input array V where V[i] is the value of the coin of the ith denomination and value A which is the amount of change we are asked to make

def changegreedy(Coins, Change):

   #Create lists
   coin_quantity = 0
   greedy_answer = []
   change_greedy = Change
   #go through each coin from the largest value to the smallest
   for i in range(len(Coins)-1, -1, -1):
      greedy_answer.insert(0, change_greedy/Coins[i])
      #add this value to coin_quantity
      coin_quantity = coin_quantity + greedy_answer[0]
      #get the modulus of our division
      change_greedy = change_greedy%Coins[i]
   
#takes as input array V where V[i] is the value of the coin of the ith denomination and value A which is the amount of change we are asked to make
   return coin_quantity, greedy_answer

		
def changedp(Coins, Change):

	T = []
	C = []
	Answer = []
	#print A
	#print Coins
	#print len(V)
	#print "Make %s from %s" %(Change, Coins)
	for i in range(0, Change+1):
		T.append(999999)
		C.append(-1)
	for i in range(0, len(Coins)):
		Answer.append(0)
	T[0] = 0
	for j in range(0, len(Coins)):
		#print Coins[i]
		for i in range(0, Change+1):
			#print j
			#print C[j]
			#print T[i]
			#print T[j]
			if i >= Coins[j]:
				if T[i] > (1 + T[i-Coins[j]]):
					T[i] = 1+T[i-Coins[j]]
					#print T[i], C[i]
					C[i] = j
	changeIndex = C[Change]
	
	
	# if C[len(C)-1] == -1:
		# print "Can't make da change"
		# return 0
	#print Coins
	#print C
	i = len(C)-1
	while i >= 1:
		# if there are no 1 denomination coins include a if C[i] == -1 then break statement here to indicate that change cannot be made
		Answer[C[i]] = Answer[C[i]] + 1
		i = i - Coins[C[i]] 
	#print C
	#if T[Change] == 999999:
		#print "Could not make change for %s" % Change
		#return 99999999
	#else:
		#print "Made %s from %s coins with largest coin of size %s  - %s" % (Change, T[Change], Coins[C[Change]], Answer)
	return T[Change], Answer
	#print T 

#Open filename and read contents into array.  Convert array elements into integers
#in the case of coins.txt list elements 0, 2, 4, etc. will be the types of coins available and list elements 1, 2, 3, etc. will be the value of change that needs to be produced.

def readProblems(filename):
	array = []
	with open(filename) as f:
		reader = csv.reader(f, skipinitialspace=True, delimiter=' ')
		for row in reader:
			array.append(row)

	for x in array:
		
		#convert items in list x from string to int7
		for i in range(len(x)):
			x[i] = int(x[i])
	f.close()		
	return array




def outputResults(filename, algorithm):
	input = readProblems(filename)
	answer = []
	answerfile = inputfile.replace('.txt',algorithm.__name__ + 'change.txt')
	timefile = inputfile.replace('.txt',algorithm.__name__+'times.csv')
	with open(answerfile, 'w') as f:
		with open(timefile, 'wb') as t:
			writer = csv.writer(t)
	#loops through input list and performs whatever algorithm 
			for i in range(0, len(input)-1, 2):
				#output results of algorithm to results.txt - modify as needed
				change = input[i+1]
				coins = input[i]
				A = change[0]
				starttime = time.time()
				changeanswer, answer = algorithm(input[i],A)
				endtime = time.time()
				duration = endtime - starttime
				#print duration
				##may need to change \r\n below to \n or \r
				#f.write(str(changeslow(input[i],input[i+1])) + "\r\n")
				#f.write(str(changegreedy(input[i],input[i+1])) + "\r\n")
				#this next one is for testing only, delete or comment out before final submission
				#f.write(str(change[0]) + "\r\n")
				for x in range(len(coins)):
					f.write(str(coins[x]) + " ")
				f.write("\n")
				for x in range(len(answer)):
					f.write(str(answer[x]) + " ")
				f.write("\n")
				#f.write(str(answer) + "\r\n")
				f.write(str(changeanswer) + "\n")
				writer.writerow([algorithm, A, duration, changeanswer])


outputResults(inputfile, changedp)
outputResults(inputfile, changegreedy)
outputResults(inputfile, changeslow)
