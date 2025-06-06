---
orphan: true
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.7
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(docs-magpylib-force)=
# Magpylib Force v0.3.1

The package `magpylib-force` provides an addon for magnetic force and torque computation between magpylib source objects.

## Installation

Install `magpylib-force` with pip:

```console
pip install magpylib-force
```

## API

The package provides only a single top-level function <span style="color: orange">**getFT()**</span> for computing force and torque.

```python
import magpylib_force as mforce

mforce.getFT(sources, targets, anchor, eps=1e-5, squeeze=True)
```

Here `sources` are Magpylib source objects that generate the magnetic field. The `targets` are the objects on which the magnetic field of the sources acts to generate force and torque. With current version 0.3.1 only `Cuboid`, `Cylinder`, `CylinderSegment`, `Polyline`, and `Circle` objects can be targets. The `anchor` denotes an anchor point which is the barycenter of the target. If no barycenter is given, homogeneous mass density is assumed and the geometric center of the target is chose as it's barycenter. `eps` refers to the finite difference length when computing the magnetic field gradient and should be adjusted to be much smaller than size of the system. `squeeze` can be used to squeeze the output array dimensions as in Magpylib's `getB`, `getH`, `getJ`, and `getM`.

The computation is based on numerically integrating the magnetic field generated by the `sources` over the `targets`, see [here](docs-force-computation) for more details. This requires that each target has a <span style="color: orange">**meshing**</span> directive, which must be provided via an attribute to the object. How `meshing` is defined:

For all objects as an integer, which defines the target number of mesh-points. In some cases an algorithm will attempt to come close to this number by splitting up magnets into quasi-cubical cells. Exceptions are:

- `Cuboid`: takes also a 3-vector that defines the number of equidistant splits along each axis resulting in a rectangular regular grid. Keep in mind that the accuracy is increased by cubical aspect ratios.
- `PolyLine`: defines the number of equidistant splits of each PolyLine segment, not of the whole multi-segmented object. The total number of mesh-points will be number of segments times meshing.

The function `getFT()` returns force and torque as `np.ndarray` of shape (2,3), or (t,2,3) when t targets are given.

The following example code computes the force acting on a cuboid magnet, generated by a current loop.

```python
import magpylib as magpy
import magpylib_force as mforce

# create source and target objects
loop = magpy.current.Circle(diameter=2e-3, current=10, position=(0, 0, -1e-3))
cube = magpy.magnet.Cuboid(dimension=(1e-3, 1e-3, 1e-3), polarization=(1, 0, 0))

# provide meshing for target object
cube.meshing = (5, 5, 5)

# compute force and torque
FT = mforce.getFT(loop, cube)
print(FT)
# [[ 1.36304272e-03  6.35274710e-22  6.18334051e-20]  # force in N
#  [-0.00000000e+00 -1.77583097e-06  1.69572026e-23]] # torque in Nm
```

```{warning}
[Scaling invariance](guide-docs-io-scale-invariance) does not hold for force computations! Be careful to provide the inputs in the correct units!
```

(docs-force-computation)=
## Computation details

The force $\vec{F}_m$ acting on a magnetization distribution $\vec{M}$ in a magnetic field $\vec{B}$ is given by

$$\vec{F}_m = \int \nabla (\vec{M}\cdot\vec{B}) \ dV.$$

The torque $\vec{T}_m$ which acts on the magnetization distribution is

$$\vec{T}_m = \int \vec{M} \times \vec{B} \ dV.$$

The force $\vec{F}_c$ which acts on a current distribution $\vec{j}$ in a magnetic field is

$$\vec{F}_c = \int \vec{j}\times \vec{B} \ dV.$$

And there is no torque. However, one must not forget that a force, when applied off-center, adds to the torque as

$$\vec{T}' = \int \vec{r} \times \vec{F} \ dV,$$

where $\vec{r}$ points from the body barycenter to the position where the force is applied.

The idea behind `magplyib-force` is to compute the above integrals by discretization. For this purpose, the target body is split up into small cells using the object `meshing` attribute. The force and torque computation is performed for all cells in a vectorized form, and the sum is returned.
