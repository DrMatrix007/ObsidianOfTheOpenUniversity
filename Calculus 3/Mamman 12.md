# שאלה 1 ![[Pasted image 20241202084225.png]]
נסתכל על נקודה $0$. נבדוק האם היא גזירה ב$f$. 
נניח כי קיימת 
$$\triangledown f(0^{[3]}) = \begin{pmatrix}
\frac{\partial f}{\partial x}(0^{[3]})\\
\frac{\partial f}{\partial y}(0^{[3]})\\
\frac{\partial f}{\partial z}(0^{[3]})\\
\end{pmatrix}$$
נחשב את הגבולות של הנגזרות החלקיות:
$$\lim_{h \rightarrow 0}(\frac{f(h,0,0)-f(0)}{h}) = \frac{\partial f}{\partial x}(0,0,0) =\lim_{h \rightarrow 0}(\frac{f(h,0,0)-f(0)}{h}) = \lim_{h \rightarrow 0}(\frac{ \frac{h^2*0*0^2}{h^8+0}-0}{h})=0$$

$$\lim_{h \rightarrow 0}(\frac{f(0,h,0)-f(0)}{h}) = \frac{\partial f}{\partial y}(0,0,0) =\lim_{h \rightarrow 0}(\frac{f(0,h,0)-f(0)}{h}) = \lim_{h \rightarrow 0}(\frac{ \frac{0^2*h*0^2}{0+h^6+0}-0}{h})=0$$

$$\lim_{h \rightarrow 0}(\frac{f(0,0,h)-f(0)}{h}) = \frac{\partial f}{\partial z}(0,0,0)=\lim_{h \rightarrow 0}(\frac{f(0,0,h)-f(0)}{h}) = \lim_{h \rightarrow 0}(\frac{ \frac{0^2*0*h^2}{0+h^4}-0}{h})=0$$
ונקבל לפי משפט 3.ג.6:
$$\triangledown f(0^{[3]}) = \begin{pmatrix}
\frac{\partial f}{\partial x}(0^{[3]})\\
\frac{\partial f}{\partial y}(0^{[3]})\\
\frac{\partial f}{\partial z}(0^{[3]})\\
\end{pmatrix}=\begin{pmatrix}
0\\
0\\
0\\
\end{pmatrix}$$
לכן נקבל:
$$\lim_{(x,y,z) \rightarrow (0,0,0)}(\frac{f(x,y,z)+f(0,0,0)- \triangledown f(0,0,0)*\begin{pmatrix}
x\\
y\\
z\\
\end{pmatrix}}{\sqrt{x^2+y^2+z^2}})=$$$$\lim_{(x,y,z) \rightarrow (0,0,0)}(\frac{\frac{x^2yz^2}{x^8+y^6+z^4}}{\sqrt{x^2+y^2+z^2}})$$
נמיר להצגה פולארית:
$$(x,y,z) \mapsto (r,\theta_1,\theta_2)$$
$$x \mapsto r \cos(\theta_1)\cos(\theta_2)$$
$$y \mapsto r \cos(\theta_1)\sin(\theta_2)$$
$$z \mapsto r \sin(\theta_1)$$
ונקבל:
$$\lim_{r \rightarrow 0^+}(\frac{\frac{(r \cos(\theta_1)\cos(\theta_2))^2(r \cos(\theta_1)\sin(\theta_2))(r \sin(\theta_1))^2}{(r \cos(\theta_1)\cos(\theta_2))^8+(r \cos(\theta_1)\sin(\theta_2))^6+(r \sin(\theta_1))^4}}{\sqrt{(r \cos(\theta_1)\cos(\theta_2))^2+(r \cos(\theta_1)\sin(\theta_2))^2+(r \sin(\theta_1))^2}}) =$$
$$\lim_{r \rightarrow 0^+}(
\frac{\frac{r^5\cos^5(\theta_1)\cos^2(\theta_2)\sin(\theta_2)\sin^2(\theta_1)}{(r \cos(\theta_1)\cos(\theta_2))^8+(r \cos(\theta_1)\sin(\theta_2))^6+(r \cos(\theta_1))^4}}{\sqrt{(r \cos(\theta_1)\cos(\theta_2))^2+(r \cos(\theta_1)\sin(\theta_2))^2+(r \cos(\theta_1))^2}})$$
נחלק ב$r^5$ את המונה והמכנה:
$$\scriptsize{\lim_{r \rightarrow 0^+}(
\frac{\cos^5(\theta_1)\cos^2(\theta_2)\sin(\theta_2)\sin^2(\theta_1)}{(r^3( \cos(\theta_1)\cos(\theta_2))^8+r(\cos(\theta_1)\sin(\theta_2))^6+( \cos(\theta_1))^4)(\sqrt{(\cos(\theta_1)\cos(\theta_2))^2+( \cos(\theta_1)\sin(\theta_2))^2+(\cos(\theta_1))^2}})}=$$
$$\frac{\cos^5(\theta_1)\cos^2(\theta_2)\sin(\theta_2)\sin^2(\theta_1)}{( \cos(\theta_1))^4)(\sqrt{(\cos(\theta_1)\cos(\theta_2))^2+( \cos(\theta_1)\sin(\theta_2))^2+(\cos(\theta_1))^2})} \ne 0$$
לכן זו סתירה להגדרה ולכן הנקודה לא גזירה ב0.
נסתכל על הנקודות$(x,y,z) \ne (0,0,0)$.
לפי משפט 3.ג.6, נחשב:
$$\triangledown f(0^{[3]}) = \begin{pmatrix}
\frac{\partial f}{\partial x}(x,y,z)\\
\frac{\partial f}{\partial y}(x,y,z)\\
\frac{\partial f}{\partial z}(x,y,z)\\
\end{pmatrix}=\begin{pmatrix}
\frac{2xyz^2(x^8+y^6+z^4)-8x^7x^2yz^2}{(x^8+y^6+z^4)^2}\\
\frac{x^2z^2(x^8+y^6+z^4)-6x^5x^2yz^2}{(x^8+y^6+z^4)^2}\\
\frac{2zyx^2(x^8+y^6+z^4)-4z^3x^2yz^2}{(x^8+y^6+z^4)^2}\\
\end{pmatrix}$$
קיבלנו ש $\frac{\partial f}{\partial x}(x,y,z),\frac{\partial f}{\partial y}(x,y,z),\frac{\partial f}{\partial z}(x,y,z)$ פונ רציפות ב$(x,y,z) \ne (0,0,0)$ ולכן היא גזירה חלקית ברציפות בכל $\mathbb{R}^2 \backslash \{0^{[3]}\}$ ולכן גזירה בכל $\mathbb{R}^2 \backslash \{0^{[3]}\}$ לפי משפט 3.ד.2
לכן הפונ' גזירה בכל $\mathbb{R}^2 \backslash \{0^{[3]}\}$
מש"ל
# שאלה 2
![[Pasted image 20241202084253.png]]
ניקח פונקציות חלקיות שגזירות בנקודה $a$:
$$f(x): \mathbb{R}^k \rightarrow M_{l \times m}(\mathbb{R}),g(x): \mathbb{R}^k \rightarrow M_{m \times n}(\mathbb{R})$$
ניקח:
$$p(x): \mathbb{R}^k \rightarrow M_{l \times n}(\mathbb{R}),\ x \mapsto f(x)g(x)$$
לכן מתקיימת הגדרת הנגזרת:
$$\lim_{h \rightarrow 0^{[k]}}\frac{f(a+h)-f(a)-Df_a(h)}{|h|}=0$$
$$\lim_{h \rightarrow 0^{[k]}}\frac{g(a+h)-g(a))-Dg_a(h)}{|h|}=0$$
ולכן, נקבל שמתקיים:
$$f(a+h)-f(a)=Df_a(h)+o(|h|)$$
$$g(a+h)-g(a)=Dg_a(h)+o(|h|)$$
ונקבל:
$$f(a+h)=f(a)+Df_a(h)+o(|h|)$$
$$g(a+h)=g(a)+Dg_a(h)+o(|h|)$$
נבדוק אם הגבול קיים וקיימת פונקציה ליניארית כאשר:
$$\frac{p(a+h)-p(a)-Dp_a(h)}{|h|}\xrightarrow[h \rightarrow 0^{[k]}]{}0$$
ונקבל:
$$\frac{f(a+h)g(a+h)-f(a)g(a)-Dp_a(h)}{|h|}\xrightarrow[h \rightarrow 0^{[k]}]{}0$$
$$\frac{(f(a)+Df_a(h)+o(|h|))(g(a)+Dg_a(h)+o(|h|))-f(a)g(a)-Dp_a(h)}{|h|}\xrightarrow[h \rightarrow 0^{[k]}]{}0$$
$$\frac{f(a)g(a)+f(a)Dg_a(h)+Df_a(h)g(a)+o(|h|)+o(|h|)-f(a)g(a)-Dp_a(h)}{|h|}\xrightarrow[h \rightarrow 0^{[k]}]{}0$$
ונקבל:
$$\frac{f(a)Dg_a(h)+Df_a(h)g(a)-Dp_a(h)}{|h|}+\frac{o(|h|)+o(|h|)}{|h|}
\xrightarrow[h \rightarrow 0^{[k]}]{}0$$

$$\frac{f(a)Dg_a(h)+Df_a(h)g(a)-Dp_a(h)}{|h|}+0
\xrightarrow[h \rightarrow 0^{[k]}]{}0$$
נראה שניתן להציב:
$$Dp_a(h)=f(a)Dg_a(h)+Df_a(h)g(a)$$
הרכבה וחיבור של פונקציות ליניאריות יוצרים פונ' ליניארית, לכן $Dp_a(h)$ היא פונ' לינארית.
לכן הנקודה גזירה וזו הנגזרת שלה. מש"ל
# שאלה 3 ![[Pasted image 20241202183929.png]]
אראה זאת באינדוקציה.
ניקח $n=1$ : 
$$f(X)=X$$
נקבל:
$$\frac{f(X+H)-f(X)-Df_X(H)}{|H|}\xrightarrow[H \rightarrow 0^{[k^2]}]{}0$$
$$\frac{X+H-X-Df_X(H)}{|H|}\xrightarrow[H \rightarrow 0^{[k^2]}]{}0$$
ולכן:
$$\frac{H-Df_X(H)}{|H|}\xrightarrow[H \rightarrow 0^{[k^2]}]{}0$$
ולכן
$$Df_X(H)=IH$$
ונקבל:
$$Df_x(I)=I=1X^0$$
לפי הנחת האינדוקציה:
$$g(x) = X^n, Df_X(I)=nX^{n-1}$$
ניקח:
$$h(X)=X^{n+1}=h_1(X)h_2(X)$$
כאשר:
$$h_1(X) = X,\ h_2(X) = X^n$$
$${Dh_1}_X(I) = I,\ {Dh_2}_X(I) = nX^{n-1}$$
לפי שאלה 2 (שניתן להתבסס עליה), נקבל:
$$Dh_X(H)=h_1(X){Dh_2}_X(H)+{Dh_1}_X(H)h_2(X)$$
נציב $H=I$:
$$Dh_X(I)=h_1(X){Dh_2}_X(I)+{Dh_1}_X(I)h_2(X)$$
$$Dh_X(I)=XnX^{n-1}+IX^n=nX^n+X^n=(n+1)X^n$$
$$Dh_X(I)=(n+1)X^n$$
ולכן האינדוקציה מתקיימת, לכל $n \in \mathbb{N}$. לכן טענת השאלה הראשונה נכונה. 
מש"ל
# שאלה 4 ![[Pasted image 20241203085445.png]]
## סעיף א
ניקח:
$$G: t \mapsto F(t)=\int^{\infty}_{0}f(x,t)dx+\int^{0}_{-\infty}f(x,t)dx$$
ניתן גם לכתוב זאת:
$$G: t \mapsto \int^{\infty}_{0}(f(x,t)+f(-x,t))dx$$
נתסכל על $\varphi$:
$$\int^{\infty}_{-\infty}\varphi(x)dx=\int^{\infty}_{0}(\varphi(x)+\varphi(-x))dx=$$
נבדוק:
$$f(x,t)+f(-x,t) < \varphi(x) + \varphi(-x)$$
ידוע כי $\varphi$ פונקציה עם ערכים חיוביים בלבד. לכן נקבל:
$$f(x,t)+f(-x,t) \le |f(x,t)+f(-x,t)| < |f(x,t)| + |f(-x,t)| < \varphi(x) + \varphi(-x)$$ פסוק אמת לפי הנתון.
לכן, מתקיים
$$|f(x,t)+f(-x,t)| < \varphi(x) + \varphi(-x)$$
לכן, לפי טענה 4.ה.3 נקבל כי $G$ פונ' מוגדרת ורציפה בקטע $[c,d]$.
הפונ' $G$ שווה לפונ' $F$. לכן $F$ רציפה ומוגדרת בקטע $[c,d]$.
מש"ל א
## סעיף ב
תהי 
$$f: \mathbb{R} \times \mathbb{R}^k \rightarrow \mathbb{R}$$
פונ' רציפה בכל המרחב ה $k+1$-ממדי. נגדיר:
$$F:\mathbb{R}^k \rightarrow \mathbb{R}$$
כאשר:
$$F:y \mapsto \int^{\infty}_{-\infty}f(x,y)dx$$
לפי הפונ' $\varphi$ ומהקורס חשבון אינפיניטסימלי 2, נקבל כי $F$ מוגדרת בכל $\mathbb{R}^k$
יהי $\varepsilon > 0$,$d \in \mathbb{R}^k$. כאשר $|d|=1$ ($d$ מסמן כיוון כלשהוא מ$0$)
ניקח
$$F|_{y_0,d}: [0,1] \rightarrow \mathbb{R}$$
כאשר
$$F|_{y_0,y}: t \mapsto F(y_0+td)=F(y_0+td)$$
מסעיף א, ניתן להסיק כי הפונ' הזו רציפה ב$0$ מימין. 
לכן, ל$\varepsilon$ קיים $\delta_0>0$ כאשר לכל $|x| < \delta_0$ מתקיים $|F|_{y_0,y}(y_0+xd)-F|_{y_0,y}(y_0)| < \varepsilon$
ניקח את ה$\delta_0$ המינימלי מכל $d$. נקרא לו $\delta_{min}$
לכן, לכל $\varepsilon >0$ קיים $\delta = \delta_{min}$
כאשר לכל $|x-y_0| < \delta$ מתקיים
$$|F|_{y_0,y}(x)-F|_{y_0,y}(y)| < \varepsilon$$
לכן הפונ' רציפה בנקודה זו.
לכן הפונ' רציפה בכל $\mathbb{R}^{k}$.
מש"ל ב.

![[Pasted image 20241203155123.png]]
ניקח את הפונ' מרחק בין הקבוצות
$$f(x,y)=|a+xu-b-yv|$$
נקבל:
$$f(x,y)=|a-b+xu-yv|$$
# שאלה 7 ![[Pasted image 20241203122356.png]]
תהי:
$$f:(x,y) \mapsto x^4+y^4 + (x - y)^3$$
הפונ' רציפה וגזירה (מורכבת מפונ' גזירות ורציפות) ב $\mathbb{R}^2$.
נמצא מתי מתקיים $\triangledown f(x,y)=0^{[2]}$:
לפי משפט 3.ג.6:
$$\triangledown f(x,y) =
\begin{pmatrix}
\frac{\partial f}{\partial x} & \frac{\partial f}{\partial y}
\end{pmatrix}$$
$$\triangledown f(x,y) =
\begin{pmatrix}
4x^3+3(x-y)^2 & 4y^3-3(x-y)^2
\end{pmatrix}$$
$$\triangledown f(x,y) =
\begin{pmatrix}
4x^3+3x^2-6xy+3y^2 & 4y^3-3x^2+6xy-3y^2
\end{pmatrix}$$
נציב:
$$\triangledown f(x,y) =
\begin{pmatrix}
4x^3+3x^2-6xy+3y^2 & 4y^3-3x^2+6xy-3y^2
\end{pmatrix}=0^{[2]}$$
נקבל:
$$\begin{cases}
4x^3+3x^2-6xy+3y^2 = 0 \\
4y^3-3x^2+6xy-3y^2 = 0\\
\end{cases} $$
נחבר משוואות:
$$4x^3=-4y^3$$
ונקבל:
$$x=-y$$
נציב ב2 המשוואות:
$$\begin{cases}
-4y^3+3y^2+6y^2+3y^2 = 0 \\
4y^3-3y^2-6y^2-3y^2 = 0\\
\end{cases} $$
ונקבל:

$$\begin{cases}
-4y^3+12y^2= 0 \\
4y^3-12y^2 = 0\\
\end{cases} $$

 $$y^2(4y-12)=0$$
 לכן קיבלנו את הנקודות הקריטיות הללו:
 $$(0,0), (-3,3)$$
 נחשב את:
 $$Hf_{(x,y)}=
 \begin{pmatrix}
	\frac{\partial f}{\partial x} \frac{\partial f}{\partial x} &&
	\frac{\partial f}{\partial x} \frac{\partial f}{\partial y} \\
	\frac{\partial f}{\partial y} \frac{\partial f}{\partial x} &&
	\frac{\partial f}{\partial y} \frac{\partial f}{\partial y} \\
\end{pmatrix}$$
נקבל: $$Hf_{(x,y)}=
 \begin{pmatrix}
	12x^2+6(x-y) &&
	-6(x-y) \\
	-6(x-y) &&
	12y^2+6(x-y) \\
\end{pmatrix}$$
נציב את הנקודות:
$$Hf_{(0,0)}=
\begin{pmatrix}
0 && 0 \\
0 && 0 \\
\end{pmatrix},
Hf_{(3,-3)}=
\begin{pmatrix}
72 && 36 \\
36 && 72 \\
\end{pmatrix},
$$
לכן הנקודה $(0,0)$ היא נק' אוכף ולכן היא לא מינימום ולא מקסימום
הנקודה $(-3,3)$ היא נק' מינימום
מש"ל.
נבדוק האם הנק' $(-3,3)$ היא מינימום של הפונ':
נמצא את הגובה של הנק':
$$f(-3,3)=(-3)^4+3^4+(-3-3)^3 = -54$$
נסתכל על הטווח $[-10,10] \times [-10,10]$. לפי משפט 6.א.4:
קיימת נק' מינימום של כל הטווח הזה. $(-3,3,-54)$. נבדוק את הקצוות של הקטע
$$-10 \le y \le 10:$$
$$f(\pm 10,y) = 10^4+y^4+(\pm 10-y)^3 > 10000 - 20^3 = 2000>0$$
$$-10 \le x \le 10:$$
$$f(x,\pm 10) = x^4+10^4+(x\pm 10)^3 > 10000 - 20^3 = 2000>0$$
לכן נקודת המינימום בקטע היא $(-3,3,-54)$.
נבדוק את שאר הנקודות ב $\mathbb{R}^2$. ניקח:
$$|x|>10,\ |y|>10$$
$$f(x,y)=x^4+y^4+(y-x)^3$$
$$f(x,y)=x^4+y^4+(y-x)(y^2-2xy+x^2)$$
$$f(x,y)=x^4+y^4+y^3-2xy^2+yx^2-xy^2+2x^2y-x^3$$
$$f(x,y)=x^4+y^4+y^3-3xy^2+3x^2y-x^3$$
$$f(x,y)=x^2(x^2-x+3y) + y^2(y^2+y-3x)$$
ניקח $a=min\{x,y\}$:
$$a^2(a^2-a+3a)+a^2(a^2+a-3a)=a^4>0$$
לכן כל נקודה אחרת היא לא נמוכה יותר מהנק' מינימום $(-3,3)$. ולכן היא הנק' מינימום ב$\mathbb{R}^2$.
מש"ל