det(I,J) :- entre(le,I,J).
det(I,J) :- entre(les,I,J).
det(I,J) :- entre(un,I,J).
det(I,J) :- entre(peu,I,K), entre(de,K,J).
det(I,J) :- entre(bien,I,K), entre(du,K,J).
det(I,J) :- entre(bien,I,K), entre(des,K,J).
det(I,J) :- entre(du,I,J).
det(I,J) :- entre(un,I,K), entre(peu,K,L), entre(de,L,J).

prnsuj(I,J) :- entre(il,I,J).
prnsuj(I,J) :- entre(j,I,J).
prnsuj(I,J) :- entre(ce,I,J).

prnobj(I,J) :- entre(le,I,J).
prnobj(I,J) :- entre(les,I,J).
prnobj(I,J) :- entre(l,I,J).

prnrel(I,J) :- entre(qu,I,J).
prnrel(I,J) :- entre(que,I,J).

adv(I,J) :- entre(bien,I,J).

verbe(I,J) :- entre(font,I,J).
verbe(I,J) :- entre(est,I,J).
verbe(I,J) :- entre(ai,I,J).
verbe(I,J) :- entre(faire,I,J).
verbe(I,J) :- entre(fait,I,J).

aux(I,J) :- entre(ai,I,J).
aux(I,J) :- entre(a,I,J).
aux(I,J) :- entre(ont,I,J).

ppas(I,J) :- entre(fait,I,J).

nomc(I,J) :- entre(fait,I,J).
nomc(I,J) :- entre(bien,I,J).
nomc(I,J) :- entre(biens,I,J).
nomc(I,J) :- entre(autres,I,J).
nomc(I,J) :- entre(gens,I,J).
nomc(I,J) :- entre(mal,I,J).

prep(I,J) :- entre(à,I,J).

sub(I,J) :- entre(bien,I,K), entre(qu,K,J).

neg1(I,J) :- entre(ne,I,J).

neg2(I,J) :- entre(pas,I,J).

ph(I,J) :- gsuj(I,K), gcompsuj(K,J).
ph(I,J) :- gn(I,K), gv(K,J).
ph(I,J) :- prnsuj(I,K), gv(K,J).
ph(I,J) :- gsubav(I,K), gsuj(K,J).

gobj(I,J) :- det(I,K), nomc(K,J).
gobj(I,J) :- prnsuj(I,K), grel(K,J).
gobj(I,J) :- gn(I,K), gprep(K,J).

gsuj(I,J) :- gn(I,K), grel(K,J).
gsuj(I,J) :- prnsuj(I,K), gv(K,J).

gv(I,J) :- vpas(I,K), gobj(K,J).
gv(I,J) :- verbe(I,K), gobj(K,J).
gv(I,J) :- verbe(I,K), grel(K,J).
gv(I,J) :- gnegaux(I,K), gadv(K,J).

gn(I,J) :- det(I,K), nomc(K,J).

gsubav(I,J) :- gsub(I,K), entre(',',K,J).
gsub(I,J) :- sub(I,K), propsub(K,J).
propsub(I,J) :- prnsuj(I,K), gv(K,J).

gcompsuj(I,J) :- entre(',',I,K), propcompsuj(K,J).
propcompsuj(I,J) :- prnsuj(I,K), gvcompsuj(K,J).
gvcompsuj(I,J) :- prnobj(I,K), gadv(K,J).

grel(I,J) :- prnrel(I,K), proprel(K,J).

proprel(I,J) :- prnsuj(I,K), gv(K,J).
proprel(I,J) :- prnsuj(I,K), verbe(K,J).
proprel(I,J) :- gn(I,K), gadv(K,J).

gprep(I,J) :- prep(I,K), gvobj(K,J).
gvobj(I,J) :- verbe(I,K), gobj(K,J).

gadv(I,J) :- verbe(I,K), adv(K,J).
gadv(I,J) :- adv(I,K), ppas(K,J).

gnegaux(I,J) :- neg1prnobj(I,K), auxneg2(K,J).

neg1prnobj(I,J) :- neg1(I,K), prnobj(K,J).

auxneg2(I,J) :- aux(I,K), neg2(K,J).

vpas(I,J) :- aux(I,K), ppas(K,J).
/*
entre(le,0,1).
entre(bien,1,2).
entre(qu,2,3).
entre(il,3,4).
entre(fait,4,5).
entre(',',5,6).
entre(il,6,7).
entre(le,7,8).
entre(fait,8,9).
entre(bien,9,10).

  
entre(le,0,1).
entre(fait,1,2).
entre(est,2,3).
entre(que,3,4).
entre(j,4,5).
entre(ai,5,6).
entre(peu,6,7).
entre(de,7,8).
entre(biens,8,9).

entre(j,0,1).
entre(ai,1,2).
entre(bien,2,3).
entre(du,3,4).
entre(mal,4,5).
entre(à,5,6).
entre(faire,6,7).
entre(ce,7,8).
entre(que,8,9).
entre(les,9,10).
entre(autres,10,11).
entre(font,11,12).
entre(bien,12,13).

entre(bien,0,1).
entre(des,1,2).
entre(gens,2,3).
entre(ont,3,4).
entre(fait,4,5).
entre(un,5,6).
entre(peu,6,7).
entre(de,7,8).
entre(bien,8,9).
*/
entre(bien,0,1).
entre(qu,1,2).
entre(il,2,3).
entre(ai,3,4).
entre(fait,4,5).
entre(du,5,6).
entre(bien,6,7).
entre(',',7,8).
entre(il,8,9).
entre(ne,9,10).
entre(l,10,11).
entre(a,11,12).
entre(pas,12,13).
entre(bien,13,14).
entre(fait,14,15).
