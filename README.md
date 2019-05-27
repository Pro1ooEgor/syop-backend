getting started

Ubuntu
```bash
cp env.template .env
```
Windows
```bash
copy env.template .env
```

postgres
```bash
sudo -u postgres psql
CREATE DATABASE syop;
CREATE USER syop_user WITH PASSWORD 'syop_password';
ALTER USER syop_user CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE syop TO syop_user;
\q
```

Windows postgres
```bash
psql -U postgres
```

