# שאלה 1 ![[Pasted image 20241206143537.png]]
נגדיר $f$:
$$f: M_{k \times k}(\mathbb{R}) \rightarrow M_{k \times k}(\mathbb{R})$$
$$f(X) = X^2$$
ניקח $V$ סביבה פתוחה של $I$.
נמצא את $Df_X$:
$$\frac{f(X+H)-f(X)-Df_X(H)}{|H|}\xrightarrow[H->0^{[k^2]}]{}0$$
$$\frac{X^2+XH+HX+H^2-X^2-Df_X(H)}{|H|}\xrightarrow[H->0^{[k^2]}]{}0$$
$$\frac{XH+HX-Df_X(H)}{|H|}+\frac{o(|H|)}{|H|}\xrightarrow[H->0^{[k^2]}]{}0$$
ונקבל:
$$Df_X(H)=XH+HX$$
מהקורס אלגברה ליניארית 1, נקבל כי הפונ' הפיכה ב $X=I$.
לפי משפט 7.א.4 (משפט הפונ' ההופכית) נקבל כי קיים כדור פתוח $B$ סביב $I$ כאשר $f(B)$ קבוצה פתוחה.
לכן קיימת סביבה סביב $I^2= I$ כאשר הסביבה הנ"ל פתוחה
מש"ל.
# שאלה 2 ![[Pasted image 20241206150602.png]]
תהי סביבה $A$ של $(a,b)$.
נניח בשלילה שהפונ' כן מוגדרת באופן סתום את $x$ כפונקציה של $y$.
נקבל שלפי מסקנה 7.ב.8, $F(x,y)$ מגדירה את $y$ כפונקציה של $x$.
נקבל כי קיים $g$ כאשר:
$$y=g(x)$$
לכל $(y,x) \in A$.
לפי הנחת השלילה, נקבל כי קיים $h$ כאשר מתקיים:
$$x=h(y)$$
ונקבל:
$$x=h(g(x))$$
לכל $x$ ב$A$.
לכן, $g$ ו $f$ הופכיות, ולכן הן חח"ע בסביבת $A$.
לפי הנתונים, ידוע כי:
$$\frac{\partial F}{\partial x}(a,b) = 0,
\frac{\partial^2 F}{\partial x^2}(a,b) \ne 0 $$
ולכן, לפי מסקנה 7.ב.8, נקבל כי:
$$g'(x)=\frac{\frac{\partial g}{\partial x}(x,g(x))}{\frac{\partial g}{\partial y}(x,g(x))}$$
לפי הנתונים:
$$g'(a)=\frac{\frac{\partial g}{\partial x}(a,g(a))}{\frac{\partial g}{\partial y}(a,g(a))}=0$$
נמצא את $g''(x)$:
$$g''(x)=\left(\frac{F_x(x,g(x))}{F_y(x,g(x))}\right)'=$$
$$
\small g''(x)=\frac{(F_{xx}(x,g(x))+F_{xy}(x,g(x))g'(x))F_y(x,g(x))-(F_{yx}(x,g(x))+F_{yy}(x,g(x))g'(x))F_x(x,g(x))}{(F_y(x,g(x)))^2}=
$$
נציב $x=a$:
$$g''(a)=\frac{(F_{xx}(a,b)+F_{xy}(a,b)g'(a))F_y(a,b)-(F_{yx}(a,b)+F_{yy}(a,b)g'(a))F_x(a,b)}{(F_y(a,b))^2}$$
לפי הנתונים ידוע כי $F_x(a,b)=0$. לכן:
$$g''(a)=\frac{(F_{xx}(a,b)+F_{xy}(a,b)g'(a))F_y(a,b)}{(F_y(a,b))^2}$$
בנוסף ידוע כי $g'(a)=0$ לכן:
$$g''(a)=\frac{(F_{xx}(a,b))F_y(a,b)}{(F_y(a,b))^2}$$
לפי הנתונים:
$$F_{xx}(a,b) \ne 0,\ F_y(a,b) \ne 0$$
ולכן:
$$g''(a) \ne 0$$
ולכן, מהקורס חשבון אינפיניטסימלי 1, נקבל כי $g(a)=b$ הינה נק' קיצון. לכן היא לא חח"ע כי בסביבה של $x=a$ מתקיים $g(a)>g(x)$ ולכן לא חח"ע. 
לכן סתירה.
לכן $x$ לא פונ' של $y$.
מש"ל.
# שאלה 3 ![[Pasted image 20241208163457.png]]
נפרק את הנק ב$S$ ל3 אופציות:
# אופציה 1: $z> \frac{3}{2}$
נקבל $(x,y,z) \in S_2 \cap (\mathbb{R}^2 \times \left(\frac{3}{2},\infty \right))$:
נבנה את הפונ:
$$f_2: \mathbb{R}^2 \times \left( \frac{3}{2},\infty \right) \rightarrow \mathbb{R}$$
$$f_2(x,y,z)=x^2+y^2+(z-2)^2$$
(המרחק ממרכז הספירה).
נקבל:
$$\triangledown f_2(x,y,z) = \begin{pmatrix}
2x &2y &2z-4
\end{pmatrix}$$
מפני שהנגזרות החלקיות רציפות
נקבל כי לכל $(x,y,z) \in S_2$ מתקיים:
$$f_2(x,y,z)=1,\ \triangledown f_2(x,y,z) \ne 0$$
ונקבל שלכל $a \in S_2$ :
$$S \cap \left(\mathbb{R}^2 \times \left( \frac{3}{2}, \infty \right)\right)=
\{ v | v \in \mathbb{R}^2 \times \left( \frac{3}{2}, \infty \right), f_2(v) = f_2(a)=1 \}=S \cap (\mathbb{R}^2 \times \left( \frac{3}{2}, \infty \right))$$
# אופציה 2: $0 < z < \frac{3}{2}$
נקבל $(x,y,z) \in S_1$.
נגדיר פונ'
$$f_1: \mathbb{R}^2 \times \left( 0, \frac{3}{2} \right) \rightarrow \mathbb{R}$$
$$f_1(x,y,z) = 3x^2+3y^2-z^2$$
נקבל כי מתקיים לכל $a \in S_1$ אם"ם ש $f(a)=0$. (לפי הגדרת $S_1$)
לכן נקבל כי לכל $a \in S_1$:
$$S_1=S_1 \cap (\mathbb{R}^2 \times \left( 0, \frac{3}{2} \right))=\{v | v \in (\mathbb{R}^2 \times \left( 0, \frac{3}{2} \right)), f(v)=f(a)=0\}$$
# אופציה 3: $z = \frac{3}{2}$
ניקח את הפונ':
$$f: \mathbb{R}^2 \times (0,\infty) \rightarrow R$$
$$f(x,y,z) = \begin{cases}
f_1(x,y,z)-1 \text{ if } z \ge \frac{3}{2} \\
\frac{f_2(x,y,z)}{3} \text{ else }
\end{cases}$$
נקבל:
$$\triangledown f(x,y,z) = \begin{cases}
\triangledown f_1(x,y,z) \text{ if } z \ge \frac{3}{2} \\
\triangledown f_2(x,y,z) \text{ if } z < \frac{3}{2} \\
\end{cases}$$

כלומר:
$$\triangledown f(x,y,z) = \begin{cases}
(2x,2y,2z-4) \text{ if } z \ge \frac{3}{2} \\
(2x,2y,-\frac{2}{3}z) \text{ if } z < \frac{3}{2} \\
\end{cases}$$
ונקבל:
$$\triangledown f(x,y,z)=\left(2x,2y,\begin{cases}
(2z - 4) \text{ if } \ge \frac{3}{2} \\
(-\frac{2}{3}z)\ \  \text{ if } < \frac{3}{2}
\end{cases} \right)$$
נבדוק האם הנגזרות הרציפות (שמהן מורכב הגרדינאט רציף):
ידוע כי הפונ' $2x$ ו $2y$ רציפות. נסתכל על:
$$(z) \mapsto \begin{cases}
(2z - 4) \text{ if } \ge \frac{3}{2} \\
(-\frac{3}{2}z)\ \  \text{ if } < \frac{3}{2}
\end{cases} $$
נבדוק האם הפונ' הנ"ל רציפה. נבדוק מהקורס חשבון אינפיניטסימלי 1:
$$\lim_{z \rightarrow \frac{3}{2}}\left((z) \mapsto \begin{cases}
(2z - 4) \text{ if } \ge \frac{3}{2} \\
(-\frac{2}{3}z)\ \  \text{ if } < \frac{3}{2}
\end{cases} \right)$$
הערך הנ"ל קיים אם"ם מתקיים:
$$\lim_{z \rightarrow \frac{3}{2}^+}\left((z) \mapsto \begin{cases}
(2z - 4) \text{ if } \ge \frac{3}{2} \\
(-\frac{2}{3}z)\ \  \text{ if } < \frac{3}{2}
\end{cases} \right) = \lim_{z \rightarrow \frac{3}{2}^-}\left((z) \mapsto \begin{cases}
(2z - 4) \text{ if } \ge \frac{3}{2} \\
(-\frac{3}{2}z)\ \  \text{ if } < \frac{3}{2}
\end{cases} \right)$$
ונקבל:
$$\lim_{z \rightarrow \frac{3}{2}^+}\left( 2z - 4 \right) = \lim_{z \rightarrow \frac{3}{2}^-}\left(-\frac{2}{3}z \right)$$
מהקורס חשבון אינפיניטסימלי 1, ומהרציפות של הביטויים האלה נקבל:
$$(2) \left( \frac{3}{2} \right) - 4 = \left( -\frac{2}{3} \right)\left(  \frac{3}{2} \right)$$
$$-1 = -1$$
קיבלנו פסוק אמת, לכן הגבול מוגדר, ולכן הפונ' רציפה כאשר $z= \frac{3}{2}$.
לכן כל הנגזרות החלקיות רציפות. לפי משפט 3.ד.10, נקבל כי $f$ גזירה ברציפות בכל הנקודות כאשר $z= \frac{3}{2}$.
נקבל לכל $a \in S$:
לפי ההגדרה של $S$ ושל $f$, ניתן להסיק כי:
$$S \cap (\mathbb{R}^2 \times (0, \infty)) = \{x | x \in (\mathbb{R}^2 \times (0, \infty)), f(x)=f(a)=0\}$$
לכן, לפי משפט 7.ג.12, נקבל כי הקבוצה $S$ היא משטח על חלק.
מש"ל.


# שאלה 4 ![[Pasted image 20241209090315.png]]
נגדיר:

$$S_A= \bigcup_{a \in A}\{ ta\ |\ t>0 \}$$

נסתכל על $S$. נניח כי $S$ משטח על.
יהי $s \in S$. לפי ההגדרה של $S$ קיימת קבוצה פתוחה $U$ ב $\mathbb{R}^k$ וקבוצה פתוחה $\Omega$ ב$\mathbb{R}^d$והומיאומורפיזם $h: \Omega \rightarrow S \cap U$ כאשר:
$$\rho(Jh_{h^{-1}(s)}) = d = k-1$$
כלומר, המטריצה הזאת בעלת דרגה מלאה:
$$\begin{pmatrix}
\frac{\partial h_1}{\partial x_1} & \dots & \frac{\partial h_1}{\partial x_{k-1}}  \\
\vdots &  \ddots & \vdots \\
\frac{\partial h_k}{\partial x_1} & \dots & \frac{\partial h_1}{\partial x_{k-1}}
\end{pmatrix}$$
לפי סעיף 2 בנתונים, נקבל כי גם המטריצה הזאת בעלת דרגה מלאה (כי העמודות בת"ל):
$$\begin{pmatrix}
\frac{\partial h_1}{\partial x_1} & \dots & \frac{\partial h_1}{\partial x_{k-1}} & s_1 \\
\vdots &  \ddots & \vdots & \vdots \\
\frac{\partial h_k}{\partial x_1} & \dots & \frac{\partial h_1}{\partial x_{k-1}} & s_k
\end{pmatrix}$$ 
נסתכל על הפונ':
$$h': \Omega \times (0, \infty) \rightarrow S_{h(\Omega)}$$
כלומר:
$$h': \Omega \times (0, \infty) \rightarrow S_{S \cap U}$$
כאשר:
$$h':(x,t) \mapsto t h(x)$$
ניתן להסיק לפי נתון (1), לפי ש$h$ הומיאומורפיזם (פונ רציפה), ומההגדרה של $S_A$, נקבל כי $h'$ ורציפה גזירה והפיכה.
ונקבל כי
$$Dh'_{(x,t)}=\begin{pmatrix}
\frac{\partial h_1}{\partial x_1} & \dots & \frac{\partial h_1}{\partial x_{k-1}} & s_1 \\
\vdots &  \ddots & \vdots & \vdots \\
\frac{\partial h_k}{\partial x_1} & \dots & \frac{\partial h_1}{\partial x_{k-1}} & s_k
\end{pmatrix}$$
לפי משפט הפונקצייה ההופכית, נקבל כי לכל $s \in S \cap U$ קיימת סביבה המכילה כדור פתוח $B$, כאשר $h'(B)$ קבוצה פתוחה. לכן $h'(\Omega \times (0, \infty))$ קבוצה פתוחה. 

האיחוד של כל הקבוצות $h'(\Omega \times (0,\infty))$ לפי $s$ הוא $S'$ לפי ההגדרה של הפונ' והקבוצות הללו. איחוד של קבוצות פתוחות היא קבוצה פתוחה ולכן $S'$ פתוחה.
מש"ל
# שאלה 5 ![[Pasted image 20241209095803.png]]
לפי 2.ד.25, נקבל כי $A$ קבוצה סגורה. אראה כי היא חסומה.
$$x^6+y^6+z^6 \le 3 $$
ונקבל:
$$x \le \sqrt[6]{3},\ y \le \sqrt[6]{3},\ z \le \sqrt[6]{3}$$
לכן הקבוצה חסומה.
ידוע כי 
$$f: (x,y,z) \mapsto xyz$$
פונקצייה רציפה.
לכן נקבל כי קיים מינימום ומקסימום.
נפריד ל4 מקרים:
# מקרה 1: $x^6+y^6+z^6=3, x= \alpha y$
נגדיר פונ:
$$\varphi:(x,y,z) \mapsto \begin{pmatrix}
x^6+y^6+z^6 & x-\alpha y
\end{pmatrix}$$
נחשב את קבוצת הווקטורים:
$$\{ \triangledown \varphi_1(x,y,z),\triangledown \varphi_2(x,y,z), \triangledown f(x,y,z) \}=$$
ונקבל:
$$\{ (6x^5,6y^5,6z^5),(1,-\alpha,0),(zy,xz,xy) \}$$
נציב במטריצה:
$$\begin{vmatrix}
6x^5 & 6y^5 & 6z^5  \\
1 & -\alpha & 0 \\
zy & xz & xy
\end{vmatrix} = $$
$$\begin{vmatrix}
6x^5 & 6y^5 & 6z^5  \\
1 & -\alpha & 0 \\
zy & xz & xy
\end{vmatrix} = $$
$$\begin{vmatrix}
6x^5 & 6y^5 + \alpha 6x^5 & 6z^5  \\
1 & 0 & 0 \\
zy & xz + \alpha zy & xy
\end{vmatrix} = (6xy^6+ \alpha 6x^6y )-(6xz^6+6\alpha yz^6)=$$
$$=6(xy^6+\alpha x^6y-(x+\alpha y)z^6)$$
נציב:
$$x=\alpha y$$
נקבל:
$$=6(\alpha y^7+ \alpha^7y^7-(2\alpha y)z^6)=6(y^7(\alpha+\alpha^7)-2\alpha y z^6)$$
הדטרמיננטה הנ"ל שווה ל$0$ אם"ם:
$$z^6=y^6 \frac{\alpha^7+\alpha}{2\alpha}$$

ונקבל:
$$x= \alpha y, z = y\sqrt[6]{ \frac{\alpha^7+\alpha}{2\alpha}}$$
נבדוק מתי:
$$(\alpha y)^6+y^6+y^6 \frac{\alpha^7+\alpha}{2\alpha}=3$$
ולכן:
$$y = \sqrt[6]{ \frac{3}{\alpha^6+1+\frac{\alpha^7+\alpha}{2\alpha}} } = 
\sqrt[6]{ \frac{2}{\alpha^6+1}}$$
ולכן $\left( \alpha\sqrt[6]{\frac{2}{\alpha^6+1}},\sqrt[6]{ \frac{2}{\alpha^6+1}},1 \right)$ נק קיצון לכל .
# מקרה 2: $x^6+y^6+z^6=3, x < \alpha y$
ניקח: 
$$\varphi: (x,y,z) \mapsto x^6+y^6+z^6$$
נקבל:
$$\triangledown \varphi(x,y,z) = \begin{pmatrix}
6x^5 & 6y^5 & 6z^5
\end{pmatrix},
\triangledown f(x,y,z) = \begin{pmatrix}
yz & xz & xy
\end{pmatrix}
$$
נראה מתי הוקטורים האלה ת"ל.
אם הם ת"ל, אזי קיים $\beta$ כאשר:
$$(6x^5,6y^5,6z^5)+ \beta (yz,xz,xy)=0$$
ונקבל:
$$6x^5=-\beta yz,\ 6y^5=-\beta xz,\ 6z^5=-\beta xy$$
ונקבל
$$\frac{6x^5}{yz} = \frac{6y^5}{xz} = \frac{6z^5}{xy}$$
ולכן:
$$x^6=y^6=z^6$$
לכן נקבל, מ $x^6+y^6+z^6=3$ :
$$x=y=z=1$$
ונקבל שנקודה זו מתקיימת אם"ם $\alpha>1$.
ונקבל:
שהנק $(1,1,1)$ היא נק קיצון אםם $\alpha > 1$.
# מקרה 3: $x^6+y^6+z^6<3, x = \alpha y$
ניקח:
$$\varphi: (x,y,z) \mapsto x- \alpha y$$
$$\triangledown \varphi(x,y,z)=(1, -\alpha, 0)$$
$$\triangledown f(x,y,z) = (yz,xz,xy)$$
נבדוק מתי הם ת"ל:
אם הם ת"ל, אזי קיים $\beta$ כאשר:
$$(yz,xz,xy) = \beta (1,-\alpha,0)$$
ונציב $x=\alpha y$:
$$(yz,\alpha yz,\alpha y^2)=\beta (1,-\alpha,0)$$
ונקבל:
$$yz=\beta,\alpha yz=-\beta \alpha, \alpha y^2=0$$
לכן נקבל: $y=x=0$ וגם:
$$\beta=0$$
ולכל $z$.
לכן, נקבל שהנק $(0,0,z)$ היא נק קיצון לכל $0 \le z < \sqrt[6]{3}$.
# מקרה 4 $x^6+y^6+z^6<3, x < \alpha y$
נראה מתי הגרדיאנט מתאפס:
$$\triangledown f(x,y,z) = (yz,xz,xy) = 0$$
ונקבל 3 אפשרויות:
אפשרות 1:
$$x=y=0, 0 \le z <\sqrt[6]{3}$$
אפשרות 2:
$$x=z=y=0$$
אפשרות 3:
$$x=z=0, 0 \le y <\sqrt[6]{3}$$
ולכן אלה גם נקודות קיצון.
לסיכום, נקבל:
$$\left( \alpha\sqrt[6]{\frac{2}{\alpha^6+1}},\sqrt[6]{ \frac{2}{\alpha^6+1}},1 \right),
(1,1,1),
(0,0,a),
(0,0,0),
(0,a,0)$$
לכל $0 \le a < \sqrt[6]{3}$.
נמצא את המינימום והמקסימום. הוא בין הנקודות הנ"ל:
## מקסימום:
כל נקודה עם 0 ערכה הוא 0. לכן הנק מקסימום תיהיה אםם $\alpha>1$:
$$f(1,1,1) = 1$$
בנוסף, נקבל כי הנק $\left( \alpha\sqrt[6]{\frac{2}{\alpha^6+1}},\sqrt[6]{ \frac{2}{\alpha^6+1}},1 \right)$ היא גם נק מקסימום ומקסימום מוחלט, אם"ם הנק הנ"ל לא מוגדרת, ונקבל:
$$f\left( \alpha\sqrt[6]{\frac{2}{\alpha^6+1}},\sqrt[6]{ \frac{2}{\alpha^6+1}},1 \right)=\alpha \sqrt[3]{\frac{2}{a^6+1}}$$

## מינימום:
כל נקודה שמכילה את $0$ באחד האיברים שלה,  היא נק' מינימום, היות וזה הערך המינימלי שהפונ' מוציאה, כי $x,y,z$ אי שליליים.
מש"ל.