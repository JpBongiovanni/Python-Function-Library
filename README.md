# Python Function Library
<h2>The Python Basics Library is an agrigation of numerous Python functions that are ready to be integrated into any Python project. The functions range from basic to advanced and can be run in both a terminal and in accompanying HTML</h2>


<h3>contents:</h3>
  
    <ul>
      <li><a href="#zigzag">Zig Zag</a></li>
      <li><a href="#callstack">Call Stack Funciton</a></li>
      <li><a href="#collatz">Collatz</a></li>
      <li><a href="#guessnum">Guess the Number</a></li>
      <li><a href="#m8">The Magic 8 Ball</a></li>
      <li><a href="#rps">Rock Paper Scissors</a></li>
    <ul>
  

<hr>
<div id="zigzag">Zig Zag - <p>The Zig Zag function makes use of a while True infinite loop and the time.sleep() function to slow down the rendering of our program in the terminal. Every tenth of a second the program prints again on a different line but with a ' ' before or after the text to give the illusion the text is "zigzagging" down the page like a snake.<p></div>
<img src="https://github.com/JpBongiovanni/Python_Basics/blob/main/movies/zigzag.gif" width="530" height="350" />

<div id="callstack">Call Stack Function - The Call Stack Function is how Python remembers where a function first started and then returns there after the function is complete. It is usually running behind the scenes but it is demonstrated here. </div>
<img src="https://github.com/JpBongiovanni/Python_Basics/blob/main/movies/abcdCallStack.gif" width="530" height="350" />

<div id="collatz">Collatz Sequence - The Collatz function takes one integer. If the integer is even then it is divided by 2, if it is odd, it is multiplied by 3 and adds 1. No one is sure why, but whatever integer is given the final result is always one.</div>
<img src="https://github.com/JpBongiovanni/Python_Basics/blob/main/movies/collatz.gif" width="530" height="350" />

<div id="guessnum">Guess the Number - The program uses the random.randint() function by way of the random module to find the target number between the set number parameters. The user is then asked for an imput and the input is checked against the target number. The program then responds with either "too low," "too high," or "correct." Each input is traced and the player will lose if the input number exceeds 6. </div>
<img src="https://github.com/JpBongiovanni/Python_Basics/blob/main/movies/guessTheNumber.gif" width="530" height="350" />

<div id="m8">The Magic 8 Ball - The program uses the random.randint() function by way of the random module to find the target number depending on the number of possible responses.</div>
<img src="https://github.com/JpBongiovanni/Python_Basics/blob/main/movies/magic8ball.gif" width="530" height="350" />

<div id="rps">Rock Paper Scissors - the program first calls the random and sys modules to use random.ranint() and sys.exit(). Three variables are then established to keep track of our wins, loses, and draws. There are two while loops at play, the first loop runs the whole game, while the second takes inputs from the player. The inner loop then breaks and the random.randint() function chooses an integer assigned to rock, paper, or scissors. The user input and the random integer are then compared and the winner is declared.</div>
<img src="https://github.com/JpBongiovanni/Python_Basics/blob/main/movies/rock_paper_scissors.gif" width="530" height="350" />






