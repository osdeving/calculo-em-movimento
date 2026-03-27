# 13. O Teorema Fundamental do Cálculo, traduzido para a cinemática

Em um curso formal de cálculo, existe um resultado central chamado **Teorema Fundamental do Cálculo**.

Aqui não precisamos da forma mais abstrata desse teorema.  
O que precisamos é da sua tradução física.

<figure class="book-figure book-motion">
  <video class="book-video" controls muted loop playsinline preload="metadata" data-autoplay-when-visible>
    <source src="media/manim/fundamental_theorem_kinematics.mp4" type="video/mp4">
    Seu navegador não conseguiu reproduzir a animação.
  </video>
  <figcaption>Derivar e integrar aparecem como rotas complementares entre posição, velocidade e aceleração.</figcaption>
</figure>

## 13.1. A versão que importa para este livro

Na linguagem da cinemática, ele aparece quase assim:

### Se eu derivar a posição, obtenho a velocidade

$$
v(t) = \frac{dx}{dt}
$$

### Se eu acumular a velocidade no tempo, recupero deslocamento

$$
\Delta x = \int v(t)\,dt
$$

### Se eu derivar a velocidade, obtenho a aceleração

$$
a(t) = \frac{dv}{dt}
$$

### Se eu acumular a aceleração no tempo, recupero variação de velocidade

$$
\Delta v = \int a(t)\,dt
$$

## 13.2. O coração da ideia

Em linguagem muito direta:

- derivar mede a taxa
- integrar reconstrói o acúmulo

Isso significa que derivada e integral não são técnicas sem relação.  
Elas são operações complementares.

Uma olha para a mudança local.  
A outra recompõe o efeito acumulado dessa mudança.

## 13.3. Por que isso é tão bonito na cinemática

Na cinemática, o teorema fica quase “visível”:

- a derivada aparece como inclinação
- a integral aparece como área

Então, quando você passa de:

- posição para velocidade
- velocidade para aceleração

está lendo inclinações.

Quando passa de:

- velocidade para deslocamento
- aceleração para variação de velocidade

está lendo áreas.

### Uma cena em que o ciclo aparece inteiro

No fundo, o teorema fundamental diz que a leitura local e a leitura acumulada não estão soltas.

Quando olhamos a inclinação de $x(t)$, estamos descobrindo a velocidade naquele instante.  
Quando depois acumulamos $v(t)$ ao longo de um intervalo, recompomos um pedaço da própria posição.

É esse ciclo que a animação abaixo tenta tornar visual:

<figure class="book-figure book-motion">
  <video class="book-video" controls muted loop playsinline preload="metadata" data-autoplay-when-visible>
    <source src="media/manim/fundamental_cycle_dashboard.mp4" type="video/mp4">
    Seu navegador não conseguiu reproduzir a animação.
  </video>
  <figcaption>A tangente em x(t) revela v(t) localmente; a área sob v(t) recompõe Delta x no intervalo. A taxa local e o acúmulo global fecham o mesmo ciclo.</figcaption>
</figure>

## 13.4. O que isso resolve pedagogicamente

Esse capítulo serve para unificar o livro.

Até aqui, você viu:

- fórmulas
- gráficos
- derivadas
- integrais

O teorema fundamental é o ponto em que tudo isso se encaixa numa só estrutura.

Ele diz, em essência:

> aquilo que a derivada mede localmente, a integral recompõe globalmente

Na cinemática, isso é exatamente a conversa entre taxa e acúmulo.

---
