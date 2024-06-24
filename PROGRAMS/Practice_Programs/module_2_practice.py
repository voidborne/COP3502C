#Q1.) C

#Q2.) D

#Q3.) C

#Q4.) C

#Q5.) C

#Q6.) B

#P1

def prompt_user_for_input():
    mass = float(input('The mass is: '))
    velocity = float(input('The velocity is: '))
    return mass, velocity

def kinetic_energy_caculator(mass, velocity):
    kinetic_energy = 0.5*mass*velocity**2
    return round(kinetic_energy, 2)

def main():
    mass, velocity = prompt_user_for_input()
    kinetic_energy = kinetic_energy_caculator(mass, velocity)
    print(f'The kinetic energy is: {kinetic_energy}')

if __name__=='__main__':
    main()


#P2




