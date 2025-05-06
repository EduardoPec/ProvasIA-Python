create database estoque;

use estoque;

create table produtos (
produto_id int primary key not null,
nome_produto varchar(60),
quantidade int not null,
preco decimal(10, 2) not null
);

insert into produtos (produto_id,nome_produto,quantidade,preco)
values (1,"Caderno",3,15), (2,"Lapis",5,3), (3,"Cola",4,10);

select * from produtos;

