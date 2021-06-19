# python_warmups


 ## readme.txt of project and their descriptions
 
 
  CS 300 - Scientific Programming - Spring 2020
 This course provides an introduction to scientific programming using the Python language.
 The course will cover basic programming, input and output of data, computation, processing, graphical output, and how to use some of the  libraries available in Python.
 All of the class examples and programming assignments will be from the areas of chemistry, biology, mathematics, data science, computer science, and physics.
 
 ===============================================================================
 ## Program 1:
 Write a program that implements Archimedes' method to find an approximation of pi by determining the length of the perimeter of a polygon inscribed within a circle.   
 For this program, assume the polygon has eight sides.
 
 https://stac.mrooms.net/pluginfile.php/139177/mod_assign/intro/circle.png
 
 In other words, if we assume that the polygon and n side of length s, we can focus our attention on a small slice of the polygon.  
 In the triangle shown in the figure, the side labeled h will have a length of 1 because we assuming a unit circle.  
 The angle labeled B can be easily computed by remembering that there are 360 degrees in a circle.  
 Thus, angle B is 360/n, and angle A is (1/2)B.  In addition, the triangle is a right triangle, so the side opposite angle A has a length of (1/2)s.
 
 In a right triangle, see the figure below, the ratio of the opposite side to the long side (or hypotenuse) is equal to the sine of angle A.  
 Because the triangle has a hypotenuse of length 1, we know that (1/2)s will simply be equal to the sine of angle A.
 
 https://stac.mrooms.net/pluginfile.php/139177/mod_assign/intro/triangle.png
 
  ===============================================================================
  ## Program 2:
  Bioinformatics is the application of computer science techniques to problems in biology.   
  Many bioinformatics applications deal with the processing of DNA.  
  DNA, which contains the genetic codes for living things, can be represented by an incredibly long string of single characters (billions). 
  This is possible because DNA is made up of a long chain of four basic chemicals called nucleotides: adenine, guanine, cytosine and thymine.  
  For computational purposes, these are abbreviated A, G, C, and T.  For example, a very short fragment of DNA could be represented by the string: ATGGCTATTGCTATTGATCGG.
  
  Cells use this code to, among other things; create chemicals (proteins) that perform many tasks within your body. 
  Therefore, certain sub-sequences of DNA are essentially a code for certain proteins. 
  When a certain protein is needed by your body (say to help digest food or to make part of a new cell), a copy of a certain part of the DNA is used to create the correct protein.
  
  Proteins are made from a sequence of amino acids, of which there are 20. 
  Each three nucleotide sequence in DNA (called a triplet) is a code for a specific amino acid. 

  The amino acid sequence for a particular protein corresponds to a sequence of nucleotides in DNA.
  A DNA sequence for a particular protein always starts with the triplet ATG (the initiation), and always ends with either TAA, TAG or TGA (stops). 
  Stops are not codes for any amino acids, they simply mark the end of the sequence for a particular protein. Here's an example of a DNA nucleotide sequence for a simple protein:
  
  ATGGCAACGTGA
  
  The protein code starts with ATG, then has triplets GCA and ACG, and is terminated by the stop triplet TGA. The amino acid sequence is (using the abbreviations): Met-Ala-Thr
  
  Frist, write a function called firstProtein(inputSequence) that returns the first substring that begins with "ATG" .  It should return the empty string if "ATG" is not found

  Second, write a  function call DNA() that prompts the user to enter a nucleotide sequence and prints out the first protein sequence.
  
  Use the dictionary given below:
  
  dict = {"TTT": "Phe", "TCT": "Ser", "TAT": "Tyr", "TGT": "Cys",
        "TTC": "Phe", "TCC": "Ser", "TAC": "Tyr", "TGC": "Cys",
        "TTA": "Leu", "TCA": "Ser", "TAA": "STOP", "TGA": "STOP",
        "TTG": "Leu", "TCG": "Ser", "TAG": "STOP", "CGT": "Trp",
        "CTT": "Leu", "CCT": "Pro", "CAT": "His", "CGC": "Arg",
        "CTC": "Leu", "CCC": "Pro", "CAC": "His", "CGC": "Arg",
        "CTA": "Leu", "CCA": "Pro", "CAA": "Gln", "CGA": "Arg",
        "CTG": "Leu", "CCG": "Pro", "CAG": "Gln", "CGG": "Arg",
        "ATT": "Ile", "ACT": "Thr", "AAT": "Asn", "AGT": "Ser",
        "ATC": "Ile", "ACC": "Thr", "AAC": "Asn", "AGC": "Ser",
        "ATA": "Ile", "ACA": "Thr", "AAA": "Lys", "AGA": "Arg",
        "ATG": "Met", "ACG": "Thr", "AAG": "Lys", "AGG": "Arg",
        "GTT": "Val", "GCT": "Ala", "GAT": "Asp", "GGT": "Gly",
        "GTC": "Val", "GCC": "Ala", "GAC": "Asp", "GGC": "Gly",
        "GTA": "Val", "GCA": "Ala", "GAA": "Glu", "GGA": "Gly",
        "GTC": "Val", "GCG": "Ala", "GAG": "Glu", "GGG": "Gly"}
		
  ===============================================================================
  ## Program 3:
  Assume you have been given the task of exploring temperature changes over the past two decades.  
  You have decided to use a file that contains the average daily temperature for January 1st, from the year 2000 till the year 2019, for seven U.S. cities 
  (note: this file contains actual information the National Climatic Data Center).  
  In addition, rather than simply presenting the data in a tabular format you have decided that it would be best to visualize 
  (i.e.,  create a plot) the data.

  Write a program the reads the temperature from the CSV file and produces a graph to illustrate the temperature variations for January 1.  
  For example, you could create a line graph for all of the cities in the data set  (see below).  Or, if you prefer you may design your own graph.
  
  ===============================================================================
  ## Program 4:
  Write a python program that:
  Finds the sequence of times when the ball passes each half meter assuming the ball is dropped at t=0.
  Create a NumPy array named y that goes from 10 to 0 in increments of -0.5 using the arange function.
  Solve position equation given above for t.  Then using this equation create a NumPy array called t to hold the times when the ball passes each half meter.
  Find the average velocity for each time interval and store the results in a NumPy array called v by using the two arrays (y and t).  Remember (from physics) that the average velocity over an interval \Delta t is defined as \bar{v} = \Delta y/\Delta t.
  Output all three arrays.
  
  ===============================================================================
  ## Program 5:
  Write a program that creates and displays an image of a living organism (i.e., a plant on animal).

  Use Pillow
  The image should have a "relevant" image pasted on top it
  The pasted (top, smaller) image should be masked
  The image should include labels for both the common and scientific names (e.g., "hedgehog", "Erinaceidae-Atelerix")
  
  ===============================================================================
  ## Program 6:
  Assume that the marketing team for your company wants to send more targeted emails to their customers.  Also, assume that you have data on the total spent by customers and their ages (see below). Your goal is to cluster the data.  What your data mining (clustering) program will ultimately show is:  young people with a lower purchasing power, middle ages people with a higher budget, and older people with a lower budget.

   customer data
  age = np.array([18, 21, 22, 24, 26, 26, 27, 30, 31, 35, 39, 40, 41, 42, 44, 46, 47, 48, 49, 54])
  spend = np.array([10, 11, 22, 15, 12, 13, 14, 33, 39, 37, 44, 27, 29, 20, 28, 21, 30, 31, 23, 24])

  create a 2D array
  data = np.column_stack((age,spend))
  Your program should:

  Plot the original data
  Perform a K-Means analysis
  Plot the clusters with the center point of each cluster being black
  The outputs should be similar to this:
  
  ===============================================================================
  ## Program 7:
  Problem scenario:  You are visiting various cities in search of the best ice cream shop; and that you are bicycling from city to city.  The graph below shows the only available bicycle paths.

  Assignment: Write a program that first creates a graph to represent the bicycle paths.  The program should then output the order that the cities will be visited assuming that you start at Sparkill and use a DFS.
  
  ===============================================================================
