# Apêndice A. Retas, gráficos e funções

Este apêndice existe para apoiar o livro sem desviar o foco principal.

O objetivo aqui não é fazer um curso completo de matemática escolar.  
É reunir, de forma organizada, aquilo que você realmente precisa saber para ler com segurança:

- expressões como $x(t)$, $v(t)$ e $a(t)$
- gráficos em eixos cartesianos
- retas e inclinação
- a ideia básica de função
- o primeiro contato com curvas parabólicas

Se, em algum momento do texto principal, aparecer uma frase como “veja o Apêndice A”, é porque algum desses pontos está sustentando o raciocínio.

## A.1. O que é uma função

Uma **função** é uma regra que associa uma entrada a uma saída.

No nosso contexto:

- entra um tempo $t$
- sai uma posição $x(t)$, ou uma velocidade $v(t)$, ou uma aceleração $a(t)$

Quando escrevemos:

$$
x(t) = 10 + 5t
$$

estamos dizendo:

- pegue o tempo $t$
- multiplique por $5$
- some $10$
- o resultado é a posição

Então:

- em $t=0$, temos $x(0)=10$
- em $t=2$, temos $x(2)=20$
- em $t=4$, temos $x(4)=30$

O símbolo entre parênteses não é decoração.  
Ele está dizendo de qual variável aquela grandeza depende.

### Como ler em voz alta

- $x(t)$: “posição em função do tempo” ou “posição no instante $t$”
- $v(t)$: “velocidade em função do tempo”
- $a(t)$: “aceleração em função do tempo”

## A.2. O que um ponto do gráfico significa

Num gráfico cartesiano, cada ponto representa um par de valores.

No gráfico $x \times t$:

- o eixo horizontal guarda o tempo
- o eixo vertical guarda a posição

Então, o ponto $(3,25)$ quer dizer:

- no instante $t=3$
- a posição vale $x=25$

Isso parece trivial, mas é uma das leituras mais importantes do livro.

Quando você olha uma curva em cinemática, não deve ver apenas um desenho.  
Deve enxergar uma coleção organizada de pares:

- tempo e posição
- tempo e velocidade
- tempo e aceleração

## A.3. O caso mais importante: a reta

Uma reta aparece quando a relação entre as variáveis é do tipo:

$$
y = ax + b
$$

Na escola, isso costuma ser chamado de **função afim**.

Nesse modelo:

- $b$ é o valor inicial, isto é, onde a reta “corta” o eixo vertical
- $a$ controla a inclinação da reta

Na linguagem da cinemática, a forma

$$
x(t) = x_0 + vt
$$

tem exatamente essa estrutura.

Basta identificar:

- a variável horizontal como $t$
- a variável vertical como $x$
- o termo inicial como $x_0$
- a inclinação como $v$

Por isso o gráfico de posição no MU é uma reta.

## A.4. Inclinação e coeficiente angular

A inclinação mede o quanto uma grandeza vertical muda quando a variável horizontal avança.

Em linguagem simples:

> inclinação = “quanto sobe ou desce” dividido por “quanto andou para o lado”

Em símbolos:

$$
\text{inclinação} = \frac{\Delta y}{\Delta x}
$$

Se estivermos no gráfico $x \times t$, isso vira:

$$
\frac{\Delta x}{\Delta t}
$$

E esse quociente tem unidade de velocidade:

$$
\frac{\text{metro}}{\text{segundo}} = \text{m/s}
$$

É aqui que matemática e física se encaixam de forma elegante.

No gráfico posição versus tempo:

- a inclinação representa velocidade

No gráfico velocidade versus tempo:

- a inclinação representa aceleração

Por isso, ao longo do livro, a palavra “inclinação” não será apenas geométrica.  
Ela terá conteúdo físico.

### Como o sinal muda a leitura

Se a reta sobe da esquerda para a direita:

- inclinação positiva
- a grandeza vertical está aumentando

Se a reta desce:

- inclinação negativa
- a grandeza vertical está diminuindo

Se a reta é horizontal:

- inclinação zero
- a grandeza vertical não muda

## A.5. Valor inicial: de onde a história começa

O termo independente, como o $b$ em $y=ax+b$, diz onde a história começa.

Na cinemática, isso aparece toda hora:

- em $x(t)=x_0+vt$, o $x_0$ é a posição inicial
- em $v(t)=v_0+at$, o $v_0$ é a velocidade inicial

Sem esse termo, você saberia o ritmo da mudança, mas não saberia o ponto de partida.

É por isso que duas retas com a mesma inclinação podem representar histórias físicas diferentes:

- uma pode começar em $x=0$
- outra pode começar em $x=20$

Elas sobem com o mesmo ritmo, mas partem de lugares distintos.

## A.6. E quando o gráfico deixa de ser reta?

Quando a variação deixa de ser linear, o gráfico também deixa de ser reta.

É o que acontece no MUV.

Se a velocidade muda com o tempo, a posição já não cresce somando sempre o mesmo tanto.  
Logo, o gráfico $x \times t$ deixa de ser linear.

No caso clássico do MUV, aparece uma função do tipo:

$$
x(t) = x_0 + v_0 t + \frac{1}{2}at^2
$$

O termo $t^2$ é o sinal matemático de que a curva não será reta.

Esse tipo de gráfico é uma **parábola**.

Você não precisa dominar teoria de parábolas para acompanhar este livro.  
Mas precisa guardar a intuição central:

- reta sugere taxa constante
- curvatura sugere taxa mudando

## A.7. O mínimo operacional que você precisa levar daqui

Se quiser resumir o apêndice em poucas ideias, guarde estas:

1. Uma função liga uma entrada a uma saída.
2. Em cinemática, o tempo costuma ser a entrada.
3. Cada ponto do gráfico representa um par de valores.
4. Reta é o retrato gráfico de uma relação linear.
5. A inclinação da reta mede uma taxa de variação.
6. No gráfico $x \times t$, essa taxa é velocidade.
7. No gráfico $v \times t$, essa taxa é aceleração.
8. Quando aparece termo em $t^2$, o gráfico tende a deixar de ser reta.

Com isso em mãos, os capítulos centrais do livro ficam muito mais transparentes.
