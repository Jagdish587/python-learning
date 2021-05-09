import math
import argparse

def volume_of_cylinder(radius, weight):
    vol = (math.pi) * (radius ** 2) * (weight)
    return vol

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-r', '--radius', type=int , required= True, help = 'Radius of integer')
parser.add_argument('-w', '--weight', type=int , required= True, help = 'weight of integer')
args = parser.parse_args()


if __name__ == '__main__':
    vol = volume_of_cylinder(args.radius, args.weight)
    print(f"volume of cylinder = {vol} ")