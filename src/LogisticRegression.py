import numpy as np
import util

from linear_model import LinearModel

class LogisticRegression(LinearModel):
    """Standard Normalized Logistic regression."""

    def fit(self, x, y):
        """Run Newton's Method to minimize J(theta) for logistic regression.

        Args:
            x: Training example inputs. Shape (m, n).
            y: Training example labels. Shape (m,).
        """
        
        # Start Code #
        '''
        I'd recommend grabbing the number of training examples and features from the x matrix.
        Note that a 2d numpy array's shape (rows x columns) is given by array.shape (tuple).
        Next you should instantiate your theta vector with this information. I recommend using a
        1d numpy array for any vector, and 2d only for matrices. That is, your theta will have shape
        (n,). Once you have that, you can calculate the update rule. The more difficult part will be
        the log loss gradient. You won't want to do this iteratively. Numpy arrays are very fast at
        matrix multiplicaton. You can achieve this with the np.dot() method. For example:
        np.dot(<matrix with shape (m, n)>, <matrix with shape(n,)>) takes the dot product of each row
        of the first matrix and the second vector, to give an (m,) vector. Perform the update on theta
        using the batch regression rule, until the l1 norm of their difference is below the threshold.
        That is: np.linalg.norm(self.theta - previous_theta, ord=1) < self.eps.
        Check the key often to guide you.
        '''
        # End Code #        

    def predict(self, x):
        """Make a prediction given new inputs x.

        Args:
            x: Inputs of shape (m, n).

        Returns:
            Outputs of shape (m,).
        """
        # Start Code
        '''
        By the time you're using the predict method, theta is fitted already. Remember that h(theta*x) is
        the probability of a positive label. Calculate the binary labels predicted for y for the given x.
        Return the predictions.
        '''
        # End Code
