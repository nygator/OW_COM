import matplotlib.pyplot as plt

class Model:
    def __init__(self, x, y, base_size_x, base_size_y, mass):
        self.x = x  # X coordinate (Bottom left corner)
        self.y = y  # Y Coordinate (bottom left corner)
        self.base_size_x = base_size_x  # Base width (mm)
        self.base_size_y = base_size_y  # Base height (mm)
        self.mass = mass  # Unit strength

class Unit:
    def __init__(self):
        self.models = []

    def add_model(self, model):
        self.models.append(model)

    def calculate_center_of_mass(self):
        total_mass = sum(model.mass for model in self.models)
        if total_mass == 0:
            return None
        x_com = sum((model.x + model.base_size_x / 2) * model.mass for model in self.models) / total_mass
        y_com = sum((model.y + model.base_size_y / 2) * model.mass for model in self.models) / total_mass
        return x_com, y_com

    def plot_unit(self):
        fig, ax = plt.subplots()
        for model in self.models:
            ax.add_patch(plt.Rectangle((model.x, model.y),
                                       model.base_size_x, model.base_size_y,
                                       edgecolor='black', facecolor='lightgray'))
            ax.text(model.x + model.base_size_x / 2, model.y + model.base_size_y / 2, str(model.mass), ha='center', va='center', fontsize=10, color='red')
        
        # Draw the center of mass
        com = self.calculate_center_of_mass()
        if com:
            plt.plot(com[0], com[1], 'ro', markersize=8, label='Center of mass')
        
        # Print the center of mass coordinates below the plot
        if com:
            com_text = f"Center of mass: ({com[0]:.2f}, {com[1]:.2f})"
            plt.figtext(0.5, 0.01, com_text, ha='center', va='bottom', fontsize=12, color='blue')
        
        plt.xlim(-10, 150)
        plt.ylim(-10, 150)
        plt.gca().set_aspect('equal')
        plt.legend()
        plt.grid(True)
        plt.show()

# Usage
unit = Unit()

# Add the models to the unit
unit.add_model(Model(0, 0, 25, 25, 1))  # Dwarf warrior
unit.add_model(Model(25, 0, 25, 25, 1))  # Dwarf Warrior
unit.add_model(Model(50, 0, 25, 25, 1))  # Dwarf Warrior
unit.add_model(Model(75, 0, 50, 50, 1))  # King on shieldbearers
unit.add_model(Model(0, 25, 25, 25, 1))  # Dwarf Warrior
unit.add_model(Model(25, 25, 25, 25, 1))  # Dwarf Warrior
unit.add_model(Model(50, 25, 25, 25, 1))  # Dwarf Warrior

unit.add_model(Model(0, 50, 25, 25, 1)) #Dwarf Warrior
unit.add_model(Model(25, 50, 25, 25, 1))
unit.add_model(Model(50, 50, 25, 25, 1))
unit.add_model(Model(75, 50, 25, 25, 1))
unit.add_model(Model(100, 50, 25, 25, 1))
unit.add_model(Model(0, 75, 25, 25, 1))

# Calculate and print the center of mass
center_of_mass = unit.calculate_center_of_mass()
print("Center of mass:", center_of_mass)

# Draw the unit
unit.plot_unit()