from brphones import Telefone
import re

telefone = "5585992970088"
i = Telefone(telefone)
print(i)




#>>>>LISTA DE CARACTERES IMPORTANRTES PARA SE TRABALHAR COM REGEX
# []	Define um range ou um grupo de caracteres	                    [0-9]; [a-z]; [abc]
#  *	Marca nenhuma, uma ou mais ocorrências	                        sol*
# {}	Quantidade de repetições de uma ocorrência definida	            [abc]{5}
# \d	Qualquer número de 0 até 9	                                    \d{3,4}
# \w	Qualquer número de a té 9 letra de a até z ou _	                \w{10}
# |	    Um ou outro                                                     @$
# ()	Captura e agrupa	                                            (\w{4})