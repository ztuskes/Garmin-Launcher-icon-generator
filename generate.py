import os
import xml.etree.ElementTree as ET
from xml.dom import minidom
from PIL import Image
from product_sizes import product_sizes

# Define the path for the original image (in the same folder as the script)
original_image = 'original.png'

# Get manifest.xml
manifest_path = input("Enter the path to the manifest.xml: ")

# Get the directory where the manifest.xml is located
manifest_dir = os.path.dirname(manifest_path)

# Load the manifest.xml and parse product IDs
tree = ET.parse(manifest_path)
root = tree.getroot()
namespace = {'iq': 'http://www.garmin.com/xml/connectiq'}
products = root.findall('.//iq:product', namespace)

# Function to handle integer sizes
def get_size(size):
    if isinstance(size, int):
        return size
    return None  # Return None if the size is invalid

# Function to generate formatted XML string
def prettify_xml(element):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(element, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")

# Resize the image and save launcher_icon.png in the correct folders
for product in products:
    product_id = product.attrib['id']
    
    if product_id in product_sizes:
        size = get_size(product_sizes[product_id])  # Get the size, handling both int and string formats
        if size:
            # Create folder structure inside the manifest directory: resources-{id}/drawables
            product_folder = os.path.join(manifest_dir, f'resources-{product_id}/drawables')
            os.makedirs(product_folder, exist_ok=True)

            # Resize and save launcher_icon.png
            img = Image.open(original_image)
            resized_img = img.resize((size, size))
            resized_img.save(os.path.join(product_folder, 'launcher_icon.png'))

            # Create the drawables XML
            drawables = ET.Element('drawables')
            bitmap = ET.SubElement(drawables, 'bitmap', id="LauncherIcon", filename="launcher_icon.png")

            # Save the formatted XML
            xml_content = prettify_xml(drawables)
            with open(os.path.join(product_folder, 'drawables.xml'), 'w') as f:
                f.write(xml_content)

print("Folders and resources created successfully!")
