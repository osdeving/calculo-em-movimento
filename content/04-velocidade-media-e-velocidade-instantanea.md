# 4. Velocidade média e velocidade instantânea

Aqui começa o cálculo de verdade.

Até aqui, observamos o movimento principalmente pelos gráficos e pelas fórmulas já prontas.  
Agora vamos construir a ideia central que permite passar do “movimento em um intervalo” para o “movimento em um instante”.

Essa passagem é o coração da derivada aplicada à cinemática.

Se a leitura de $x(t)$ como função ainda estiver insegura, vale consultar antes o [Apêndice A, seções A.1 e A.2](26-apendice-a-retas-graficos-e-funcoes.md).  
Se a noção de inclinação estiver nebulosa, o ponto mais útil é o [Apêndice A, seção A.4](26-apendice-a-retas-graficos-e-funcoes.md).

## 4.1. Velocidade média

Em um intervalo de tempo $\Delta t$, a velocidade média é:

$$
v_{\text{méd}} = \frac{\Delta x}{\Delta t}
$$

Aqui aparecem duas abreviações:

- $\Delta x$ = variação de posição
- $\Delta t$ = variação de tempo

A palavra “média” importa muito aqui.

Ela está dizendo que não estamos descrevendo, ainda, o comportamento em cada instante do percurso.  
Estamos descrevendo o efeito global do movimento entre um começo e um fim.

É parecido com dizer:

- “qual foi a nota média do semestre?”
- “qual foi o consumo médio do carro na viagem?”
- “qual foi a velocidade média no trecho entre duas cidades?”

Em todos esses casos, você comprime um intervalo inteiro em um único número representativo.

Se o intervalo começa no instante $t$ e termina no instante $t+\Delta t$, então:

- posição inicial = $x(t)$
- posição final = $x(t+\Delta t)$
- tempo inicial = $t$
- tempo final = $t+\Delta t$

Esse jeito de escrever é importante porque deixa claro que:

- estamos olhando para uma função posição $x(t)$
- escolhemos um instante de partida $t$
- avançamos um pequeno intervalo $\Delta t$
- perguntamos quanto a posição mudou nesse pedaço

Essa escrita parece mais abstrata do que um exemplo numérico, mas ela nos prepara para a passagem ao limite logo adiante.

Usamos agora duas ideias matemáticas bem simples:

1. variação = valor final $-$ valor inicial
2. a posição é dada por uma função do tempo, escrita como $x(t)$

Logo,

$$
\Delta x = x(t+\Delta t) - x(t)
$$

e

$$
\Delta t = (t+\Delta t) - t
$$

Substituindo essas duas escritas na fórmula compacta, obtemos:

$$
v_{\text{méd}}
=
\frac{x(t+\Delta t)-x(t)}{(t+\Delta t)-t}
=
\frac{x(t+\Delta t)-x(t)}{\Delta t}
$$

Essa forma parece mais carregada, mas não é uma nova fórmula.  
É a mesma velocidade média escrita em linguagem de função.

Na seção 4.2, vamos usar exatamente essa escrita para encolher o intervalo e chegar à velocidade instantânea.

O ganho conceitual aqui é grande:

- a forma curta $\frac{\Delta x}{\Delta t}$ é ótima para cálculo rápido
- a forma expandida $\frac{x(t+\Delta t)-x(t)}{\Delta t}$ é ótima para pensamento matemático

É essa segunda forma que permite falar em derivada.

Isso responde:

> “Em média, quanto a posição mudou por unidade de tempo nesse intervalo?”

### Exemplo físico

Imagine um carro entre dois postes de medição:

- em $t = 2\,s$, ele está em $x=30\,m$
- em $t = 5\,s$, ele está em $x=66\,m$

![Cenário: carro entre dois postes de medição ao longo do eixo S](assets/10_postes_medicao.svg)

Veja a mesma situação em movimento:

<figure class="book-figure book-motion">
  <video class="book-video" controls muted loop playsinline preload="metadata" data-autoplay-when-visible>
    <source src="media/manim/average_velocity_posts.mp4" type="video/mp4">
    Seu navegador não conseguiu reproduzir a animação.
  </video>
  <figcaption>Animação: o carro sai de x = 30 m em t = 2 s, chega a x = 66 m em t = 5 s e explicita Delta x, Delta t e v_med.</figcaption>
</figure>

Vamos ler o exemplo com calma.

Do instante $2$ s até o instante $5$ s:

- o carro andou de $30$ m para $66$ m
- portanto, a variação de posição foi $36$ m
- o intervalo de tempo teve duração de $3$ s

Então:

$$
v_{\text{méd}} = \frac{66-30}{5-2} = \frac{36}{3} = 12\ \text{m/s}
$$

Isso não significa necessariamente que ele estava a $12\ \text{m/s}$ o tempo todo.  
Significa apenas que **o efeito médio** naquele intervalo foi esse.

Essa observação é muito importante.

O carro pode ter:

- começado mais devagar
- acelerado no meio do trecho
- desacelerado perto do fim

Mesmo assim, a velocidade média do intervalo continua sendo $12\ \text{m/s}$ se o deslocamento total foi $36$ m em $3$ s.

### Um segundo exemplo curto

Suponha que uma empilhadeira saia de $x=4$ m no instante $t=1$ s e chegue a $x=16$ m no instante $t=4$ s.

Então:

$$
\Delta x = 16-4 = 12
$$

e

$$
\Delta t = 4-1 = 3
$$

Logo:

$$
v_{\text{méd}} = \frac{12}{3} = 4\ \text{m/s}
$$

Perceba que o mecanismo do raciocínio é sempre o mesmo:

1. identificar começo e fim do intervalo
2. calcular a variação de posição
3. calcular a variação de tempo
4. dividir uma pela outra

### O que a velocidade média mede, de fato

Ela mede uma **taxa global de variação**.

Isso é mais profundo do que parece, porque a derivada nascerá justamente da tentativa de transformar uma taxa global em uma taxa local.

Se quiser reforçar a ideia de taxa e inclinação antes de seguir, consulte o [Apêndice A, seção A.4](26-apendice-a-retas-graficos-e-funcoes.md).

---

## 4.2. O salto conceitual: e se eu encolher o intervalo?

Agora vem a ideia de limite.

Se eu quiser a velocidade **num instante**, eu posso pegar um intervalo muito pequeno em torno daquele instante.

Em vez de olhar o comportamento entre tempos bem separados, eu olho assim:

$$
v_{\text{méd}} = \frac{x(t+\Delta t)-x(t)}{\Delta t}
$$

e vou tornando $\Delta t$ cada vez menor:

$$
\Delta t \to 0
$$

Em linguagem menos simbólica, estamos fazendo o seguinte:

- primeiro olhamos um intervalo relativamente largo
- depois olhamos um intervalo menor
- depois um intervalo ainda menor
- e perguntamos para qual valor essa razão está tendendo

Esse “encolher o intervalo” é a ponte entre o mundo da média e o mundo do instante.

### Uma animação da secante encolhendo até virar tangente

<figure class="book-figure book-motion">
  <video class="book-video" controls muted loop playsinline preload="metadata" data-autoplay-when-visible>
    <source src="media/manim/secant_to_tangent.mp4" type="video/mp4">
    Seu navegador não conseguiu reproduzir a animação.
  </video>
  <figcaption>A reta secante usa dois pontos separados. Quando Delta t encolhe, a secante se aproxima da tangente, que representa a velocidade instantânea.</figcaption>
</figure>

### Uma leitura numérica simples

Imagine, apenas para treinar a ideia, que a posição seja dada por

$$
x(t)=t^2
$$

e queremos entender a velocidade no instante $t=2$.

Se pegarmos alguns intervalos:

- de $2$ até $3$, a média é $\frac{9-4}{3-2}=5$
- de $2$ até $2{,}5$, a média é $\frac{6{,}25-4}{2{,}5-2}=4{,}5$
- de $2$ até $2{,}1$, a média é $\frac{4{,}41-4}{2{,}1-2}=4{,}1$

Os valores vão se aproximando de $4$.

Isso sugere que a velocidade instantânea em $t=2$ é $4$.

Quando esse processo funciona, nasce a **velocidade instantânea**:

$$
v(t) = \lim_{\Delta t \to 0}\frac{x(t+\Delta t)-x(t)}{\Delta t}
$$

Essa é a definição de derivada aplicada à posição.

Ela parece densa numa primeira leitura, mas a ideia por trás dela é única:

> velocidade instantânea = limite das velocidades médias em intervalos cada vez menores

Ou seja, a derivada não cai do céu.  
Ela é uma resposta precisa para um problema físico muito natural.

> Em linguagem intuitiva:
>
> a velocidade instantânea é a velocidade média em um intervalo tão pequeno que ele “encosta” num único instante.

---

## 4.3. Visão geométrica: secante e tangente

No gráfico $x \times t$:

- a **velocidade média** é a inclinação da reta secante entre dois pontos
- a **velocidade instantânea** é a inclinação da reta tangente naquele ponto

![Secante e tangente em x(t)](assets/03_secante_tangente.svg)

### Leitura física

Isso é um dos encontros mais bonitos entre matemática e física, porque junta duas linguagens:

- linguagem física: “rapidez de mudança”
- linguagem geométrica: “inclinação da curva”

Na secante, usamos dois pontos separados:

- ela representa a velocidade média em um intervalo

Na tangente, usamos a direção da curva em um único ponto:

- ela representa a velocidade instantânea

Se você quiser revisar com calma o que é inclinação de uma reta, volte ao [Apêndice A, seção A.4](26-apendice-a-retas-graficos-e-funcoes.md).  
Isso ajuda bastante a desmistificar a tangente.

Na prática:

- inclinação grande $\Rightarrow$ velocidade grande
- inclinação nula $\Rightarrow$ velocidade zero
- inclinação negativa $\Rightarrow$ velocidade negativa

### O que este capítulo preparou

Ao terminar este capítulo, você deve sair com três ideias muito firmes:

1. velocidade média mede a variação global de posição por variação de tempo
2. velocidade instantânea nasce quando o intervalo encolhe para zero
3. geometricamente, isso corresponde à passagem da secante para a tangente

No próximo passo, vamos formalizar isso como derivada, mas sem transformar o livro num curso abstrato de análise.  
Continuaremos sempre ancorados na interpretação física.

---
