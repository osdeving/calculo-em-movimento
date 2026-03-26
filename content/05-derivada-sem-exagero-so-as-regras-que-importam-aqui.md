# 5. Derivada sem exagero: só as regras que importam aqui

Há muitas regras de derivação em cálculo.  
Mas, para MU e MUV, você precisa de um conjunto muito pequeno.

## 5.1. Regra 1 — derivada de constante

Se $c$ é constante,

$$
\frac{d}{dt}(c) = 0
$$

Exemplo físico:
- $x_0$ é posição inicial, número fixo
- então a taxa de variação de $x_0$ é zero

---

## 5.2. Regra 2 — derivada de $t$

$$
\frac{d}{dt}(t) = 1
$$

Logo, se houver uma constante multiplicando $t$:

$$
\frac{d}{dt}(kt) = k
$$

Isso é exatamente o que faz a velocidade constante aparecer no MU.

---

## 5.3. Regra 3 — derivada de $t^2$

$$
\frac{d}{dt}(t^2) = 2t
$$

Portanto,

$$
\frac{d}{dt}\left(\frac{1}{2}at^2\right) = at
$$

Esse é o pedaço-chave do MUV.

---

## 5.4. Regra 4 — derivada da soma

Se

$$
f(t) = g(t) + h(t)
$$

então

$$
f'(t) = g'(t) + h'(t)
$$

Na prática:

$$
\frac{d}{dt}\left(x_0 + v_0 t + \frac{1}{2}at^2\right)
=
\frac{d}{dt}(x_0)
+
\frac{d}{dt}(v_0 t)
+
\frac{d}{dt}\left(\frac{1}{2}at^2\right)
$$

---
