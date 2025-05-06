create database gerenciador;

use gerenciador;

create table clientes (
		id_cliente int auto_increment key not null,
        nome varchar(30) not null,
        idade int not null,
        cidade varchar(20)
        );