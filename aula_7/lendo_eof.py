while True:
    try:    
        linha = input()
        print('conteudo da linha')
        print(linha)
    except EOFError:
        break
        
print('FIM')