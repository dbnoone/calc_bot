from DB import DB

DB.query("""create table admins(
         id       int(255)     not null primary key,
         is_admin tinyint(3)   not null,
         alias    varchar(255) not null)"""
         )

DB.query("""INSERT INTO admins (id, is_admin, alias) VALUES (%s, %s, %s)""", (413081486, 1, 'Алексей Голованов'))

DB.query("""create table categories(
         id   int(255) auto_increment primary key,
         name varchar(32) null)"""
         )

DB.query("""create table subcategories(
         id            int(255) auto_increment primary key,
         name          varchar(255)            not null,
         parent_cat_id int(255)                not null,
         charge_type   int(255)     default 0  not null,
         charge        varchar(255) default '' not null)"""
         )
