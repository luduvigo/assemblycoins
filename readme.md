#IMMEDIATE PROBLEMS

 - cannot prevent uncoloring coins because we have no good way to keep track of input colors
      need database

- color address conversion still doesnt work

- cannot do mass declarations because, although I can produce numerous outputs at once,
they will uncolor prior coins




##ISSUES

1)  Currently Create Raw Transactions can UNCOLOR coins by
indisciminately using unspent inputs

2)  How to make Color Address





##IMPROVEMENTS
make transactions a class


####RESOLVED

3)  Metadata bug, turned out LEB128 encoding was flawed in edge case

4)  RESOLVED ERROR IN CRAFTING TRANSACTION FOR TRANSFER TXS

transfer color coin API call works as a function but not as a HTTP API, check it out
