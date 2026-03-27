# 2. As três funções da cinemática

Na engenharia e na física, o movimento costuma ser descrito por três funções do tempo:

$$
x = x(t), \qquad v = v(t), \qquad a = a(t)
$$

Essas três escritas parecem simples, mas organizam praticamente todo o livro.

Se a leitura de função ainda estiver enferrujada, este é um bom momento para consultar o [Apêndice A, seções A.1 e A.2](26-apendice-a-retas-graficos-e-funcoes.md).

## 2.1. O que significa escrever x(t)

Quando escrevemos $x(t)$, estamos dizendo:

> a posição depende do tempo

Isso quer dizer que:

- para cada instante $t$, existe uma posição associada
- se o tempo muda, a posição pode mudar

Por exemplo, se um carrinho anda para a frente, então a posição que ele ocupa em $t=1$ s não precisa ser a mesma que ocupa em $t=4$ s.

Em outras palavras, o tempo é a entrada da função, e a posição é a saída.

Uma maneira de fixar essa ideia é imaginar a função como uma pequena máquina conceitual:
o valor de $t$ entra, a função $x(t)$ processa esse valor, e a posição correspondente sai na outra ponta.

Na animação abaixo, repare em três coisas ao mesmo tempo:

- o cronômetro marca o tempo que está entrando
- a máquina $x(t)$ recebe esse tempo e devolve uma posição
- o carro, no eixo $S$, aparece cada vez mais à frente conforme o tempo aumenta

<figure class="book-figure book-motion">
  <video class="book-video" controls muted loop playsinline preload="metadata" data-autoplay-when-visible>
    <source src="media/manim/position_function_machine.mp4" type="video/mp4">
    Seu navegador não conseguiu reproduzir a animação.
  </video>
  <figcaption>Animação: o tempo entra na função x(t), a posição sai como resposta, e o carro ocupa posições cada vez maiores no eixo S.</figcaption>
</figure>

## 2.2. O mesmo vale para velocidade e aceleração

Quando escrevemos $v(t)$:

> a velocidade depende do tempo

Quando escrevemos $a(t)$:

> a aceleração depende do tempo

Isso nos permite representar vários cenários:

- velocidade constante
- velocidade aumentando
- velocidade diminuindo
- aceleração nula
- aceleração constante

Ou seja, em vez de pensar o movimento como uma frase solta, começamos a pensá-lo como um sistema de relações entre grandezas.

## 2.3. A hierarquia física entre as três funções

Essas funções não vivem isoladas.

Há uma ordem natural entre elas:

- a posição diz **onde** o corpo está
- a velocidade diz **como a posição está mudando**
- a aceleração diz **como a velocidade está mudando**

Em forma de leitura:

- da posição nasce a pergunta sobre velocidade
- da velocidade nasce a pergunta sobre aceleração

Mais adiante, vamos traduzir isso por derivadas:

$$
v(t) = \frac{dx}{dt}
$$

$$
a(t) = \frac{dv}{dt}
$$

Mas, por enquanto, o importante é sentir a cadeia física antes da cadeia simbólica.

## 2.4. Uma imagem mental que ajuda muito

Imagine um carro numa estrada reta.

A posição responde:

> “em que ponto da estrada ele está?”

A velocidade responde:

> “com que rapidez esse ponto está mudando?”

A aceleração responde:

> “com que rapidez a própria velocidade está mudando?”

Se o carro mantém a mesma velocidade, a aceleração é zero.  
Se o carro pisa no acelerador, a velocidade passa a variar e a aceleração deixa de ser zero.

## 2.5. O que este capítulo prepara

Nos próximos passos do livro, vamos olhar essas três grandezas de dois jeitos:

- por fórmulas
- por gráficos

Essa dupla de leitura é decisiva.

Uma boa prática, desde já, é nunca olhar apenas a equação.  
Tente sempre perguntar:

- que grandeza está sendo descrita?
- como ela depende do tempo?
- como isso apareceria num gráfico?

É essa atitude que transforma cálculo em ferramenta de interpretação, e não só em conta.

---
