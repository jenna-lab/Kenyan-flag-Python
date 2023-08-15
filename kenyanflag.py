import matplotlib
matplotlib.use('TkAgg') 
import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patches

 
#  plotting the colors
a = patches.Rectangle((0, 7), width=9, height=2, facecolor="#000000", edgecolor="grey")
b = patches.Rectangle((0, 6.8), width=9, height=0.4, facecolor="#FFFFFF", edgecolor="grey")
c = patches.Rectangle((0, 5), width=9, height=2, facecolor="#FF0000", edgecolor="grey")
d = patches.Rectangle((0, 4.8), width=9, height=0.4, facecolor="#FFFFFF", edgecolor="grey")
e = patches.Rectangle((0, 3), width=9, height=2, facecolor="#008000", edgecolor="grey")

m,n = py.subplots()
n.add_patch(a)
n.add_patch(b)
n.add_patch(c)
n.add_patch(d)
n.add_patch(e)

# kenyan shield



# Set the limits of the plot
n.set_xlim(0, 9)
n.set_ylim(0, 11) 

# Remove the x and y ticks
n.set_xticks([])
n.set_yticks([])

# Save the figure to a file
py.savefig('kenyan_flag.png', bbox_inches='tight', dpi=300)

n.axis('equal')

# Display the image
py.show()