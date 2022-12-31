"""
The Zombie Apocaplypse!

S' = sigma - beta*S*Z - delta_S*S
I' = beta*S*Z - rho*I - delta_I*I
Z' = rho*I - alpha*S*Z
R' = delta_S*S + delta_I*I + alpha*S*Z
"""

import numpy as np

class SIZR:
    def __init__(
        self, sigma, beta, rho, delta_S, delta_I, alpha, S0, I0, Z0, R0
    ):
        for name, argument in locals().items():
            if name not in ('self', 'S0', 'I0', 'R0', 'Z0'):
                if isinstance(argument, (float, int)):
                    setattr(self, name, lambda self, value=argument: value)
                elif callable(argument):
                    setattr(self, name, argument)

        self.initial_conditions = [S0, I0, Z0, R0]

    def __call__(self, u, t):
        """RHS of system of ODEs"""

        S, I, Z, _ = u

        return np.asarray([
            self.sigma(t) - self.beta(t)*S*Z - self.delta_S(t)*S,
            self.beta(t)*S*Z - self.rho(t)*I - self.delta_I(t)*I,
            self.rho(t)*I - self.alpha(t)*S*Z,
            self.delta_S(t)*S + self.delta_I(t)*I + self.alpha(t)*I
        ])
#
# if __name__ == "__main__":
#
#     """ The three phases of the Zombie apocaplypse
#
#     Phase 1: initial phase
#     Lasts four hours. Some humans meet one zombie.
#     sigma = 20, beta = 0.03, rho = 1, S0 = 60, Z0 = 1
#
#     Phase 2: Hysteria
#     Lasts 24 hours. Zombie threat is evident.
#     beta = 0.0012, alpha = 0.0016, delta_I = 0.014, sigma = 2,
#     rho = 1
#
#     Phase 3: Counter-attack
#     Lasts five hours.
#     alpha = 0.006, beta = 0 (no humans are infected),
#     delta_S = 0.007, rho = 1, delta_I = 0.05
#     """

