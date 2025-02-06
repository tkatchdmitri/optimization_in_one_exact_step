# Optimization in One Exact Step

What if instead of doing deep learning optimization through a series of approximate steps you took a single exact step?

If you're standing on a mountain and there are mountains all around you and you wish to get to sea level, could you figure out which way to go and how far simply by the feeling of the ground beneath your feet?

If the mountain range is infinitely differentiable then the answer is yes. Otherwise, the answer is no.

In deep learning the loss function is usually infinitely differentiable but the data is noisy. If you had infinite data and compute could you solve the optimization problem in a single step? Intuitively the answer seems to be yes.

You would simply compute all the orders of all the derivatives at the point at which you stand -- the curvature of the Earth beneath your feet.

This implies a different sort of optimization regime where you spend most of your time computing higher order derivatives at a single point instead of computing first order derivatives at many points.

Less jumping around, more direct solutions, sounds appealing right?
