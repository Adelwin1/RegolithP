from regolith_properties import RegolithProperties

class MaterialModel:
    def __init__(self, regolith_properties):
        self.regolith_properties = regolith_properties

    def calculate_deformation(self, stress):
        deformation = stress / self.regolith_properties.density
        return deformation

    def calculate_thermal_conductivity(self, temperature):
        thermal_conductivity = self.regolith_properties.thermal_conductivity * (1 + 0.01 * temperature)
        return thermal_conductivity