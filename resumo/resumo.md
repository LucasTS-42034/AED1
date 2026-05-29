# Resumo Detalhado dos Conceitos Python no Repositório AED1

Baseado na leitura direta dos códigos Python (ex: aula01.py, listas.py, utils.py, exerc.py, aula03.py, fat.py), aqui está um resumo focado em conceitos chave como **int, string, casting, estruturas básicas**, com exemplos extraídos dos arquivos.

## 1. Tipos Básicos: int, string, float
- **String**: Retornada por `input()`. Exemplo em `aula01.py`:
  ```python
  idade = input(\"Digite sua idade \\n\")  # string como '25'
  print(type(idade))  # <class 'str'>
  ```
- **int**: Números inteiros. Usado em cálculos.
- **float**: Comentado em `aula01.py`: `num = 1.5` (`type(num)` = float).
- **Tupla**: `teste = 1,5` (tuple em `aula01.py`).

## 2. Casting (Conversão de Tipos)
- Comum para `input()` (string → int/float). Exemplo `aula01.py`:
  ```python
  idade = input(\"Digite sua idade \\n\")  # string
  idade = int(idade)  # casting para int
  print(idade + \"2\")  # Erro! Mistura int + str (precisa str(idade) ou +2)
  print(type(idade))  # <class 'int'>
  ```
- Em `aula03.py`: `int(input(...))` direto.
- `fat.py`: `int(4)` hardcoded.

## 3. Operações em Strings e Números
- Concatenação: `print(idade + \"2\")` (falha sem casting).
- Aritmética: `media = int((nota1 + nota2 + nota3) / 3)` (`aula03.py`).
- `%` (modulo): `dados[j] % 2 == 0` para pares (`exerc.py`).

## 4. Estruturas de Dados: Listas, Tuplas, Sets, Dicts
- **Listas**: Manipulação comum.
  ```python
  # listas.py
  list2 = [1,2,3,4,5,6,7,8,9]
  print(sum(list2), min(list2), max(list2), all(list2), sorted(list2))
  feira = [\"Laranjas\", \"Macas\", \"Uvas\"]
  feira.append(\"cebola\"); print(feira)
  feira.pop(); print(feira)
  ```
  - `exerc.py`: Loops while para filtrar `>10`, contar pares, max, contadores → dict.
    ```python
    lis = [3,7,10,15,22,30]
    i=0; while i != len(lis): if lis[i]>10: print(lis[i]); i+=1
    thisdict = {1:cont1, 2:cont2, ...}; print(thisdict)
    ```
- **Tupla**: `tuple = (1,2,3)` (`listas.py`).
- **Set**: `set1 = {\"Laranjas\", \"Macas\", \"Uvas\"}`; `add/remove` (`listas.py`).
- **Matriz (list of lists)**: Comentado em `utils.py` com loops for aninhados para contar elementos.

## 5. Condicionais (if/else)
- `aula03.py`:
  ```python
  if media > 70: print(\"Aprovado!\")
  if 70 > media > 40: print(\"Exame\")
  if 40 > media: print(\"Reprovado\")
  ```
- `exerc.py`: `if lis[i] > 10`.

## 6. Loops: while e for
- **While**: Predominante (contadores manuais).
  - `exerc.py`: Percorrer listas, contar, encontrar max.
- **For**: `utils.py` (matriz): `for linha in range(len(matri)): for coluna in range(len(matri[linha])): ...`

## 7. Funções
- **Definição básica**: `utils.py` (comentadas: `def apresenta(nome): print(...)`).
- **Recursão**: `fat.py`:
  ```python
  def fat(n):
      if n == 0: return 1
      else: return n * fat(n-1)
  print(fat(4))  # 24
  ```
- **Global**: `utils.py`: `global value; value +=1`.
- `__name__`: `print(__name__)` em `utils.py`.

## 8. Outros Conceitos
- **Funções built-in**: `len()`, `sum/min/max/all/sorted`, `range()`, `int()`.
- **Imports**: `main.py` importa `dede`.
- **Bugs Comuns no Repositório**: Casting falho, loops `while i != len()` (off-by-one), `&` em vez de `and`, `int()` em vars vazias.

Este resumo usa **códigos reais lidos** para ilustrar conceitos como solicitado. Repositório foca em prática básica (loops + listas + condicionais)."

