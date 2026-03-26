# 5. Derivada sem exagero: só as regras que importam aqui

Há cursos de cálculo que passam bastante tempo construindo regras de derivação para muitas famílias de funções.

Aqui não precisamos disso tudo.

Para entender MU e MUV com segurança, basta um conjunto pequeno de ideias, desde que elas sejam bem entendidas.

## 5.1. O que a derivada está fazendo, em essência

Derivar uma função significa medir sua taxa de variação instantânea.

Na cinemática:

- derivada da posição $\Rightarrow$ velocidade
- derivada da velocidade $\Rightarrow$ aceleração

Então, quando derivamos uma expressão como $x(t)$, não estamos só manipulando símbolos.  
Estamos perguntando:

> “qual é o ritmo local de mudança desta grandeza?”

## 5.2. Regra 1: derivada de constante

Se $c$ é constante,

$$
\frac{d}{dt}(c) = 0
$$

Isso faz sentido fisicamente.

Se um valor não muda com o tempo, sua taxa de mudança é zero.

Exemplo:

- $x_0$ é uma posição inicial fixa
- se é fixa, não cresce nem diminui com o tempo
- logo, sua derivada é zero

## 5.3. Regra 2: derivada de t

$$
\frac{d}{dt}(t) = 1
$$

Isso quer dizer que a função “identidade do tempo” cresce uma unidade para cada unidade de tempo.

Se houver uma constante multiplicando $t$, temos:

$$
\frac{d}{dt}(kt) = k
$$

Essa é uma regra central para o MU.

Quando você deriva um termo linear em $t$, sobra a constante que estava como coeficiente.  
Em linguagem geométrica, isso equivale a dizer que a inclinação de uma reta é constante.

Se quiser revisar a ligação entre reta e inclinação, o [Apêndice A, seções A.3 e A.4](26-apendice-a-retas-graficos-e-funcoes.md) ajuda bastante.

## 5.4. Regra 3: derivada de t^2

$$
\frac{d}{dt}(t^2) = 2t
$$

Essa regra é a peça-chave do MUV.

Ela nos mostra que:

- uma função quadrática gera, ao derivar, uma função linear

Por isso, quando a posição tem um termo em $t^2$, a velocidade costuma ganhar um termo em $t$.

Aplicando ao caso clássico:

$$
\frac{d}{dt}\left(\frac{1}{2}at^2\right) = at
$$

Esse é exatamente o pedaço que faz a velocidade no MUV depender linearmente do tempo.

## 5.5. Regra 4: derivada da soma

Se

$$
f(t) = g(t) + h(t)
$$

então

$$
f'(t) = g'(t) + h'(t)
$$

Em outras palavras, podemos derivar termo a termo.

Na prática:

$$
\frac{d}{dt}\left(x_0 + v_0 t + \frac{1}{2}at^2\right)
=
\frac{d}{dt}(x_0)
+
\frac{d}{dt}(v_0 t)
+
\frac{d}{dt}\left(\frac{1}{2}at^2\right)
$$

Isso deixa a conta organizada e evita a sensação de “mágica”.

## 5.6. O mínimo que basta para este livro

Com essas quatro regras, já conseguimos:

- derivar a equação do MU
- derivar a equação do MUV
- sair de $x(t)$ para $v(t)$
- sair de $v(t)$ para $a(t)$

Não é um curso completo de derivação, e não precisa ser.

O objetivo aqui é outro:

> usar o cálculo como linguagem para entender movimento

Nos próximos dois capítulos, vamos aplicar exatamente esse conjunto mínimo às fórmulas clássicas do MU e do MUV.

---
