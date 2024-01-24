
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

2. Compiling a model - define the loss function(in other words, the function which tells our model how wrong it is) and the optimizers(tells our model how to improve the patterns its learning) and evaluation metrics(what we can use to interpret the performance of our model).

3. Fitting a model - letting the model try to find patterns between X & y (features and labels).