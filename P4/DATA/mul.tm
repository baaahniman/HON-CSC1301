%% The TM is given an input
%% of the form of a regular expression sa*ma*e, e.g.
%% saaamaae
%% It halts with placing n1*n2 a's after e, where
%% n1 is the number of a's between s and m and
%% n2 is the number of a's between m and e.
%%
1,2,s,s,r
2,3,a,x,r
2,11,m,m,l
3,3,a,a,r
3,4,m,m,r
4,5,a,x,r
4,9,e,e,l
5,5,a,a,r
5,6,e,e,r
6,6,a,a,r
6,7,#,a,l
7,7,a,a,l
7,8,e,e,l
8,8,a,a,l
8,4,x,x,r
9,9,x,a,l
9,10,m,m,l
10,10,a,a,l
10,2,x,x,r
11,11,x,a,l
11,h,s,s,r