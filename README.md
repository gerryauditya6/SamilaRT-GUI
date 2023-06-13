# SamilaRT - GUI

This repository contains code for a graphical user interface (GUI) implementation of the SamilaRT project. SamilaRT is a generative image visualization tool that uses mathematical functions to create unique and visually interesting images.

## Getting Started

1. Clone this repository to your local machine or download the source code as a ZIP file.

2. Navigate to the directory where the code is located.

3. Install the required packages using the following command:

  ```shell
  pip install -r requirements.txt
  ```

4. Open a terminal or command prompt in that directory.

5. Run the Python file using the following command:

```
python samilartgui.py
```


6. The GUI window will appear, featuring a label, an image widget, a text input, a spinner, and a "Generate and Plot" button.

7. Enter a seed value in the text input or leave it empty to use a random seed.

8. Select a projection from the spinner. Choose from the available options: Rectilinear, Polar, Aitoff, Hammer, Lambert, and Mollweide.

9. Click the "Generate and Plot" button.

10. The code will generate two generative images based on the selected seed and projection. The images will be plotted and saved to a file.

11. The image widget will update to display the generated image.

12. Repeat steps 5 to 9 to generate and display different images with varying seed values and projections.

## Screenshot
<div>
  <img src="images/screenshot1.png" alt="Gambar 1" width="400" style="margin-right: 20px">
  <img src="images/screenshot2.png" alt="Gambar 2" width="400">
</div>

## Additional Notes

- Each combination of seed and projection will produce a unique image.

- The code utilizes mathematical functions to generate the images.

- Experiment with different seeds and projections to create visually interesting images.

- The generated images can be saved to files for further use or analysis.

- Feel free to modify the code and explore different functionalities of the SamilaRT tool.

- Enjoy exploring the creative possibilities with SamilaRT!

