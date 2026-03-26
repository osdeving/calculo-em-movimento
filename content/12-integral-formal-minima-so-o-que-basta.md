# 12. Integral formal mínima: só o que basta

Se você quiser escrever isso com linguagem de integral, fica assim:

## 12.1. Deslocamento a partir da velocidade

$$
\Delta x = \int_0^t v(\tau)\,d\tau
$$

Esse $\tau$ é só um nome para a variável de integração.  
Poderia ser outra letra.

No MUV:

$$
v(\tau) = v_0 + a\tau
$$

Então:

$$
\Delta x = \int_0^t (v_0 + a\tau)\,d\tau
$$

Usando as regras mais simples de integral:

$$
\int v_0\,d\tau = v_0\tau
$$

$$
\int a\tau\,d\tau = a\frac{\tau^2}{2}
$$

Logo,

$$
\Delta x = \left[v_0\tau + \frac{a\tau^2}{2}\right]_0^t
$$

Substituindo os limites:

$$
\Delta x = \left(v_0 t + \frac{at^2}{2}\right) - 0
$$

Portanto:

$$
\Delta x = v_0 t + \frac{1}{2}at^2
$$

e de novo:

$$
x = x_0 + v_0 t + \frac{1}{2}at^2
$$

---

## 12.2. Variação de velocidade a partir da aceleração

Da mesma forma:

$$
\Delta v = \int_0^t a(\tau)\,d\tau
$$

No MUV, $a(\tau)=a$ constante, então:

$$
\Delta v = \int_0^t a\,d\tau = a\int_0^t d\tau = a[t]_0^t = at
$$

Logo:

$$
v - v_0 = at
$$

portanto:

$$
v = v_0 + at
$$

> Isso mostra o papel da integral com clareza:
>
> - acumular aceleração ao longo do tempo dá variação de velocidade
> - acumular velocidade ao longo do tempo dá deslocamento

---
