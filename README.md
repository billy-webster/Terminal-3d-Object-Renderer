# 3D Renderer in Terminal

A terminal-based 3D renderer built with Python and `curses` that helped me learn fundamental computer graphics concepts using mathematical transformations and projections.

## Features

* **Multiple 3D Shapes**: Cube, Pyramid, House, and Cone
* **Interactive Controls**:

  * Mouse drag to rotate objects
  * Mouse wheel to zoom in/out
  * Press 'q' to quit
* **Real-time Rendering**: Uses terminal characters for display
* **Mathematical Foundation**: Implements core 3D graphics algorithms

## Mathematical Algorithms

### 1. Perspective Projection

The renderer converts 3D coordinates ((x, y, z)) into 2D screen coordinates ((x', y')) using **perspective projection**:

![Formula1](screenshots/sc1.png)

Where:

* (d) is the projection distance (default: 5)
* ((x, y, z)) are the 3D coordinates of a point
* ((x', y')) are the resulting 2D screen coordinates

---

### 2. Arcball Rotation

Arcball allows smooth object rotation with the mouse by mapping screen coordinates to a virtual sphere.

### 3. Line Drawing (Bresenham’s Algorithm)

To draw lines between projected points on the terminal grid:

1. Compute differences:

![Formula2](screenshots/sc2.png)

2. Determine step directions:

![Formula3](screenshots/sc3.png)

3. Initialize the error term:

![Formula4](screenshots/sc4.png)

4. Plot points iteratively and update (err) until the endpoint is reached.


---

## Usage

```bash
cd 3d-renderer
python run.py
```

* Select a shape by pressing the corresponding number key
* Use the mouse to rotate and zoom

---

## Dependencies

* Python 3.6+
* NumPy
* curses (standard library on Unix systems)

---
