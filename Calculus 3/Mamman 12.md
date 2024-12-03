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
![[Pasted image 20241203085445.png]]