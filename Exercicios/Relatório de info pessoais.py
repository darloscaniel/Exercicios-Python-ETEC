print ('')
print ('Relatório')
print (' ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
print ('Solicitando entrada de dados')
print ('----------------------------')
nome = input("Informe o nome do usuário: ")         
ano_at =float (input("Informe o ano atual: "))   
dn =float (input("Informe o ano de nascimento: "))
sexo = (input('Informe o sexo do usuário: '))
cid_n_u = (input('Informe a cidade natal do usuário: '))
na_u = (input('Informe a nacionalidade do usuário: '))
est_c_u= (input('Informe o estado civil do usuário: '))
esc_u= (input('Informe a escolaridade do usuário: '))
end_u= (input('Informe o endereço completo do usuário: '))
print ('')
i=ano_at-dn
print ('|------------------------------|')
print ('|       Exibindo o relatório   |')
print ('|------------------------------|')          
print ('')
print ('Nome do usuário: ',nome)
print ('Ano de nascimento: ',dn)
print ('idade: ',i)
print ('Sexo: ',sexo)
print ('Cidade natal: ',cid_n_u)
print ('Nascionalidade: ',na_u)
print ('Estado Civil: ',est_c_u)
print ('Escolaridade: ',esc_u)
print ('Endereço Completo: ',end_u)
print ('')
print ('* FIM DO Processo *')
print ('')
print ('--- OBRIGADO POR USAR O PYTHON ---')
