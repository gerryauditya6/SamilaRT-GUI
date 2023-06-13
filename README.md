# SamilaRT - GUI

This repository contains code for a graphical user interface (GUI) implementation of the SamilaRT project. SamilaRT is a generative image visualization tool that uses mathematical functions to create unique and visually interesting images.

## Prerequisites

Before running the code, ensure that you have the following dependencies installed:

- Kivy framework

You can install the Kivy framework using the following command:

```
pip install kivy
```

## Getting Started

1. Clone this repository to your local machine or download the source code as a ZIP file.

2. Navigate to the directory where the code is located.

3. Open a terminal or command prompt in that directory.

4. Run the Python file using the following command:

```
python samilartgui.py
```


5. The GUI window will appear, featuring a label, an image widget, a text input, a spinner, and a "Generate and Plot" button.

6. Enter a seed value in the text input or leave it empty to use a random seed.

7. Select a projection from the spinner. Choose from the available options: Rectilinear, Polar, Aitoff, Hammer, Lambert, and Mollweide.

8. Click the "Generate and Plot" button.

9. The code will generate two generative images based on the selected seed and projection. The images will be plotted and saved to a file.

10. The image widget will update to display the generated image.

11. Repeat steps 6 to 10 to generate and display different images with varying seed values and projections.

## Additional Notes

- Each combination of seed and projection will produce a unique image.

- The code utilizes mathematical functions to generate the images.

- Experiment with different seeds and projections to create visually interesting images.

- The generated images can be saved to files for further use or analysis.

- Feel free to modify the code and explore different functionalities of the SamilaRT tool.

- Enjoy exploring the creative possibilities with SamilaRT!

## Screenshot
![SamilaRT GUI](images/screenshot1.png)
![SamilaRT GUI](images/screenshot2.png)
