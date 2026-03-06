# 📊 IAFX Prime v8 - Guia Completo do Usuário

## 🎯 O Que é o IAFX Prime v8?

O **IAFX Prime v8** é a versão 2.0 do Expert Advisor inteligente para MetaTrader 5. Mantém toda a robustez da v7 e **adiciona uma nova estratégia de negociação: FIMATHE** (estratégia de canais e rompimentos).

Agora você tem **2 estratégias independentes** para gerar o primeiro sinal:
- ✅ **IAFX** (Confluência de Indicadores)
- ✅ **FIMATHE** (Canais e Rompimentos)

**Ambas podem ser habilitadas/desabilitadas** via inputs, oferecendo flexibilidade total!

---

## 🚀 O Que Mudou da v7 para v8?

| Característica | v7 | v8 |
|---|:---:|:---:|
| Grid (Médio + Super) | ✅ | ✅ |
| Indicadores (RSI, MACD, Bollinger, etc) | ✅ | ✅ |
| Breakeven Cascading | ✅ | ✅ |
| Trailing Stop Individual | ✅ | ✅ |
| Sistema de 3 Alertas (A/B/C) | ✅ | ✅ |
| Meta Diária (3 regras) | ✅ | ✅ |
| Filtro Macro (VIX, Carry) | ✅ | ✅ |
| **Estratégia FIMATHE** | ❌ | ✅ |
| **Dual Strategy (IAFX + FIMATHE)** | ❌ | ✅ |

---

## 🎯 Principais Funcionalidades

### ✅ Duas Estratégias de Entrada (Primeira Ordem)

#### 🔷 **Estratégia IAFX (Confluência de Indicadores)**
- **Como funciona**: Combina múltiplos indicadores técnicos
- **Indicadores suportados**:
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence)
  - Bollinger Bands
  - Bjacare (Moving Average)
  - ADX (Average Directional Index)
  - Heiken Ashi
  - Estocástico
  - Volume
- **Entrada**: Requer mínimo de sinais confluindo (default: 4)
- **Sinal ADX**: Requer ADX_F = "ON" (ADX acima do threshold)
- **Entrada**: Sinais de compra/venda simultâneos bloqueados (evita confusão)

#### 🟦 **Estratégia FIMATHE (Canais e Rompimentos)** ← NOVO!
- **O que é**: Sistema de identificação de canais de consolidação
- **Como funciona**:
  1. Mede o **topo** (highest high) dos últimas N barras
  2. Mede o **fundo** (lowest low) dos últimas N barras
  3. Calcula **zona neutra** = 50% do canal (ponto de equilíbrio)
  4. Calcula **zona de rompimento** = % configurável do canal
  5. Gera sinal:
     - **"C" (Compra)**: quando preço rompe ABAIXO da zona de rompimento
     - **"V" (Venda)**: quando preço rompe ACIMA da zona de rompimento
     - **"X" (Neutro)**: fora das zonas de rompimento
- **Parâmetros**:
  - `fimathe_barras`: Número de barras para calcular o canal (default: 50)
  - `fimathe_percentual_ruptura`: % da zona de rompimento (default: 0.5 = 50%)

### ⚙️ **Lógica de Entrada Dual (Race Condition)**

Quando **ambas as estratégias** estão habilitadas, o primeiro sinal a aparecer abre a ordem:

```
if (usar_IAFX && usar_FIMATHE)
   // Avalia IAFX primeiro
   if (sinal_IAFX == "C" ou "V")
      → Abre ordem com IAFX
   
   // Se IAFX não sinalizou, avalia FIMATHE
   else if (sinal_FIMATHE == "C" ou "V")
      → Abre ordem com FIMATHE

   // Se ambas na mesma candle:
   // IAFX tem prioridade (avaliada primeiro)
```

**Configurações possíveis:**

| Config | Comportamento |
|--------|--------------|
| `usar_IAFX=true, usar_FIMATHE=false` | Apenas IAFX (como v7) |
| `usar_IAFX=false, usar_FIMATHE=true` | Apenas FIMATHE (novo sistema) |
| `usar_IAFX=true, usar_FIMATHE=true` | Dual: IAFX → FIMATHE |

### Grid Super (Agressivo) - Dinâmica VKGLinear
- **Quando usa**: Quando já existe mais de 1 ordem aberta e o preço se afasta `grid_super_pontos` pontos
- **Como funciona**:
  - Ativação puramente por distância em pontos (não depende de indicadores)
  - Abre posições com volume multiplicado (mais agressivo)
  - Fecha a posição mais antiga quando o conjunto fica lucrativo (dinâmica VKGLinear)
  - Mantém apenas as posições mais recentes
- **Parâmetro**: `grid_super_pontos` (padrão: 75 pontos)

### Grid Médio (Defensivo)
- **Quando usa**: Quando o mercado está em reversão
- **Como funciona**:
  - Abre posições defensivas sem aumentar agressividade
  - Limite máximo de 15 ordens para proteger a conta
  - Espera o conjunto todo ficar lucrativo
- **Vantagem**: Mais seguro em mercados laterais
- **Limite**: Máximo de 15 ordens (configurável)

---

## 🛡️ Sistema de Defesa em 3 Camadas

**IDÊNTICO ao v7** - Todos os mecanismos de proteção funcionam igual:

### 🟡 **Alerta A - Grid Adaptativo**
- **Ativado por**: DD% >= `alertaDDA` (padrão 10%) **OU** VIX >= `vix_alerta_a` (padrão 21.0)
- **O que acontece**: Grid aumenta 1.5x
- **Exemplo**: Se grid era 150 pontos, vira 225 pontos

### 🟠 **Alerta B - Mudança de Timeframe**
- **Ativado por**: DD% >= `alertaDDB` (padrão 20%) **OU** VIX >= `vix_alerta_b` (padrão 24.0)
- **O que acontece**: Todos os indicadores mudam para timeframe de segurança (M15)

### 🔴 **Alerta C - Modo Emergência (30% DD)**
- **O que acontece**: Reduz multiplicador de lote pela metade
- **Objetivo**: Proteção máxima do capital em situação crítica

---

## 💰 Sistema Inteligente de Fechamento

**IDÊNTICO ao v7**:

### 🎯 **Alvos Dinâmicos**
- **Alvo Principal**: 0.5% do balance (padrão)
- **Alvo Parcial**: 0.25% do balance (padrão)
- **Fecha automaticamente**: Quando lucro atingir os alvos

### 🌙 **Alvos por Horário**
- **Horário reduzido**: 22h às 6h (padrão)
- **Multiplicador**: 0.5x (metade do alvo)

---

## 📅 Sistema de Meta Diária - 3 Regras Inteligentes

**IDÊNTICO ao v7** - Todas as 3 regras funcionam normalmente:

### 🎯 **Regra 1: Meta Diária de 1%**
- Se lucro >= 1% do balance → fecha tudo

### 🕖 **Regra 2: Proteção 17h-19h (Brasília)**
- Se lucro realizado > loss flutuante → fecha tudo

### 📅 **Regra 3: Friday 3% Semanal**
- Sexta-feira após 12h, se lucro semanal >= 3% → fecha tudo

---

## ⚙️ Inputs Novos da v8

### Seção: ESTRATEGIAS (v8)

```
◈ usar_IAFX [true/false]
   → Ativar estratégia IAFX (confluência de indicadores)
   Padrão: true
   
◈ usar_FIMATHE [true/false]
   → Ativar estratégia FIMATHE (canais e rompimentos)
   Padrão: false
   Dica: Comece com false e ative depois de testar
   
◈ fimathe_barras [1-500]
   → Número de barras para calcular o canal
   Padrão: 50
   Recomendado: 50-100 para timeframes M5/M15
   
◈ fimathe_percentual_ruptura [0.1-1.0]
   → Percentual da zona de rompimento (0.5 = 50%)
   Padrão: 0.5
   Menor valor = zona mais restritiva = menos sinais
   Maior valor = zona mais aberta = mais sinais
```

---

## 📊 Como Usar a Estratégia FIMATHE

### Exemplo 1: Apenas FIMATHE
```
usar_IAFX = false
usar_FIMATHE = true
fimathe_barras = 50
fimathe_percentual_ruptura = 0.5
```
✅ O robô só abre primeira ordem via FIMATHE
✅ Depois segue com grid, trailing, breakeven (idêntico v7)

### Exemplo 2: Dual (IAFX + FIMATHE)
```
usar_IAFX = true
usar_FIMATHE = true
fimathe_barras = 50
fimathe_percentual_ruptura = 0.5
```
✅ Avalia IAFX primeiro (se sinalar → abre)
✅ Se IAFX não sinalar → avalia FIMATHE
✅ Primeira a sinalar gera a ordem
✅ IAFX tem prioridade (é avaliada primeiro)

### Exemplo 3: Conservador (Apenas IAFX, como v7)
```
usar_IAFX = true
usar_FIMATHE = false
```
✅ Funciona exatamente como v7
✅ Estratégia FIMATHE totalmente desativada

---

## 🎓 Dicas de Configuração FIMATHE

### 🔍 **Entendendo a Zona de Rompimento**

Canal identificado nas últimas 50 barras:
```
Topo (máxima): 1,2500
Fundo (mínima): 1,2400
Tamanho: 100 pontos

Zona neutra (50%): 1,2450
Zona rompimento (50% do tamanho): 50 pontos
  - Compra: < 1,2450
  - Venda: > 1,2450
```

### ⚡ **Ajustando Sensibilidade**

| Parâmetro | Conservador | Moderado | Agressivo |
|-----------|------------|----------|-----------|
| fimathe_barras | 100 | 50 | 30 |
| fimathe_percentual_ruptura | 0.7 | 0.5 | 0.3 |
| Resultado | Menos sinais | Equilibrado | Mais sinais |

### 🔄 **Combinando com IAFX**

Quando ambas ativas:
- **IAFX** = Estratégia baseada em indicadores (mais confirmação)
- **FIMATHE** = Estratégia baseada em preço (mais rápida)

Juntas formam um sistema robusto com entrada rápida (FIMATHE) ou confirmada (IAFX).

---

## ✅ Configuração Recomendada para v8

### 📌 **Teste Inicial (Demo)**
```
usar_IAFX = true
usar_FIMATHE = true
fimathe_barras = 50
fimathe_percentual_ruptura = 0.5
Grid Médio: 150 pontos
Grid Super: 75 pontos
Lote base: 0.01
Meta diária: 1%
```

### 🚀 **Producao (Após 1 mês de sucesso)**
```
usar_IAFX = true
usar_FIMATHE = true
fimathe_barras = 50
fimathe_percentual_ruptura = 0.5
Grid Médio: 150 pontos
Grid Super: 75 pontos
Lote base: 0.01-0.05 (conforme saldo)
Meta diária: 1-1.5%
```

---

## 📝 Novidades Técnicas da v8

✅ Struct `FimathData` para armazenar cálculos FIMATHE
✅ Função `CalcularFimathe()` que identifica canais em tempo real
✅ Lógica de race condition (primeira estratégia a sinalizar abre)
✅ Logs diferenciados: `[COMPRA-IAFX]` vs `[COMPRA-FIMATHE]`
✅ Filtros respeitados: tipo_op, horários, grid, macro, exposição

---

## ⚠️ Avisos Importantes

### 🔴 **Gestão de Risco**
- **Nunca** opere com todo o capital de uma vez
- Reserve no mínimo **40% do capital** como margem de segurança
- Monitore o DD% diariamente
- Respeite os alertas de defesa
- Teste FIMATHE em demo **antes** de usar em conta real

### 🟡 **FIMATHE Específico**
- Comece com `usar_FIMATHE=false` e `usar_IAFX=true`
- Depois ative FIMATHE gradualmente
- Monitore a frequência de sinais (não deve ser muito alta)
- Ajuste `fimathe_percentual_ruptura` conforme teste

### 🟢 **Boas Práticas**
- Comece sempre com dual desativado (apenas IAFX)
- Ative FIMATHE após entender seu comportamento
- Use a meta diária para garantir lucros consistentes
- Respeite os horários de baixa liquidez
- Mantenha backups da v7

---

## 📂 Arquivos da v8

```
IAFX Prime v8.mq5          ← Código fonte (editar no MetaEditor)
IAFX Prime v8.ex5          ← Arquivo compilado (usar no MT5)
IAFX Prime v7.ex5          ← Versão anterior (manter como backup)
GUIA_IAFX_PRIME_V8.md      ← Este guia
```

---

## 🔄 Migração da v7 para v8

✅ **v7 permanece intacta** - Você pode continuar usando se preferir
✅ **Configurações v7 compatíveis** - v8 aceita todas as mesmas configs
✅ **Ativar gradualmente** - Comece com FIMATHE desativado

### Passos:
1. Baixe `IAFX Prime v8.ex5`
2. Copie para pasta de Experts do MT5
3. Em novo gráfico, adicione v8
4. Configure `usar_IAFX=true, usar_FIMATHE=false` (como v7)
5. Teste em demo 1-2 semanas
6. Depois ative FIMATHE se desejar

---

## 📞 Suporte

Para dúvidas sobre:
- **IAFX (v7)**: Consulte `GUIA_IAFX_PRIME_V7.md`
- **FIMATHE (v8)**: Veja seção "Estratégia FIMATHE" neste guia
- **Geral**: Contate o desenvolvedor

---

## ⚖️ Isenção de Responsabilidade

**AVISO IMPORTANTE**:

Negociar com robôs envolve alto risco e pode não ser adequado para todos os investidores. Resultados anteriores não são garantia de performance futura. Você é o único responsável pelas operações realizadas.

É **fundamental** testar em conta de demonstração antes de operar com capital real.

**Trading de forex e CFDs pode resultar em perdas que excedem seu investimento inicial.**

---

*Documento criado para IAFX Prime v8 - Versão 1.0 - Março 2026*
