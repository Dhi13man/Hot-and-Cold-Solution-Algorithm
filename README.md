# Hot-and-Cold-Solution-Algorithm


This is a simple Hot and Cold guessing game for any customisable range, and a recursion-based, binary splitting algorithm that can guess the number, even for extremely high ranges, perfectly in low number of chances, and with only up to 5% error even when number of chances are not adequate.

The game generates a random Target number in the given range, completely unknown to the player/algorithm. Their task is then to guess it based on the feedback(Warmer, Colder) they get from the game, upon making random guesses. The number of total guesses given to achieve this are limited.

----

# Customizable Game Parameters:
1. Lower limit of Range to be guessed in
2. Upper limit of Range to be guessed in
3. Number of chances that the user/algorithm will be given to arrive at Target number
4. Whether the human or whether the algorithm tries to guess the Target number
5. If algorithm is guessing the number, then whether the solution should be shown step by step, or instantaneously


# Potential practical usage:
The AlgorithmSolve() method can be used with a Game class object to make more intelligent guesses, for lower time consumption in practical situations.
For this purpose, the (Warmer/Colder) feedback from the Game class object can be programmed to be provided based on response data from the real life environment. 

This will drastically reduce the number of potential guesses required to find a hidden target, even when the total range to be guessed from reaches the billions.
