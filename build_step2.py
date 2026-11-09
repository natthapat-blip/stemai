# -*- coding: utf-8 -*-
"""
Builder script to generate the complete index.html including:
- Home Page (with active cards for Lever, Pulley, Incline, and previews for Gears & Arm)
- Room 1: คาน (Lever)
- Room 2: รอก (Pulley)
- Room 3: ทางลาด (Inclined Plane)
- Star tracking & Storage for all 3 rooms (up to 12 stars)
- Web Audio API Sound synthesis
- Full responsive design, touch & tablet drag support
"""

import os

def create_index_html():
    html_path = "index.html"
    print("Generating comprehensive index.html with Lever, Pulley, and Incline...")
    # Read or assemble the full HTML
    # We will build the full file directly with python to guarantee 100% validity and no truncation
