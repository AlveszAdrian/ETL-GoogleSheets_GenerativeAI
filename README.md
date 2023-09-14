# Sobre o Projeto
Minha ideia inicial era criar um código em python que fosse abastecido por uma planilha, mas eu fiquei com preguiça de abastecer a planilha(para ser mais realista), então resolvi usar um forms, o próprio forms gera uma planilha que é atualizada automaticamente, então o código ia ficar interativo. Após a planilha abastecida, o código iria criar uma lista sobre as pessoas e gerar uma mensagem individual usando a API do ChatGPT da openIA para cada um e assim enviar um email(algo requerido no form) para enviar uma mensagem no email de cada um.

### Um simples projeto de ETL
Sou um aprendiz no ramo de programação e queria saber como o ETL funciona na prática então fiz esse projeto e pedi para alguns amigos meu preencherem o formulário para deixar mais interessante.

# Extract
para extrair dados usei a [API do google sheets](https://developers.google.com/sheets/api/guides/concepts?hl=pt-br) que é bem simples de utilizar apenas importando-as como escopo. 
apenas segui os passos que estavam nos documentos e pronto!
lembrando que como sou iniciante tive problemas no tratamento dos dados em formato de lista, mas logo pude superar isso de "maneira bruta"

# Transform
Com os dados separados chegou a hora de transformalos com uma IA Generativa, o ChatGPT. Usando a própria [API disponibilizada pela OPENAI](https://platform.openai.com/docs/api-reference/authentication) no site deles, é capaz de criar textos usando inteligência artificial de ponta, mas é claro com um custo.

# Load
Aqui foi onde eu parei, mas a ideia continua a mesma, Pegar essa mensagem e envia-lá individualmente para cada email com a biblioteca [SMTPL]()

# Expectativa
Esse foi o meu primeiro projeto em python, por isso é uma gambiarra, mas espero poder criar outros envolvendo mais ainda a ciência de dados. Essa ideia foi baseada em uma atividade do [Santander Bootcamp 2023 - Ciência de Dados com Python](https://web.dio.me/track/71477949-f762-43c6-9bf2-9cf3d7f61d4a)


# liguagem utilizada
![My Skills](https://skillicons.dev/icons?i=py)
# Contato
[![My Skills](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/in/adrian-alves-927b8714a/)
