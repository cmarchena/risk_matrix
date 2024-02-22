from colorama import init, Fore
import matplotlib.pyplot as plt

# Initialize colorama
init()
risk_matrix = [
    [4,'low', "blue", "\033[94m"],
    [6,'moderate',"green", '\033[92m'],
    [8,'high',"orange", '\033[93m'],
    [10, 'extreme', "red", '\033[91m']
]

color_mapping = {
    "blue": Fore.BLUE,
    "green": Fore.GREEN,
    "orange": Fore.YELLOW,
    "red": Fore.RED
}

def calculateRiskLevel(impact, likeliness):
    risk_level = impact + likeliness
    risk_value = ""
    for item in risk_matrix:
        if risk_level <= item[0]:
            risk_value = color_mapping[item[2]] + item[1]
            return f'For risk with impact {impact} and likeliness {likeliness} the level is {risk_value}'
      
impact = int(input("Enter the impact: "))
likeliness = int(input("Enter the likeliness: "))
print(calculateRiskLevel(impact, likeliness))


risk_levels = [item[0] for item in risk_matrix] 
risk_labels = [item[1] for item in risk_matrix]

fig, ax = plt.subplots()
ax.plot(risk_levels)

ax.set_title('Risk Matrix')
ax.set_xlabel('Risk Level')
ax.set_xticks(risk_levels)
ax.set_xticklabels(risk_labels)

plt.savefig('risk_matrix.png')
