# 10. Integral no MUV: por que $x = x_0 + v_0 t + \frac{1}{2}at^2$?

Aqui está uma das passagens mais bonitas do livro.

No MUV, a velocidade varia linearmente com o tempo:

$$
v(t)=v_0+at
$$

> Se você quiser a origem dessa reta de velocidade partindo de $a(t)=a$, ela será construída na seção 12.2.  
> Aqui vamos usá-la como entrada geométrica para montar a área sob o gráfico $v \times t$.

## 10.1. O que queremos descobrir

Queremos sair da informação sobre velocidade e chegar à posição.

Em outras palavras:

> se eu conheço a velocidade ao longo do tempo, quanto deslocamento foi acumulado?

No MUV, esse acúmulo aparece como área sob uma reta no gráfico $v \times t$.

## 10.2. O gráfico gera um trapézio

Como a velocidade começa em $v_0$ e cresce linearmente, o gráfico $v \times t$ entre $0$ e $t$ forma um trapézio.

![MUV: área como retângulo + triângulo](assets/05_muv_vt_area.svg)

Uma estratégia pedagógica excelente é decompor o trapézio em duas partes:

- um retângulo
- um triângulo

Assim, a fórmula aparece quase sem esforço.

## 10.3. Primeira parte: o retângulo

Se a velocidade permanecesse apenas em $v_0$, sem aceleração adicional, a área acumulada seria:

$$
A_1 = v_0 t
$$

Essa é a parte do deslocamento que vem do movimento “básico”, sem considerar o ganho extra de velocidade.

## 10.4. Segunda parte: o triângulo

Com aceleração constante, a velocidade cresce de $v_0$ até $v_0+at$.

Então o pedaço “a mais” na altura do gráfico é:

$$
at
$$

Esse ganho extra, ao longo do intervalo, forma um triângulo de:

- base $t$
- altura $at$

Logo:

$$
A_2 = \frac{1}{2}\cdot t \cdot at = \frac{1}{2}at^2
$$

## 10.5. Somando as duas contribuições

O deslocamento total é a soma das duas áreas:

$$
\Delta x = A_1 + A_2
$$

Ou seja:

$$
\Delta x = v_0 t + \frac{1}{2}at^2
$$

Agora basta recolocar a posição inicial:

$$
x = x_0 + \Delta x
$$

Portanto:

$$
x = x_0 + v_0 t + \frac{1}{2}at^2
$$

## 10.6. O significado dos dois termos principais

Essa dedução também é boa porque permite uma leitura física limpa:

- $v_0 t$ é a parte que o corpo andaria só por já sair com velocidade inicial
- $\frac{1}{2}at^2$ é o ganho extra causado pela aceleração ao longo do tempo

Isso ajuda muito a não ver a fórmula como um bloco único e misterioso.

## 10.7. Um exemplo numérico curto

Considere:

- $x_0=5$ m
- $v_0=3$ m/s
- $a=2$ m/s$^2$
- $t=4$ s

Então:

$$
\Delta x = 3\cdot 4 + \frac{1}{2}\cdot 2 \cdot 4^2
$$

$$
\Delta x = 12 + 16 = 28
$$

Logo:

$$
x=5+28=33
$$

Se você quiser interpretar:

- $12$ m vêm do “andar básico” com a velocidade inicial
- $16$ m vêm do efeito adicional da aceleração

## 10.8. Por que este capítulo é decisivo

Aqui a fórmula do MUV deixa de ser uma expressão pronta de ensino médio e passa a ser:

> posição inicial + área do retângulo + área do triângulo

Essa leitura é extremamente poderosa porque mostra, sem esconder nada, de onde o termo $\frac{1}{2}at^2$ realmente nasce.

---
