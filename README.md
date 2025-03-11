# Optimization in One Exact Step

What if instead of doing deep learning optimization through a series of approximate steps you took a single exact step?

If you're standing on a mountain and there are mountains all around you and you wish to get to sea level, could you figure out which way to go and how far simply by the feeling of the ground beneath your feet?

If the mountain range is infinitely differentiable then the answer is yes. Otherwise, the answer is no.

In deep learning the loss function is usually infinitely differentiable but the data is noisy. If you had infinite data and compute could you solve the optimization problem in a single step? Intuitively the answer seems to be yes.

You would simply compute all the orders of all the derivatives at the point at which you stand -- the curvature of the Earth beneath your feet.

This implies a different sort of optimization regime where you spend most of your time computing higher order derivatives at a single point instead of computing first order derivatives at many points.

Less jumping around, more direct solutions, sounds appealing right?

## Brains

### Data

Some might say multi-step optimization is ideal because of the need to process a large amount of data continuously. How much data does a revolutionary theory require?

### Focus

Others might argue that internal thoughts must be multi-step based. Must attention span be ADD?

### Biology

Lastly, some might argue that since biological neurons can't send information backwards and thereby require mere approximations to the backpropagation algorithm within the brain, that higher order derivatives are implausible, but this is accurate only when considering one-to-one mappings of artificial neurons and synapses to biological ones.

## Generalization

Some might argue we don't want a minimum on the training data but the validation data leading to a generalization issue. However, flatter solutions generalize better and this can be guaranteed if we one-step to the point that has all higher order derivatives close to zero.

## Humans

Do humans one-stepp or n-step? Derivatives take time to compute. So possibly humans one-step but not instantenously. Perhaps dopamine has something to do with how long a human is willing to compute derivatives. 

How is this implemented in human spiking neural networks? Is spiking even a fact of nature? If you assume 1000 trillion synapses you get that the length of an axon is roughly 1/1000th of a 4 feet, which sounds reasonable.

Ignoring the spiking hypothesis for the moment and proceeding with the network hypothesis for the origins of intelligence, we might also hypothesize that the requirements for data decrease with time.
