import itchat,time

def lc():
    print("Login!")

def ec():
    print("exit")

itchat.auto_login(hotReload=True)
if itchat.send_msg("hello world.","filehelper"):
    print("success")
else:
    print("fail")


