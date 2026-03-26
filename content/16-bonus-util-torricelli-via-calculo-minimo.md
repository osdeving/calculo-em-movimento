# 16. Bônus útil: Torricelli via cálculo mínimo

Essa parte é opcional, mas muito boa para engenharia porque elimina o tempo.

Queremos chegar em:

$$
v^2 = v_0^2 + 2a(x-x_0)
$$

Começamos de:

$$
a = \frac{dv}{dt}
$$

Mas também sabemos que:

$$
v = \frac{dx}{dt}
$$

Então podemos escrever:

$$
a = \frac{dv}{dt}
= \frac{dv}{dx}\cdot\frac{dx}{dt}
$$

Como $\dfrac{dx}{dt}=v$, fica:

$$
a = v\frac{dv}{dx}
$$

Reorganizando:

$$
v\,dv = a\,dx
$$

Se a aceleração for constante, integramos os dois lados:

$$
\int_{v_0}^{v} v\,dv
=
\int_{x_0}^{x} a\,dx
$$

Calculando:

$$
\left[\frac{v^2}{2}\right]_{v_0}^{v}
=
a[x]_{x_0}^{x}
$$

Logo:

$$
\frac{v^2 - v_0^2}{2} = a(x-x_0)
$$

Multiplicando por $2$:

$$
v^2 - v_0^2 = 2a(x-x_0)
$$

Portanto:

$$
v^2 = v_0^2 + 2a(x-x_0)
$$

> Essa derivação é muito valiosa porque mostra que Torricelli não é uma fórmula solta.
> Ela cai de um pedaço curto de cálculo com grande significado físico.

---
