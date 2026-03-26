# 16. Bônus útil: Torricelli via cálculo mínimo

Esta parte é opcional, mas muito valiosa.

A fórmula de Torricelli é uma das mais úteis da cinemática porque elimina o tempo da jogada.  
Isso é excelente quando o problema pede relação direta entre velocidade, aceleração e posição.

Queremos chegar em:

$$
v^2 = v_0^2 + 2a(x-x_0)
$$

## 16.1. Partindo das definições

Sabemos que:

$$
a = \frac{dv}{dt}
$$

e também:

$$
v = \frac{dx}{dt}
$$

Agora vem a ideia central: combinar essas duas relações.

## 16.2. Ligando velocidade e posição

Podemos escrever:

$$
\frac{dv}{dt} = \frac{dv}{dx}\cdot\frac{dx}{dt}
$$

Como $\dfrac{dx}{dt}=v$, fica:

$$
a = v\frac{dv}{dx}
$$

Reorganizando:

$$
v\,dv = a\,dx
$$

Esse é o ponto-chave da dedução.

Ele diz, em essência, que podemos relacionar a variação da velocidade diretamente com a variação da posição, sem carregar o tempo explicitamente.

## 16.3. Integrando os dois lados

Se a aceleração for constante, integramos:

$$
\int_{v_0}^{v} v\,dv
=
\int_{x_0}^{x} a\,dx
$$

Calculando cada lado:

$$
\left[\frac{v^2}{2}\right]_{v_0}^{v}
=
a[x]_{x_0}^{x}
$$

Logo:

$$
\frac{v^2-v_0^2}{2}=a(x-x_0)
$$

Multiplicando tudo por $2$:

$$
v^2-v_0^2=2a(x-x_0)
$$

Portanto:

<!-- formula: Fórmula de Torricelli -->
$$
v^2=v_0^2+2a(x-x_0)
$$

## 16.4. Por que essa fórmula é tão útil

Torricelli brilha quando:

- o tempo não é dado
- o tempo nem precisa aparecer
- queremos distância de frenagem ou velocidade em certa posição

Por exemplo, em problemas de frenagem, muitas vezes a pergunta real é:

> “de quantos metros preciso para parar?”

E não:

> “quanto tempo até parar?”

Nesses casos, eliminar o tempo simplifica muito o raciocínio.

## 16.5. O que vale perceber nesta dedução

O ganho maior não é só obter mais uma fórmula.

O ganho maior é perceber que Torricelli:

- não é fórmula solta
- não é exceção misteriosa
- cai de um pedaço curto de cálculo com grande significado físico

Esse tipo de leitura é exatamente o que diferencia decorar de compreender.

---
