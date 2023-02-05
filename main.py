"""
A translater for pig latin to eng and eng to pig latin...

Auther : Cactochan

-------------------------------------------------------------

Commands : piglatin help
           piglatin to <text-in-eng>
           piglatin from <text-in-piglatin>
"""

from rich import print
import sys

ascii_art = r"""[yellow1]
$$$$$$$\  $$\                 $$\            $$\     $$\
$$  __$$\ \__|                $$ |           $$ |    \__|
$$ |  $$ |$$\  $$$$$$\        $$ | $$$$$$\ $$$$$$\   $$\ $$$$$$$\
$$$$$$$  |$$ |$$  __$$\       $$ | \____$$\\_$$  _|  $$ |$$  __$$\
$$  ____/ $$ |$$ /  $$ |      $$ | $$$$$$$ | $$ |    $$ |$$ |  $$ |
$$ |      $$ |$$ |  $$ |      $$ |$$  __$$ | $$ |$$\ $$ |$$ |  $$ |
$$ |      $$ |\$$$$$$$ |      $$ |\$$$$$$$ | \$$$$  |$$ |$$ |  $$ |
\__|      \__| \____$$ |      \__| \_______|  \____/ \__|\__|  \__|
              $$\   $$ |
              \$$$$$$  |
               \______/[/yellow1]
"""
vov = "aeiou"

def to(txt):
    output = ""
    words = txt.split(" ")
    for word in words:
        if not word.isalpha() or len(word) == 1 or word[0] == "y":
            output += word + " "
            continue
        if word == "":
            continue
        if word[0] in vov:
            output += word + "yay "
        else:
            output += f"{word[1:]}{word[0]}ay "
    return output

def from_(pig_latin):
    output = ""
    words = pig_latin.split(" ")
    for word in words:
        if not word.isalpha() or len(word) == 1 or word[len(word)-2:] != "ay" :
            output += word + " "
            continue
        if word == "":
            continue
        if word[len(word)-3:] == "yay":
            output += word[0:len(word)-3] + " "
        else:
            output += word[-3] + word[0:-3] + " "
    return output

if __name__ == "__main__":
    
    try:
        command = sys.argv[1]
    except:
        print("[red]  [-] Command not given. [use help for cmds] [/red]")
        quit()

    if command not in ["to", "from", "help"]:
        print("[red]  [-] Command not found. [use help for cmds] [/red]")
        quit()

    print(ascii_art)

    if command == "help":
        print(f"""[blue] 
...............................................
Commands : piglatin help
           piglatin to <text-in-eng>
           piglatin from <text-in-piglatin>
...............................................
        [/blue]""")
    elif command == "to":
        try:
            txt = ""
            for e in range(0,len(sys.argv)):
                if e == 0 or e == 1:
                    pass
                else:
                    txt += " "+ sys.argv[e]
            txt[0]
            print("\n")
            print(f"[medium_spring_green][bold] ENG-PIGLATIN : [/bold]{to(txt)}[/medium_spring_green]")
        except:
            print("[red]  [-] Text not provided. [/red]")
    elif command == "from":
        try:
            txt = ""
            for e in range(0,len(sys.argv)):
                if e == 0 or e == 1:
                    pass
                else:
                    txt += " "+ sys.argv[e]
            txt[0]
            print("\n")
            print(f"[dark_orange][bold] PIGLATIN-ENG : [/bold]{from_(txt)}[/dark_orange]")
        except:
            print("[red]  [-] Text not provided. [/red]")
