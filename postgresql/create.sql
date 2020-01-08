

CREATE TABLE providers(name_provider text, type_product text);
ALTER TABLE providers
ADD CONSTRAINT name_provider_pk PRIMARY KEY(name_provider);

CREATE TABLE viewers(email text, nikname text, firstname text, lastname text, age int, country text);
ALTER TABLE viewers
ADD CONSTRAINT email_pk PRIMARY KEY(email);

CREATE TABLE products(name_product text, price int, provider_name_provider text);
ALTER TABLE products
ADD CONSTRAINT name_products_pk PRIMARY KEY(name_product),
ADD CONSTRAINT provider_name_provider_fk FOREIGN KEY(provider_name_provider) REFERENCES providers (name_provider);

CREATE TABLE advs(name_adv text, description text, products_name_product text);
ALTER TABLE advs
ADD CONSTRAINT name_adv_pk PRIMARY KEY(name_adv),
ADD CONSTRAINT products_name_product_fk FOREIGN KEY(products_name_product) REFERENCES products (name_product);

CREATE TABLE ViewersCanProducts(transasction text, product_name_product text, product_price int, viewers_email text);
ALTER TABLE ViewersCanProducts
ADD CONSTRAINT transasction_pk PRIMARY KEY(transasction),
ADD CONSTRAINT products_name_product_fk FOREIGN KEY(products_name_product) REFERENCES products (name_product),
ADD CONSTRAINT products_price_fk FOREIGN KEY(products_price) REFERENCES products (price),
ADD CONSTRAINT viewers_email_fk FOREIGN KEY(viewers_email) REFERENCES viewers (email);
