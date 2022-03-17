from mcpi import minecraft
mc=minecraft.Minecraft.create()
while True:
	input(str(Message))
	mc.postToChat(Message)