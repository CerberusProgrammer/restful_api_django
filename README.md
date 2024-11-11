# Instalacion

## Inicializar entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar el servidor

```bash
python manage.py runserver
```

## Crear superusuario

```bash
python manage.py createsuperuser
```

## Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```
