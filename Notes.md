
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