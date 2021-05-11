--run psql -U postgres -f psqlcreator.sql
create database gpuinstockbotdb;
create user admin with password 'superuser';
alter role admin set client_encoding to 'utf8'; --req by django
alter role admin set timezone to 'UTC'; --req by django
grant all privileges on database gpuinstockbotdb to admin;
\q
