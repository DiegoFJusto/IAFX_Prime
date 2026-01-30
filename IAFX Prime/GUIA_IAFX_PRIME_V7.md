# 📊 IAFX Prime v7 - Guia Completo do Usuário

## 🎯 O Que é o IAFX Prime v7?

O **IAFX Prime v7** é um Expert Advisor (robô de negociação) inteligente para MetaTrader 5 que opera com estratégias deGrid (grade) combinadas com sistemas avançados de proteção de capital e gestão de risco.

---

## 🚀 Principais Funcionalidades

### ✅ Estratégias de Operação

O robô trabalha com **duas estratégias principais** que se adaptam conforme o mercado:

#### 🔷 **Grid Super (Agressivo)**
- **Quando usa**: Quando identifica uma tendência forte
- **Como funciona**:
  - Abre posições com volume multiplicado (mais agressivo)
  - Fecha a posição mais antiga quando o conjunto fica lucrativo
  - Mantém apenas as posições mais recentes
- **Vantagem**: Aproveita tendências fortes rapidamente
- **Cuidado**: Mais agressivo, requer atenção ao DD%

#### 🔶 **Grid Médio (Defensivo)**
- **Quando usa**: Quando o mercado está em reversão
- **Como funciona**:
  - Abre posições defensivas sem aumentar agressividade
  - Limite máximo de 15 ordens para proteger a conta
  - Espera o conjunto todo ficar lucrativo
- **Vantagem**: Mais seguro em mercados laterais
- **Limite**: Máximo de 15 ordens (configurável)

---

## 🛡️ Sistema de Defesa em 3 Camadas

O robô possui **3 alertas de defesa** que ativam automaticamente conforme o Drawdown (DD%) aumenta:

### 🟡 **Alerta A - Grid Adaptativo (10% DD)**
- **O que acontece**: Grid aumenta 1.5x
- **Por quê**: Espaça mais as ordens para dar mais "respiro" ao mercado
- **Exemplo**: Se grid era 150 pontos, vira 225 pontos
- **Objetivo**: Reduzir velocidade de abertura de novas posições

### 🟠 **Alerta B - Mudança de Timeframe (20% DD)**
- **O que acontece**: Todos os indicadores mudam para timeframe de segurança
- **Por quê**: Timeframe maior = sinais mais confiáveis
- **Padrão**: Muda para M15 (15 minutos)
- **Objetivo**: Buscar sinais mais robustos e evitar ruído do mercado

### 🔴 **Alerta C - Modo Emergência (30% DD)**
- **O que acontece**: Grid Super entra em modo super conservador
- **Como funciona**:
  - Reduz multiplicador de lote pela metade
  - Mantém apenas 50% do multiplicador original
- **Objetivo**: Proteção máxima do capital em situação crítica

---

## 💰 Sistema Inteligente de Fechamento

### 🎯 **Alvos Dinâmicos (Novo!)**

Em vez de valores fixos em dólar, o robô agora trabalha com **percentual do seu saldo**:

- **Alvo Principal**: 0.5% do balance (padrão)
- **Alvo Parcial**: 0.25% do balance (padrão)
- **Vantagem**: Se adapta automaticamente ao crescimento da sua conta

#### 📍 **Fechamento em 2 Níveis**

**Nível 1 - Poucas Ordens (< 3 ordens)**
- Alvo: 0.5% do balance
- Fecha: Todas as ordens de uma vez

**Nível 2 - Muitas Ordens (≥ 3 ordens)**
- Primeiro: Fecha 50% das ordens quando atingir 0.25% (Fechamento Parcial)
- Depois: Fecha o restante quando atingir 0.5% (Alvo Final)

### 🌙 **Alvos por Horário (Novo!)**

O robô reduz os alvos durante horários de **baixa liquidez**:

- **Horário reduzido**: 22h às 6h (padrão)
- **Multiplicador**: 0.5x (metade do alvo)
- **Por quê**: Menos liquidez = menos ambição = mais segurança

---

## 📅 Sistema de Meta Diária - 3 Regras Inteligentes

### 🎯 **Regra 1: Meta Diária de 1%**
**Quando**: A qualquer momento do dia
**Condição**: Se o lucro total do dia atingir 1% do balance inicial
**Ação**:
- ✅ Fecha TODAS as posições
- 🔒 Bloqueia o robô até o próximo dia
- 💡 **Objetivo**: Garantir lucro consistente e evitar devolver ganhos

**Exemplo Prático**:
- Balance inicial do dia: R$ 10.000
- Meta: R$ 100 (1%)
- Às 14h você já ganhou R$ 100 → Robô fecha tudo e para até amanhã

---

### 🕐 **Regra 2: Proteção 17h-19h Brasília**
**Quando**: Entre 17h e 19h (horário de Brasília)
**Condição**: Se o lucro realizado do dia for maior que as perdas flutuantes
**Ação**:
- ✅ Fecha TODAS as posições
- 🔒 Garante dia positivo
- 💡 **Objetivo**: Proteger lucros já realizados contra reversões

**Exemplo Prático**:
- Lucro realizado no dia: R$ 150
- Posições abertas com perda flutuante: -R$ 80
- São 18h → Como R$ 150 > R$ 80, fecha tudo garantindo +R$ 70 no dia

---

### 📆 **Regra 3: Sexta-feira com 3% Semanal**
**Quando**: Sexta-feira, a partir das 12h
**Condição**: Se o lucro da semana (realizado + flutuante) for ≥ 3%
**Ação**:
- ✅ Fecha TODAS as posições (positivas e negativas)
- 🔒 Garante 3% da semana
- 📅 Só reabre domingo à noite
- 💡 **Objetivo**: Garantir semana lucrativa e descanso de fim de semana

**Exemplo Prático**:
- Balance: R$ 10.000
- Meta semanal: R$ 300 (3%)
- Sexta-feira 14h: Lucro da semana = R$ 320
- → Robô fecha tudo, garante os 3% e descansa até domingo

---

## 🔐 Breakeven Cascata

### O que é?
Sistema que **move o Stop Loss de TODAS as posições juntas** quando o preço médio se torna lucrativo.

### Como funciona?
1. Calcula o preço médio de todas as posições abertas
2. Quando o mercado passa desse preço médio (ficando positivo)
3. Move o SL de todas as ordens para o breakeven (ponto de equilíbrio)
4. **Resultado**: Protege lucro em bloco

### Vantagens:
- ✅ Protege todo o conjunto de ordens
- ✅ Evita perder lucro já conquistado
- ✅ Funciona automaticamente

---

## ⚙️ Configurações e Inputs - Explicação Detalhada

### 📋 **Seção: Configurações Básicas**

#### `Chave de acesso - licença`
- **O que é**: Código de ativação do robô
- **Valor**: Fornecido pelo desenvolvedor
- **Importante**: Sem a chave correta, o robô não opera

#### `Modo de operação`
- **Opções**:
  - `1 - Automático`: Robô decide tudo sozinho
  - `2 - Manual-Semiautomático`: Você inicia, robô gerencia
- **Recomendado**: Automático para traders experientes

#### `Tipo de operação`
- **Opções**:
  - `0 - Compras e Vendas`: Opera nos dois sentidos
  - `1 - Somente Compras`: Apenas LONG
  - `2 - Somente Vendas`: Apenas SHORT
  - `3 - Swap +`: Opera apenas no lado com swap positivo
- **Dica**: Use "Swap +" para minimizar custos overnight

---

### 💵 **Seção: Gestão Financeira**

#### `Tamanho do lote para ordens`
- **O que é**: Volume inicial das ordens
- **Padrão**: 0.01 (micro lote)
- **Ajuste**: Conforme tamanho da sua conta
- **Fórmula sugerida**: Balance ÷ 10.000 = lote base

#### `Valor acima de 1 multiplica lot nas agressões de tendência`
- **O que é**: Multiplicador para operações de tendência forte
- **Padrão**: 1.0 (sem multiplicar)
- **Exemplo**: 1.5 = aumenta 50% o lote em tendências
- **Cuidado**: Valores altos aumentam risco

#### `Grid em pontos`
- **O que é**: Distância entre cada ordem em pontos
- **Padrão**: 150 pontos
- **Ajuste**:
  - Menor = Mais ordens (mais agressivo)
  - Maior = Menos ordens (mais conservador)

---

### 🎯 **Seção: Alvos e Fechamentos**

#### `Alvo de PL para fechar ordens (em moeda)`
- **O que é**: Antigo sistema de alvo fixo
- **Padrão**: $0.54
- **Status**: Substituído pelo sistema percentual

#### `Qtd de ordens para nivel 2`
- **O que é**: A partir de quantas ordens muda o alvo
- **Padrão**: 3 ordens
- **Explicação**:
  - Menos de 3 ordens = usa alvo maior
  - 3 ou mais ordens = usa alvo menor (mais fácil de atingir)

#### `Alvo de PL para fechar ordens nivel2 (em moeda)`
- **O que é**: Alvo quando tem muitas ordens
- **Padrão**: $0.10
- **Objetivo**: Facilitar fechamento com muitas posições

---

### 📊 **Seção: Alvos Percentuais (NOVO!)**

#### `Usar alvo em % do balance`
- **O que é**: Ativa sistema de alvo dinâmico
- **Padrão**: true (ativado)
- **Vantagem**: Se adapta ao crescimento da conta

#### `Alvo em % do balance`
- **O que é**: Percentual do saldo para fechar tudo
- **Padrão**: 0.5% (meio porcento)
- **Exemplo**: Conta de R$ 10.000 → alvo de R$ 50

#### `Ativar fechamento parcial`
- **O que é**: Fecha metade das ordens antes do alvo final
- **Padrão**: true (ativado)
- **Vantagem**: Realiza lucro gradualmente

#### `% de ordens a fechar no parcial`
- **O que é**: Quantas ordens fechar no fechamento parcial
- **Padrão**: 50% (metade)
- **Exemplo**: 10 ordens abertas → fecha 5 no parcial

#### `% do balance para fechamento parcial`
- **O que é**: Quando ativa o fechamento parcial
- **Padrão**: 0.25% (metade do alvo final)
- **Sequência**:
  1. Atinge 0.25% → Fecha 50% das ordens
  2. Atinge 0.5% → Fecha o restante

---

### 🌙 **Seção: Alvos por Horário (NOVO!)**

#### `Alvos diferentes por horário`
- **O que é**: Ativa/desativa sistema de horários
- **Padrão**: true (ativado)
- **Por quê**: Adapta-se à liquidez do mercado

#### `Hora início alvo reduzido (22 = 22h)`
- **O que é**: Quando começa período de baixa liquidez
- **Padrão**: 22h (10 da noite)
- **Ajuste**: Conforme seu fuso horário

#### `Hora fim alvo reduzido (6 = 6h)`
- **O que é**: Quando termina período de baixa liquidez
- **Padrão**: 6h (manhã)
- **Período**: Das 22h às 6h = 8 horas

#### `Multiplicador alvo no horário reduzido`
- **O que é**: Quanto reduz o alvo durante esse período
- **Padrão**: 0.5 (metade)
- **Exemplo**: Alvo normal R$ 50 → vira R$ 25 à noite

---

### 📅 **Seção: Meta Diária (NOVO!)**

#### `Ativar meta diária (fecha tudo ao atingir)`
- **O que é**: Liga/desliga sistema de meta diária
- **Padrão**: true (ativado)
- **Recomendação**: Manter ativado para proteger lucros

#### `Meta diária em % do balance inicial`
- **O que é**: Percentual do saldo para meta do dia
- **Padrão**: 1.0% (um porcento)
- **Exemplo**: Conta R$ 10.000 → meta de R$ 100/dia

#### `Hora início verificação meta (Brasília)`
- **O que é**: Quando começa verificar Regra 2
- **Padrão**: 17h (5 da tarde)
- **Importante**: Horário de Brasília

#### `Hora fim verificação meta (Brasília)`
- **O que é**: Quando termina verificação Regra 2
- **Padrão**: 19h (7 da noite)
- **Janela**: 17h às 19h = 2 horas

---

### 🛑 **Seção: Stops**

#### `Valor do stop (em moeda)`
- **O que é**: Stop loss fixo em dólar
- **Padrão**: 0.00 (desativado)
- **Exemplo**: 50 = fecha tudo ao perder $50

#### `Valor do stop (em % de Drawdown)`
- **O que é**: Stop loss baseado em DD%
- **Padrão**: 0.00 (desativado)
- **Exemplo**: 40 = fecha tudo se DD chegar a 40%

#### `Acionar stop-cross estratégia B`
- **O que é**: Stop em cruzamento de indicadores
- **Padrão**: true (ativado)
- **Uso**: Para estratégia de tendência

---

### 🛡️ **Seção: Sistema de Defesa**

#### `% do alerta A (defesa aumento de grid)`
- **O que é**: DD% para ativar Alerta A
- **Padrão**: 10.00% (dez porcento)
- **Ação**: Aumenta grid em 1.5x

#### `% do alerta B (defesa aumento de time frame)`
- **O que é**: DD% para ativar Alerta B
- **Padrão**: 20.00% (vinte porcento)
- **Ação**: Muda para timeframe de segurança

#### `% do DD para ativar modo emergência`
- **O que é**: DD% para ativar Alerta C
- **Padrão**: 30.00% (trinta porcento)
- **Ação**: Modo ultra conservador

#### `Limite máximo de ordens Grid Médio`
- **O que é**: Máximo de ordens na estratégia defensiva
- **Padrão**: 15 ordens
- **Objetivo**: Evitar overtrading

#### `Período de Segurança`
- **O que é**: Timeframe usado no Alerta B
- **Padrão**: M15 (15 minutos)
- **Opções**: M5, M15, M30, H1, H4

---

### 🌍 **Seção: Gestão de Exposição**

#### `Máximo exposição moeda por pares`
- **O que é**: Quantos pares pode ter com a mesma moeda
- **Padrão**: 1 (um par por moeda)
- **Exemplo**:
  - Se já tem EURUSD aberto
  - Não abre EURJPY (EUR repetido)
  - Objetivo: Evitar overexposição a uma moeda

---

### 📈 **Seção: Indicadores**

#### `Usar RSI na confluência`
- **O que é**: Incluir RSI nas análises
- **Padrão**: false (desativado)
- **RSI**: Força relativa

#### `Usar MACD na confluência`
- **O que é**: Incluir MACD nas análises
- **Padrão**: true (ativado)
- **MACD**: Convergência/Divergência de médias

#### `Usar ADX na confluência`
- **O que é**: Incluir ADX nas análises
- **Padrão**: true (ativado)
- **ADX**: Força da tendência

#### `Usar Bollinger na confluência`
- **O que é**: Incluir Bandas de Bollinger
- **Padrão**: true (ativado)
- **Bollinger**: Volatilidade

#### `Usar Bjacare na confluência`
- **O que é**: Incluir indicador Jacaré
- **Padrão**: true (ativado)
- **Bjacare**: Sistema de médias

#### `Usar HH na confluência`
- **O que é**: Incluir Heiken Ashi
- **Padrão**: false (desativado)
- **HH**: Candlesticks suavizados

---

### 🔒 **Seção: Breakeven**

#### `Habilitar breakevan`
- **O que é**: Ativa sistema de Breakeven Cascata
- **Padrão**: true (ativado)
- **Recomendação**: Sempre manter ativado

---

## 🎓 Dicas de Uso

### ✅ **Configuração Conservadora**
```
Lote: 0.01
Grid: 200 pontos
Alvo percentual: 0.5%
Meta diária: 1%
Alerta A: 10%
Alerta B: 20%
Alerta C: 30%
Limite Grid Médio: 10 ordens
```

### ⚡ **Configuração Moderada**
```
Lote: 0.02
Grid: 150 pontos
Alvo percentual: 0.5%
Meta diária: 1.5%
Alerta A: 12%
Alerta B: 22%
Alerta C: 32%
Limite Grid Médio: 15 ordens
```

### 🚀 **Configuração Agressiva** (Apenas para experientes)
```
Lote: 0.03
Grid: 100 pontos
Multiplicador tendência: 1.5
Alvo percentual: 0.7%
Meta diária: 2%
Alerta A: 15%
Alerta B: 25%
Alerta C: 35%
Limite Grid Médio: 20 ordens
```

---

## ⚠️ Avisos Importantes

### 🔴 **Gestão de Risco**
- **Nunca** opere com todo o capital de uma vez
- Reserve no mínimo **40% do capital** como margem de segurança
- Monitore o DD% diariamente
- Respeite os alertas de defesa

### 🟡 **Manutenção**
- Acompanhe o desempenho semanalmente
- Ajuste configurações conforme resultados
- Teste em conta demo antes de usar em conta real
- Mantenha o robô atualizado

### 🟢 **Boas Práticas**
- Comece sempre com configuração conservadora
- Aumente risco gradualmente conforme ganha experiência
- Use a meta diária para garantir lucros consistentes
- Respeite os horários de baixa liquidez

---

## 📞 Suporte

Para dúvidas, sugestões ou suporte:
- 📧 Contate o desenvolvedor: Diego Justo
- 📅 Mantenha o robô sempre atualizado
- 🔄 Versão atual: 7.0

---

## ⚖️ Isenção de Responsabilidade

**AVISO IMPORTANTE**:

Negociar com robôs envolve alto risco e pode não ser adequado para todos os investidores. Resultados anteriores não são garantia de performance futura. Você é o único responsável pelas operações realizadas.

É **fundamental** testar em conta de demonstração antes de operar com capital real.

**Trading de forex e CFDs pode resultar em perdas que excedem seu investimento inicial.**

---

*Documento criado para IAFX Prime v7 - Versão 1.0 - Janeiro 2026*
