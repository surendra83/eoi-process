## Dev/stage/prod Deployment

## Clone/copy Repository
https://github.com/uhc-tech-employer-individual-ancillary/eoi-validation-api.git

```
git clone https://github.com/uhc-tech-employer-individual-ancillary/eoi-validation-api.git

cd eoi-validation-api

```
## Create Deployment Enviroment

```
mkdir -p deploy/env
tourch deploy/env/dev.env
tourch deploy/env/stage.env
tourch deploy/env/prod.env

chmod 700 deploy deploy/env
chmod 600 deploy/env/*.env

```
## create config Files

- deploy/env/dev.env
- deploy/env/dev.env
- deploy/env/dev.env

```
# Dev Config
# deploy/env/dev.env

DEPLOY_ENV=dev
APP_PORT=8000
DB_SERVER=dev-sql-server.example.internal
DB_DATABASE=EOI_Dev
DB_USER=eoi_app
DB_PASSWORD=replace-with-dev-secret
JWT_SECRET_KEY=replace-with-a-long-random-dev-secret

# Staing Config
# deploy/env/stage.env

DEPLOY_ENV=stage
APP_PORT=8000
DB_SERVER=prod-sql-server.example.internal
DB_DATABASE=EOI_Prod
DB_USER=eoi_app
DB_PASSWORD=replace-with-production-secret
JWT_SECRET_KEY=replace-with-a-long-random-production-secret

# Prod Config
# deploy/env/prod.env
DEPLOY_ENV=prod
APP_PORT=8000
DB_SERVER=prod-sql-server.example.internal
DB_DATABASE=EOI_Prod
DB_USER=eoi_app
DB_PASSWORD=replace-with-production-secret
JWT_SECRET_KEY=replace-with-a-long-random-production-secret

```

Confirm network access from the Linux host/container to SQL Server on port 1433. 

The SQL Server host must be reachable from Docker, and its firewall must allow the host or Docker subnet.

## Build and start development:

```
DEPLOY_ENV=dev docker compose up -d --build
or 
DEPLOY_ENV=stage docker compose up -d --build
or
DEPLOY_ENV=prod APP_VERSION=1.0.0 docker compose up -d --build

```

## Verify deployment:

```
docker compose ps
docker compose logs -f eoi-validation-api
curl http://localhost:8000/healthcheck

```
## check Api and test Open API documentation:

```
http://<linux-server-host>:8000/docs

```







