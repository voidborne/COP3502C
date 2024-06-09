def kinetic_energy_calculator(mass, velocity):
    kinetic_energy = 0.5 * mass * velocity ** 2
    return kinetic_energy

def prompt_user_for_input():
    mass = float(input('Enter mass: '))
    velocity = float(input('Enter velocity: '))
    return mass, velocity

def main():
    mass, velocity = prompt_user_for_input()
    kinetic_energy = kinetic_energy_calculator(mass, velocity)
    print(f'The kinetic energy is {kinetic_energy:.2f} joules.')

if __name__=='__main__':
    main()
