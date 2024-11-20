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
$$\varphi_{0}(x) = \frac{2}{r}*(f(x) + b - a)$$
כאשר קיימת $A\in M^{\mathbb{R}}_{k\times k}$ כאשר:
$$\varphi_{0}(x) = xA^t+\frac{2}{r}(b-a)$$
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
יהי
$$x \in \partial(A\backslash \partial A)$$
לכן קיימת נקודה $x \in \mathbb{R}^k$ כאשר:
$$\forall \text{Neighbourhood D of }x(\exists a,b \in D(a \in A \backslash \partial A \text{ and } b \notin A \backslash \partial A))$$
ונקבל:
$$\exists \text{Neighbourhood D of }x(\exists a,b \in D((a \in A \text{ and } (b \notin A \text{ or } b \in \partial A))))$$
יהי סביבה $D$ של $x$. קיים $b \in D$ כאשר $b \notin A$ או $b \in \partial A$
## אפשרות אחת: $b \notin A$
קיימת נקודה מחוץ ל$A$, ולכן יש איבר ב$A$ ואיבר מחוץ ל$A$
## אפשרות שנייה: $b \in \partial A$
לפי הגדרת $b$, לכל סביבה של $b$, כולל $D$, ולכן יש איבר ב$A$ ואיבר מחוץ ל$A$
לכן, לכל סביבה של x מתקיים:
$$\forall \text{Neighbourhood D of }x(\exists a,b \in D(a \in A \text{ and } b \notin A))$$
לכן מתקיים
$$ x \in \partial A $$
לכן
$$\partial ( A \backslash \partial A ) \subseteq \partial A $$
מש"ל


# שאלה 3
![[Pasted image 20241116232851.png]]
## כיוון 1
נניח כי $U$ קבוצה פתוחה.
נניח בשלילה כי קיים $a \in \mathbb{R}$ כאשר מתקיימת ההגדרה הנגדית לגבול:
$$\exists \varepsilon>0(\forall \delta>0(\exists a<x<a+\delta(f(x)-f(a) \ge \varepsilon)))$$
אראה כי קיימת נקודה $c \in U$ כאשר:
$$\exists c\in U(\forall \text{Neighbourhood D of }c \exists a,b \in \mathbb{R}^k(a \in U \text{ and } b \notin U))$$
מהנחת השלילה, נקבל:
$$\exists \varepsilon>0(\forall \delta>0(\exists a<x<a+\delta(f(x) \ge f(a)+\varepsilon)))$$
לפי הערכים מהנחת השלילה, ניקח את הנקודות: 
$$(a,f(a)+\varepsilon) \in U$$
$$(a,f(a)+\varepsilon-\frac{\delta}{2}) \in U$$
$$f(x) \ge f(a)+\varepsilon \implies (x,f(a)+\varepsilon) \notin U$$
נקבל שלכל $\delta>0$, המרחק בינהן הוא:
$$d = \sqrt{(a-x)^2+(f(a)+\varepsilon - f(a) - \varepsilon)^2}$$
$$d = |x-a|$$
$$0 < x-a < \delta$$
לכן, לכל סביבה של הנקודה $(a,f(a)+\varepsilon)$
קיים $\delta > 0$ כאשר הנקודות $(x,f(a)+\varepsilon),(a,f(a)+\varepsilon-\frac{\delta}{2})$ נמצאת בסביבה זו.
לכן $c$ מקיימת
$$\forall \text{Neighbourhood D of }c \exists a,b \in \mathbb{R}^k(a \in U \text{ and } b \notin U))$$
לכן $U$ לא פתוחה. לכן קיבלנו סתירה.
ולכן, הגבול מתקיים לכל $a$.
## כיוון 2
נניח כי מתקיים:
$$\forall a(\ \lim_{x->a^+}{f(x)}=f(a))$$
יהי $a \in \mathbb{R}$
ידוע כי מתקיים:
$$\forall \varepsilon>0(\exists \delta>0(a<x<a+\delta \implies |f(x)-f(a)| < \varepsilon))$$
מפני ש $x>a$, ו$f$ פונ' מונוטונית עולה, נקבל כי מתקיים:

$$\forall \varepsilon>0(\exists \delta>0(\forall a-\delta<x<a+\delta (f(x) < f(a)+\varepsilon)))$$
יהי $\varepsilon>0$. לכן קיים $\delta>0$ כאשר $\forall a<x<a+\delta (f(x) < f(a)+\varepsilon)$
ניקח את הנקודה $(a,f(a)+2\varepsilon)$. 
אראה כי קיימת סביבה לנקודה זו המוכלת ב $U$:
ניקח את הקבוצה הפתוחה:
$$U_a = \{(x,y)|\ y>f(x) \text{ and } a-\delta<x<a+\delta \}$$
ידוע כי לכל $a-\delta<x<a+\delta$ מתקיים $f(x)<f(a)+\varepsilon$
לכן,
$$(a-\delta,a+\delta) \times (f(a)+\varepsilon,\infty) \subseteq U_a$$
לפי טענה 2.א.29 מכרך א' בספר הלימוד,
נקבל כי הקבוצה $(a-\delta,a+\delta) \times (f(a)+\varepsilon,\infty)$ היא קבוצה פתוחה
ידוע כי מתקיים $(a,f(a)+2\varepsilon) \in U_a$
ולכן היא סביבה של נקודה זו.
לכן, קבוצה זו היא קבוצה פתוחה

קיבלנו שהצד הראשון גורר את השני והצד השני גורר את הראשון
לכן הטענות הללו שקולות
מש"ל
# שאלה 4 ![[Pasted image 20241119092213.png]]
נסתכל על הגבול
$$\lim_{x \rightarrow 0^{[k]}}{\frac{e^{ -\frac{1}{|x|} }}{(\displaystyle\sum_{i=1}^{k}|x_i|)^{\alpha}}} = \lim_{x \rightarrow 0^{[k]}}{\frac{e^{ -\frac{1}{|x|} }}{\left(\sqrt{\displaystyle\sum_{i=1}^{k}|x_i|}\right)^{2\alpha}}}$$
יהי $x \in U$ איבר בסביבה של $0^{[k]}$
ידוע כי מתקיים:
$$0\le {\frac{e^{ -\frac{1}{|x|} }}{\left(\sqrt{\displaystyle\sum_{i=1}^{k}|x_i|}\right)^{2\alpha}}} \le

{\frac{e^{ -\frac{1}{|x|} }}{\left(\sqrt{\displaystyle\sum_{i=1}^{k}x_i^2}\right)^{2\alpha}}} = 

{\frac{e^{ -\frac{1}{|x|} }}{\left(|x|\right)^{2\alpha}}}$$
ידוע כי לפי חוק הסנדוויץ' 2.ו.1 בכרך א, מתקיים:
$$0\le \lim_{x \rightarrow 0^{[k]}}{\frac{e^{ -\frac{1}{|x|} }}{\left(\sqrt{\displaystyle\sum_{i=1}^{k}|x_i|}\right)^{2\alpha}}} \le

\lim_{x \rightarrow 0^{[k]}}{\frac{e^{ -\frac{1}{|x|} }}{\left(|x|\right)^{2\alpha}}}$$
נסתכל על הגבול
$$\lim_{x \rightarrow 0^{[k]}}{\frac{e^{ -\frac{1}{|x|} }}{\left(|x|\right)^{2\alpha}}}$$
נקבל:
$$\lim_{x \rightarrow 0^{[k]}}{\frac{e^{ -\frac{1}{|x|} }}{\left(|x|\right)^{2\alpha}}} = \lim_{x \rightarrow 0^+} \frac{e^{-\frac{1}{x}}}{x^{2 \alpha}}$$
מהקורס חשבון אינפיניטסימלי 1, הגבול הבא שקול:
$$\lim_{x \rightarrow \infty}\frac{e^{-x}}{\frac{1}{x^{2\alpha}}} $$
ונקבל:
$$\lim_{x \rightarrow \infty}\frac{x^{2a}}{e^x}$$
נשתמש בחוק לופיטל ונקבל:
$$\lim_{x\rightarrow \infty}{\frac{2ax^{2a-1}}{e^x}}$$
נשתמש בו עוד $n$ פעמים עד שמתקיים $2a-n<0$, ונקבל:
$$\lim_{x \rightarrow \infty}\frac{\left(\displaystyle\prod^{2a+n-1}_{i=2a}i\right)x^{n-2a}}{e^x}$$
ונקבל:
$$\lim_{x \rightarrow \infty}\frac{\left(\displaystyle\prod^{2a+n-1}_{i=2a}i\right)x^{n-2a}}{e^x}=\text{"}\frac{0}{\infty}\text{"}=0$$
לכן מתקיים
$$0\le \lim_{x \rightarrow 0^{[k]}}{\frac{e^{ -\frac{1}{|x|} }}{\left(\sqrt{\displaystyle\sum_{i=1}^{k}|x_i|}\right)^{2\alpha}}} \le

\lim_{x \rightarrow 0^{[k]}}{\frac{e^{ -\frac{1}{|x|} }}{\left(|x|\right)^{2\alpha}}}=0$$
ונקבל: 
$$\lim_{x \rightarrow 0^{[k]}}{\frac{e^{ -\frac{1}{|x|} }}{\left(\displaystyle\sum_{i=1}^{k}|x_i|\right)^\alpha}}=
\lim_{x \rightarrow 0^{[k]}}{\frac{e^{ -\frac{1}{|x|} }}
{\left(\sqrt{\displaystyle\sum_{i=1}^{k}|x_i|}\right)^{2\alpha}}}=0$$
מש"ל
# שאלה 5
![[Pasted image 20241118182805.png]]
## סעיף א
ניקח $S=\{(x,y,z)\ |\ (x^2+y^2+z^2)^2 = x^2+y^2\}$
אראה כי קיימת פונ' $h$ שהיא הומיאומורפיזם מ$S$ ל$\mathbb{R}^2$
נסתכל על הקבוצה $S$
ניקח $(x,y,z) \in S$
לכן,
$$(x^2+y^2+z^2)^2=x^2+y^2 / \sqrt{}$$
$$x^2+y^2+z^2=\pm \sqrt{x^2+y^2} $$
$$z^2=(\pm \sqrt{x^2+y^2})-x^2-y^2 $$
אם ה"פלוס מינוס יהיה מינוס" אזי צד אחד במשוואה תמיד יהיה חיובי והצד השני תמיד יהיה שלילי, לכן הוא לא יכול להיות מינוס.
ונקבל:
$$z=\pm \sqrt{\sqrt{x^2+y^2}-x^2-y^2} $$

ניקח 
$f:  S \rightarrow \mathbb{R}^2 \backslash \{(0,0,0)\}$ כאשר:
$$f(x,y,z) = \begin{cases} (x,y) &\text{if } z>=0 \\ \left( \frac{x}{x^2+y^2},\frac{y}{x^2+y^2} \right) &\text{else }  \end{cases}$$
אראה שקיימת פונ' הופכית ל$f$ ולכן היא הומיאומורפיזם
ניקח:
$$f(x,y) = \begin{cases} \left( \frac{x}{x^2+y^2},\frac{y}{x^2+y^2},\sqrt{\frac{1}{\sqrt{x^2+y^2}}-\frac{1}{x^2+y^2}} \right) &\text{if } z>0 \\ (x,y,-\sqrt{\sqrt{x^2+y^2}-x^2-y^2}) &\text{else }  \end{cases}$$
לכן, $f$ הומיאומורפיזם
ולכן הקבוצה $S$ היא משטח (כמובן ש $\mathbb{R}^2 \backslash \{(0,0,0)\}$ קבוצה פתוחה)
משל א
## סעיף ב
יהי $r \in (0,1]$
נסתכל 
ניקח:
$$S_1 = \{(x,y,z)\ |\ (x,y,z) \in S \cap B(0^{[3]},r)  \text{ and } z \ge 0 \}$$
$$S_2 = \{(x,y,z)\ |\ (x,y,z) \in S \cap B(0^{[3]},r) \text{ and } z \le 0 \}$$
נניח כי קיימת מסילה $\varphi$ מהנקודה $a \in S_1$ ל $b \in S_2$.
ניקח את האיבר השלישי במסילה זו:
$$[\varphi]_3$$
מפני שהמסילה היא פונ' רציפה, כך גם כל איברי הפונ', ולכן גם הפונ' $[\varphi]_3$ רציפה.
ממשפט ערך הביניים של קושי מהקורס חשבון אינפיניטסמילי 1, נקבל כי מתקיים:
$$\forall{a_3 \ge y \ge b_3}(\exists x(([\varphi]_3)(x)=y)$$
ולכן, לפי הגדרת $a$ ו $b$, נקבל כי קיים $x$ כאשר:
$$([\varphi]_3)(x)=0$$
נסתכל על $\varphi(x)=c$
לפי הגדרת נקודה ב $S$,נקבל:
$$c_3=\pm \sqrt{\sqrt{c_1^2+c_2^2}-c_1^2-c_2^2}$$
$$c_3=0$$
ונקבל:
$$0=\sqrt{c_1^2+c_2^2}-c_1^2-c_2^2$$
$$0=\sqrt{c_1^2+c_2^2}-c_1^2-c_2^2$$
$$c_1^2+c_2^2=\sqrt{c_1^2+c_2^2}$$
$$(c_1^2+c_2^2)^2=c_1^2+c_2^2$$
ונקבל:
$$(c_1^2+c_2^2)(c_1^2+c_2^2-1)=0$$
ונקבל:
$$c_1^2+c_2^2=0 \text{ or } c_1^2+c_2^2=1$$
נפריד למקרים:
### אפשרות 1: $c_1^2+c_2^2=1$
נקבל כי
$$c\notin B(0^{[3]},r)$$
### אפשרות 2: $c_1^2+c_2^2=0$, כלומר $c=0^{[3]}$
נקבל כי 
$$c \in B(0^{[3]},r)$$
לכל $r \in (0,1]$.
לכן המסילה חייבת לעבור ב $0^{[3]}$, ולכן זו סתירה כי איבר זה לא נמצא בקבוצה.
לכן הקבוצה $S \cap B(0^{[3]},r)$ לא קשורה מסילתית.
נסתכל על הקבוצות $S'_1=S_1 \cup \{0^{[3]}\},S'_2 = S_2 \cup \{0^{[3]}\}$, כאשר אראה שהן קשורות מסילתית, ומפני שיש להן נקודה משותפת $0^{[k]}$ אזי האיחוד של שתיהן קשור מסילתית.
לפני, נגדיר יותר במדיוק את הקבוצות $S'_1,S'_2$ניקח נקודה ב$S$, ונראה האם היא ב $B(0^{[3]},r)$
$$(x,y,\sqrt{\sqrt{x^2+y^2}-x^2-y^2})) \in S$$
$$x^2+y^2+\left(\sqrt{\sqrt{x^2+y^2}-x^2-y^2}\right) ^2 < r$$
$$x^2+y^2-x^2-y^2+\sqrt{x^2+y^2} < r$$
ונקבל:
$$x^2+y^2 < r^2$$
### הקבוצה הראשונה: $S'_1 = \{(x,y,z)\ |\ (x,y,z) \in S \text{ and } z \ge 0 \text{ and } x^2+y^2<r^2 \} \cup \{0^{[3]}\}$
ניקח את הפונ' 

$$f_1: \{(x,y)\ |\ x^2+y^2 < r^2\} \rightarrow S'_1$$
$$f_1(x,y) = (x,y,\sqrt{\sqrt{x^2+y^2}-x^2-y^2}) \in S'_1$$
לכן הפונ $f_1$ רציפה, וידוע כי $B(0^{[2]},r^2)$ קשורה מסילתית.
לכן, נקבל
$$f_1(B(0^{[2]},r^2)) = S'_1$$
ולפי טענה 2.ט.2 מספר הלימוד, הקבוצה $S'_1$ קשורה מסילתית

### הקבוצה השנייה: $S'_2 = \{(x,y,z)\ |\ (x,y,z) \in S \text{ and } z \le 0 \text{ and } x^2+y^2<r^2 \} \cup \{0^{[3]}\}$
ניקח את הפונ' 

$$f_2: \{(x,y)\ |\ x^2+y^2 < r^2\} \rightarrow S'_2$$
$$f_2(x,y) = (x,y,-\sqrt{\sqrt{x^2+y^2}-x^2-y^2}) \in S'_2$$
לכן הפונ $f$ רציפה, וידוע כי $B(0^{[2]},r^2)$ קשורה מסילתית.
לכן, נקבל
$$f_2(B(0^{[2]},r^2)) = S'_2$$
ולפי טענה 2.ט.2 מספר הלימוד, הקבוצה $S'_2$ קשורה מסילתית.
לכן הקבוצות הללו קשורות מסילתית.
ניקח $a \in S'_1, b \in S'_2$. אראה שהם קשורים מסילתית.
ניקח מסילה מ $a$ ל $0^{[3]}$, ומסילה מ $0^{[3]}$ ל- $b$. 
לכן קיימת מסילה מ$a$, ל$0^{[k]}$, ל$b$ היא מסילה שעוברת ב $S'_1 \cup S'_2 = S\cap B(0^{[2]},r^2) \cup {0^{[3]}}$.
ולכן כל 2 נקודות בקבוצות הללו קשורות מסילתית,
ולכן הקבוצה $S'_1 \cup S'_2 = S\cap B(0^{[2]},r^2) \cup {0^{[3]}}$ קשורה מסילתית.
הקבוצה $S \cap B(0^{[3]},r)$ לא קשורה מסילתית.
מש"ל ב