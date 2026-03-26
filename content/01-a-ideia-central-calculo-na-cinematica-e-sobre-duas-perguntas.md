# 1. A ideia central: cálculo, na cinemática, é sobre duas perguntas

Muita gente entra em cálculo achando que vai encontrar um conjunto de regras formais, símbolos estranhos e manipulações meio desligadas do mundo físico.

Na cinemática, vale a pena começar de outro jeito.

Aqui, o cálculo nasce de duas perguntas muito concretas.  
Se você entender profundamente essas duas perguntas, quase todo o restante do livro passa a fazer sentido como resposta organizada.

## 1.1. Pergunta A: quão rápido algo está mudando agora?

Essa é a pergunta da **taxa de variação instantânea**.

Ela aparece de vários modos:

- quão rápido a posição do carro está mudando?
- quão rápido a velocidade está mudando?
- quão rápido a temperatura, a corrente ou a pressão estão mudando?

Na cinemática, as respostas mais importantes são:

- a taxa de mudança da posição é a velocidade
- a taxa de mudança da velocidade é a aceleração

É aqui que entra a **derivada**.

Em linguagem intuitiva:

> derivar é medir o ritmo local da mudança

Essa palavra “local” importa.  
Não estamos falando do comportamento médio em um intervalo inteiro.  
Estamos falando do comportamento em torno de um instante.

## 1.2. Pergunta B: quanto foi acumulado ao longo do tempo?

Agora pense no problema inverso.

Se eu conheço o comportamento instantâneo e quero recuperar o efeito total, o que faço?

Exemplos:

- se sei a velocidade ao longo do tempo, quanto o corpo andou?
- se sei a aceleração ao longo do tempo, quanto a velocidade mudou?

Aqui entra a **integral**.

Em linguagem intuitiva:

> integrar é somar, de forma organizada, pequenos efeitos acumulados

Na cinemática, a leitura geométrica disso é fortíssima:

- área sob o gráfico $v \times t$ representa deslocamento
- área sob o gráfico $a \times t$ representa variação de velocidade

Mas aqui já vale antecipar um detalhe importante, para não nascer uma intuição incompleta.

Quando o gráfico fica **acima** do eixo do tempo, a contribuição entra positiva.  
Quando o gráfico fica **abaixo** do eixo do tempo, a contribuição entra negativa.

Em linguagem física, isso significa o seguinte:

- velocidade positiva tende a empurrar a posição no sentido positivo do eixo
- velocidade negativa tende a empurrar a posição no sentido oposto

Então a integral, na cinemática, não mede apenas “quanto desenho apareceu sob a curva”.  
Ela mede um **acúmulo com sinal**.

Esse ponto vai aparecer com mais calma no [capítulo 8, seção 8.4](08-o-caminho-inverso-integral-como-acumulo.md) e volta de modo formal no [capítulo 12, seção 12.3](12-integral-formal-minima-so-o-que-basta.md).

## 1.3. O livro inteiro gira em torno desse par

Se quisermos dizer tudo em uma forma bem compacta:

- **derivada** = taxa de variação
- **integral** = acúmulo

Mas essa frase curta só fica viva quando ligada a perguntas físicas.

Por isso, ao longo do livro, vamos insistir sempre nesta tradução:

- inclinação de curva $\leftrightarrow$ taxa
- área sob gráfico $\leftrightarrow$ acúmulo

## 1.4. Como isso aparece na cinemática

Quando você vê uma posição $x(t)$:

- pode perguntar como ela está mudando agora
- resposta: derivada $\Rightarrow$ velocidade

Quando você vê uma velocidade $v(t)$:

- pode perguntar quanto ela acumulou em um intervalo
- resposta: integral $\Rightarrow$ deslocamento

O mesmo vale um nível acima:

- derivada da velocidade $\Rightarrow$ aceleração
- integral da aceleração $\Rightarrow$ variação de velocidade

Esse encadeamento é o coração matemático da cinemática.

## 1.5. O que você deve guardar deste primeiro capítulo

Antes de avançar, vale sair com um mapa mental claro:

1. O cálculo, aqui, não começa em abstração; começa em perguntas físicas.
2. A derivada responde “quão rápido está mudando agora?”.
3. A integral responde “quanto foi acumulado ao longo do intervalo?”.
4. Na cinemática, essas ideias aparecem o tempo todo em posição, velocidade e aceleração.

Nos próximos capítulos, vamos preparar a linguagem necessária para essa conversa: primeiro as funções do tempo, depois os gráficos, depois a velocidade média e instantânea, e só então a derivada e a integral de forma mais explícita.

---
