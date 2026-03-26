# 12. Integral formal mínima: só o que basta

Até aqui, já usamos bastante a leitura geométrica da integral:

- área em $v \times t$ produz deslocamento
- área em $a \times t$ produz variação de velocidade

Agora vamos escrever essa ideia na linguagem formal mínima da integral, mas sem perder o fio físico.

## 12.1. Deslocamento a partir da velocidade

A regra geral é:

$$
\Delta x = \int_0^t v(\tau)\,d\tau
$$

Esse $\tau$ é apenas a variável de integração.  
Poderia ser outra letra. O importante é que:

- estamos acumulando velocidade
- do instante inicial $0$
- até o instante final $t$

### Aplicando ao MUV

No MUV:

$$
v(\tau)=v_0+a\tau
$$

Então:

$$
\Delta x = \int_0^t (v_0 + a\tau)\,d\tau
$$

Agora usamos as regras mais simples da integral, termo a termo.

Para o primeiro termo:

$$
\int v_0\,d\tau = v_0\tau
$$

Para o segundo:

$$
\int a\tau\,d\tau = a\frac{\tau^2}{2}
$$

Logo:

$$
\Delta x = \left[v_0\tau + \frac{a\tau^2}{2}\right]_0^t
$$

Substituindo os limites:

$$
\Delta x = \left(v_0 t + \frac{at^2}{2}\right) - 0
$$

Portanto:

$$
\Delta x = v_0 t + \frac{1}{2}at^2
$$

E, somando a posição inicial:

$$
x = x_0 + v_0 t + \frac{1}{2}at^2
$$

## 12.2. Variação de velocidade a partir da aceleração

Agora fazemos o mesmo raciocínio um nível acima.

A regra geral é:

$$
\Delta v = \int_0^t a(\tau)\,d\tau
$$

No MUV, a aceleração é constante:

$$
a(\tau)=a
$$

Então:

$$
\Delta v = \int_0^t a\,d\tau
$$

Como $a$ é constante:

$$
\Delta v = a\int_0^t d\tau
$$

E como a integral de $1$ em relação a $\tau$ é $\tau$:

$$
\Delta v = a[\tau]_0^t = at
$$

Logo:

$$
v-v_0=at
$$

Portanto:

$$
v=v_0+at
$$

## 12.3. O que a linguagem formal acrescenta

Do ponto de vista prático, os capítulos 9 e 10 já entregaram as fórmulas.

Então por que escrever a versão formal?

Porque ela revela a estrutura geral por trás dos casos particulares.

Em linguagem integral:

- acumular velocidade gera deslocamento
- acumular aceleração gera variação de velocidade

Isso vale não só para MU e MUV, mas como princípio mais amplo da cinemática.

## 12.4. O equilíbrio certo para este livro

Não precisamos mergulhar em teoria avançada de integração para tirar proveito disso.

O suficiente, aqui, é entender:

1. o que está sendo acumulado
2. em que intervalo estamos acumulando
3. por que a unidade final faz sentido fisicamente

Com esse tripé, a integral deixa de parecer uma notação opaca e passa a parecer o que ela realmente é: uma forma compacta de somar efeitos contínuos.

---
