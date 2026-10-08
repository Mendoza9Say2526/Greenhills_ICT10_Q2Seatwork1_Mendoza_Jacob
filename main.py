# Nickname Atlas Python
from pyscript import display, document

southeastcountries = ['Brunei', 'Cambodia', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Timor-Leste', 'Vietnam']
coolnicknames = ['Land of Unexpected Treasures', 'Kingdom of Wonder', 'Emerald of the Equator', 'Land of a Million Elephants' 'Land of Diversity', 'The Golden Land' 'The Welcoming Home', 'The Lion City', 'Land of Smiles', 'Land of the Crocodile', 'Land of the Blue Dragon']

# function for revealing the nickname
def reveal_nickname(e):
    nickname = document.getElementById("country").value
    document.getElementById("div1").innerHTML = ""

    display(nickname, target="div1") #displaying the country's nickname


