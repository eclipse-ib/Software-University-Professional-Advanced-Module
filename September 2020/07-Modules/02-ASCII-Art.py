import pyfiglet


def figlet_msg(msg):
    text = pyfiglet.figlet_format(msg)
    print(text)


msg = input()
figlet_msg(msg)