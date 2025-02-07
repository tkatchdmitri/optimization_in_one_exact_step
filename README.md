# Optimization in One Exact Step

What if instead of doing deep learning optimization through a series of approximate steps you took a single exact step?

If you're standing on a mountain and there are mountains all around you and you wish to get to sea level, could you figure out which way to go and how far simply by the feeling of the ground beneath your feet?

If the mountain range is infinitely differentiable then the answer is yes. Otherwise, the answer is no.

In deep learning the loss function is usually infinitely differentiable but the data is noisy. If you had infinite data and compute could you solve the optimization problem in a single step? Intuitively the answer seems to be yes.

You would simply compute all the orders of all the derivatives at the point at which you stand -- the curvature of the Earth beneath your feet.

This implies a different sort of optimization regime where you spend most of your time computing higher order derivatives at a single point instead of computing first order derivatives at many points.

Less jumping around, more direct solutions, sounds appealing right?

## Humans

Some might say multi-step optimization is ideal because of the need to process a large amount of data continuously. How much data intake did Einstein require during his invention of relativity?

Others might argue that internal thoughts must be multi-step based. What was Einstein's attention span like?

Lastly, some might argue that since biological neurons can't send information backwards and thereby require mere approximations to the backpropagation algorithm within the brain, that higher order derivatives are implausible, but this is only accurate when considering only one-to-one mappings of artificial neurons and synapses to biological ones.

Related: https://proceedings.neurips.cc/paper_files/paper/2018/file/0a1bf96b7165e962e90cb14648c9462d-Paper.pdf
