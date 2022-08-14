# PortfolioProjectsPython
Data Analysis

Making the game of Wordle:

Link to the original website of the game : https://wordlegame.org/

Rules of the game: 

The rules are very simple: You need to guess the hidden word (from 4 to 11 letters) in 6 tries. To get started, just type any word on the first line. If the letter is guessed correctly and is in the correct place, it will be highlighted in green, if the letter is in the word, but in the wrong place - in yellow, and if the letter is not in the word, it will remain gray. Can you guess the hidden word in 6 tries?

Steps: 

0-	 Imported a dictionary of English words and cleaned the csv file for the purpose of game

1-	 Link to the original dictionary dataset: “”

2-	Read the csv into a list of words

3-	Modified the list of words for only words with length of 5 and lower case 

4-	Randomly selected a word for the game

5-	Made a function which keeps track of the players moves and wins

6-	Receive the player guesses and make sure the guess is a valid word as well as the right length

7-	Give hints to the player if he/she guesses any character right

8-	Closing the game with a winning prompt or a time out prompt depending on the game

9-	On a different notebook I then tried to find the valid words based on a calculation of scores for each word depending on how many frequent characters they have.

10-	Link to find the most frequent alphabet characters: https://en.wikipedia.org/wiki/Letter_frequency

11-	At the end of this notebook I came up with the best possibility of the words from the existing dictionary to increase the chances of a win at the start of the game





