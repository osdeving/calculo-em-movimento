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

## 8.4. O plano para os próximos capítulos

Não vamos começar pela forma mais abstrata da integral.

Vamos fazer o caminho mais pedagógico:

1. primeiro, interpretar geometricamente o MU
2. depois, interpretar geometricamente o MUV
3. só então escrever a linguagem formal mínima da integral

Essa ordem ajuda porque o aluno vê a ideia nascer antes de ver a notação.

## 8.5. O que você deve levar daqui

Se este capítulo precisasse caber em uma única frase, seria esta:

> integral é a forma matemática de acumular pequenos efeitos ao longo do tempo

Nos próximos capítulos, essa frase vai ganhar corpo:

- no MU, com a área de um retângulo
- no MUV, com a soma de retângulo e triângulo, ou com a área de um trapézio

É daí que brotarão as fórmulas clássicas do ensino médio de um modo muito mais transparente.

---
