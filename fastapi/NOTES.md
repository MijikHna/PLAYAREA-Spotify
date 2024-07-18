# Notizen

## postgres

* `docker-compose exec db psql -h localhost -U playarea2_user --dbname=playarea2_db`
* `\l` - list all databases
* `\d+` - list all tables (relations) in the current database
* `\c playarea2_db` - connect to DB playarea2_db
* `\d TABLENAME` - describe Table TABLENAME

* für Triggers nach **Pl/pgSQL** googeln

## backend

Man kann mit `starlette.config.Config` einfacher and **.env** variablen drankommen

### Mako

* Template Library in Python geschrieben
* konzeptuell ist eingebettener Python
* rendert Python code ins z.B html Template

### Alembic

* Mangagement Tool für Models, dass SQLAlchemy, Mako benutzt
* Setup
´´´
yourproject/
    alembic/
        env.py
        README
        script.py.mako
        versions/
            3512b954651e_add_account.py
            2b1ae634e5cd_add_order_id.py
´´´

* ´alembic´ - Source Code für Migration Env.
* `env.py` - Script der ausgeführt wird, wenn Alembic Tool aufgerufen wird
* `script.py.mako` - Mako Template, um Migration Scripts zu erstellen

* Alembic kommt mit eigener CLI (kann man Alembic Projekte ertellen, verwalten)
* ´alembic.ini´ wird erstellt, beim Ausführen von ´alembic init --template {generic/async/miltidb/pylons} .´ Hat Settings für Alembic inne.
* `alembic revision -m "create account table"` - Migration Skript erstellen

* `alembic upgrade head` - bis zur letzten Migration laufen (man kann auch die Revissionnummer anstelle von `head` angeben)

* `alembic upgrade +2`, `alembic downgrade ae10+2` - Migration relative zur Aktuellen oder zur bestimmten Revision laufen
* `alembic current`
* `alembic history --verbose`
* `alembic history -r-3:current`
* `alembic downgrade base` `alembic upgrade head`

## frontend

### Vite

* `npm init vite@latest` - Vite wird selbst anzeigen, welche Optionen es anbietet. Unter anderem kann man auch ein Projekt mit vue-ts erstellen
