'''
Name: Angelina Patterson
Start Date: 7/3/25
Description: The purpose of this program is to simulate the results from Figure 1 of Section 2.21.
Reference: Example 1 under section 2.21 from the paper "Artificial Chemistries—A Review" by "P . Dittrich et al. "
'''
import numpy as np
import matplotlib.pyplot as plt
import random
#Define molecules
molecules = {"A": 5, "B": 5} # store into a dictionary
# keeps tracks of the reactions that occur while the program runs
updated_molecules = []
#Define the reactions r1 - r4
def r1(molecules):
    if molecules["A"] >= 2:
        molecules["B"] += 1
    # for returning a value
        return True
    return None
def r2(molecules):
    if molecules["A"] >= 1 and molecules["B"] >= 1:
        molecules["B"] += 1
        return True
    return None
def r3(molecules):
    if molecules["B"] >= 1 and molecules["A"] >= 1:
        molecules["B"] += 1
        return True
    return None
def r4(molecules):
    if molecules["B"] >= 2:
        molecules["A"] += 1
        return True
    return None
# store r1 - r4 into an array to be randomly selected
reactions = [r1, r2, r3, r4]
# loop to apply the reactions at random for a certain amount of steps
step = 1
# for retrying
retry = 0
while step <= 10:
    # random selection of reactions
    rand_rxn = random.choice(reactions)
    # set for checking if enough molecules to run
    run_results = rand_rxn(molecules)
    # if a reactions occurs append to the empty array and break to step in the loop
    if run_results:
        # convert molecule count to %
        total = molecules["A"] + molecules["B"]
        percentage_A = (molecules["A"] / total) * 100
        percentage_B = (molecules["B"] / total) * 100
        updated_molecules.append((step,percentage_A, percentage_B))
        # step up by to run the loop again and looks to apply the reactions once more
        step += 1
        # rest counter if needed
        retry = 0
    # increasing retry counter each time it fails
    else:
        retry += 1
    # to keep it not infinitely retrying it will stop if this condition is met
    if retry >= 10:
        break
# plot the reactions on to a plot
# Unpack the tuples into separate step, concentration a and b
steps, Concentration_A, Concentration_B = zip(*updated_molecules)
# creating the plot
plt.figure(figsize=(10, 5))
plt.plot(steps, Concentration_A, label="Concentration of A ( %)", color="blue")
plt.plot(steps, Concentration_B, label="Concentration of B ( %)", color="orange")
# Labels for the plot
plt.xlabel("Step")
plt.ylabel("Concentration %")
plt.title("Concentration of A and B for a population m = 10")
plt.legend()
plt.grid(True)
# print the plot
plt.show()










