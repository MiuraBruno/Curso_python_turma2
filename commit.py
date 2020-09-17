import os 
mensagem = input()
os.system('git add *')
os.system('git commit -m "' + mensagem + '"')
os.system('git push')
