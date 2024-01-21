# Image Blender

This script provides a simple GUI to blend two images together, generating a series of intermediate images that transition from the first image to the second.

## Dependencies

The script requires the following Python libraries:
- OpenCV (`cv2`)
- NumPy (`numpy`)
- Tkinter (`tkinter`)
- PIL (`PIL`)

You can install these with pip:

```bash
pip install opencv-python numpy tkinter pillow
```

## How to Use

1. Run the script. A window will open with buttons to select two images and generate intermediates.

```bash
python script_name.py
```

2. Click the "Select Image 1" button and choose an image file. The selected image will be displayed in the window.

3. Click the "Select Image 2" button and choose a second image file. The second image will be displayed below the first.

4. Click the "Generate Intermediates" button. A dialog will pop up asking for the number of intermediate images to generate. Enter a number between 1 and 100.

5. The script will generate the specified number of intermediate images, each one blending the two original images together more than the last. The images are saved in the same directory as the script, with names like "intermediate_1.png", "intermediate_2.png", etc.

6. A message will be displayed in the window indicating the number of intermediates generated and saved.

## Notes

- The script resizes the input images to be the same size before blending them. The size is determined by the smaller of the two images.
- The blending is done by linear interpolation between the pixel values of the two images.
- The script uses the Tkinter library for the GUI and the OpenCV and PIL libraries for image processing.
