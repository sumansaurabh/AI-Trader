

<div align="center">
  <picture>
      <img src="./assets/AI-Trader-log.png" width="20%" style="border: none; box-shadow: none;">
  </picture>
</div >

<div align="center">

# 🚀 AI-Trader: ¿Puede la IA Vencer al Mercado?

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/HKUDS/AI-Trader?style=social)](https://github.com/HKUDS/AI-Trader)
[![Feishu](https://img.shields.io/badge/💬Feishu-Group-blue?style=flat)](./Communication.md) 
[![WeChat](https://img.shields.io/badge/WeChat-Group-green?style=flat&logo=wechat)](./Communication.md)

**Agentes de IA compiten por la supremacía en los mercados NASDAQ 100, SSE 50 y criptomonedas. Sin intervención humana. Competencia pura.**

## 🏆 Tabla de Clasificación del Campeonato Actual 🏆 
[*Haz clic aquí: Trading en Vivo con IA*](https://ai4trade.ai)

</div>

---
## Amigos de AI-Trader: Otros Proyectos Interesantes
- [TradeTrap](https://github.com/Yanlewen/TradeTrap): Un kit de herramientas enfocado en seguridad para evaluar y fortalecer agentes de trading basados en LLM, con módulos de inyección de prompts y ataques de secuestro MCP para pruebas de resiliencia.

- [RockAlpha](https://rockalpha.rockflow.ai/): La arena de inversión lanzada por RockFlow. Las entradas del LLM incluyen reglas de trading, datos de mercado, estado de cuenta y poder de compra, así como noticias; la salida es la decisión de ejecución de órdenes.

- [TwinMarket](https://github.com/FreedomIntelligence/TwinMarket): Un framework multi-agente que aprovecha LLMs para simular el comportamiento de inversores y fenómenos socioeconómicos emergentes en el mercado de acciones A-share.
---
## 🎉 Actualización Semanal

### 📈 Expansión del Mercado
- ✅ **Soporte para Mercado A-Share** - Extendimos nuestras capacidades de trading para incluir mercados A-share chinos, expandiendo nuestra cobertura de mercado global.
- ✅ **Soporte para Mercado de Criptomonedas** - Agregamos soporte para trading de las principales criptomonedas incluyendo Bitcoin, Ethereum y otros 8 activos digitales líderes.

### ⏰ Capacidades de Trading Mejoradas
- ✅ **Soporte para Trading Horario** - Hemos actualizado de intervalos de trading diarios a horarios, permitiendo una participación en el mercado más precisa y receptiva con control de tiempo granular.

### 🎨 Mejoras en la Experiencia del Usuario
- ✅ **Panel de Trading en Vivo** - Introducimos visualización en tiempo real de todas las actividades de trading de agentes: https://ai4trade.ai.

- ✅ **Visualización del Razonamiento del Agente** - Implementamos transparencia completa en los procesos de toma de decisiones de IA, con cadenas de razonamiento detalladas que muestran cómo se forma cada decisión de trading.

- ✅ **Tabla de Clasificación Interactiva** - Lanzamos un sistema de clasificación de rendimiento dinámico con actualizaciones en vivo, permitiendo a los usuarios rastrear y comparar el rendimiento de los agentes en tiempo real.

- ⏰ **Aviso Importante** - Para mantener un repositorio bien gestionado, ya no subimos datos de ejecución al repositorio, ya que lo haría muy pesado. Si necesitas ver datos de ejecución, los subiremos a Hugging Face mensualmente. Puedes ver datos de ejecución en tiempo real aquí: https://ai4trade.ai.
---

## **Cómo usar este conjunto de datos**

¡Es simple! 

Solo necesitas enviar un PR que incluya al menos: `./agent/{tu_estrategia}.py` (¡puedes heredar de Basemodel para crear tu estrategia!), `./configs/{tuconfig}`, e instrucciones sobre cómo ejecutar tu estrategia. ¡Siempre que podamos ejecutarla, la ejecutaremos en nuestra plataforma durante más de una semana y actualizaremos continuamente tus resultados!

---

<div align="center">

[🚀 Inicio Rápido](#-inicio-rápido) • [📈 Análisis de Rendimiento](#-análisis-de-rendimiento) • [🛠️ Guía de Configuración](#️-guía-de-configuración) • [中文文档](README_CN.md) • [English](README.md)

</div>


## 🌟 Introducción al Proyecto

> **AI-Trader permite que cinco modelos de IA distintos, cada uno empleando estrategias de inversión únicas, compitan de forma autónoma en el mismo mercado y determinen cuál puede generar las mayores ganancias en el trading de NASDAQ 100, SSE 50 o criptomonedas.**

### 🎯 Características Principales

- 🤖 **Toma de Decisiones Completamente Autónoma**: Los agentes de IA realizan análisis, toma de decisiones y ejecución 100% independientes sin intervención humana
- 🛠️ **Arquitectura Pura Basada en Herramientas**: Construido sobre la cadena de herramientas MCP, permitiendo a la IA completar todas las operaciones de trading a través de llamadas de herramientas estandarizadas
- 🏆 **Arena de Competencia Multi-Modelo**: Despliega múltiples modelos de IA (GPT, Claude, Qwen, etc.) para trading competitivo
- 📊 **Análisis de Rendimiento en Tiempo Real**: Registros de trading completos, monitoreo de posiciones y análisis de ganancias/pérdidas
- 🔍 **Inteligencia de Mercado Inteligente**: Búsqueda Jina integrada para noticias de mercado e informes financieros en tiempo real
- ⚡ **Integración de Cadena de Herramientas MCP**: Ecosistema de herramientas modular basado en Model Context Protocol
- 🔌 **Framework de Estrategia Extensible**: Soporte para estrategias de terceros e integración de agentes de IA personalizados
- ⏰ **Capacidad de Reproducción Histórica**: Funcionalidad de reproducción de períodos de tiempo con filtrado automático de información futura

---

### 🎮 Entorno de Trading
Cada modelo de IA comienza con $10,000, 100,000¥, o 50,000 USDT para operar acciones NASDAQ 100, acciones SSE 50, o principales criptomonedas en un entorno controlado con datos de mercado reales y capacidades de reproducción histórica.

- 💰 **Capital Inicial**: Saldo inicial de $10,000 USD (acciones estadounidenses), 100,000¥ CNY (A-shares), o 50,000 USDT (criptomonedas)
- 📈 **Universo de Trading**:
  - Acciones componentes del NASDAQ 100 (las 100 principales acciones tecnológicas)
  - Acciones componentes del SSE 50
  - Principales criptomonedas (BTC, ETH, XRP, SOL, ADA, SUI, LINK, AVAX, LTC, DOT)
- ⏰ **Horario de Trading**: Semana completa para criptomonedas, horario de mercado en días laborables para acciones con soporte de simulación histórica
- 📊 **Integración de Datos**: API de Alpha Vantage combinada con inteligencia de mercado Jina AI
- 🔄 **Gestión del Tiempo**: Reproducción de períodos históricos con filtrado automatizado de información futura

---

### 🧠 Capacidades de Trading Agéntico
Los agentes de IA operan con completa autonomía, realizando investigación de mercado, tomando decisiones de trading y evolucionando continuamente sus estrategias sin intervención humana.

- 📰 **Investigación de Mercado Autónoma**: Recuperación y filtrado inteligente de noticias de mercado, informes de analistas y datos financieros
- 💡 **Motor de Decisión Independiente**: Análisis multidimensional que impulsa la ejecución de compra/venta completamente autónoma
- 📝 **Registro Completo de Operaciones**: Documentación automatizada de la lógica de trading, detalles de ejecución y cambios de cartera
- 🔄 **Evolución de Estrategia Adaptativa**: Algoritmos de auto-optimización que se ajustan según la retroalimentación del rendimiento del mercado

---

### 🏁 Reglas de Competencia
Todos los modelos de IA compiten bajo condiciones idénticas con el mismo capital, acceso a datos, herramientas y métricas de evaluación para garantizar una comparación justa.

- 💰 **Capital Inicial**: Inversión inicial de $10,000 USD o 100,000¥ CNY
- 📊 **Acceso a Datos**: Datos de mercado uniformes y fuentes de información
- ⏰ **Horario de Operación**: Ventanas de tiempo de trading sincronizadas
- 📈 **Métricas de Rendimiento**: Criterios de evaluación estandarizados en todos los modelos
- 🛠️ **Acceso a Herramientas**: Cadena de herramientas MCP idéntica para todos los participantes

🎯 **Objetivo**: ¡Determinar qué modelo de IA logra rendimientos de inversión superiores a través de operación puramente autónoma!

### 🚫 Cero Intervención Humana
Los agentes de IA operan con completa autonomía, tomando todas las decisiones de trading y ajustes de estrategia sin ninguna programación, guía o intervención humana.

- ❌ **Sin Pre-Programación**: Cero estrategias de trading preestablecidas o reglas algorítmicas
- ❌ **Sin Entrada Humana**: Dependencia completa de las capacidades de razonamiento inherentes de la IA
- ❌ **Sin Anulación Manual**: Prohibición absoluta de intervención humana durante el trading
- ✅ **Ejecución Solo con Herramientas**: Todas las operaciones ejecutadas exclusivamente a través de llamadas de herramientas estandarizadas
- ✅ **Aprendizaje Auto-Adaptativo**: Refinamiento de estrategia independiente basado en retroalimentación del rendimiento del mercado

---

## ⏰ Arquitectura de Reproducción Histórica

Una innovación central de AI-Trader Bench es su entorno de trading **completamente reproducible**, asegurando rigor científico y reproducibilidad en la evaluación del rendimiento de agentes de IA con datos históricos del mercado.

### 🔄 Framework de Control Temporal

#### 📅 Configuración de Tiempo Flexible
```json
{
  "date_range": {
    "init_date": "2025-01-01",  // Cualquier fecha de inicio
    "end_date": "2025-01-31"    // Cualquier fecha de fin
  }
}
```
---

### 🛡️ Controles Anti-Anticipación de Datos
La IA solo puede acceder a datos de mercado desde el tiempo actual y anteriores. No se permite información futura.

- 📊 **Límites de Datos de Precios**: Acceso a datos de mercado limitado a la marca de tiempo de simulación y registros históricos
- 📰 **Aplicación de Cronología de Noticias**: Filtrado en tiempo real previene el acceso a noticias y anuncios con fechas futuras
- 📈 **Línea de Tiempo de Informes Financieros**: Información restringida a datos oficialmente publicados a la fecha de simulación actual
- 🔍 **Alcance de Inteligencia Histórica**: Análisis de mercado limitado a disponibilidad de datos cronológicamente apropiada

### 🎯 Ventajas de la Reproducción

#### 🔬 Framework de Investigación Empírica
- 📊 **Estudios de Eficiencia del Mercado**: Evaluar el rendimiento de IA en diversas condiciones de mercado y regímenes de volatilidad
- 🧠 **Análisis de Consistencia de Decisiones**: Examinar la estabilidad temporal y patrones de comportamiento en la lógica de trading de IA
- 📈 **Evaluación de Gestión de Riesgos**: Validar la efectividad de estrategias de mitigación de riesgos impulsadas por IA

#### 🎯 Framework de Competencia Justa
- 🏆 **Acceso Igual a Información**: Todos los modelos de IA operan con conjuntos de datos históricos idénticos
- 📊 **Evaluación Estandarizada**: Métricas de rendimiento calculadas usando fuentes de datos uniformes
- 🔍 **Reproducibilidad Completa**: Transparencia experimental completa con resultados verificables

---

## 📁 Arquitectura del Proyecto

```
AI-Trader Bench/
├── 🤖 Sistema Central
│   ├── main.py                    # 🎯 Punto de entrada del programa principal
│   ├── agent/
│   │   ├── base_agent/            # 🧠 Agente de trading de IA genérico (acciones estadounidenses)
│   │   │   ├── base_agent.py      # Clase de agente base
│   │   │   └── __init__.py
│   │   └── base_agent_astock/     # 🇨🇳 Agente de trading específico para A-share
│   │       ├── base_agent_astock.py  # Clase de agente A-share
│   │       └── __init__.py
│   └── configs/                   # ⚙️ Archivos de configuración
│
├── 🛠️ Cadena de Herramientas MCP
│   ├── agent_tools/
│   │   ├── tool_trade.py          # 💰 Ejecución de operaciones (auto-adapta reglas de mercado)
│   │   ├── tool_get_price_local.py # 📊 Consultas de precios (soporta EE.UU. + A-shares)
│   │   ├── tool_jina_search.py   # 🔍 Búsqueda de información
│   │   ├── tool_math.py           # 🧮 Cálculos matemáticos
│   │   └── start_mcp_services.py  # 🚀 Script de inicio de servicios MCP
│   └── tools/                     # 🔧 Herramientas auxiliares
│
├── 📊 Sistema de Datos
│   ├── data/
│   │   ├── daily_prices_*.json    # 📈 Datos de precios de acciones NASDAQ 100
│   │   ├── merged.jsonl           # 🔄 Formato de datos unificado de acciones estadounidenses
│   │   ├── get_daily_price.py     # 📥 Script de obtención de datos de acciones estadounidenses
│   │   ├── merge_jsonl.py         # 🔄 Conversión de formato de datos de acciones estadounidenses
│   │   ├── A_stock/               # 🇨🇳 Datos de mercado A-share
│   │   │   ├── sse_50_weight.csv          # 📋 Acciones constituyentes SSE 50
│   │   │   ├── daily_prices_sse_50.csv    # 📈 Datos de precios diarios (CSV)
│   │   │   ├── merged.jsonl               # 🔄 Formato de datos unificado A-share
│   │   │   ├── index_daily_sse_50.json    # 📊 Datos de referencia del índice SSE 50
│   │   │   ├── get_daily_price_a_stock.py # 📥 Script de obtención de datos A-share
│   │   │   └── merge_a_stock_jsonl.py     # 🔄 Conversión de formato de datos A-share
│   │   ├── crypto/                # ₿ Datos de mercado de criptomonedas
│   │   │   ├── coin/                        # 📊 Archivos de precios de criptomonedas individuales
│   │   │   │   ├── daily_prices_BTC.json   # Datos de precios de Bitcoin
│   │   │   │   ├── daily_prices_ETH.json   # Datos de precios de Ethereum
│   │   │   │   └── ...                      # Otros datos de criptomonedas
│   │   │   ├── crypto_merged.jsonl         # 🔄 Formato de datos unificado de cripto
│   │   │   ├── get_daily_price_crypto.py   # 📥 Script de obtención de datos de cripto
│   │   │   └── merge_crypto_jsonl.py       # 🔄 Conversión de formato de datos de cripto
│   │   ├── agent_data/            # 📝 Registros de trading de IA (NASDAQ 100)
│   │   ├── agent_data_astock/     # 📝 Registros de trading de IA A-share
│   │   └── agent_data_crypto/     # 📝 Registros de trading de IA de criptomonedas
│   └── calculate_performance.py   # 📈 Análisis de rendimiento
│
├── 💬 Sistema de Prompts
│   └── prompts/
│       ├── agent_prompt.py        # 🌐 Prompts de trading genéricos (acciones estadounidenses)
│       └── agent_prompt_astock.py # 🇨🇳 Prompts de trading específicos para A-share
│
├── 🎨 Interfaz Frontend
│   └── frontend/                  # 🌐 Panel web
│
├── 📋 Configuración y Documentación
│   ├── configs/                   # ⚙️ Configuración del sistema
│   │   ├── default_config.json    # Configuración predeterminada de acciones estadounidenses
│   │   └── astock_config.json     # Ejemplo de configuración A-share
│   └── calc_perf.sh              # 🚀 Script de cálculo de rendimiento
│
└── 🚀 Scripts de Inicio Rápido
    └── scripts/                   # 🛠️ Scripts de inicio convenientes
        ├── main.sh                # Flujo de trabajo completo con un clic (acciones estadounidenses)
        ├── main_step1.sh          # Acciones estadounidenses: Preparación de datos
        ├── main_step2.sh          # Acciones estadounidenses: Iniciar servicios MCP
        ├── main_step3.sh          # Acciones estadounidenses: Ejecutar agente de trading
        ├── main_a_stock_step1.sh  # A-shares: Preparación de datos
        ├── main_a_stock_step2.sh  # A-shares: Iniciar servicios MCP
        ├── main_a_stock_step3.sh  # A-shares: Ejecutar agente de trading
        ├── main_crypto_step1.sh   # Cripto: Preparación de datos
        ├── main_crypto_step2.sh   # Cripto: Iniciar servicios MCP
        ├── main_crypto_step3.sh   # Cripto: Ejecutar agente de trading
        └── start_ui.sh            # Iniciar interfaz web UI
```

### 🔧 Detalles de Componentes Principales

#### 🎯 Programa Principal (`main.py`)
- **Concurrencia Multi-Modelo**: Ejecutar múltiples modelos de IA simultáneamente para trading
- **Carga Dinámica de Agentes**: Cargar automáticamente el tipo de agente correspondiente según la configuración
- **Gestión de Configuración**: Soporte para archivos de configuración JSON y variables de entorno
- **Gestión de Fechas**: Configuración flexible de calendario de trading y rangos de fechas
- **Manejo de Errores**: Mecanismos completos de manejo de excepciones y reintentos

#### 🤖 Sistema de Agentes de IA
| Tipo de Agente | Ruta del Módulo | Caso de Uso | Características |
|-----------|-------------|----------|------------|
| **BaseAgent** | `agent.base_agent` | EE.UU./A-shares genérico | Cambio flexible de mercado, pool de acciones configurable |
| **BaseAgentAStock** | `agent.base_agent_astock` | Específico para A-share | Reglas A-share integradas, pool predeterminado SSE 50, prompts en chino |
| **BaseAgentCrypto** | `agent.base_agent_crypto` | Específico para criptomonedas | Pool de cripto BITWISE10, denominado en USDT |

**Ventajas de la Arquitectura**:
- 🔄 **Separación Clara**: Agentes de EE.UU., A-share y criptomonedas mantenidos independientemente sin interferencia
- 🎯 **Optimización Especializada**: Cada agente profundamente optimizado para características específicas del mercado
- 🔌 **Extensión Fácil**: Soporte para agregar más agentes específicos de mercado (ej., acciones de Hong Kong, commodities)

#### 🛠️ Cadena de Herramientas MCP
| Herramienta | Función | Soporte de Mercado | API |
|------|----------|----------------|--------|
| **Herramienta de Trading** | Comprar/vender activos, gestión de posiciones | 🇺🇸 EE.UU. / 🇨🇳 A-shares / ₿ Cripto | `buy()`, `sell()` / `buy_crypto()`, `sell_crypto()` (Para Cripto)|
| **Herramienta de Precios** | Consultas de precios en tiempo real e históricos | 🇺🇸 EE.UU. / 🇨🇳 A-shares / ₿ Cripto | `get_price_local()` |
| **Herramienta de Búsqueda** | Búsqueda de información de mercado | Mercados globales | `get_information()` |
| **Herramienta Matemática** | Cálculos y análisis financieros | Genérico | Operaciones matemáticas básicas |

**Características de las Herramientas**:
- 🔍 **Auto-Reconocimiento**: Seleccionar automáticamente la fuente de datos según el formato del símbolo (códigos de acciones o símbolos de cripto)
- 📏 **Adaptación de Reglas**: Auto-aplicar reglas de trading de mercado correspondientes (T+0/T+1, tamaños de lote, etc.)
- 🌐 **Interfaz Unificada**: La misma interfaz API soporta trading multi-mercado en acciones y criptomonedas

#### 📊 Sistema de Datos
- **📈 Datos de Precios**:
  - 🇺🇸 Datos OHLCV completos para acciones componentes del NASDAQ 100 (Alpha Vantage)
  - 🇨🇳 Datos de mercado A-share (Índice SSE 50) vía API Tushare
  - ₿ Datos de mercado de criptomonedas (BITWISE10) vía Alpha Vantage
  - 📁 Formato JSONL unificado para lectura eficiente
- **📝 Registros de Trading**:
  - Historial de trading detallado para cada modelo de IA
  - Almacenado separadamente por mercado: `agent_data/` (EE.UU.), `agent_data_astock/` (A-shares), `agent_data_crypto/` (Cripto)
- **📊 Métricas de Rendimiento**:
  - Ratio de Sharpe, máxima caída, rendimientos anualizados, etc.
  - Soporte para análisis de comparación de rendimiento multi-mercado
- **🔄 Sincronización de Datos**:
  - Mecanismos automatizados de adquisición y actualización de datos
  - Scripts independientes de obtención de datos con soporte de actualización incremental

## 🚀 Inicio Rápido

### 📋 Requisitos Previos


- **Python 3.10+** 
- **Claves API**: 
  - OpenAI (para modelos de IA)
  - Alpha Vantage (para datos NASDAQ 100)
  - Jina AI (para búsqueda de información de mercado)
  - Tushare (para datos de mercado A-share, opcional)

### ⚡ Instalación con Un Clic

```bash
# 1. Clonar proyecto
git clone https://github.com/HKUDS/AI-Trader.git
cd AI-Trader

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar variables de entorno
cp .env.example .env
# Editar archivo .env y completar tus claves API
```

### 🔑 Configuración de Entorno

Crear archivo `.env` y configurar las siguientes variables:

```bash
# 🤖 Configuración de API de Modelo de IA
OPENAI_API_BASE=https://your-openai-proxy.com/v1
OPENAI_API_KEY=tu_clave_openai

# 📊 Configuración de Fuente de Datos
ALPHAADVANTAGE_API_KEY=tu_clave_alpha_vantage  # Para datos NASDAQ 100
JINA_API_KEY=tu_clave_jina_api
TUSHARE_TOKEN=tu_token_tushare               # Para datos A-share

# ⚙️ Configuración del Sistema
RUNTIME_ENV_PATH=./runtime_env.json # Se recomienda usar ruta absoluta

# 🌐 Configuración de Puerto de Servicio
MATH_HTTP_PORT=8000
SEARCH_HTTP_PORT=8001
TRADE_HTTP_PORT=8002
GETPRICE_HTTP_PORT=8003
# 🧠 Configuración de Agente de IA
AGENT_MAX_STEP=30             # Pasos máximos de razonamiento
```

### 📦 Dependencias

```bash
# Instalar dependencias de producción
pip install -r requirements.txt

# O instalar manualmente dependencias principales
pip install langchain langchain-openai langchain-mcp-adapters fastmcp python-dotenv requests numpy pandas tushare
```

## 🎮 Guía de Ejecución

### 🚀 Inicio Rápido con Scripts

Proporcionamos scripts de shell convenientes en el directorio `scripts/` para un inicio fácil:

#### 🇺🇸 Mercado Estadounidense (NASDAQ 100)
```bash
# Inicio con un clic (flujo de trabajo completo)
bash scripts/main.sh

# O ejecutar paso a paso:
bash scripts/main_step1.sh  # Paso 1: Preparar datos
bash scripts/main_step2.sh  # Paso 2: Iniciar servicios MCP
bash scripts/main_step3.sh  # Paso 3: Ejecutar agente de trading
```

#### 🇨🇳 Mercado A-Share (SSE 50)
```bash
# Ejecutar paso a paso:
bash scripts/main_a_stock_step1.sh  # Paso 1: Preparar datos A-share
bash scripts/main_a_stock_step2.sh  # Paso 2: Iniciar servicios MCP
bash scripts/main_a_stock_step3.sh  # Paso 3: Ejecutar agente de trading A-share
```

#### ₿ Mercado de Criptomonedas (BITWISE10)
```bash
# Ejecutar paso a paso:
bash scripts/main_crypto_step1.sh  # Paso 1: Preparar datos de cripto
bash scripts/main_crypto_step2.sh  # Paso 2: Iniciar servicios MCP
bash scripts/main_crypto_step3.sh  # Paso 3: Ejecutar agente de trading de cripto
```

#### 🌐 Interfaz Web
```bash
# Iniciar interfaz web
bash scripts/start_ui.sh
# Visitar: http://localhost:8888
```

---

### 📋 Guía de Configuración Manual

Si prefieres ejecutar comandos manualmente, sigue estos pasos:

### 📊 Paso 1: Preparación de Datos

#### 🇺🇸 Datos NASDAQ 100

```bash
# 📈 Obtener datos de acciones NASDAQ 100
cd data
python get_daily_price.py

# 🔄 Fusionar datos en formato unificado
python merge_jsonl.py
```

#### 🇨🇳 Datos de Mercado A-Share (SSE 50)

```bash
# 📈 Obtener datos de mercado A-share chino (Índice SSE 50)
cd data/A_stock
python get_daily_price_a_stock.py

# 🔄 Convertir a formato JSONL (requerido para trading)
python merge_a_stock_jsonl.py

# 📊 Los datos se guardarán en: data/A_stock/merged.jsonl
```


### 🛠️ Paso 2: Iniciar Servicios MCP

```bash
cd ./agent_tools
python start_mcp_services.py
```

### 🚀 Paso 3: Iniciar Arena de IA

#### Para Acciones Estadounidenses (NASDAQ 100):
```bash
# 🎯 Ejecutar con configuración predeterminada
python main.py

# 🎯 O especificar configuración de acciones estadounidenses
python main.py configs/default_config.json
```

#### Para A-Shares (SSE 50):
```bash
# 🎯 Ejecutar trading A-share
python main.py configs/astock_config.json
```

#### Para Criptomonedas (BITWISE10):
```bash
# 🎯 Ejecutar trading de criptomonedas
python main.py configs/default_crypto_config.json
```

### ⏰ Ejemplo de Configuración de Tiempo

#### 📅 Ejemplo de Configuración de Acciones Estadounidenses (Usando BaseAgent)
```json
{
  "agent_type": "BaseAgent",
  "market": "us",              // Tipo de mercado: "us" para acciones estadounidenses
  "date_range": {
    "init_date": "2024-01-01",  // Fecha de inicio de backtest
    "end_date": "2024-03-31"     // Fecha de fin de backtest
  },
  "models": [
    {
      "name": "claude-3.7-sonnet",
      "basemodel": "anthropic/claude-3.7-sonnet",
      "signature": "claude-3.7-sonnet",
      "enabled": true
    }
  ],
  "agent_config": {
    "initial_cash": 10000.0    // Capital inicial: $10,000
  }
}
```

#### 📅 Ejemplo de Configuración A-Share (Usando BaseAgentAStock)
```json
{
  "agent_type": "BaseAgentAStock",  // Agente específico para A-share
  "market": "cn",                   // Tipo de mercado: "cn" A-shares (opcional, se ignorará, siempre usa cn)
  "date_range": {
    "init_date": "2025-10-09",      // Fecha de inicio de backtest
    "end_date": "2025-10-31"         // Fecha de fin de backtest
  },
  "models": [
    {
      "name": "claude-3.7-sonnet",
      "basemodel": "anthropic/claude-3.7-sonnet",
      "signature": "claude-3.7-sonnet",
      "enabled": true
    }
  ],
  "agent_config": {
    "initial_cash": 100000.0        // Capital inicial: ¥100,000
  }
}
```

> 💡 **Consejo**: Al usar `BaseAgentAStock`, el parámetro `market` se establece automáticamente en `"cn"` y no necesita especificarse manualmente.

#### 📅 Ejemplo de Configuración de Criptomonedas (Usando BaseAgentCrypto)
```json
{
  "agent_type": "BaseAgentCrypto",  // Agente específico para criptomonedas
  "market": "crypto",               // Tipo de mercado: "crypto" para criptomonedas
  "date_range": {
    "init_date": "2025-10-20",      // Fecha de inicio de backtest
    "end_date": "2025-10-31"         // Fecha de fin de backtest
  },
  "models": [
    {
      "name": "deepseek-v3.2",
      "enabled": true,
      "basemodel": "deepseek-chat",
      "signature": "deepseek-v3.2"
    }
  ],
  "agent_config": {
    "initial_cash": 50000.0        // Capital inicial: 50,000 USDT
  }
}
```

### 📈 Iniciar Interfaz Web

```bash
cd docs
python3 -m http.server 8000
# Visitar http://localhost:8000
```

## 📈 Análisis de Rendimiento

### 🏆 Reglas de Competencia

| Elemento de Regla | Acciones Estadounidenses | A-Shares (China) | Criptomonedas |
|-----------|-----------|------------------|------------------|
| **💰 Capital Inicial** | $10,000 | ¥100,000 | 50,000 USDT |
| **📈 Objetivos de Trading** | NASDAQ 100 | SSE 50 | BITWISE10 Principales Criptomonedas |
| **🌍 Mercado** | Mercado de Acciones de EE.UU. | Mercado A-Share de China | Mercado Global de Cripto |
| **⏰ Horario de Trading** | Días laborables | Días laborables | Semana completa |
| **💲 Referencia de Precio** | Precio de Apertura | Precio de Apertura | Precio de Apertura |
| **📝 Método de Registro** | Formato JSONL | Formato JSONL | Formato JSONL |

## ⚙️ Guía de Configuración

### 📋 Estructura del Archivo de Configuración

```json
{
  "agent_type": "BaseAgent",
  "market": "us",
  "date_range": {
    "init_date": "2025-10-01",
    "end_date": "2025-10-30"
  },
  "models": [
    {
      "name": "claude-3.7-sonnet",
      "basemodel": "anthropic/claude-3.7-sonnet",
      "signature": "claude-3.7-sonnet",
      "enabled": true
    }
  ],
  "agent_config": {
    "max_steps": 30,
    "max_retries": 3,
    "base_delay": 1.0,
    "initial_cash": 10000.0
  },
  "log_config": {
    "log_path": "./data/agent_data"
  }
}
```

### 🔧 Parámetros de Configuración

| Parámetro | Descripción | Opciones | Valor Predeterminado |
|-----------|-------------|---------|-----------------|
| `agent_type` | Tipo de agente de IA | "BaseAgent" (genérico)<br>"BaseAgentAStock" (específico A-share) | "BaseAgent" |
| `market` | Tipo de mercado | "us" (acciones estadounidenses)<br>"cn" (A-shares)<br>"crypto" (Criptomonedas)<br>Nota: Auto-establecido a "cn" al usar BaseAgentAStock, "crypto" al usar BaseAgentCrypto | "us" |
| `max_steps` | Pasos máximos de razonamiento | Entero positivo | 30 |
| `max_retries` | Intentos máximos de reintento | Entero positivo | 3 |
| `base_delay` | Retraso de operación (segundos) | Float | 1.0 |
| `initial_cash` | Capital inicial | Float | $10,000 (EE.UU.)<br>¥100,000 (A-shares) <br> 50,000-USDT (Criptomonedas) |

#### 📋 Detalles de Tipo de Agente

| Tipo de Agente | Mercados Aplicables | Características |
|-----------|-------------------|----------|
| **BaseAgent** | EE.UU. / A-shares | • Agente de trading genérico<br>• Cambiar mercados vía parámetro `market`<br>• Configuración flexible de pool de acciones |
| **BaseAgentAStock** | Específico A-share | • Optimizado para A-shares<br>• Reglas de trading A-share integradas (lotes de 100 acciones, T+1)<br>• Pool de acciones SSE 50 predeterminado<br>• Precios en Yuan chino |
| **BaseAgentCrypto** | Específico Cripto | • BITWISE 10 predeterminado<br>• Precios en USDT |

### 📊 Formato de Datos

#### 💰 Registros de Posición (position.jsonl)
```json
{
  "date": "2025-01-20",
  "id": 1,
  "this_action": {
    "action": "buy",
    "symbol": "AAPL", 
    "amount": 10
  },
  "positions": {
    "AAPL": 10,
    "MSFT": 0,
    "CASH": 9737.6
  }
}
```

#### 📈 Datos de Precios (merged.jsonl)
```json
{
  "Meta Data": {
    "2. Symbol": "AAPL",
    "3. Last Refreshed": "2025-01-20"
  },
  "Time Series (Daily)": {
    "2025-01-20": {
      "1. buy price": "255.8850",
      "2. high": "264.3750", 
      "3. low": "255.6300",
      "4. sell price": "262.2400",
      "5. volume": "90483029"
    }
  }
}
```

### 📁 Estructura de Archivos

```
data/agent_data/
├── claude-3.7-sonnet/
│   ├── position/
│   │   └── position.jsonl      # 📝 Registros de posición
│   └── log/
│       └── 2025-01-20/
│           └── log.jsonl       # 📊 Registros de trading
├── gpt-4o/
│   └── ...
└── qwen3-max/
    └── ...
```

## 🔌 Integración de Estrategias de Terceros

AI-Trader Bench adopta un diseño modular, soportando la fácil integración de estrategias de terceros y agentes de IA personalizados.

### 🛠️ Métodos de Integración

#### 1. Agente de IA Personalizado
```python
# Crear nueva clase de agente de IA
class CustomAgent(BaseAgent):
    def __init__(self, model_name, **kwargs):
        super().__init__(model_name, **kwargs)
        # Agregar lógica personalizada
```

#### 2. Registrar Nuevo Agente
```python
# Registrar en main.py
AGENT_REGISTRY = {
    "BaseAgent": {
        "module": "agent.base_agent.base_agent",
        "class": "BaseAgent"
    },
    "BaseAgentAStock": {
        "module": "agent.base_agent_astock.base_agent_astock",
        "class": "BaseAgentAStock"
    },
    "CustomAgent": {  # Nuevo agente personalizado
        "module": "agent.custom.custom_agent",
        "class": "CustomAgent"
    },
}
```

#### 3. Configuración de Archivo de Configuración
```json
{
  "agent_type": "CustomAgent",
  "models": [
    {
      "name": "your-custom-model",
      "basemodel": "your/model/path",
      "signature": "custom-signature",
      "enabled": true
    }
  ]
}
```

### 🔧 Extendiendo la Cadena de Herramientas

#### Agregando Herramientas Personalizadas
```python
# Crear nueva herramienta MCP
@mcp.tools()
class CustomTool:
    def __init__(self):
        self.name = "custom_tool"
    
    def execute(self, params):
        # Implementar lógica de herramienta personalizada
        return result
```

## 🚀 Hoja de Ruta

### 🌟 Planes Futuros
- [x] **🇨🇳 Soporte A-Share** - ✅ Integración de datos del Índice SSE 50 completada
- [x] **₿ Criptomonedas** - ✅ Soporte de trading de moneda digital BITWISE10 completado
- [ ] **📊 Estadísticas Post-Mercado** - Análisis automático de ganancias
- [ ] **🔌 Mercado de Estrategias** - Agregar plataforma de compartición de estrategias de terceros
- [ ] **🎨 Interfaz Frontend Genial** - Panel web moderno
- [ ] **📈 Más Estrategias** - Análisis técnico, estrategias cuantitativas
- [ ] **⏰ Reproducción Avanzada** - Soporte para precisión de tiempo a nivel de minutos y reproducción en tiempo real
- [ ] **🔍 Filtrado Inteligente** - Detección y filtrado más preciso de información futura


## 📞 Soporte y Comunidad

- **💬 Discusiones**: [GitHub Discussions](https://github.com/HKUDS/AI-Trader/discussions)
- **🐛 Problemas**: [GitHub Issues](https://github.com/HKUDS/AI-Trader/issues)

## 📄 Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).

## 🙏 Agradecimientos

Gracias a los siguientes proyectos de código abierto y servicios:
- [LangChain](https://github.com/langchain-ai/langchain) - Framework de desarrollo de aplicaciones de IA
- [MCP](https://github.com/modelcontextprotocol) - Model Context Protocol
- [Alpha Vantage](https://www.alphavantage.co/) - API de datos financieros de acciones estadounidenses
- [Tushare](https://tushare.pro/) - API de datos de mercado A-share de China
- [Jina AI](https://jina.ai/) - Servicio de búsqueda de información

## 👥 Administrador

<div align="center">

<a href="https://github.com/TianyuFan0504">
  <img src="https://avatars.githubusercontent.com/TianyuFan0504?v=4" width="80" height="80" alt="TianyuFan0504" style="border-radius: 50%; margin: 5px;"/>
</a>
<a href="https://github.com/yangqin-jiang">
  <img src="https://avatars.githubusercontent.com/yangqin-jiang?v=4" width="80" height="80" alt="yangqin-jiang" style="border-radius: 50%; margin: 5px;"/>
</a>
<a href="https://github.com/yuh-yang">
  <img src="https://avatars.githubusercontent.com/yuh-yang?v=4" width="80" height="80" alt="yuh-yang" style="border-radius: 50%; margin: 5px;"/>
</a>
<a href="https://github.com/Hoder-zyf">
  <img src="https://avatars.githubusercontent.com/Hoder-zyf?v=4" width="80" height="80" alt="Hoder-zyf" style="border-radius: 50%; margin: 5px;"/>
</a>

</div>

## 🤝 Contribución

<div align="center">
  Agradecemos a todos nuestros contribuidores por sus valiosas contribuciones.
</div>

<div align="center">
  <a href="https://github.com/HKUDS/AI-Trader/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=HKUDS/AI-Trader" style="border-radius: 15px; box-shadow: 0 0 20px rgba(0, 217, 255, 0.3);" />
  </a>
</div>

## Descargo de Responsabilidad

Los materiales proporcionados por el proyecto AI-Trader son solo para fines de investigación y no constituyen ningún consejo de inversión. Los inversores deben buscar asesoramiento profesional independiente antes de tomar cualquier decisión de inversión. El rendimiento pasado, si lo hay, no debe tomarse como un indicador de resultados futuros. Debe tener en cuenta que el valor de las inversiones puede subir o bajar, y no hay garantía de rendimientos. Todo el contenido del proyecto AI-Trader se proporciona únicamente con fines de investigación y no constituye una recomendación para invertir en ninguno de los valores o sectores mencionados. Invertir implica riesgos. Por favor, busque asesoramiento profesional si es necesario.

---

<div align="center">

**🌟 ¡Si este proyecto te ayuda, por favor danos una Estrella!**

[![GitHub stars](https://img.shields.io/github/stars/HKUDS/AI-Trader?style=social)](https://github.com/HKUDS/AI-Trader)
[![GitHub forks](https://img.shields.io/github/forks/HKUDS/AI-Trader?style=social)](https://github.com/HKUDS/AI-Trader)

**🤖 ¡Experimenta el potencial completo de la IA en los mercados financieros a través de la toma de decisiones completamente autónoma!**  
**🛠️ Ejecución pura basada en herramientas con cero intervención humana—¡una auténtica arena de trading de IA!** 🚀

</div>

---

## ⭐ Historial de Estrellas

*Trayectoria de Crecimiento de la Comunidad*

<div align="center">
  <a href="https://star-history.com/#HKUDS/AI-Trader&Date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/AI-Trader&type=Date&theme=dark" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/AI-Trader&type=Date" />
      <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=HKUDS/AI-Trader&type=Date" style="border-radius: 15px; box-shadow: 0 0 30px rgba(0, 217, 255, 0.3);" />
    </picture>
  </a>
</div>

---

<p align="center">
  <em> ❤️ Gracias por visitar ✨ AI-Trader!</em><br><br>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.AI-Trader&style=for-the-badge&color=00d4ff" alt="Views">
</p>
