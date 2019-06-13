# Dynamic Mode Decomposition

Dynamic Mode Decomposition (DMD) is originated in the fluid dynamics community decomposing complex flows into a simple representation based on spatiotemporal coherent structures. DMD is an equation-free, data-driven method capable of providing an accurate decomposition of a complex system into set of dynamic modes (spatiotemporal coherent structures) from snapshots or measurements which may be utilized for short-time future state prediction and control. The objective of provided codes is to study and implement the DMD as a powerful tool for analyzing the dynamics of nonlinear systems.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on your system.

### Prerequisites

- **No configuration.**
  * you only need Python3 on your machine.

### Installing

A step by step series of examples that tell you how to get a development env running

Start with importing all necessary packages!

```
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
...
```

## Running the tests and results

An example of getting some data out of the system or using it for a little demo will be here soon!

### Break down into end to end tests

Explaination of different typse of tests on DMD / mrDMD /DMDc/ EDMD / ... and their limitations will be here soon!

```
Invariance: in translation and/or rotational invariance of low-rank objects embedded in data.
Transient phenomena: characterization of transient time phenomena
...
```

## Authors

* **Farzad F. Bigelow** - *Initial work* - [FarzadFBigelow](https://github.com/FarzadFBigelow)

## References
*1. Tu, Jonathan H., Clarence W. Rowley, Dirk M. Luchtenburg, Steven L. Brunton, and J. Nathan Kutz. "On dynamic mode decomposition: theory and applications." arXiv preprint arXiv:1312.0041 (2013).

*2. Proctor, J. L., Brunton, S. L., & Kutz, J. N. (2016). Dynamic mode decomposition with control. SIAM Journal on Applied Dynamical Systems, 15(1), 142-161.

*3. Bai, Z., Kaiser, E., Proctor, J. L., Kutz, J. N., & Brunton, S. L. (2019). Dynamic mode decomposition for compressive system    identification. AIAA Journal, 1-14.

## Acknowledgments

* Certainly, I must thank researchers, Steven L. Brunton, Nathan Kutz, Clancy Rowley for providing such precious resources and appreciate the dedicated time, effort and the patience they have considered for such precious research and making them widely available for everyone to grow as an independent researcher.
