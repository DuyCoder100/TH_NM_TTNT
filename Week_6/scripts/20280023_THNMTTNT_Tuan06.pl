parent(marry, bill).
parent(tom, bill).
parent(tom, liz).
parent(bill, ann).
parent(bill, sue).
parent(sue, jim).
woman(marry).
man(tom).
man(bill).
woman(liz).
woman(sue).
woman(ann).
man(jim).
child(Y, X):- parent(X, Y).
mother(X, Y):- parent(X, Y), woman(X).
father(X, Y):- parent(X, Y), man(X).
grandparent(X, Z):- parent(X, Y), parent(Y, Z).
sister(X, Y) :- parent(Z, X), parent(Z, Y), woman(X).
/*Bai tap thuc hanh tuan 06:
Cau 1:
a: Truy van: ?-parent(jim, X).
   Ket qua: false.
b: Truy van: ?-parent(X, jim).
   Ket qua: X = sue.
c: Truy van: ?-parent(marry, X), parent(X, part).
   Ket qua: false.
d: Truy van: ?-parent(marry, X), parent(X, y), parent(y, jim).
   Ket quaL false.

Cau 2:
a. Menh de: ?-parent(X, bill).
   Ket qua: X = marry;
            X = tom;
            false.
   marry va tom la cha me cua bill.
b. Menh de: ?-child(X, marry).
   Ket qua: X = bill.
   marry co con ten la bill.
c. Menh de: ?-grandparent(X, sue).
   Ket qua: X = marry;
            X = tom;
            false.
   sue la chau cua marry va tom.
*/
