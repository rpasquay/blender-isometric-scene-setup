# Implementation Details

Here is the method to set up the camera explained in detail:

1. The ground plane is a square of side length $S$ and the camera is orthographic and positioned at $(S/2, -S/2, C_z)$ with rotations $X=60°, Z=45°$. What we need to find given the desired resolution is $C_z$.

2. The bottom corner of the ground plane in camera view is at $B = (S/2, -S/2, 0)$.

3. For an orthogonal camera the vertical position in the image of a point in the world is its dot product with the camera's "up" vector (local $Y$ axis). We have two rotations that we can express as matrices and multiply the $(0, 1, 0)$ local up vector with them which gives $up = (-\sin(45°)\cos(60°), \cos(45°)\cos(60°), \sin(60°))$

4. The vertical position of the bottom corner $B = (S/2, -S/2, 0)$ relative to the camera center $C = (S/2, -S/2, C_z)$ is:
$Y_B = (B - C) \cdot up = (0, 0, -C_z) \cdot (-\sin(45°)\cos(60°), \cos(45°)\cos(60°), \sin(60°)) = -C_z \sin(60°)$

5. The distance from the image center to the bottom edge is $(d/2) \cdot (height / width)$ where $width$ and $height$ are the desired width and height of the image and $d$ is the diagonal of the square ground plane, which equals the orthographic scale (i.e., the visible width in the camera view). The bottom edge is therefore at $Y_{edge} = -(d/2) \cdot (height / width)$.

6. Setting $Y_B = Y_{edge}$ gives us $-C_z \sin(60°) = -(d/2) \cdot (height / width)$. Solving for $C_z$: $C_z = d \cdot height / (2 \cdot width \cdot \sin(60°))$

Now we have the orthographic scale and position of the camera that we need to use given a desired image resolution and ground plane side length for the image to contain the ground plane viewed at $45°$ rotation around $Z$ and $60°$ rotation around $X$ right at the bottom of the image with the ground plane's left, right and bottom vertices exactly lining up with the resulting image's left, right and bottom borders.
