%% This TM accepts strings made up of a's and b's
%% with n a's followed n b's followed by n a's
%% example aaabbbaaa
1,2,a,*,r
1,h,#,#,r
2,2,a,a,r
2,3,b,b,r
3,3,b,b,r
3,4,a,a,l
4,5,b,a,r
5,5,a,a,r
5,6,#,#,l
6,7,a,#,l
7,8,a,#,l
8,8,a,a,l
8,8,b,b,l
8,1,*,*,r