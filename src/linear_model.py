class LinearModel(object):
    """Base class for linear models."""

    def __init__(self, g=(lambda z: z), learning_rate=1, max_iter=100, eps=1e-5,
                 theta_0=None, verbose=True):
        """
        Args:
            g: The g(h(x)) function that the model will use. This should be in the format of
                a python lambda function. The default is just the identity function.
            learning_rate: The learning rate for the iterative algorithms like Linear Regression and
                Logistic Regression. This determines the step size of the updates to theta.
            max_iter: Maximum number of iterations the algorithm will complete.
            eps: Threshold for determining convergence.
            theta_0: Initial guess for theta. If None, use the zero vector.
            verbose: Print loss values during training.
        """

        self.g = g
        self.theta = theta_0
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.eps = eps

    def fit(self, x, y):
        """Fit the model depending on whichever algorithm you're using in the child class
        of Linear Model.

        Args:
            x: Training example inputs. Shape (m, n).
            y: Training example labels. Shape (m,).
        """
        raise NotImplementedError('Subclass of LinearModel must implement fit method.')

    def predict(self, x):
        """Make a prediction given new inputs x.

        Args:
            x: Inputs of shape (m, n).

        Returns:
            Outputs of shape (m,).
        """
        raise NotImplementedError('Subclass of LinearModel must implement predict method.')
