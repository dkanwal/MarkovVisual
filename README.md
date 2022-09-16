# MarkovVisual
A project that utilizes turtle combined with a Markov decision matrix to create artwork made of shapes. 

Title of system: GeoTurtle Painter

Setup:

I was able to set up this code using a single python script which is run through the main() method. There are helper functions that create a Markov Matrix and get the next state. There is a function for each of the four shapes as well. The main method executes the helper functions and the shape functions which have the turtle draw. 

There is an existing call to main at the bottom of the script, so after making sure you are running python3 and have the tk extention simply download and run the file in terminal using Python3 to get results. If you would like to change the number of calls to the Markov matrix, you can do this by changing the number of iterations of the for-loop in main(). 

This project is personally meaningful to me because of the shapes that are used to make the artwork. Each shape is near and dear to my heard due to my passion in math and more specifically geometry. I have always been a numbers guy and mostly stumble over my words when I write (exhibit A, this paragraph). I thought it would be interesting to have my system create art using some shapes that I view are foundations of geometry. 

I was immediately pushed out of my comfort zome in this project through a little systems programming. My python was not working properly with turtle, so I had to do some digging in terminal, and quickly shook off the rust in that area and got to work. It was interesting to investigate the tools within numpy that allow for navigating around state spaces using a Markov matrix. Going forward I'd like to use more Python extension packages and explore their uses.

I do believe this system is creative, however I do not think it is aware of its creativity. When the program is run through multiple state spaces, new shapes are formed when the four shapes come together. This system itself is clever in moving from state to state because it is able to do it quickly and decisively calculating the probabilities of a transition to another state. I'd like to give a shoutout to Crystal for giving me the tip of using np.random.choice() which can use a row's probabilities to transition to the next state all in one function call. 