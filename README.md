
13-01-2024
- Tensor:- Someway of representing information into numbers.
- What we are going to cover:-
    - TensorFlow basics & fundamentals
    - Preprocessing data (getting it into tensors)
    - Building and using pretrained deep learning models
    - Fitting a model to the data(learning patterns)
    - Making predictions with a model(using patterns)
    - Evaluating model predictions
    - Saving and loading models
    - Using a trained model to make predictions on custom data

- TensorFlow model workflow:-
    1. Get data ready (turn into tensors).
    2. Build or pick a pretrained model(to suit your problem).
    3. Fit the model to the data and make a prediction.
    4. Evaluate the model.
    5. Improve through experimentation.
    6. Save and reload your trained model.

- How to approach this course:-
    - Write code (lots of it, follow along , let's make mistakes together)
        - Motto #1: "If in doubt, run the code"
    - Explore & experiment
        - Motto #2:"Experiment, experiment, experiment"
        - Motto #3:"Visualize, visualize, visualize" (recreate things in ways you can understand them).
    - Ask questions (including the dumb ones)
    - Do the exercises (try them yourself before looking at the solutions)
    - Share your work
    - Avoid (strictly):-
        - Overthinking the process
        - The "I can't learn it" mentality.

- What we've created so far:
    - Scalar: a single number
    - Vector: a number with direction(e.g. wind speed and direction)
    - Matrix: a 2-dimensional array of numbers
    - Tensor: an n-dimensional array of numbers (when n can be any number, a 0-dimensional tensor is a scalar, a 1-dimensional tensor is a vector)

15-01-2024
- tf.random.set_seed(42): this sets random seed at global level
- tf.random.shuffle(not_shuffled, seed=42): this sets random seed at operational level i.e. only for specific operation.


17-01-2024
| Attribute | Meaning | Code |
| --- | --- | --- |
| Shape | The length(number of elements) of each of the dimensions of a tensor. | tensor.shape | 
| Rank | The number of tensor dimensions. A scalar has rank 0, a vector has rank 1, a matrix is rank 2, a tensor has rank n | tensor.ndim |
| Axis or dimension | A particular dimension of a tensor | tensor[0], tensor[:. 1]...|
| Size | The total number of items in the tensor | tf.size(tensor) |
 

19-01-2024
- Matrix multiplication is called as dot product i.e elements of rows get multiplied with columns

20-01-2024
- tf.tensordot(a, b, axes) :- Tensordot (also known as tensor contraction) sums the product of elements from a and b over the indices specified by a_axes and b_axes.

21-01-2024
(Neural Network Regression with TensorFlow)
- What we're going to cover
    - Architecture of a neural network regression model
    - Input shapes and output shapes of a regression model (features and lables)
    - Creating custom data to view and fit
    - Steps in modelling
        - Creating a model, compiliing a model, fitting a model, evaluating a model
    - Different evaluation methods
    - Saving and loading models
    
24-01-2024
Steps in modelling with TensorFlow

1. Creating a model - define the input and output layers, as well as the hidden layers of a deep learning model.

2. Compiling a model - define the loss function and the optimizersand evaluation metrics.
    * Loss - how wrong your model's predictions are compared to the truth labels(you want to minimise this).
    * Optimizer - how your model should update its internal patterns to better its predictions.
    * Metrics - human interpretable values for how well your model is doing.

3. Fitting a model - letting the model try to find patterns between X & y (features and labels).
    * Epochs - how many times the model will go through all of the training examples.

4. Evaluate the model on the test data (how reliable are our model's predictions?)


25-01-2024
**Improving our model**

We can improve our model, by altering the steps we took to create a model.

1. **Creating a model** - here we might add more layers, increase the number of hidden units (all called neurons) within each of the hidden layers, change the activation function of each layer.

2. **Compiling a model** - here we might change the optimization funciton or perhaps the **learning rate** of the optimization function.
 
3. **Fitting a model** - here we might fit a model for more **epochs** (leave it training for longer) or on more data (give the model more examples to learn from).


**Common way to improve a deep learning model:**
- Adding layers
- Increase the number of hidden units
- Change the activation functions
- Change the optimization function
- **Change the learning rate**
- Fitting on more data
- Fitting for longer


**Evaluating a model**
When it comes to evaluation there are 3 words you should memorize:
`Visualize, visualize , visualize`

It's good idea to visualize:
* The data - what data are we working with? What does it look like?
* The model itself - what does our model look like?
* The training of a model - how does a model perform while it learns?
* The predictions of the model - how do the predictions of amodel line up against the ground truth (the original labels)?


![Alt text](image.png)

* Total params - total number of parameters in the model.
* Trainable parameters - these are the parameters(patterns) the model can update as it trains.
* Non-trainable params - these parameters aren't updated during training (this is typical when you bring in already learn patterns or parameters from other models during transfer learning)


26-01-2024
- There are two main formats we can save our model's too:
1. The SavedModel format
2. The HFF5 (.h5)

04-02-2024
| Scaling type | What it does | Scikit-Learn Function | When to use |
| --- | --- | --- | --- |
| Scale  (also referred to as normalisation) | Converts all values to between 0 and 1 while preserving the original distribution | MinMaxScaler | Use as default scaler with neural networks.|
| Standardization | Removes the mean and divides each value by the standard deviation. | StandardScaler | Transform a feature to have close to normal distribution (caution: this reduces the effect of outliers). |


06-02-2024
** Neural Network Classificaiton in TensorFlow**

What we're going to cover
* Architecture of ea neural network classifacation model
* Input shapes and output shapes of a classification model (features and labels)
* Creating custom data to view and fit
* Steps in modelling
    - Creating a model, compiling a model, fitting a model, evaluating a model
* Different classification evaluation method
* Saving and loading models


07-02-2024

A classification is where you try to classify something as one thing or another.

A few types of classification problems:
* Binary classification
* Multiclass classification
* Multilabel classification