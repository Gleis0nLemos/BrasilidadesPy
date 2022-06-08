
from acess_cep import BuscaEndereco
cep = "62886410"
objeto_cep = BuscaEndereco(cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)

#>>>>>>>>>>>>>LISTA DE CARACTERES IMPORTANRTES PARA SE TRABALHAR COM REGEX<<<<<<<<<<<<<<<<<
# []	Define um range ou um grupo de caracteres	                    [0-9]; [a-z]; [abc]
#  *	Marca nenhuma, uma ou mais ocorrências	                        sol*
# {}	Quantidade de repetições de uma ocorrência definida	            [abc]{5}
# \d	Qualquer número de 0 até 9	                                    \d{3,4}
# \w	Qualquer número de 0 até 9 ou letra de a até z ou _	            \w{10}
# |	    Um ou outro                                                     @$
# ()	Captura e agrupa	                                            (\w{4})
# %A	Dias da semana por extenso	                                    Sunday, Monday, ...
# %d	Dias do mês	                                                    01, 02, ..., 31
# %m	Meses em formato de números	                                    01, 02, ..., 12
# %y	Ano em formato de 2 dígitos	                                    99, 15
# %Y	Ano em formato de 4 dígitos	                                    1993, 2011
# %H	Hora em formato decimal	                                        00, 01, ..., 23
# %M	Minuto em formato decimal	                                    00, 01, ..., 59
# %S	Segundo em formato decimal	                                    00, 01, ..., 59