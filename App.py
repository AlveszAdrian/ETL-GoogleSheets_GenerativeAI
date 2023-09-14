from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import google.auth
from googleapiclient.errors import HttpError


# define o escopo de acesso da API do Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly'] # Define o escopo de acesso da API do Google Sheets



def main(): # Função para verificar credenciais e acessar a planilha
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())


    
    service = build('sheets', 'v4', credentials=creds) # Cria o serviço de acesso a API
    sheet = service.spreadsheets()
    Planilha = sheet.values().get(spreadsheetId='SEU ID DE PLANILHA AQUI', # ID da planilha
                                range=f'Página1!A1:G200').execute() # Range de acesso da planilha


    values = Planilha.get('values', []) 

    #print(values) # Imprime os valores da planilha
    return values # Retorna os valores da planilha para serem usados em outro arquivo

values = main()# Chama a função main para acessar a planilha


#print(values) # Imprime os valores da planilha

def get_nomes(values): # Função para retornar os nomes dos alunos
    nomes = []
    for i in range(1, len(values)):
        nomes.append(values[i][1])
    return nomes
print(get_nomes(values)) # Imprime os nomes dos alunos

def get_email(values): # Função para retornar os emails dos alunos
    email = []
    for i in range(1, len(values)):
        email.append(values[i][0])
    return email
print(get_email(values)) # Imprime os emails dos alunos

def get_ajuda(values): # Função para retornar se o aluno precisa de ajuda
    ajuda = []
    for i in range(1, len(values)):
        ajuda.append(values[i][2])
    return ajuda
print(get_ajuda(values)) # Imprime se o aluno precisa de ajuda

users = get_nomes(values) # Atribui os nomes dos alunos a variavel use


import openai

openai.api_key = "SUA CHAVE DE API AQUI"

def generate_ai_news(user):
  completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
      {
          "role": "system",
          "content": "Você é um especialista em markting bancário."
      },
      {
          "role": "user",
          "content": f"Crie uma mensagem para {user}"
      }
    ]
  )
  return completion.choices[0].message.content.strip('\"')

for user in get_nomes(values): # Loop para gerar as mensagens para cada aluno
  news = generate_ai_news(user)
  print(news)
  user['news'].append({
      "description": news
  })
  
  
