getting started
```bash
cp env.template .env
```

postgres
```bash
sudo -u postgres psql
CREATE DATABASE syop;
CREATE USER syop_user WITH PASSWORD 'syop_password';
ALTER USER syop_user CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE adlynx TO syop_user;
\q
```

