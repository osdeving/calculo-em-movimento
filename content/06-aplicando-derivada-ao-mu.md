# 6. Aplicando derivada ao MU

Agora vamos usar a derivada sobre a expressão do movimento uniforme.

No MU:

$$
x(t) = x_0 + vt
$$

> Aqui a lei horária do MU entra como hipótese de trabalho para enxergarmos o papel da derivada.  
> A origem geométrica dessa expressão será construída na seção 9.

<figure class="book-figure book-motion">
  <video class="book-video" controls muted loop playsinline preload="metadata" data-autoplay-when-visible>
    <source src="media/manim/mu_derivative_bridge.mp4" type="video/mp4">
    Seu navegador não conseguiu reproduzir a animação.
  </video>
  <figcaption>No MU, derivar a reta de x(t) equivale a extrair sua inclinação constante, e isso reaparece como v(t).</figcaption>
</figure>

## 6.1. O que esperamos encontrar

Antes da conta, vale perguntar o que a física já sugere.

No MU:

- a velocidade é constante
- então a derivada da posição deve devolver um valor constante

Ou seja, já esperamos que o resultado final seja:

$$
v(t) = v
$$

A conta serve para mostrar que a linguagem algébrica e a interpretação física batem.

## 6.2. Derivando passo a passo

Começamos com:

$$
\frac{dx}{dt} = \frac{d}{dt}(x_0 + vt)
$$

Pela derivada da soma:

$$
\frac{dx}{dt} = \frac{d}{dt}(x_0) + \frac{d}{dt}(vt)
$$

Agora aplicamos as regras básicas:

- a derivada de $x_0$ é zero, porque $x_0$ é constante
- a derivada de $vt$ é $v$, porque $v$ é constante multiplicando $t$

Logo:

$$
\frac{dx}{dt} = 0 + v = v
$$

Portanto:

$$
v(t) = \frac{dx}{dt} = v
$$

## 6.3. O significado físico da conta

Essa conta curta carrega uma interpretação muito importante.

Se a posição é da forma

$$
x(t)=x_0+vt
$$

então ela cresce de maneira linear no tempo.  
Em gráfico, isso significa uma reta.

E a inclinação dessa reta é justamente $v$.

Se você quiser reforçar a ligação entre função linear, reta e inclinação, volte ao [Apêndice A, seções A.3 e A.4](26-apendice-a-retas-graficos-e-funcoes.md).

## 6.4. Um exemplo numérico rápido

Suponha:

$$
x(t)=12+4t
$$

Derivando:

$$
\frac{dx}{dt}=4
$$

Isso quer dizer que o corpo mantém velocidade constante de $4\ \text{m/s}$.

Em leitura física:

- ele pode começar na posição $12$ m
- mas, a partir daí, acrescenta sempre $4$ m por segundo

O valor inicial muda a reta de lugar, mas não muda sua inclinação.

## 6.5. O que este capítulo mostrou

A derivada do MU confirma algo que o gráfico já sugeria:

> reta em $x(t)$ $\Rightarrow$ inclinação constante $\Rightarrow$ velocidade constante

No próximo capítulo, vamos repetir a mesma lógica para o MUV.  
A diferença é que, ali, a posição não será mais reta, e por isso a derivada não devolverá uma constante simples logo de saída.

---
