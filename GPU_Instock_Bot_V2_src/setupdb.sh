psql -U postgres -f psqlcreator.sql  #logs into postgres and creates the database
python manage.py migrate
psql gpuinstockbotdb < betadatadump #imports data into database for gpu's
