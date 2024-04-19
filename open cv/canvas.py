import cv2
import numpy as np

# Create a blank canvas
canvas = np.zeros((500, 500, 3), dtype="uint8")

# Set up text properties
text = "Hello World!"
position = (50, 200)  # Coordinates
font_scale = 1         # Font scaling factor
color = (255, 255, 255)  # Text color (white)
thickness = 2          # Line width

# Choose desired font style from available options
font = cv2.FONT_HERSHEY_SIMPLEX

# Add text onto the canvas
cv2.putText(canvas, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

# Display the final output
cv2.imshow("Output", cv2.cvtColor(canvas, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()