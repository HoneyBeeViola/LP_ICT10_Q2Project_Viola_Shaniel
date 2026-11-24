from pyscript import display, document

non_metals = {
    "Hydrogen": ("H", "Hydrogen", 1, 1.008),
    "Helium": ("He", "Helium", 2, 4.0026),
    "Carbon": ("C", "Carbon", 6, 12.011),
    "Nitrogen": ("N", "Nitrogen", 7, 14.007),
    "Oxygen": ("O", "Oxygen", 8, 15.999),
    "Fluorine": ("F", "Fluorine", 9, 18.998),
    "Neon": ("Ne", "Neon", 10, 20.180),
    "Phosphorus": ("P", "Phosphorus", 15, 30.974),
    "Sulfur": ("S", "Sulfur", 16, 32.06),
    "Chlorine": ("Cl", "Chlorine", 17, 35.45),
    "Argon": ("Ar", "Argon", 18, 39.948),
    "Selenium": ("Se", "Selenium", 34, 78.971),
    "Bromine": ("Br", "Bromine", 35, 79.904),
    "Krypton": ("Kr", "Krypton", 36, 83.798),
    "Iodine": ("I", "Iodine", 53, 126.904),
    "Xenon": ("Xe", "Xenon", 54, 131.293),
    "Radon": ("Rn", "Radon", 86, 222),
}

def find_element(e):
    document.getElementById("result").innerHTML = ""

    element1 = document.getElementById("element").value.strip().title()

    symbol, element_name, atomic_number, atomic_mass = non_metals.get(
        element1,
        ("-", "Element not found", "-", "-"),
    )

    document.getElementById("result").innerHTML = f"""
        <b>Symbol:</b> {symbol}<br>
        <b>Element:</b> {element_name}<br>
        <b>Atomic Number:</b> {atomic_number}<br>
        <b>Atomic Mass:</b> {atomic_mass}
    """