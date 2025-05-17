# L.E.A.D.
The LED Enabled Automated Database is an electronics sorting program that integrates with the DigiKey API to allow you to quickly scan or manually add components to your system. As well as led integration to allow you to create physical location indicators.

# Brief Overview
L.E.A.D. is a free, open source project designed to simplify the management of electronic component inventories. By seamlessly integrating the Digikey API, L.E.A.D. automatically fetches up-to-date component details, so you don't have to spend hours entering data manually. With its built-in LED-based visual tracking, locating parts in your storage becomes as simple as a glance. Developed with a focus on minimal setup and maximum flexibility, L.E.A.D. is perfect for makers, hobbyists, and professionals who want a hassle-free, community-driven solution for their inventory challenges. Contributions and customizations are warmly welcomed as the project evolves.

# Features
+ Digikey API Search
+ Component Cataloguing
+ Component Search
+ Physical output to integrate into physical location tracking
+ Barcode Scanning

# How It Works
## DigiKey API Integration
The system interfaces with DigiKey’s API. When a user inputs a part number, L.E.A.D. sends a request to DigiKey's API. The response includes detailed product information such as pricing, stock availability, manufacturer details, and datasheets. This data is then stored in the component catalog for future reference.

## Barcode Parsing & Manual Entry
The system supports barcode scanning to quickly decode component information. The barcode decoder extracts part numbers and quantities, which are then verified against the existing database. If a part is not found in DigiKey’s database, users are given the option to manually add it. The system also automatically assigns storage locations for newly added parts.

## LED-Based Location Identification
Each component is assigned a unique location code within the storage system. A custom LED control system communicates with an Arduino to illuminate the corresponding LED, visually guiding users to the exact location of a part. When a component is checked out, the system prompts the user to confirm its retrieval and turns off the LED once the part is replaced.

## Automated Inventory Management
The backend system maintains a component catalog in JSON format, logging stock levels, part numbers, and locations.
A low-stock alert system identifies components that are running low and flags them in the user interface.
A Bill of Materials (BOM) processing feature allows users to import BOM files, checking part availability and automatically updating stock levels.
User Interface & Control

The frontend is built using Tkinter, providing an intuitive UI for searching, adding, and managing components.
A search function enables users to filter parts by part number, location, or type.
Bulk operations allow for scanning and adding multiple parts at once.

# Setup
This guide will walk you through downloading the code from GitHub, getting a DigiKey API key, and configuring the config file to link everything together.

## Downloading and Running Program
This is a basic overview on downloading and running the program. This is for beginners feel free to ignore.

### Dowloading From GitHub
1. Click on the Code button near the top right of the page
2. Select Download zip
3. Extract the zip file
4. Install requirements.txt
5. Run the main file to start the program

## Digikey API
To interact with DigiKey's API, you need an API key.

### Steps to Obtain a DigiKey API Key:
Create a DigiKey Developer Account:

1. Go to DigiKey [API Portal](https://developer.digikey.com)
2. Sign in or create an account.
#### Register for API Access:
1. Navigate to Organizations
2. Create new organization and name it
3. Next select "Create New Production App"
4. Name you App and enable "ProductInformation V4"
5. Save and go to view tab here you will find your Client Id and Client Secret. Save these as they are needed for the your app script

### Digikey API Setup
1. Rename config_template.json in the config directory to config.json
2. Fill in the Blank Client ID and Client Secret sections in config.json

# Using L.E.A.D.
After opening the program you are left on a main menu page that lists types of components in the system. As well as any that have reached low stock. Your main navigation is throught the navigation button at the top left, the Add menu allows you to manually add components and they're data. Alternatively you can scan in a barcode. The search menu is fairly self explanitory. In the add and search menues you can double click to ecit or highlight a component.



