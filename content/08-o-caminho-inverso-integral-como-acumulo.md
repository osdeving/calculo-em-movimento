# 8. O caminho inverso: integral como acúmulo

Até aqui, a derivada apareceu como resposta para perguntas do tipo:

> “qual é a taxa de mudança agora?”

Agora vamos olhar o movimento pelo caminho inverso.

Se eu conheço a taxa instantânea e quero recuperar o efeito total ao longo de um intervalo, entro no território da **integral**.

## 8.1. A pergunta física da integral

Na cinemática, a integral responde perguntas como:

- se eu sei a velocidade em cada instante, quanto o corpo andou no intervalo?
- se eu sei a aceleração em cada instante, quanto a velocidade mudou?

Perceba a mudança de foco:

- a derivada olha para o comportamento local
- a integral reconstrói o efeito acumulado

## 8.2. A leitura geométrica mais importante

Aqui aparece uma das ideias geométricas mais poderosas do livro:

- área sob o gráfico de $v \times t$ = deslocamento
- área sob o gráfico de $a \times t$ = variação de velocidade

Essa leitura vale mesmo antes de escrever integrais formais.  
Primeiro podemos pensar em figuras simples:

- retângulos
- triângulos
- trapézios

Depois, quando a situação ficar mais geral, escrevemos isso com o símbolo de integral.

<figure class="book-figure book-motion">
  <video class="book-video" controls muted loop playsinline preload="metadata" data-autoplay-when-visible>
    <source src="media/manim/integral_accumulation_overview.mp4" type="video/mp4">
    Seu navegador não conseguiu reproduzir a animação.
  </video>
  <figcaption>A integral nasce da ideia de somar pequenas contribuições ao longo do intervalo; quando refinamos a partição, os retângulos acompanham melhor a curva.</figcaption>
</figure>

## 8.3. Por que “área” faz sentido aqui

No gráfico $v \times t$:

- o eixo vertical mede velocidade
- o eixo horizontal mede tempo

Multiplicar essas duas grandezas dá:

$$
\frac{\text{m}}{\text{s}} \cdot \text{s} = \text{m}
$$

Ou seja, a unidade da área já sugere deslocamento.

No gráfico $a \times t$:

$$
\frac{\text{m}}{\text{s}^2} \cdot \text{s} = \frac{\text{m}}{\text{s}}
$$

Agora a unidade sugere variação de velocidade.

Esse tipo de checagem dimensional é muito útil para não transformar a integral em algo puramente decorado.

## 8.4. Quando a área entra com sinal negativo

Até aqui, a palavra “área” pode dar a impressão de que tudo entra sempre somando.

Na cinemática, não é bem assim.

Se o gráfico de $v(t)$ ficar abaixo do eixo do tempo durante parte do intervalo, então a velocidade está negativa nessa faixa.  
Fisicamente, isso quer dizer que o móvel está empurrando a posição no sentido oposto ao sentido positivo escolhido para o eixo.

Nesse caso:

- a parte acima do eixo contribui positivamente para $\Delta x$
- a parte abaixo do eixo contribui negativamente para $\Delta x$

O resultado final não é “a soma dos tamanhos absolutos das áreas”.  
O resultado final é o **saldo algébrico** dessas contribuições.

<figure class="book-figure book-motion">
  <video class="book-video" controls muted loop playsinline preload="metadata" data-autoplay-when-visible>
    <source src="media/manim/signed_area_overview.mp4" type="video/mp4">
    Seu navegador não conseguiu reproduzir a animação.
  </video>
  <figcaption>Quando o gráfico cruza o eixo, a parte acima conta positiva e a parte abaixo conta negativa; a integral lê esse saldo.</figcaption>
</figure>

Isso ajuda a separar duas ideias que, no começo, costumam se confundir:

- **deslocamento**: pode ser positivo, negativo ou zero
- **distância percorrida**: é sempre não negativa

Se um corpo anda para a frente e depois volta, a distância total aumenta o tempo todo.  
Já o deslocamento líquido pode diminuir, zerar ou até trocar de sinal.

Essa distinção é decisiva para usar integrais com maturidade física.

## 8.5. O plano para os próximos capítulos

Não vamos começar pela forma mais abstrata da integral.

Vamos fazer o caminho mais pedagógico:

1. primeiro, interpretar geometricamente o MU
2. depois, interpretar geometricamente o MUV
3. só então escrever a linguagem formal mínima da integral

Essa ordem ajuda porque o aluno vê a ideia nascer antes de ver a notação.

## 8.6. O que você deve levar daqui

Se este capítulo precisasse caber em uma única frase, seria esta:

> integral é a forma matemática de acumular pequenos efeitos ao longo do tempo

Nos próximos capítulos, essa frase vai ganhar corpo:

- no MU, com a área de um retângulo
- no MUV, com a soma de retângulo e triângulo, ou com a área de um trapézio
- quando o gráfico cruzar o eixo, com contribuições positivas e negativas no mesmo intervalo

É daí que brotarão as fórmulas clássicas do ensino médio de um modo muito mais transparente.

---
