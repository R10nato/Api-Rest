# Api Rest

 Criando uma Api Rest com Django

 Irei criar uma api com funcionalides de CRUD de pacientes de um hospital
 
 test pelo sie
 Alterei o settings.py - Coloquei meu app 'hospital' e mudei para pt-br

 criei um template com um index.html como home

 criei um form.html em templates dentro do app hospital

trabalharemos agora com banco de dados Sqlite e com o formulário interligado as colunas do banco.

app/models.py - No arquivo models do Django vamos realizar a criação das colunas do banco de dados:

antes instalar python -m pip install Pillow

Posteriormente rodaremos o seguinte comando no terminal: python manage.py makemigrations
python manage.py migrate

Migrations for 'hospital':
  hospital\migrations\0001_initial.py
    - Create model Paciente

depois criar um supur usuario com python manage.py createsuperuser
instalando pip install djangorestframework

