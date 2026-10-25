'''
This file will contain code for performing your comparisons. It should perform (or have a setting that lets us perform) ***ALL*** your comparisons when run. 
We recommend adding the ability to run a subset of the comparisons for testing purposes (as illustrated below). 
'''
import problems as prb
import algorithms as alg

compsToRun = [0]

if 0 in compsToRun: 
  winsZero=0
  winsOne=0
  draws=0
   
  for i in range(100):
    compGame = prb.Game(prb.TicTacToe(),alg.RandomAgent(),alg.RandomAgent(),False)
    outcome  = compGame.playGame()
    if outcome == 0:
      winsZero+=1
    if outcome == 1:
      winsOne+=1
    if outcome == -1:
      draws+=1  
      
  print(f"P0 Wins: {winsZero}\nP1 Wins: {winsOne}\nDraws: {draws}")  
  
