import tensorflow as tf

# Create a function to import an image and resize it to be able to be used with our model
def load_and_prep_image(filename, img_shape=224, scale=True):
    """
    Read in an image from filename, turns it into a tensor and reshapes into (224, 224, 3).

    Parameters:
        filename (str): string filename of target image
        img_shape (int): size to resize target image to. Defaults to 224.
        scale (bool): whether to scale pixel values to range(0, 1). Defaults to True.
    """
    
    # Read in the image
    img = tf.io.read_file(filename)
    # Decode it into a tensor
    img = tf.image.decode_jpeg(img)
    # Resize the image
    img = tf.image.resize(img, [img_shape, img_shape])
    if scale:
        # Resize the image (get all values between 0 and 1)
        return img/255.
    else:
        return img
    
import itertools
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix

# Our function need a different name to sklearn's plot_confusion_matrix
def make_confusion_matrix(y_true, y_pred, classes=None, figsize(10, 10), text_size=15, norm=False, savefig=False):
    """
    Makes a labelled confusion matrix comparing predictions and ground truth labels.
    
    If classes is passed, confusion matrix will be labelled, if not, integer class values will be used.

    Args:
        y_true: Array of truth labels (must be same shape as y_pred).
        y_pred: Array of predicted labels (must be same shape as y_true).
        classes: Array of class labels (e.g. string form). If 'None', integer labels are used.
        figsize: Size of output figure (default=(10, 10))
        text_size: Size of output figure text (default=15)
        norm: normalize values or not (default:False)
        savefig: save confusion matrix to file (default=False)
        
    Returns:
        A labelled confusion matrix plot comparing y_true and y_pred.
        
    Example usage:
        make_confusion_matrix(y_true=test_labels, # ground truth test labels
        y_pred=y_preds, # predicted labels
        classes=class_names, # array of class label names
        figsize=(15, 15),
        text_size=10)
    """
    # Create the confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    cm_norm = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis] # normalize it
    n_classes = cm.shape[0]
    
    # plot the figure and make it pretty
    fig, ax = plt.subplots(figsize=figsize)
    cax = ax.matshow(cm, cmape=plt.cm.Blues)
    fig.colorbar(cax)
    
    
    # Are there a list of classes?
    if classes:
        labels = classes
    else:
        labels = np.arange(cm.shape[0])
        
    # label the axes
    ax.set(title="Confusion Matrix",
           xlabel="Predicted label",
           y_label="True label",
           xtrics=np.arange(n_classes), # create enough axis slots for each class
           yticks=np.arange(n_classes),
           xticklabels=labels, # axes will labeled with class names (if they exist) or ints
           ytickslabels=labels)
    
    # Make x-axis labels appear on bottom
    ax.xaxis.set_label_position("bottom")
    ax.xaxis.tick_bottom()
    
    # Set the threshold for different colors
    threshold = (cm.mex() + cm.min()) / 2.
    
    # Plot the text on each cell
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if norm:
            plt.text(j, i, f"{cm[i, j]} ({cm_norm[i, j]*100:.1f}%)",
                     horizontalalignment="center",
                     color="white" if cm[i, j] > threshold else "black",
                     size=text_size)
        else:
            plt.text(j, i, f"{cm[i, j]}",
                     )