from build_house_with_doors_entry import BuildHouseWithDoorsEntry
from build_house_with_garage_entry import BuildHouseWithGarageEntry

def build_house_with_doors():
  house = BuildHouseWithDoorsEntry()
  return house.buildHouse()

def build_house_with_garage():
  house = BuildHouseWithGarageEntry()
  return house.buildHouse()

def main():
  print("Construyendo casa con puertas en la entrada:")
  steps = build_house_with_doors()
  for step in steps:
    print(step)

  print("\nConstruyendo casa con garaje en la entrada:")
  steps = build_house_with_garage()
  for step in steps:
    print(step)

if __name__ == "__main__":
  main()