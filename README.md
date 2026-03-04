# Isometric Scene Setup

Provides an easy way for isometric scene setup for games and rendering of 2D view space normals.

## Features

This addon adds two operators to Blender:

- Setup an isometric scene. It adds a square ground plane of a desired size and a camera that is positioned precisely so that the ground plane is aligned to the left, right and bottom borders of the image.
- Render the scene with a specific material that emits normals for 2D rendering.

## Installation

Install from https://extensions.blender.org/approval-queue/isometric-scene-setup/

## Usage

Both functions can be found in Blender's 3D view in the sidebar (shortcut: N). Look for a tab called "Isometric".

## Functions

### Scene setup

This function adds a camera and a plane. You can specify the side length of the square ground plane.

The camera it adds can be configured in terms of desired resolution and is positioned so that the ground plane's left, bottom and right vertices align with the image's left, bottom and right borders.

![Scene setup panel](screenshots/Screenshot%202026-03-03%20at%2015.34.52.png)

### 2D Normals

This function renders the scene with a material override. The material that is being used transforms the 3D normals of the object to view space and renders them out to an image.

This image then can be used as a normal map for 2D sprites in Game Engines like Godot.

![Normal map panel](screenshots/Screenshot%202026-03-03%20at%2015.36.48.png)

![Rendered normal map](screenshots/Screenshot%202026-03-03%20at%2015.36.08.png)

![Standard render for comparison](screenshots/Screenshot%202026-03-03%20at%2015.36.40.png)

For implementation details on how the camera position is calculated, see [IMPLEMENTATION.md](IMPLEMENTATION.md).

## Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency management and [fake-bpy-module](https://github.com/nutti/fake-bpy-module) as a type stub for Blender's `bpy` API, enabling autocompletion and type checking outside of Blender.

Setup:

```sh
uv sync
```

This installs `fake-bpy-module-latest` as a dev dependency, which provides type stubs for `bpy` so that editors and tools like mypy can resolve Blender API types.

The addon was scaffolded and is developed using the [Blender Development](https://marketplace.visualstudio.com/items?itemName=JacquesLucke.blender-development) VS Code extension by Jacques Lucke, which allows starting Blender from VS Code, live-reloading addons on save and debugging with breakpoints.

### Building

To build the extension as a `.zip`, run your local Blender executable from the terminal:

```sh
/path/to/blender --command extension build
```

On macOS this is typically:

```sh
/Applications/Blender.app/Contents/MacOS/Blender --command extension build
```

This produces a `.zip` file in the project root that can be installed in Blender.

## Acknowledgements

Special thanks to [CG Cookie](https://cgcookie.com/) and their course "Utility" on Blender addon development. 🍪 🧡
