Create database if not exists 5CLogin;
Use 5CLogin;

Create table if not exists user (
    username varchar(35) not null,
    email varchar(60),
    password char(64) not null,
    DataN date,
    primary key (username)
);