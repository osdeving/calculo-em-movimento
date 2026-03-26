# 10. Integral no MUV: por que $x = x_0 + v_0 t + \frac{1}{2}at^2$?

Aqui está uma das partes mais importantes do curso.

No MUV,

$$
v(t) = v_0 + at
$$

> Se você quiser a origem dessa reta de velocidade partindo de $a(t)=a$, ela será construída na seção 12.2.
> Aqui vamos usá-la como entrada geométrica para montar a área sob o gráfico $v \times t$.

No gráfico $v \times t$, isso é uma reta.  
A área sob essa reta, de $0$ até $t$, é um trapézio.

![MUV: área como retângulo + triângulo](assets/05_muv_vt_area.svg)

Podemos dividir essa área em duas partes:

## Parte 1 — retângulo
Altura $v_0$, base $t$:

$$
A_1 = v_0 t
$$

## Parte 2 — triângulo
A velocidade cresce de $v_0$ até $v_0+at$, então o “extra” é $at$.

Base $t$, altura $at$:

$$
A_2 = \frac{1}{2}\cdot t \cdot at = \frac{1}{2}at^2
$$

Somando:

$$
\Delta x = A_1 + A_2 = v_0 t + \frac{1}{2}at^2
$$

Logo,

$$
x = x_0 + \Delta x
$$

e portanto:

$$
x = x_0 + v_0 t + \frac{1}{2}at^2
$$

> Essa talvez seja a interpretação geométrica mais bonita do MUV:
>
> o termo $v_0 t$ é a parte “que já vinha andando”  
> e o termo $\frac{1}{2}at^2$ é o ganho extra vindo da aceleração.

---
