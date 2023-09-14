# Sobre o Projeto
Minha ideia inicial era criar um código em Python que fosse abastecido por uma planilha, mas eu fiquei com preguiça de preenchê-la (para ser mais realista), então resolvi usar um formulário, o próprio formulário gera uma planilha que é atualizada automaticamente, então o código ficaria interativo. Após a planilha ser preenchida, o código criaria uma lista com as informações das pessoas e geraria uma mensagem individual usando a API do ChatGPT da OpenAI para cada uma, e assim enviar um e-mail (algo solicitado no formulário) com uma mensagem para o e-mail de cada pessoa.

### Um simples projeto de ETL
Sou um aprendiz no ramo de programação e queria saber como o ETL funciona na prática. Então, fiz esse projeto e pedi para alguns amigos meus preencherem o formulário para deixá-lo mais interessante.

# Extract
para extrair dados usei a [API do google sheets](https://developers.google.com/sheets/api/guides/concepts?hl=pt-br) que é bem simples de utilizar apenas importando-as como escopo. Apenas segui os passos que estavam nos documentos e pronto! Lembrando que, como sou iniciante, tive problemas no tratamento dos dados em formato de lista, mas logo pude superar isso de maneira mais 'bruta'.

# Transform
Com os dados separados chegou a hora de transforma-los com uma IA Generativa, o ChatGPT. Usando a própria [API disponibilizada pela OPENAI](https://platform.openai.com/docs/api-reference/authentication) no site deles, é capaz de criar textos usando inteligência artificial de ponta, mas é claro com um custo.

# Load
Aqui foi onde eu parei, mas a ideia continua a mesma, Pegar essa mensagem e envia-lá individualmente para cada email com a biblioteca [SMTPL]()

# Expectativa
Este foi o meu primeiro projeto em Python, por isso é um trabalho improvisado, mas espero poder criar outros envolvendo ainda mais a ciência de dados. Essa ideia foi inspirada por uma atividade do [Santander Bootcamp 2023 - Ciência de Dados com Python](https://web.dio.me/track/71477949-f762-43c6-9bf2-9cf3d7f61d4a)


# liguagem utilizada
![My Skills](https://skillicons.dev/icons?i=py)
# Contato
[![My Skills](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/in/adrian-alves-927b8714a/)
