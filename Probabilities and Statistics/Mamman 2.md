![[Pasted image 20260404165553.png]]
## סעיף א

![[Mamman 2 Question 1 Seif 1]]


![[Pasted image 20260404165634.png]]
## סעיף א
נסמן את המאורע $A_n$, שהוא המאורע שהמתג $n$ סגור.
נסמן ב $B$ את המאורע שקיים זרם מ$A$ ל$B$ .
נקבל:
$$
P(B)=P((A_1 union A_2 union A_3) union (A_4 sect (A_5 union A_6)))= \
P(A_1 union A_2 union A_3) + P(A_4 sect (A_5 union A_6)) - P((A_1 union A_2 union A_3) inter (A_4 sect (A_5 union A_6))) = \
$$
לפי עיקרון ההפרדה וההכללה
$$
=P(A_1 union A_2 union A_3) + P(A_4)P(A_5 union A_6) - P(A_1 union A_2 union A_3) P(A_4 sect (A_5 union A_6))
$$
מפני שהמאורעות לא תלויים, נקבל:
$$
=1-P(A_1^C sect A_2^C sect A_3^C) + P(A_4)(1-P(A_5^C sect A_6^C)) -\ (1-P(A_1^C sect A_2^C sect A_3^C))P(A_4)(1-P(A_5^C sect A_6^C))) = \
=1-P(A_1^C) P(A_2^C) P(A_3^C) + P(A_4)(1-P(A_5^C)P(A_6^C)) -\ (1-P(A_1^C) P(A_2^C) P(A_3^C))P(A_4)(1-P(A_5^C) P(A_6^C))) 
$$
ולפי הנתונים נקבל:
$$1-0.4^3 + 0.5(1-0.5^2) - (1-0.4^3)0.5(1-0.5^2) = 0.96$$
מש"ל א
## סעיף ב
נתון: $P(A_5) = 0$
נעדכן את הנוסחא:
$$=1-P(A_1^C) P(A_2^C) P(A_3^C) + P(A_4)(1-P(A_5^C)P(A_6^C)) -\ (1-P(A_1^C) P(A_2^C) P(A_3^C))P(A_4)(1-P(A_5^C) P(A_6^C)))= \
=1-P(A_1^C) P(A_2^C) P(A_3^C) + P(A_4)(1-1P(A_6^C)) -\ (1-P(A_1^C) P(A_2^C) P(A_3^C))P(A_4)(1-1P(A_6^C)))=
$$
ונקבל:
$$1-0.4^3 + 0.5(1-0.5) - (1-0.4^3)0.5(1-0.5) = 0.952$$
ונקבל $1-0.952 = 0.048$
מש"ל ב
## סעיף ג
צריך לבדוק האם מתקיים:
(במצב של $P(A_4^C inter B)$ הזרם יכול לזרום אך ורק מהענף העליון)
$$
P(A_4^C inter B) = P(A_4^C)P(B) \ 
0.468 = 0.5(1-0.4^3) != 0.5 dot 0.96 = 0.48
$$
לכן הם תלויים!
מש"ל ג


# שאלה 3
![[Pasted image 20260404165625.png]]
## סעיף א
נגדיר את המאורע של קובץ חשוד בתור $E$ .
נמצא את:
$$P(E inter B) = P(B) P(E|B) = 0.3 dot 0.4 = 0.12$$
מש"ל א
## סעיף ב
נחשב את נוסחת ההסתברות השלמה:
$$
P(E) = P(A) P(E|A) + P(B) P(E|B) + P(C) P(E|C) = \
P(E) = 0.5 dot 0.1 + 0.3 dot 0.4 + 0.2 dot 0.7 = 0.31 
$$
מש"ל ב
## סעיף ג
נרצה למצוא את (בעזרת נוסחת בייס):
$$1 - P(C|E) = 1 - (P(E|C)P(C))/(P(E))=1-(0.2 dot 0.7)/0.31 = 17/31 approx 0.548$$
מש"ל ג
# שאלה 4
![[Pasted image 20260404165645.png]]
## סעיף א
נחשב (בעזרת הנתונים, נוסחאת הכפל, והסתברות מותנית):
$$
P(B^C inter C) = P(C) - P(B inter C) = \
P(C) - (P(A inter B inter C) + P(A^C inter B inter C)) = \
P(C) - (P(B inter C | A) P(A) + P(A^C inter B inter C)) = \
P(C) - (P(B | A) P(C | A) P(A) + P(A^C inter B inter C)) = \
P(C) - (P(B) P(C inter A) + P(A^C inter B inter C)) = \
0.5 - (0.5 dot 0.4  + 0.05) = 0.25
$$
מש"ל א
## סעיף ב
נחשב את:
$$
P(B union C | A) = P(B|A) + P(C|A) - P(B inter C | A) = \
P(B inter C | A) = P(B) + 
$$
