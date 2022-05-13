# Genius API Client

## Como configurar o ambiente:

• Criar um arquivo oculto .env com as seguintes informações:

```
FLASK_ENV=production
DEBUG=False

GENIUS_ACCESS_TOKEN= seu_token_de_acesso

AWS_ACCESS_KEY_ID= sua_chave_id_de_acesso
AWS_SECRET_ACCESS_KEY= sua_chave_de_acesso
```

## Instalando dependências

'''pip install requirements.txt'''

## Para consultar os dados na API

Será necessário rodar o comando: '''flask run''' e acessar a url: '''http://127.0.0.1:5000/get_artist_top_songs/nome_do_artista'''
