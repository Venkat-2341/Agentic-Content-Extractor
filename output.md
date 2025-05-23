
## Page 1


Venkatakrishnan E  
23110357 
Problem 1:  
 
Discuss why Diffusion Maps work well for time-series clustering. 
 
●​ Diffusion maps capture the underlying manifold structure of high dimensional 
time series data 
●​ It constructs a graph based representation of the data, where we group points 
based on local similarity(which is basically the DTW distance), the edges of the 
graph are the transition probabilities​
 
●​ We can find non linear temporal patterns with the help of diffusion maps 
●​ Time-series data often contain noise and non-linear variations, but diffusion maps 
mainly focuses on the global structure thus reducing the impact of noise 
●​ Diffusion Maps reduce the dimensionality while preserving meaningful distances. 
​
 
Why Diffusion Maps outperform PCA/t-SNE? 
 
PCA assumes a linear structure, but the time series data generally is non linear, this is 
evident from the lower ARI and silhouette score compared to diffusion maps. 
t-SNE is designed for visualization and relies on pairwise similarities to map data points 
into a lower-dimensional space. 
t-SNE can distort the global structure thus making it not suitable for clustering of time 
series data. 
Higher ARI scores indicate better clustering alignment with true labels, higher values of 
Silhouette score indicate better separation between clusters. 
 
Technique 
ARI score 
Silhouette score 
Diffusion Maps 
0.53 
0.52 
PCA 
0.39 
0.45 
tSNE 
0.24 
0.47 
​


## Page 2


### Images


The image presents a scatter plot graph with the title "Diffusion Map Embedding for the first two components with time=1". The graph features six distinct groups of data points, each represented by a unique color.

*   Red data points: 
    *   The red data points are clustered in the upper left region of the graph.
    *   They exhibit a negative correlation between the two variables.
    *   The red data points are more densely packed than the other groups.
*   Yellow data points: 
    *   The yellow data points are located in the upper right region of the graph.
    *   They also show a negative correlation between the two variables.
    *   The yellow data points are less densely packed than the red data points.
*   Blue data points: 
    *   The blue data points are situated in the middle region of the graph.
    *   They display a positive correlation between the two variables.
    *   The blue data points are relatively evenly distributed.
*   Green data points: 
    *   The green data points are found in the lower left region of the graph.
    *   They demonstrate a positive correlation between the two variables.
    *   The green data points are less densely packed than the blue data points.
*   Purple data points: 
    *   The purple data points are located in the lower right region of the graph.
    *   They exhibit a negative correlation between the two variables.
    *   The purple data points are more densely packed than the green data points.
*   Grey data points: 
    *   The grey data points are scattered throughout the graph.
    *   They do not display a clear correlation between the two variables.
    *   The grey data points are the least densely packed among all the groups.

In summary, the graph illustrates the distribution of six distinct groups of data points, each with its own unique characteristics and correlations between the two variables. The red and yellow data points are clustered in the upper regions, while the blue, green, and purple data points are distributed in the middle and lower regions. The grey data points are scattered throughout the graph without a clear correlation.

The image presents a scatter plot of PCA embedding, which is a statistical technique used to reduce the dimensionality of data by projecting it onto a lower-dimensional space while preserving the most important features. The plot displays the relationships between various activities, such as walking, sitting, standing, and laying, in a two-dimensional space.

Here are the key features of the image:

*   **Title**: The title of the plot is "PCA Embedding," indicating that it represents the results of a principal component analysis (PCA) on the data.
*   **Axes**: The x-axis is labeled as "Axis 1" and the y-axis is labeled as "Axis 2." The axes are not labeled with specific units, but they appear to represent the first and second principal components of the data.
*   **Data Points**: The plot shows a collection of data points, each representing a single observation or sample. The data points are colored according to the activity they belong to: red for walking, yellow for walking upstairs, blue for walking downstairs, green for sitting, pink for standing, and grey for laying.
*   **Distribution**: The data points are scattered throughout the plot, with some clusters and patterns visible. For example, the walking activities tend to cluster together in the top-left corner of the plot, while the sitting and standing activities form a diagonal line in the middle of the plot.
*   **Correlation**: The plot suggests that there is a positive correlation between the first and second principal components, as the data points tend to increase in both directions as you move from left to right and top to bottom.
*   **Outliers**: There are a few outliers visible in the plot, particularly in the walking and sitting activities. These outliers may represent unusual or anomalous observations that do not fit with the rest of the data.

Overall, the PCA embedding plot provides a visual representation of the relationships between the different activities and the underlying structure of the data. It can be used to identify patterns, correlations, and outliers in the data, and to gain insights into the characteristics of each activity.

**Answer**: The scatter plot shows the PCA embedding of various activities, including walking, sitting, standing, and laying. The plot reveals a positive correlation between the first and second principal components, with clusters and patterns visible in the data. The plot also highlights a few outliers, particularly in the walking and sitting activities. Overall, the plot provides a useful visual representation of the relationships between the activities and the underlying structure of the data.


## Page 3


Why using DTW 
 
●​ In time-series clustering  we mostly care about the shape of trends, not the raw 
values at a timestamp. 
●​ DTW focuses on overall similarity by warping the time axis to align similar 
patterns thus making it more meaningful than Euclidean distance. 
●​ Euclidean distance compares points one to one and thus it is very sensitive to 
misalignment.

### Images


The image presents a scatter plot illustrating the relationship between two variables, with each point representing a distinct data point. The x-axis is labeled "Axis 1" and spans from -60 to 60, while the y-axis is labeled "Axis 2" and ranges from -60 to 30.

**Data Points and Colors:**

The data points are categorized into six groups, each denoted by a specific color:

* Red: WALKING
* Yellow: WALKING_UPSTAIRS
* Blue: WALKING_DOWNSTAIRS
* Green: SITTING
* Pink: STANDING
* Gray: LAYING

**Scatter Plot Characteristics:**

The scatter plot exhibits a random distribution of points, with no discernible pattern or trend. The points are scattered across the plot, with some clusters visible for certain categories.

**Axis Labels and Tick Marks:**

The x-axis is labeled "Axis 1" and features tick marks at intervals of 20, ranging from -60 to 60. Similarly, the y-axis is labeled "Axis 2" and has tick marks at intervals of 10, spanning from -60 to 30.

**Background and Title:**

The background of the scatter plot is white, providing a clean and neutral visual context. The title of the plot is "tSNE Embedding," which suggests that the data has been embedded using t-distributed stochastic neighbor embedding (t-SNE), a technique used to visualize high-dimensional data in a lower-dimensional space.

**Overall Impression:**

The scatter plot appears to be a representation of diverse data points, possibly from a machine learning or data science context. The use of t-SNE embedding and the random distribution of points suggest that the data may be complex and high-dimensional. The different colors used to represent each category add an additional layer of complexity to the plot, making it challenging to discern patterns or trends without further analysis.


## Page 4


Problem 2:

### Images


The image presents a comprehensive performance analysis of various machine learning algorithms, focusing on their accuracy and speed. The title "Performance Analysis: Accuracy & Speed" is displayed at the top.

**Main Points:**

* **Accuracy Comparison (Mean Best Value Found)**
	+ Function: Optimizer
	+ Mean Best Value: 1.7829e-08
	+ Std Best Value: 1.3768e-09
	+ Lower values indicate better accuracy.
	+ List of algorithms and their corresponding accuracy values.
* **Convergence Speed Comparison (Mean Function Evaluations)**
	+ Function: Optimizer
	+ Mean Function Evaluations: 1154
	+ Std Function Evaluations: 265
	+ Lower values indicate faster convergence (fewer function calls).
	+ List of algorithms and their corresponding convergence speed values.

**Summary:**

The image provides a detailed comparison of the accuracy and convergence speed of different machine learning algorithms. The results show that some algorithms, such as Ackley Simulated Annealing and Rosenbrock Simulated Annealing, have lower accuracy values and faster convergence speeds compared to others. The image suggests that these algorithms may be more suitable for certain tasks or applications. Overall, the image provides valuable insights into the performance of various machine learning algorithms, allowing users to make informed decisions when choosing an algorithm for their specific needs.


## Page 5


Here for Rosenbrock the value is <10^-9, it nearly converged to 0 for all three optimization 
techniques, as Rosenbrock was fairly straightforward compared to Ackey and the Rastrigin. 
 
For all 3 functions, simulated annealing has given the least value which indicates the best 
accuracy as our optimal solution is 0. 
 
Now in the sense of time taken for convergence, simulated annealing even though it gave us 
the best results has taken a lot of time to converge, nearly 20000 function evaluations.

### Images


Based on the horizontal bar plot, here is a structured description of the graph:

**Title**: The title of the graph is "Accuracy (Avg. Best Value Found)".

**X-axis**: The x-axis represents the different functions being evaluated, which are:

1. Ackley
2. Rastrigin Function
3. Rosenbrock

**Y-axis**: The y-axis represents the accuracy values, with major ticks at:

1. 10^-9
2. 10^-7
3. 10^-5
4. 10^-3
5. 10^-1

There are also minor ticks between the major ticks.

**Bars**: There are three groups of bars, each representing a different optimizer:

1. **Green bars** ( Optimizer ): This group has three bars, one for each function. The bars are all at the same height, approximately 10.
2. **Blue bars** ( CMA-ES ): This group also has three bars, one for each function. The bars are all at the same height, approximately 10.2.
3. **Dark Blue bars** ( Nelder-Mead and Simulated Annealing ): This group has three bars, one for each function. The bars are all at the same height, approximately 10.2.

**Bar lengths**: The lengths of the bars are all similar, with some minor variations.

**Overall**: The graph shows that the optimizers have similar accuracy values across the different functions, with some minor variations. The green bars (Optimizer) are slightly shorter than the blue bars (CMA-ES) and dark blue bars (Nelder-Mead and Simulated Annealing).

Based on the horizontal bar plot, here is a detailed description of the graph:

**Title**: The title of the graph is "Convergence Speed (Avg. Function Evals)".

**X-axis**: The x-axis represents the different functions being evaluated, which are Ackley, Rastrigin, and Rosenbrock.

**Y-axis**: The y-axis represents the average number of function evaluations required for convergence. The major ticks are at 0, 5000, 10000, 15000, and 20000. The minor ticks are at intervals of 1000.

**Bars**: There are three groups of bars, each representing a different optimizer. The optimizers are not explicitly labeled, but they are differentiated by color.

* **Green bars**: The green bars represent one of the optimizers. The values for each function are:
	+ Ackley: approximately 3000
	+ Rastrigin: approximately 3000
	+ Rosenbrock: approximately 4000
* **Purple bars**: The purple bars represent another optimizer. The values for each function are:
	+ Ackley: approximately 1000
	+ Rastrigin: approximately 1000
	+ Rosenbrock: approximately 1000
* **Blue bars**: The blue bars represent the third optimizer. The values for each function are:
	+ Ackley: approximately 22000
	+ Rastrigin: approximately 21000
	+ Rosenbrock: approximately 21000

**Error bars**: Each bar has an error bar associated with it, indicating the standard deviation of the average function evaluations. The error bars are not explicitly labeled, but they provide a visual representation of the uncertainty in the data.

Overall, the graph suggests that the green and purple optimizers perform similarly, with relatively low average function evaluations for all three functions. In contrast, the blue optimizer requires significantly more function evaluations for convergence, particularly for the Ackley function.


## Page 6


The plots for the optimization trajectories(These plots are also present in the collab notebook)

### Images


The image depicts a graph titled "Nelder-Mead Trajectory on Rosenbrock Function (2D)". The graph features a multi-colored, lattice-like grid, with purple lines representing various trajectories, and red lines indicating the Nelder-Mead trajectory. Several yellow lines illustrate the Global Minimum. A star shape in yellow marks a specific point within the Global Minimum. The x-axis and y-axis are labeled with values ranging from -2 to 3 and -1.5 to 3, respectively. The graph also includes a yellow box in the upper-right corner, which displays numerical values.

**Key Features:**

*   **Title:** Nelder-Mead Trajectory on Rosenbrock Function (2D)
*   **Grid:** Multi-colored, lattice-like grid
*   **Trajectories:** Purple lines representing various trajectories
*   **Nelder-Mead Trajectory:** Red lines indicating the Nelder-Mead trajectory
*   **Global Minimum:** Yellow lines illustrating the Global Minimum
*   **Star:** Yellow star marking a specific point within the Global Minimum
*   **Axes:** X-axis and y-axis labeled with values ranging from -2 to 3 and -1.5 to 3, respectively
*   **Yellow Box:** Upper-right corner displaying numerical values

**Visual Representation:**

The graph presents a complex, multi-dimensional visualization of the Nelder-Mead trajectory on the Rosenbrock function. The use of different colors and line styles effectively distinguishes between various trajectories and highlights the Global Minimum. The star shape in yellow serves as a clear indicator of the specific point within the Global Minimum. Overall, the graph provides a detailed and informative representation of the Nelder-Mead trajectory on the Rosenbrock function.

The provided image is a 3D plot of the Nelder-Mead Trajectory on Rosenbrock Function, which includes a line representing the trajectory and a contour plot of the function. The trajectory is represented by a red line, and the function is represented by a purple surface. The x and y axes are labeled with numerical values, and the z-axis is labeled with function values. The image also includes a legend that explains the meaning of the different colors used in the plot.

*   **Trajectory Line**
    *   The trajectory line is a red line that starts at the bottom left of the plot and moves upward and to the right.
    *   The line passes through several points on the surface of the function, indicating the path taken by the Nelder-Mead algorithm.
    *   The line ends at the top right of the plot, where the function value is highest.
*   **Rosenbrock Function**
    *   The Rosenbrock function is a 2D function that is often used as a test problem in optimization algorithms.
    *   The function has a valley-like shape, with a minimum value at the center.
    *   The function is represented by a purple surface in the plot, with contours of equal function value.
*   **Legend**
    *   The legend explains the meaning of the different colors used in the plot.
    *   The red line represents the Nelder-Mead trajectory.
    *   The purple surface represents the Rosenbrock function.
    *   The green star represents the global minimum of the function.
*   **X and Y Axes**
    *   The x-axis and y-axis are labeled with numerical values, ranging from -2 to 2.
    *   The axes are spaced at equal intervals, with tick marks at every 0.5 units.
*   **Z-Axis**
    *   The z-axis is labeled with function values, ranging from 0 to 2500.
    *   The axis is spaced at equal intervals, with tick marks at every 500 units.

Overall, the image provides a visual representation of the Nelder-Mead trajectory on the Rosenbrock function, allowing users to understand the behavior of the algorithm and the shape of the function.


## Page 7


### Images


The image is a graph of a simulated annealing trajectory on the Rosenbrock function, with the title "Simulated Annealing Trajectory on Rosenbrock Function (2D)".

*   The graph is a 2D plot with x and y axes.
    *   The x-axis ranges from -2.0 to 2.0, and the y-axis ranges from -1.0 to 3.0.
    *   The graph shows multiple curves in purple, green, blue, and yellow colors.
    *   The curves are layered on top of each other, with the purple curve being the most prominent.
    *   There are several points marked on the graph with yellow stars.
*   The graph has a legend in the top-right corner that explains the colors used for the curves.
    *   The legend indicates that the purple curve represents the "Simulated Annealing" trajectory.
    *   The green curve represents the "Global Minimum" trajectory.
    *   The blue curve represents the "Simulated Annealing" trajectory.
    *   The yellow curve represents the "Global Minimum" trajectory.
*   The graph has a grid pattern in the background, with horizontal and vertical lines separating the different sections of the graph.
    *   The grid pattern helps to visualize the shape and structure of the curves.
*   The graph has a title at the top that indicates the name of the function being plotted.
    *   The title reads "Simulated Annealing Trajectory on Rosenbrock Function (2D)".
    *   The title provides context for the graph and helps to understand the purpose of the plot.

In summary, the image is a graph of a simulated annealing trajectory on the Rosenbrock function, with multiple curves in different colors representing different trajectories. The graph has a legend that explains the colors used for the curves, and a grid pattern in the background that helps to visualize the shape and structure of the curves. The title indicates the name of the function being plotted, and provides context for the graph.

The image presents a 3D graph illustrating the trajectory of simulated annealing on the Rosenbrock function, with a title that clearly indicates its purpose. The graph is accompanied by a legend that explains the colors used in the plot.

*   **Title:** The title of the graph is "Simulated Annealing Trajectory on Rosenbrock Function (3D)".
*   **Legend:** The legend explains the colors used in the plot, with blue representing simulated annealing and yellow representing the global minimum.
*   **Graph:** The graph is a 3D plot that shows the trajectory of simulated annealing on the Rosenbrock function. The x-axis represents the input variables, the y-axis represents the output variable, and the z-axis represents the function value.
*   **Trajectory:** The trajectory of simulated annealing is represented by a blue line that starts at the global minimum and moves towards the top-right corner of the plot. The trajectory is curved, indicating that the simulated annealing algorithm is exploring different regions of the function space.
*   **Global Minimum:** The global minimum is represented by a yellow star at the bottom-left corner of the plot. The global minimum is the point at which the function has its lowest value.
*   **Function Value:** The function value is represented by the height of the plot, with higher values corresponding to points closer to the top-right corner of the plot.

Overall, the image provides a clear visualization of the trajectory of simulated annealing on the Rosenbrock function, highlighting the algorithm's ability to explore different regions of the function space and converge towards the global minimum.


## Page 8


### Images


The image presents a graph titled "CMA-ES Trajectory on Rosenbrock Function (2D)" and features a white background with black text. The graph is divided into two sections: a left-hand side and a right-hand side.

**Left-Hand Side:**

* The x-axis is labeled with values ranging from -2.0 to 2.0, while the y-axis is labeled with values ranging from -1.0 to 3.0.
* A green line represents the CMA-ES trajectory, which starts at approximately (-1.5, -0.5) and ends at around (1.5, 1.5).
* Purple lines represent the Rosenbrock function, which is a 2D function that has multiple local minima.
* Yellow lines represent the global minimum of the Rosenbrock function, which is located at (1, 1).
* A green star indicates the starting point of the CMA-ES trajectory.

**Right-Hand Side:**

* The x-axis is labeled with values ranging from 0.1 to 615.8, while the y-axis is labeled with values ranging from 0.1 to 0.3.
* A series of horizontal lines represents the function value, with the lowest value being 0.1 and the highest value being 615.8.
* A vertical line represents the CMA-ES trajectory, which starts at approximately 0.1 and ends at around 615.8.
* A yellow line represents the global minimum of the Rosenbrock function, which is located at 1.0.

Overall, the image shows the trajectory of the CMA-ES algorithm on the Rosenbrock function, with the algorithm starting at a random point and converging to the global minimum. The graph also highlights the multiple local minima of the Rosenbrock function and the global minimum, which is located at (1, 1).

The image shows a 3D graph with a purple surface and a yellow-green mountain-like shape, titled "CMA-ES Trajectory on Rosenbrock Function (3D)". The graph has a grid pattern in the background and is accompanied by a color bar on the right side, which displays values ranging from -2.0 to 2000.

*   The graph's title suggests that it represents the trajectory of the CMA-ES algorithm on the Rosenbrock function.
*   The purple surface appears to be a 3D representation of the Rosenbrock function, with the x and y axes representing the input variables and the z-axis representing the output value.
*   The yellow-green mountain-like shape superimposed on the surface may represent the optimal solution or the global minimum of the function.
*   The color bar on the right side of the graph indicates that the values range from -2.0 to 2000, suggesting that the function has a wide range of possible outputs.
*   The grid pattern in the background of the graph provides a sense of scale and helps to visualize the shape of the function.
*   Overall, the graph appears to be a visualization of the Rosenbrock function, which is a common test function used in optimization algorithms. The presence of the CMA-ES algorithm and the global minimum suggests that the graph is being used to illustrate the performance of the algorithm on this particular function.


## Page 9


### Images


This image depicts a 2D graph with a title, "Nelder-Mead on Rastrigin Function," and a color-coded legend. The graph features concentric circles in purple, green, and yellow hues, set against a pale yellow background. The legend includes four key indicators:

• Red: Nelder-Mead Path
• Red dot: Nelder-Mead Start
• Red star: Nelder-Mead End
• Gold star: Global Minimum

The x-axis spans from -4 to 4, while the y-axis ranges from -4 to 4. The graph is accompanied by a vertical column of numbers on the right side, which appears to represent a function value. The overall impression is that of a computer-generated plot.

The image depicts a 3D graph of the Nelder-Mead algorithm, a popular optimization method in machine learning and data science, demonstrating its function on the Rosenbrock function, a test problem used to evaluate optimization algorithms. The graph shows the algorithm's performance over time, with the x-axis representing the number of iterations and the y-axis representing the objective function value. The graph also includes various annotations and labels, such as the initial guess, the final solution, and the convergence criteria. The graph provides a visual representation of the algorithm's behavior and performance, allowing for easy interpretation and analysis.

*Answer*: "Nelder-Mead Optimization Algorithm on the Rosenbrock Function: A Visual Representation of Performance Over Time".


## Page 10


### Images


The image presents a visual representation of simulated annealing on the Rastrigin function, a mathematical optimization problem. The graph displays the function's values in a 2D space, with the x-axis and y-axis representing the input variables. The title "Simulated Annealing on Rastrigin Function" is prominently displayed at the top.

**Key Features:**

*   A blue line indicates the simulated annealing path, tracing the algorithm's progression.
*   Two blue dots mark the simulated annealing start and end points.
*   A yellow star represents the global minimum point.
*   The x-axis and y-axis are labeled with numerical values, ranging from -4 to 4.
*   The function values are displayed on the right side of the graph, with a range of 0 to 47.42.

**Visual Representation:**

The graph features a colorful background with a repeating pattern of circles, creating a visually appealing and complex landscape. The use of different colors for the simulated annealing path, start and end points, and global minimum point adds to the graph's clarity and readability.

**Conclusion:**

Overall, the image provides a clear and concise visualization of the simulated annealing algorithm's performance on the Rastrigin function. The graph effectively communicates the algorithm's progress and highlights the global minimum point, making it an informative and engaging visual representation of the optimization process.

The image presents a 3D graph illustrating the simulated annealing process on the Rastrigin function. The graph is titled "Simulated Annealing on Rastrigin Function (3D View)" and features a color-coded legend.

**Color-Coded Legend:**

* Blue: Simulated Annealing Path
* Blue: Simulated Annealing Start
* Blue: Simulated Annealing End
* Yellow: Global Minimum

**Graph Features:**

* The x-axis ranges from -4 to 4, with increments of 2.
* The y-axis ranges from -4 to 4, with increments of 2.
* The z-axis, representing the function value, ranges from 0 to 50, with increments of 10.
* The graph displays a 3D surface plot with multiple peaks and valleys.
* The simulated annealing path is depicted in blue, starting from the bottom left and moving upwards to the top right.
* The global minimum is marked with a yellow star at the bottom left of the graph.
* The simulated annealing start and end points are also marked with blue stars at the bottom left and top right of the graph, respectively.

**Overall Impression:**

The graph provides a clear visual representation of the simulated annealing process on the Rastrigin function. The color-coded legend and 3D surface plot allow for easy identification of the simulated annealing path, global minimum, and start and end points. The graph suggests that the simulated annealing process is able to find the global minimum, but the path taken to reach it is not necessarily the most direct.


## Page 11


### Images


The image depicts a graph illustrating the relationship between CMA-ES Path, Global Minimum, and CMA-ES End, titled "CMA-ES on Rastrigin Function." The graph is divided into two axes: the x-axis, labeled "X," and the y-axis, labeled "Y." The plot is a colorful representation of a function, with a range of colors indicating different values.

The graph features four distinct labels:

*   **CMA-ES Path:** Represented by a green line that spans from the top-left corner to the bottom-right corner of the graph.
*   **Global Minimum:** Marked by a yellow star at the center of the graph.
*   **CMA-ES End:** Indicated by a purple star at the top-left corner of the graph.

The graph also includes a legend, which provides additional information about the colors used to represent different values. The legend lists the following colors and their corresponding values:

*   **47.42:** A yellow color
*   **42.26:** A light green color
*   **37.11:** A pale green color
*   **31.95:** A light blue color
*   **26.79:** A blue color
*   **21.63:** A dark blue color
*   **16.48:** A purple color
*   **11.32:** A pink color
*   **6.16:** A light pink color
*   **1.00:** A dark pink color

Overall, the graph provides a visual representation of the relationship between CMA-ES Path, Global Minimum, and CMA-ES End, with the legend providing additional context and information about the colors used. The graph appears to be a complex and detailed representation of a mathematical function, with multiple variables and relationships being depicted.

This image is a 3D graph titled "CMA-ES on Rastrigin Function (3D View)" in the top center, accompanied by a legend in the upper right corner. The graph features a color-coded representation of the function value, with a color scale ranging from yellow to purple, and a function value axis ranging from -50 to 50. The x-axis (horizontal) and y-axis (vertical) range from -4 to 4.

The graph displays a 3D surface with a gradient of colors, indicating the function value. The 3D surface is composed of multiple hills, making it challenging to discern any patterns. However, the graph appears to show a clear distinction between the highest and lowest function values.

The legend in the upper right corner provides a key to the colors used in the graph, with yellow indicating the highest function values and purple indicating the lowest function values. The graph also includes a grid, which helps to further clarify the relationship between the x-axis, y-axis, and function value.


## Page 12


### Images


The image presents a graph illustrating the Nelder-Mead algorithm in action, showcasing its ability to navigate through a complex landscape of peaks and valleys. The graph's title, "Nelder-Mead on Ackley Function," indicates that it is specifically designed to demonstrate the algorithm's performance on this particular function.

Here are the key features of the graph:

*   **Graph Title**: The title "Nelder-Mead on Ackley Function" is prominently displayed at the top of the graph.
*   **Graph Axes**: The x-axis and y-axis are labeled with numerical values, providing a clear scale for measuring the function's output.
*   **Graph Lines and Shapes**: The graph features various lines and shapes that represent different aspects of the Nelder-Mead algorithm. These include:
    *   **Nelder-Mead Path**: A red line that represents the path taken by the algorithm as it searches for the minimum value of the function.
    *   **Nelder-Mead Start**: A yellow star that marks the starting point of the algorithm.
    *   **Nelder-Mead End**: A green star that indicates the ending point of the algorithm.
    *   **Global Minimum**: A purple circle that represents the global minimum of the function.
    *   **Function Value**: A series of vertical lines on the right-hand side of the graph that show the function value at various points along the x-axis.

In summary, the graph provides a visual representation of the Nelder-Mead algorithm's performance on the Ackley function, highlighting its ability to navigate complex landscapes and find the global minimum. The graph's clear labeling and color-coding make it easy to understand and interpret the results.

The provided image presents a 3D surface plot illustrating the Nelder-Mead optimization algorithm's performance on the Ackley function.

The surface plot displays the Ackley function's values in a 3D space, with the x-axis and y-axis representing the input variables and the z-axis representing the function's output. The plot has a range of colors, indicating different function values. The darkest red color marks the Nelder-Mead path, the red star indicates the starting point, the yellow star represents the global minimum, and the light purple color corresponds to the end point of the Nelder-Mead algorithm.

The plot is accompanied by a legend explaining the different colors and symbols used in the graph. The title of the plot, "Nelder-Mead on Ackley Function (3D View)," provides context for the visualization.

Overall, the image effectively illustrates the Nelder-Mead algorithm's performance on the Ackley function, providing a clear and concise visual representation of the optimization process.


## Page 13


### Images


The attached image presents a graph with the title "Simulated Annealing on Ackley Function". The y-axis is labeled "Function Value", and the x-axis is labeled "x". The graph displays a series of blue lines that resemble a winding path, with multiple blue dots and a yellow star marking specific points along the path. Additionally, there are several purple diamond shapes scattered throughout the graph, as well as a large purple square in the background.

The graph also includes a legend in the top-right corner, which states that the blue lines represent the "Simulated Annealing Path", the blue dots represent the "Simulated Annealing Start", and the yellow star represents the "Global Minimum". The legend also provides a scale for the y-axis, ranging from 0.33 to 47.39.

Overall, the graph appears to be a visual representation of the simulated annealing algorithm's performance on the Ackley function, with the blue path showing the algorithm's progress towards finding the global minimum. The graph provides a clear and concise visualization of the algorithm's performance, making it easier to understand and interpret the results.

The image presents a 3D graph illustrating the simulated annealing process on the Ackley function, with a title that reads "Simulated Annealing on Ackley Function (3D View)". The graph features a light blue, green, and yellow color scheme, accompanied by a legend in the top-right corner that explains the color coding.

**Key Features:**

* The graph displays a 3D surface plot of the Ackley function, which is a continuous function commonly used in optimization problems.
* The x-axis and y-axis are labeled with numerical values, ranging from -4 to 4, indicating the input variables of the function.
* The z-axis is also labeled with numerical values, ranging from -2 to 12, representing the output or objective function value.
* A blue line connects multiple points on the surface, tracing the path of the simulated annealing algorithm as it searches for the optimal solution.
* The blue dots represent the starting points of the simulated annealing process, marked by a blue dot at the origin (0, 0, 0).
* The yellow star indicates the global minimum of the Ackley function, located at approximately (0, 0, -2.6).
* The light blue, green, and yellow colors represent the simulated annealing path, start, and end points, respectively.

**Visual Insights:**

* The graph reveals that the simulated annealing algorithm starts at the origin and explores the surrounding region, gradually converging towards the global minimum.
* The path of the algorithm appears to be influenced by the Ackley function's landscape, with the algorithm oscillating between different local minima before eventually finding the global minimum.
* The color scheme effectively highlights the progress of the algorithm, with the blue path transitioning to green and yellow as it approaches the global minimum.

**Conclusion:**

The graph provides a clear visualization of the simulated annealing process on the Ackley function, demonstrating how the algorithm navigates the complex landscape to find the optimal solution. The color-coded representation and annotated features offer valuable insights into the algorithm's behavior and performance.


## Page 14


### Images


The image presents a visual representation of the CMA-ES (Coordinate Matching Adaptation Evolutionary Strategy) algorithm's performance on the Ackley function, a classic benchmark in optimization problems. The graph illustrates the algorithm's ability to navigate the complex landscape of the Ackley function, with the x-axis representing the input variables and the y-axis representing the function value.

*   **Graph Title:** CMA-ES on Ackley Function
*   **Axes:**
    *   **X-axis:** Representing the input variables
    *   **Y-axis:** Representing the function value
*   **Legend:**
    *   **CMA-ES Path:** Green line indicating the path taken by the algorithm
    *   **CMA-ES Start:** Green star marking the starting point of the algorithm
    *   **CMA-ES End:** Green diamond marking the ending point of the algorithm
    *   **Global Minimum:** Yellow star indicating the global minimum of the Ackley function
*   **Visualization:**
    *   The graph displays the CMA-ES path as a green line, with the starting point marked by a green star and the ending point marked by a green diamond.
    *   The global minimum of the Ackley function is indicated by a yellow star.
    *   The graph also shows the function value on the y-axis, ranging from 0.33 to 47.39.
*   **Key Points:**
    *   The CMA-ES algorithm is designed to optimize the Ackley function, which has multiple local minima.
    *   The algorithm's path is shown as a green line, indicating its ability to navigate the complex landscape of the Ackley function.
    *   The starting point of the algorithm is marked by a green star, and the ending point is marked by a green diamond.
    *   The global minimum of the Ackley function is indicated by a yellow star, highlighting the algorithm's ability to converge to the optimal solution.

In summary, the image provides a visual representation of the CMA-ES algorithm's performance on the Ackley function, showcasing its ability to navigate the complex landscape and converge to the global minimum. The graph illustrates the algorithm's path, starting point, ending point, and global minimum, providing valuable insights into its optimization capabilities.

The image presents a 3D surface plot, titled "CMA-ES on Ackley Function (3D View)". The plot features a color-coded representation of the Ackley function, with the x-axis and y-axis labeled as "x" and "y", respectively. The z-axis is not explicitly labeled but is represented by the colors.

**Key Features:**

*   **Surface Plot:** The surface plot displays the Ackley function in three dimensions, providing a visual representation of its behavior.
*   **Color-Coded Representation:** The plot uses a color-coded system to represent the values of the Ackley function, with different colors corresponding to specific ranges of values.
*   **Axes Labels:** The x-axis and y-axis are labeled as "x" and "y", respectively, while the z-axis is not explicitly labeled but is represented by the colors.
*   **Grid Lines:** The plot features grid lines that intersect at right angles, creating a grid-like pattern.
*   **Title:** The title of the plot is "CMA-ES on Ackley Function (3D View)", indicating that the plot is related to the CMA-ES algorithm applied to the Ackley function.

**Overall:**

The image provides a visual representation of the Ackley function in three dimensions, allowing for a better understanding of its behavior and properties. The color-coded representation and grid lines help to identify patterns and trends in the data. The title and labels provide context and clarity about the plot's content and purpose.


## Page 15


Trade-offs of each method. 
 
Nelder Mead 
Advantages: 
●​ Works well for non-differentiable functions. 
●​  Performs well on low-dimensional problems. 
Disadvantages: 
●​ Inefficient for high-dimensional problems. 
●​ Can get stuck in a local minima. 
●​ It's very sensitive to the initial guess, it did not converge when for the Ackely function 
when the initial guess was (-1, 1) but did so when it was (-0.2, 0.2). 
●​ If the function is very noisy and rapidly changes, nelder mead finds it difficult to find the 
optimal solution. 
 
Simulated Annealing 
Advantages: 
●​ Works well for non-differentiable functions. 
●​ It can escape local minima, which nelder mead generally struggles with. 
●​ Robust in non-smooth environments, and works well even in noisy environments. 
●​ Good for black-box functions. 
●​  Performs well on low-dimensional problems. 
Disadvantages: 
●​ Slow convergence, it takes a lot of iterations to converge as seen in the convergence 
speeds plots above. 
●​ Performance degrades for very large search spaces, not efficient in higher dimensional 
problems. 
 
 
CMA-ES 
Advantages: 
●​ Works well for non-differentiable functions. 
●​ Works well even in high dimensional space, which the above two optimization methods 
failed. 
●​ Robust in non-smooth environments, and works well even in noisy environments. 
●​ Good for black-box functions. 
Disadvantages: 
●​ Slow convergence, it takes a lot of iterations to converge as seen in the convergence 
speeds plots above. 
●​ Stores a full covariance matrix, making it costly for very high dimensions. 
●​ It's an overkill for small search spaces.


## Page 16


Final Conclusion 
 
●​ Use Nelder-Mead if you need a quick, low-dimensional local optimization and the given 
function is not very complex. 
 
●​ Use Simulated Annealing if there are a lot of minimas and we want to find the global 
minima, even though it takes time, but it eventually reaches the optimal solution. 
 
●​ If we are working with higher dimensional data and we have the memory capacity(to 
store the covariance matrix) we can use CMA-ES.