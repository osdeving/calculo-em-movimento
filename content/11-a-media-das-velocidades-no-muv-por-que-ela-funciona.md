# 11. A média das velocidades no MUV: por que ela funciona?

Uma dúvida muito comum é esta:

> “Por que, no MUV, podemos usar $\dfrac{v_0+v}{2}$?”

A resposta curta é:

> porque o gráfico $v \times t$ é uma reta

Mas vale desenvolver isso com mais calma.

<figure class="book-figure book-motion">
  <video class="book-video" controls muted loop playsinline preload="metadata" data-autoplay-when-visible>
    <source src="media/manim/muv_average_velocity.mp4" type="video/mp4">
    Seu navegador não conseguiu reproduzir a animação.
  </video>
  <figcaption>No MUV, o trapézio sob o gráfico pode ser reescrito como um retângulo de mesma base e altura média.</figcaption>
</figure>

## 11.1. O que significa tirar a média aqui

No MUV, a velocidade não fica fixa.  
Ela começa em $v_0$ e termina em $v$.

Se a variação entre esses extremos é linear, então o valor médio ao longo do intervalo coincide com a média aritmética dos extremos:

$$
v_{\text{méd}} = \frac{v_0 + v}{2}
$$

Isso não vale por mágica.  
Vale porque o crescimento de $v(t)$ é uniforme no tempo.

## 11.2. O argumento geométrico

No gráfico $v \times t$, o deslocamento é a área sob a reta.

Essa área pode ser lida de duas formas:

- como área de um trapézio
- como área de um retângulo de altura igual à velocidade média

Se as duas áreas representam o mesmo deslocamento, então:

$$
\Delta x = v_{\text{méd}}\,t
$$

E, para uma reta, essa altura média é:

$$
v_{\text{méd}} = \frac{v_0 + v}{2}
$$

Logo:

$$
\Delta x = \frac{v_0 + v}{2}\,t
$$

## 11.3. Recuperando a fórmula do MUV

Se substituirmos

$$
v = v_0 + at
$$

na média:

$$
\Delta x = \frac{v_0 + (v_0 + at)}{2}\,t
$$

$$
\Delta x = \frac{2v_0 + at}{2}\,t
$$

$$
\Delta x = \left(v_0 + \frac{at}{2}\right)t
$$

$$
\Delta x = v_0 t + \frac{1}{2}at^2
$$

E recuperamos exatamente a expressão já obtida pela decomposição em retângulo e triângulo.

## 11.4. O ponto conceitual que vale ouro

O importante não é decorar só a continha da média.  
O importante é saber **quando** essa média simples faz sentido.

No MUV:

- faz sentido, porque $v(t)$ é linear

Em um movimento qualquer, com gráfico curvo de velocidade:

- essa média simples dos extremos não é garantidamente a velocidade média real

Isso evita um erro muito comum em exercícios.

## 11.5. Uma forma intuitiva de pensar

Se a velocidade aumenta “de modo regular”, então:

- a metade do caminho entre o valor inicial e o final representa bem o comportamento médio do intervalo

É por isso que, em MUV, essa conta funciona tão bem.

Não porque “o professor mandou”, mas porque a geometria do gráfico sustenta a fórmula.

---
