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
        
        # We are fed numpy arrays with the given shapes for x and y. This problem does not have a theta0
        # intercept column.
        # set our x and y dimension variable
        m_samples = x.shape[0]
        n_features = x.shape[1]
        
        # We'll first create a new theta vector. Remember it should be the same length as the number
        # of features of the x matrix (including the intercept column if we have one).
        if self.theta is None:
            self.theta = np.zeros(n_features)

        count = 0
        while True:
            if count % 3000 == 0:
                print("Theta on iteration " + str(count), self.theta)
            count += 1
            previous_theta = np.copy(self.theta)

            # Prepare our theta times x argument to be fed into the g function.
            theta_x_arg = np.dot(x, previous_theta)

            # Create our ell gradient function.
            ell_grad = (1 / m_samples) * np.dot(x.T, y - self.g(theta_x_arg))

            # Update your theta.
            self.theta = previous_theta + self.learning_rate * ell_grad
                        
            # Check to see that the new theta is within our threshold for determining convergence.
            if np.linalg.norm(self.theta - previous_theta, ord=1) < self.eps:
                break

    def predict(self, x):
        """Make a prediction given new inputs x.

        Args:
            x: Inputs of shape (m, n).

        Returns:
            Outputs of shape (m,).
        """
        # compute probability
        probs = self.g(np.matmul(x, self.theta))
        # (probs >= .5) gives a numpy array of booleans, to which you apply the astype method. As an int type,
        # False is 0 and True is 1. So this gives binary labels.
        predictions = (probs >= 0.5).astype(np.int)
        return predictions
