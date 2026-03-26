# 7. Aplicando derivada ao MUV

Agora vamos repetir a estratégia do capítulo anterior, mas no caso do MUV.

Partimos da expressão:

$$
x(t) = x_0 + v_0 t + \frac{1}{2}at^2
$$

> Aqui a lei horária do MUV também entra primeiro como hipótese de trabalho.  
> A construção geométrica dela aparece na seção 10, e a forma integral mínima aparece na seção 12.1.

<figure class="book-figure book-motion">
  <video class="book-video" controls muted loop playsinline preload="metadata" data-autoplay-when-visible>
    <source src="media/manim/muv_derivative_cascade.mp4" type="video/mp4">
    Seu navegador não conseguiu reproduzir a animação.
  </video>
  <figcaption>No MUV, a derivada desce um nível de complexidade: parábola em x(t), reta em v(t), constante em a(t).</figcaption>
</figure>

## 7.1. O que esperamos da derivada

No MUV:

- a posição não cresce de forma linear
- a velocidade muda com o tempo
- a aceleração é constante

Então a expectativa física é esta:

- derivar $x(t)$ deve produzir uma função linear $v(t)$
- derivar $v(t)$ deve produzir uma constante $a$

Ou seja, o comportamento algébrico já deveria espelhar o comportamento físico.

## 7.2. Primeira derivada: saindo de x(t) para v(t)

Derivamos termo a termo:

$$
\frac{dx}{dt}
=
\frac{d}{dt}(x_0)
+
\frac{d}{dt}(v_0 t)
+
\frac{d}{dt}\left(\frac{1}{2}at^2\right)
$$

Aplicando as regras:

- $\frac{d}{dt}(x_0)=0$
- $\frac{d}{dt}(v_0 t)=v_0$
- $\frac{d}{dt}\left(\frac{1}{2}at^2\right)=at$

Logo:

$$
v(t) = \frac{dx}{dt} = v_0 + at
$$

Chegamos, assim, à equação horária da velocidade no MUV.

## 7.3. Segunda derivada: saindo de v(t) para a(t)

Agora derivamos a velocidade:

$$
\frac{dv}{dt} = \frac{d}{dt}(v_0 + at)
$$

Como $v_0$ é constante e $a$ também:

$$
\frac{dv}{dt} = 0 + a
$$

Portanto:

$$
a(t)=a
$$

## 7.4. O pacote completo do MUV

Juntando as três camadas:

$$
x(t) = x_0 + v_0 t + \frac{1}{2}at^2
$$

$$
v(t) = v_0 + at
$$

$$
a(t) = a
$$

Esse trio é a assinatura clássica do MUV.

Observe a hierarquia:

- posição: quadrática
- velocidade: linear
- aceleração: constante

É exatamente isso que os gráficos também mostravam no capítulo 3.

## 7.5. O sentido físico dessa cascata

Esse capítulo é importante porque mostra algo muito bonito:

> ao derivar, descemos um nível de complexidade da função

No MUV:

- a posição tem termo em $t^2$
- a velocidade fica só com termo em $t$
- a aceleração vira constante

Isso não é coincidência técnica.  
É o retrato matemático da estrutura física do movimento uniformemente variado.

## 7.6. Um exemplo curto para fixar

Considere:

$$
x(t)=5+3t+t^2
$$

Derivando:

$$
v(t)=3+2t
$$

Derivando de novo:

$$
a(t)=2
$$

Leitura física:

- a posição cresce com curvatura
- a velocidade cresce linearmente
- a aceleração permanece constante

É exatamente a lógica do MUV.

---
