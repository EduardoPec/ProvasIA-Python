create database provaestoque;

use provaestoque;

create table estoque (
estoqueID int primary key auto_increment,
produtoID int not null,
fornecedorID int not null,
quantidade int not null,
data_entrada date not null,
foreign key (produtoID) references produtos (produtoID),
foreign key (fornecedorID) references fornecedor (fornecedorID)
);

create table produtos (
produtoID int primary key auto_increment,
nome_produto varchar(60)
);

create table fornecedor (
fornecedorID int primary key auto_increment,
nome_fornecedor varchar(60)
);

alter table estoque add check (quantidade > 0);

select estoque.estoqueID, estoque.quantidade, estoque.data_entrada
from estoque
left join produtos on estoque.produtoID = produtos.produtoID
left join fornecedor on estoque.fornecedorID = fornecedor.fornecedorID
union
select estoque.estoqueID, estoque.quantidade, estoque.data_entrada
from estoque
right join produtos on estoque.produtoID = produtos.produtoID
right join fornecedor on estoque.fornecedorID = fornecedor.fornecedorID;


