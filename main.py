# Nickname Atlas Python
from pyscript import display, document

# function for revealing the nickname
def reveal_nickname(e):
    nickname = document.getElementById("country").value
    document.getElementById("div1").innerHTML = ""

    display(nickname, target="div1") #displaying the country's nickname


