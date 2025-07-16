'''
Name: Angelina Patterson
Start Date: 7/3/25
Description: The purpose of this program is to simulate the results from Figure 1 of Section 2.21.
Second practice attempt with no random selection.
Reference: Example 1 under section 2.21 from the paper "Artificial Chemistries—A Review" by P Dittrich et al. 
'''
import numpy as np
import matplotlib.pyplot as plt
import random
#Define molecules
molecules = {"A": 5, "B": 5} # store into a dictionary
# keeps track of the reactions that occur while the program runs
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
# Store r1-r4 into an array to be randomly selected
reactions = [r1, r2, r3, r4]
for step in range(10):
    # if the reaction cannot occur
    reaction_occur = False

    for reaction in reactions:
        # check reaction
        run_results = reaction(molecules)

        # for when a reaction occurs
        if run_results:
            # convert molecule count to %
            total = molecules["A"] + molecules["B"]
            percentage_A = (molecules["A"] / total) * 100
            percentage_B = (molecules["B"] / total) * 100
            updated_molecules.append((step, percentage_A, percentage_B))

            # to see if the reaction is valid
            reaction_occur = True
            break

    # after applying all the reactions and if none works it will break
    if not reaction_occur:
        break

# plot the reactions onto a plot
# Unpack the tuples into separate steps, concentrating a and b
steps, Concentration_A, Concentration_B = zip(*updated_molecules)
# creating the plot
plt.figure(figsize=(10, 5))
plt.plot(steps, Concentration_A, label="Concentration of A ( %)", color="blue")
plt.plot(steps, Concentration_B, label="Concentration of B ( %)", color="orange")
# Labels for the plot
plt.xlabel("Step")
plt.ylabel("Concentration %")
plt.title("Concentration of A and B for a population m = 10^3")
plt.legend()
plt.grid(True)
# print the plot
plt.show()
