"""NFT Crypto Billionaire Script

This Python3 program creates a single 2000px square image from scratch to be later minted and sold as a popular high-valued NFT.

NFTs are traded and sold, thus I would like to optimize towards popularity in terms of subject matter, coloring, style, etc...

That said, the following topics can be helpful to explore:
- Markovian Theory / Stochastic Processes
- Chaos Theory
- Game Theory
- Blockchain & Cryptocurrency
- Economics
- Physics
- Biology
- Color Theory
- Color Blending
- Linear Algebra
- Image Processing
- Image Manipulation
- Image Editing
"""

# Imports
from PIL import Image, ImageDraw
import random
import sys
import os
import colorsys
from colour import Color
import seaborn as sns
import numpy as np
import math

# Global Variables
preppy_pastel_colors = ['#F8B195', '#F67280', '#C06C84', '#6C5B7B', '#355C7D', '#1B1464', '#845EC2', '#D65DB1', '#FF6F91', '#FF9671', '#FFC75F', '#F9F871', '#D0EC64', '#91D400', '#4DB700', '#00B3A4', '#00B894', '#00A99D', '#00A093', '#018270', '#005056', '#1F618D', '#3B5998', '#536DFE', '#6C5B7B', '#8E44AD', '#C0392B', '#D35400', '#E67E22', '#F39C12', '#F1C40F', '#F1C40F', '#F39C12', '#E67E22', '#D35400', '#C0392B', '#8E44AD', '#6C5B7B', '#536DFE', '#3B5998', '#1F618D', '#005056', '#00A093', '#00A99D', '#00B894', '#00B3A4', '#91D400', '#D0EC64', '#F9F871', '#FFC75F', '#FF9671', '#FF6F91', '#D65DB1', '#845EC2', '#355C7D', '#1B1464', '#6C5B7B', '#C06C84', '#F67280', '#F8B195']
preppy_pastel_colors = [Color(color).get_rgb() for color in preppy_pastel_colors]

# Functions
def get_random_color(pastel_colors=True):
    """Returns a random color (r, g, b) tuple with values between 0 and 255.

    Keyword arguments:
    pastel_colors -- Boolean indicating whether to return a pastel color or a random color
    """
    if pastel_colors:
        return random.choice(preppy_pastel_colors)
    else:
        return tuple([random.randrange(256) for _ in range(3)])

def create_image(width, height, color):
    """Create a blank image of the given width, height, and color."""
    image = Image.new('RGB', (width, height), color)
    return image
