import transactions

fromaddr="173CJ9wxuZFbJyDbkJ89AfpAkqx5PatxMk"
colornumber=666
colorname="MississippiKoin"
destination=fromaddr
fee_each=0.00005
private_key="5J9rUR4aSrEsPL1ChHdC7D1rXUtrsyCSqp9ZM9bnKA5Ubh9vBBA"
description=""
a= transactions.make_new_coin(fromaddr, colornumber, colorname, destination, fee_each, private_key, description)

print a
