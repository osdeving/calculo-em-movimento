# 14. Um comentário sobre curvas: só o necessário

Até agora, trabalhamos sobretudo com casos muito bem comportados:

- MU: velocidade constante
- MUV: velocidade linear no tempo

Mas vale registrar a regra mais geral.

## 14.1. Quando o gráfico de velocidade é uma curva qualquer

Se $v(t)$ não for uma reta, mas uma curva qualquer, a regra geral continua válida:

$$
\Delta x = \int_{t_1}^{t_2} v(t)\,dt
$$

Geometricamente:

- área sob a curva de $v \times t$ = deslocamento

![Movimento geral: área sob curva de v(t)](assets/07_vt_curva_geral.svg)

Ou seja, a interpretação de área não depende de a curva ser reta.  
Ela continua funcionando quando o movimento fica mais complicado.

## 14.2. Um painel mais completo da curva

Quando o gráfico deixa de ser uma reta simples, ainda assim podemos fazer três leituras poderosas no mesmo desenho:

- o valor do gráfico em um instante
- a inclinação local da curva naquele ponto
- a área acumulada desde o início do intervalo

Isso merece ser visto em movimento, porque a cena ajuda a fixar que:

- o ponto mostra o valor instantâneo de $v(t)$
- a tangente mostra a taxa local de mudança
- a área assinada acumula o efeito total até aquele instante

<figure class="book-figure book-motion">
  <video class="book-video" controls muted loop playsinline preload="metadata" data-autoplay-when-visible>
    <source src="media/manim/general_curve_dashboard.mp4" type="video/mp4">
    Seu navegador não conseguiu reproduzir a animação.
  </video>
  <figcaption>Mesmo em uma curva qualquer, o gráfico ainda entrega três leituras: valor local, inclinação local e área assinada acumulada.</figcaption>
</figure>

Esse tipo de painel é útil porque prepara o olhar para movimentos menos escolares, em que a curva pode subir, descer, cruzar o eixo e mudar de ritmo várias vezes.

## 14.3. Por que então focamos em MU e MUV?

Porque eles já concentram o essencial do raciocínio:

- leitura de gráfico
- interpretação de inclinação
- interpretação de área
- uso prático de derivada e integral

Além disso, MU e MUV cobrem uma enorme parte da cinemática básica que aparece em cursos iniciais.

## 14.4. O limite certo deste livro

Este material não pretende esgotar movimentos arbitrários.

O foco principal é:

- MU: $v(t)$ constante
- MUV: $v(t)$ linear

Mesmo ficando nesse recorte, você já ganha o pedaço mais útil do cálculo para a cinemática elementar e intermediária.

## 14.5. O que vale guardar

Se precisar levar só uma frase deste capítulo, leve esta:

> área sob o gráfico $v \times t$ continua significando deslocamento, mesmo quando o gráfico deixa de ser simples

Essa ideia será útil sempre que você encontrar movimentos menos “escolares” e mais reais.

---
