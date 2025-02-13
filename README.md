# Old World: Center of Mass calculator
## Overview
The program calculates the center of mass for a unit composed of multiple models, each with their own position, base size, and mass (unit strength). It also provides a visual representation of the unit's formation and the center of mass.

## Installation
This project requires **Anaconda** to manage dependencies and run the program in Spyder. Follow these steps to set up the environment:

1. **Install Anaconda**:
   - Download and install Anaconda from [here](https://www.anaconda.com/download).

2. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/old-world-center-of-mass.git

Usage

    Open the center_of_mass.py file in Spyder.

    Modify the unit.add_model() calls to define your unit's models. Each model requires:

        x, y: Bottom-left corner coordinates of the model's base.

        base_size_x, base_size_y: Dimensions of the model's base in millimeters.

        mass: The unit strength (mass) of the model.

    Run the script to calculate the center of mass and visualize the unit.

I am not sure if you're supposed to calculate center of mass weighted, but that's how I did it. If not, just use the same mass and base size for all the models.

## Contributing
Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
