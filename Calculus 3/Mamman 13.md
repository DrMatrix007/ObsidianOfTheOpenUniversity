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
נבנה הומיאומורפיזם מ$S$ ל$\mathbb{R}^2 \backslash \{(0,0)\}$.
$$h:S \rightarrow \mathbb{R}^2 \backslash \{(0,0)\}$$
$$h:(x,y,z) \mapsto 
\begin{cases}
(x,y)& \text{ if }z \ge 2  \\
\left( \frac{x}{x^2+y^2}, \frac{y}{x^2+y^2} \right) & \text{ else }
\end{cases}$$
אמצא את $h^{-1}$:
$$S_2=\{(x,y,z)|x^2+y^2+(z-2)^2=1\}$$
$$S_2=\left\{ (x,y,z)|z=\pm \sqrt{1-x^2-y^2}+2,z > \frac{3}{2}  \right\}$$
$$$$
# שאלה 4 ![[Pasted image 20241209090315.png]]
נגדיר:
$$S'= \bigcup_{a \in S}\{ ta\ |\ t>0 \}$$
# שאלה 5 ![[Pasted image 20241209095803.png]]
