import numpy as np
from .base import ScalarField


class EigenValuesScalarField(ScalarField):
    """
    Parameters
    ----------
    ev : list of str
        Column names of the eigen values.
        Tip:
            ev = self.add_scalar_field("eigen_values", ...)
    """

    def __init__(self, *, pyntcloud, ev):
        super().__init__(pyntcloud=pyntcloud)
        self.k = ev[0].split("e1")[1]
        self.ev = ev

    def extract_info(self):
        self.ev0 = self.pyntcloud.points[self.ev[0]]
        self.ev1 = self.pyntcloud.points[self.ev[1]]
        self.ev2 = self.pyntcloud.points[self.ev[2]]


class Anisotropy(EigenValuesScalarField):
    """
    """
    def compute(self):
        name = "anisotropy{}".format(self.k)
        self.to_be_added[name] = (self.ev0 - self.ev2) / self.ev0


class Curvature(EigenValuesScalarField):
    """
    """
    def compute(self):
        name = "curvature{}".format(self.k)
        self.to_be_added[name] = self.ev2 / (self.ev0 + self.ev1 + self.ev2)


class Eigenentropy(EigenValuesScalarField):
    """
    """
    def compute(self):
        name = "eigenentropy{}".format(self.k)
        
        log_ev0 = self.ev0 * np.log(self.ev0)
        log_ev1 = self.ev1 * np.log(self.ev1)
        log_ev2 = self.ev2 * np.log(self.ev2)

        self.to_be_added[name] = -(log_ev0 + log_ev1 + log_ev2)


class EigenSum(EigenValuesScalarField):
    """
    """
    def compute(self):
        name = "eigen_sum{}".format(self.k)
        self.to_be_added[name] = self.self.ev0 + self.self.ev1 + self.self.ev2


class Linearity(EigenValuesScalarField):
    """
    """
    def compute(self):
        name = "linearity{}".format(self.k)
        
        self.to_be_added[name] = (self.ev0 - self.ev1) / self.ev0


class Omnivariance(EigenValuesScalarField):
    """
    """
    def compute(self):
        name = "omnivariance{}".format(self.k)
        
        self.to_be_added[name] = (self.ev0 * self.ev1 * self.ev2) ** (1 / 3)


class Planarity(EigenValuesScalarField):
    """
    """
    def compute(self):
        name = "planarity{}".format(self.k)
        
        self.to_be_added[name] = (self.ev1 - self.ev2) / self.ev0


class Sphericity(EigenValuesScalarField):
    """
    """
    def compute(self):
        name = "sphericity{}".format(self.k)
        
        self.to_be_added[name] = self.ev2 / self.ev0
