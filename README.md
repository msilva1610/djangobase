# djangobase
template para iniciar testes com django - inicio rápido

# Sequencia inicial

Iniciando um projeto sem mistérios

```
python3 - m venv venv
# no ubuntu
source venv/bin/activate

```

### Criar um projeto e os diretórios

```
mkdir djangobase
cd djangobase
python magage.py startapp mysite
```

### Instalar o django dentro do virtualenv
```
pip install django==1.11
```

### Manter sempre o requeriments.txt atualizado
```
pip freeze > requeriments.txt
```

### Criar a primeira aplicação django
Não esquecer do ponto ao final da linha
```
django-admin startproject mysite .
```

### Criando o database
```
python manage.py migrate
```

### Criando as tabelas do projeto caso tenha models
```
python magage.py makemigrations nome-do-app
```

### Criando usuário admin do django-admin
```
python manage.py createsuperuser
```

### Rodandno o projeto
```
python manage.py runserver
```

# Setup dos arquivos do django

## settings.py

Configurar o arquivo settings inicialmente. Lembrar de alterar o ```ALLOWED_HOSTS = []``` para ter acesso externo ao projeto Django.

### Incluir a aplicação criada.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # my apps
    'django_tables2',
    'tabela',
]
```

### Configurar o regional settings

```python
LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'
```

### Incluir configuração para os arquivos estáticos.
A configuração dos arquivos estáticos serão utilizados no deploy em servidores apache ou nginx

```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```