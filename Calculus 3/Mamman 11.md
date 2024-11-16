# שאלה 1 
![[Pasted image 20241113130523.png]]

 נתון:
 קיימת פונ $\varphi$ כאשר:
 $$\varphi(B(0^{[k]};1)) = B(a;r)$$
 צ"ל:
 $$\varphi(S(0^{[k]};1)) = S(a;r)$$
 נסתכל על $\varphi$ : (פונקציה אפינית)
$$\varphi(x) = f(x) + b$$
ניקח פונ' 
$$\varphi_{0}(x) = \frac{2}{r}*f(x) + b - a$$
כאשר קיימת $A\in M^{\mathbb{R}}_{k\times k}$ כאשר:
$$\varphi_{0}(x) = xA^t+b-a$$
לפי הגדרת $\varphi, \varphi_{0}$ נקבל:
$$\varphi_{0}(B(0^{[k]};1)) = B(0^{[k]};2)$$
נסתכל על הבסיס הסטנדרטי $E=(e_{1},e_{2},\dots,e_{k})$ מעל $\mathbb{R}^{k}$, ונקבל:
$$\forall 1\leq n\leq k(\exists x \in B(0^{[k]},1)(\varphi_{0}(x)=e_{n}))$$
לכן $A$ מטריצה הפיכה ולכן הפונקציה

$$f_{0}(x) = xA^t$$
הפיכה ועל, (מהקורס אלגברה ליניארית 1) 
ולכן, ניתן להבין בבירור כי הפונקציה $\varphi_{0}$ הפיכה ועל.
לכן, הפונקציה $\varphi$ הפיכה ועל.
## כיוון 1:
יהי:
$$ c \in S(a,r)$$
לכן קיימות סדרות $(d_{n}),(e_{n})$  כאשר: (לפי הגדרת $\partial B(a;r)$)
$$ \lim_{ n \to \infty } {(d_{n})} = c = \lim_{ n \to \infty } {(e_{n})} $$
$$ \forall n>0 (d_{n} \in B(a,r),e_{n} \notin B(a,r)) $$
נגדיר את הסדרות $(a_{n})_{n},(b_{n})_{n}$ באופן הבא:
$$\forall n>0(a_{n}=\varphi^{-1}(d_{n}),b_{n}=\varphi^{-1}(e_{n}),)$$
נסתכל על הסדרות הללו ונקבל: 
$$\forall n>0(d_{n} \in B(a,r)) \implies \forall n>0(a_{n} \in B(0^{[k]},1))$$
בנוסף, מפני ש $\varphi$ פונ חח"ע,אז לא יכול להיות $b_n$ ,שנמצא מחוץ ל $B(0;1)$, ומקיים $b_n \in B(a;r)$
$$\forall n>0(e_{n} \notin B(a,r)) \implies \forall n>0(b_{n} \notin B(0^{[k]},1))$$
אך ידוע כי מתקיים
$$\lim_{ n \to \infty }(d_{n})=\lim_{ n \to \infty } (e_{n})=c $$
כלומר, (מפני ש $\varphi$ רציפה אז גם $\varphi^{-1}$ רציפה)
$$\lim_{ n \to \infty }(\varphi^{-1}(d_{n})) = \lim_{ n \to \infty }(\varphi^{-1}(e_{n})) = \varphi^{-1}(c)$$
ונקבל
$$\lim_{ n \to \infty } (a_{n}) = \lim_{ n \to \infty }(b_{n}) = \varphi^{-1}(c) $$
לכן, מתקיים:

$$\forall \text{Neighbourhood D of }\varphi^{-1}(c)(\exists n,m(a_{n} \in D\ \text{and}\ b_{m} \in D)) $$
ידוע כי
$$\forall n>0(a_{n} \in B(0^{[k]},1))$$
$$\forall n>0(b_{n} \notin B(0^{[k]},1))$$
ונקבל כי 
$$\varphi^{-1}(c) \in \partial B(0;1)$$
כלומר, 
$$\varphi^{-1}(c) \in S(0^{[k]};1)$$
לכן
$$c \in \varphi(S(0^{[k]};1))$$
ונקבל 
$$S(a;r) \subseteq \varphi(S(0^{[k]};1)) $$
## כיוון 2:
יהי:
$$y \in \varphi(S(0^{[k]};1)),x \in \mathbb{R}^{k}$$
כאשר:
$$\varphi(x) = y$$
ניקח סדרות $(d_{n}),(e_{n})$  כאשר: (לפי הגדרת $\partial B(0^{[k]};1)$)
$$ \lim_{ n \to \infty } {(d_{n})} = x = \lim_{ n \to \infty } {(e_{n})} $$
$$ \forall n>0 (d_{n} \in B(0^{[k]},1),e_{n} \notin B(0^{[k]},1)) $$
מפני ש $\varphi$ פונ' חח"ע, נקבל:
$$\forall n>0(\varphi(d_n) \in B(a;r),\varphi(e_n) \notin B(a;r))$$
מפני ש $\varphi$ פונ' רציפה, נקבל:
$$\lim_{n \rightarrow \infty}(\varphi(d_n)) = \varphi(\lim_{n \rightarrow \infty}(d_n)) = \varphi(x) = y =\varphi(\lim_{n \rightarrow \infty}(e_n))= \lim_{n \rightarrow \infty}(\varphi(e_n))$$
לפי הסדרות $(\varphi(d_n)),(\varphi(e_n))$, ולפי התנהגותן סביב $y$, נקבל כי 
$$\forall \text{Neighbourhood D of }y(\exists n,m(\varphi(d_n) \in D\ \text{and}\ \varphi(e_{m}) \in D)) $$
כאשר
$$ \forall n>0 (d_{n} \in B(0^{[k]},1),e_{n} \notin B(0^{[k]},1)) $$
לכן, לפי הגדרת $y$ נקבל:
$$y \in \partial B(a;r)$$
כלומר,
$$y \in S(a;r)$$
ולכן,
$$\varphi(S(0^{[k]};1)) \subseteq S(a;r)  $$
ולפי הכלה דו כיוונית, נקבל:
$$\varphi(S(0^{[k]};1)) = S(a;r)  $$
מש"ל
# שאלה 2
![[Pasted image 20241116224136.png]]
נניח בשלילה כי קיים
$$x \in \partial(A\backslash \partial A), x \notin \partial A $$
לכן קיימת נקודה $x \in \mathbb{R}^k$ כאשר:
$$\forall \text{Neighbourhood D of }x(\exists a,b \in D(a \in A \backslash \partial A \text{ and } b \notin A \backslash \partial A))$$
ומתקיים:
$$\exists \text{Neighbourhood D of }x(D \subseteq A \text{ or } D \subseteq \mathbb{R}^k\backslash A)$$
נזכור שמתקיים בכל מקרה $x \notin \partial A$, ולכן מתקיים:
$$\forall \text{Neighbourhood D of }x(\exists a,b \in D(a \in A  \text{ and } b \notin A))$$
ידוע כי קיימת סביבה $D$ כאשר $D \subseteq A$ או $D \subseteq \mathbb{R}^k \backslash A$
אך זו סתירה כי לכל סביבה D קיים איבר ב$A$ וקיים איבר לא ב$A$
לכן, קיבלנו סתירה, ולכן ההנחה שגוייה
לכן מתקיים
$$\partial(A \backslash \partial A) \subseteq \partial A$$
מש"ל