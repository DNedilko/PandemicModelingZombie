import numpy as np
from tqdm import tqdm

class ODESolver:

    def __init__(self, f):
        self.f = f

    def set_initial_conditions(self, U0):

        if isinstance(U0, (int, float)):

            self.number_of_eqns = 1
            U0 = float(U0)
        else:
            # System of eqns
            U0 = np.asarray(U0)
            self.number_of_eqns = U0.size
        self.U0 = U0

    def solve(self, time_points):

        self.t = np.asarray(time_points)
        n = self.t.size

        self.u = np.zeros((n, self.number_of_eqns))

        self.u[0, :] = self.U0

        # Integrate
        for i in tqdm(range(n - 1), ascii=True):
            self.i = i
            self.u[i + 1] = self.advance()

        return self.u, self.t

        def advance(self):

            raise NotImplementedError


class RungeKutta4(ODESolver):
    def advance(self):
        u, f, i, t = self.u, self.f, self.i, self.t
        dt = t[i + 1] - t[i]
        dt2 = dt / 2
        K1 = dt * f(u[i, :], t[i])
        K2 = dt * f(u[i, :] + 0.5 * K1, t[i] + dt2)
        K3 = dt * f(u[i, :] + 0.5 * K2, t[i] + dt2)
        K4 = dt * f(u[i, :] + K3, t[i] + dt)
        return u[i, :] + (1 / 6) * (K1 + 2 * K2 + 2 * K3 + K4)

class ForwardEuler(ODESolver):
    def advance(self):
        u, f, i, t = self.u, self.f, self.i, self.t
        dt = t[i + 1] - t[i]
        return u[i, :] + dt * f(u[i, :], t[i])