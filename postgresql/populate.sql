

INSERT INTO advs (name_adv, description, products_name_product)
VALUES('adv123', 'i love cofe Jacobs minlin', 'Jacobs minlin1');
INSERT INTO advs (name_adv, description, products_name_product)
VALUES('fdjadv-327', 'i love cofe Jacobs black', 'Jacobs black');
INSERT INTO advs (name_adv, description, products_name_product)
VALUES('43-327', 'i love cofe Neskafe black', 'Neskafe black');
INSERT INTO advs (name_adv, description, products_name_product)
VALUES('dfd', 'i  like cofe Neskafe black', 'Neskafe black');

select * from advs

INSERT INTO products (name_product, price, provider_name_provider)
VALUES ('Jacobs minlin', 99,'Jacobs');
INSERT INTO products (name_product, price, provider_name_provider)
VALUES ('Jacobs black', 89,'Jacobs');
INSERT INTO products (name_product, price, provider_name_provider)
VALUES ('Neskafe black', 89,'Nestle');
INSERT INTO products (name_product, price, provider_name_provider)
VALUES ('Neskafe mini', 15,'Nestle');

select * from products


INSERT INTO providers (name_provider, type_product)
VALUES('Jacobs', 'Coffe');
INSERT INTO providers (name_provider, type_product)
VALUES('Nestle', 'Coffe');
INSERT INTO providers (name_provider, type_product)
VALUES('ProcteAndGambel', 'Сandy');




INSERT INTO viewers (nikname, email, firstname, lastname, age, country)
VALUES('I am a superman', 'udsjjh@gmail.com','Oleg','Dobrov', 23, 'Ukraine');
INSERT INTO viewers (nikname, email, firstname, lastname, age, country)
VALUES('kata123', 'katusha@gmail.com','Kateryna','Dolib', 25, 'Ukraine');
INSERT INTO viewers (nikname, email, firstname, lastname, age, country)
VALUES('BigBoss', 'Dorian@gmail.com','Dorian','Horodskiy', 38, 'Englend');
INSERT INTO viewers (nikname, email, firstname, lastname, age, country)
VALUES('LitelGirl', 'AllaMandra@gmail.com','Alla','Mandra', 15, 'Ukraine');

select * from viewers



INSERT INTO ViewersCanProducts (transasction, product_name_product, product_price, viewers_email)
VALUES('647249343', 'Jacobs black', '89', 'udsjjh@gmail.com');
INSERT INTO ViewersCanProducts (transasction, products_name_product, products_price, viewers_email)
VALUES('kl430920k-43', 'Jacobs minlin', '99', 'udsjjh@gmail.com');

INSERT INTO ViewersCanProducts (transasction, products_name_product, products_price, viewers_email)
VALUES('fdkl-438-278', 'Jacobs minlin', '99', 'Dorian@gmail.com');
INSERT INTO ViewersCanProducts (transasction, products_name_product, products_price, viewers_email)
VALUES('fdkl-438-279', 'Jacobs minlin', '99', 'Dorian@gmail.com');

INSERT INTO ViewersCanProducts (transasction, products_name_product, products_price, viewers_email)
VALUES('fdkl-438-280', 'Jacobs minlin', '99', 'Dorian@gmail.com');



select * from ViewersCanProducts
