
# Garmin Resource Generator

This repository contains a Python script designed to automate the creation of Garmin device-specific resource folders and files, based on the products listed in a Garmin Connect IQ `manifest.xml`. The script generates the necessary folder structure, resizes launcher icons based on product specifications, and creates a `drawables.xml` file for each product.

## Features

- Parses a `manifest.xml` file to extract Garmin product IDs.
- Automatically generates `resources-{product_id}/drawables` folders.
- Resizes a `launcher_icon.png` image based on predefined sizes for each product.
- Creates a `drawables.xml` file for each product, referencing the resized launcher icon.
- Uses a predefined list of product IDs and icon sizes stored in `product_sizes.py`.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed **Python 3.x** on your machine.
- You have installed the necessary Python libraries (`Pillow` for image processing).

## Installation

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/garmin-resource-generator.git
   cd garmin-resource-generator
   ```

2. **Install the Required Libraries**

   Use `pip` to install the required dependencies:

   ```bash
   pip install Pillow
   ```

   `Pillow` is the Python Imaging Library used to handle image resizing.

3. **Prepare the Files**

   - Place the original launcher icon image (e.g., `original.png`) in the same directory as the script. This image will be resized for each product.
   - Ensure that you have a valid `manifest.xml` file, which contains the product IDs to generate resources for.

## Setup

1. **Ensure the Following Files Are in the Directory:**

   - `generate.py`: The main script that automates the folder and resource creation.
   - `product_sizes.py`: A Python module containing a predefined list of Garmin product IDs and corresponding icon sizes.
   - `original.png`: The original launcher icon to be resized for each product.
   - `manifest.xml`: The Garmin Connect IQ manifest file with a list of products.

   The directory structure should look like this:

   ```
   garmin-resource-generator/
   ├── generate.py
   ├── product_sizes.py
   ├── original.png
   └── manifest.xml
   ```

2. **Edit `product_sizes.py` (Optional)**

   If necessary, update `product_sizes.py` with new Garmin product IDs or change icon sizes. The file contains a dictionary mapping product IDs to their icon sizes in pixels.

   Example `product_sizes.py`:

   ```python
   # product_sizes.py

   product_sizes = {
       "venu2": 70,
       "epix2": 60,
       "fr965": 65
   }
   ```

## How to Run

1. **Place the Files in the Same Directory:**

   Ensure that `manifest.xml` and `original.png` are in the same directory as the `generate.py` script.

2. **Run the Script:**

   To run the script, use the following command:

   ```bash
   python generate.py
   ```

3. **Provide the Path to `manifest.xml`:**

   The script will prompt you to enter the path to the `manifest.xml` file. For example:

   ```bash
   Enter the path to the manifest.xml: /path/to/your/manifest.xml
   ```

4. **Script Behavior:**

   - The script reads the `manifest.xml` file and extracts the list of Garmin product IDs.
   - For each product found in the manifest, it generates a folder structure in the format `resources-{product_id}/drawables`.
   - The `original.png` image is resized according to the predefined size for each product and saved as `launcher_icon.png` in the respective folder.
   - A `drawables.xml` file is created in each folder, referencing the resized launcher icon.

## Example Workflow

1. **Example `manifest.xml`:**

   Below is an example of what your `manifest.xml` might look like:

   ```xml
   <iq:manifest xmlns:iq="http://www.garmin.com/xml/connectiq" version="3">
       <iq:application entry="App" id="example-app-id" launcherIcon="@Drawables.LauncherIcon" minSdkVersion="4.2.0" name="@Strings.AppName" type="watchface" version="1.0.7">
           <iq:products>
               <iq:product id="venu2"/>
               <iq:product id="epix2"/>
           </iq:products>
       </iq:application>
   </iq:manifest>
   ```

   When running the script with this manifest, the script will generate resource folders for `venu2` and `epix2`.

2. **Output Folder Structure:**

   After running the script, your folder structure will look like this:

   ```
   resources-venu2/
   └── drawables/
       ├── launcher_icon.png
       └── drawables.xml

   resources-epix2/
   └── drawables/
       ├── launcher_icon.png
       └── drawables.xml
   ```

3. **Sample `drawables.xml`:**

   Each `drawables.xml` will contain the following content:

   ```xml
   <drawables>
       <bitmap id="LauncherIcon" filename="launcher_icon.png" />
   </drawables>
   ```

## Customization

1. **Modify Icon Sizes:**

   If you need to modify the icon sizes for specific Garmin products, you can update the `product_sizes.py` file. This file contains a dictionary where the keys are product IDs and the values are their respective icon sizes.

   Example:

   ```python
   product_sizes = {
       "venu2": 70,
       "epix2": 60,
       "fr965": 65
   }
   ```

2. **Handling Different Manifest Files:**

   Ensure that your `manifest.xml` follows the Garmin Connect IQ standard format. If needed, you can adjust the script to accommodate specific manifest formats.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributions

Feel free to fork this repository and submit pull requests if you'd like to contribute. Please make sure to follow the standard coding practices and include proper documentation for any changes.

## Contact

For any questions or support, you can reach out via GitHub or by opening an issue in the repository.
