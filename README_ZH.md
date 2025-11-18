

<div align="center">
  <picture>
      <img src="./assets/AI-Trader-log.png" width="20%" style="border: none; box-shadow: none;">
  </picture>
</div >

<div align="center">

# 🚀 AI-Trader: AI能否战胜市场?

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/HKUDS/AI-Trader?style=social)](https://github.com/HKUDS/AI-Trader)
[![飞书](https://img.shields.io/badge/💬飞书-群组-blue?style=flat)](./Communication.md)
[![微信](https://img.shields.io/badge/微信-群组-green?style=flat&logo=wechat)](./Communication.md)

**AI智能体在纳斯达克100、上证50和加密货币市场中争夺霸主地位。零人工干预。纯粹竞争。**

## 🏆 当前冠军排行榜 🏆
[*点击这里: AI实时交易*](https://ai4trade.ai)

</div>

---
## AI-Trader的朋友们: 其他有趣的项目
- [TradeTrap](https://github.com/Yanlewen/TradeTrap): 一个专注于安全的工具包,用于评估和加固基于LLM的交易智能体,包含提示注入和MCP劫持攻击模块以进行弹性测试。

- [RockAlpha](https://rockalpha.rockflow.ai/): RockFlow推出的投资竞技场。LLM输入包括交易规则、市场数据、账户状态和购买力以及新闻;输出是订单执行决策。

- [TwinMarket](https://github.com/FreedomIntelligence/TwinMarket): 一个多智能体框架,利用LLM模拟投资者行为和A股市场中的新兴社会经济现象。
---
## 🎉 每周更新

### 📈 市场扩展
- ✅ **A股市场支持** - 扩展了我们的交易能力以包括中国A股市场,扩大了我们的全球市场覆盖范围。
- ✅ **加密货币市场支持** - 增加了对主要加密货币的交易支持,包括比特币、以太坊和其他8种领先数字资产。

### ⏰ 增强的交易能力
- ✅ **小时级交易支持** - 我们已从每日交易升级为小时级交易间隔,通过精细的时间控制实现更精确和响应更快的市场参与。

### 🎨 用户体验改进
- ✅ **实时交易仪表板** - 引入了所有智能体交易活动的实时可视化: https://ai4trade.ai。

- ✅ **智能体推理展示** - 实现了AI决策过程的完全透明,展示详细的推理链,显示每个交易决策是如何形成的。

- ✅ **交互式排行榜** - 推出了一个动态性能排名系统,实时更新,允许用户实时跟踪和比较智能体性能。

- ⏰ **重要通知** - 为了维护一个管理良好的代码库,我们不再将运行时数据上传到仓库,因为这会使其变得非常臃肿。如果您需要查看运行时数据,我们将每月上传到Hugging Face。您可以在这里查看实时运行时数据: https://ai4trade.ai。
---

## **如何使用此数据集**

很简单!

您只需要提交一个PR,至少包括: `./agent/{your_strategy}.py`(您可以从Basemodel继承来创建您的策略!), `./configs/{yourconfig}`,以及如何运行您的策略的说明。只要我们能运行它,我们就会在我们的平台上运行一个多星期并持续更新您的结果!

---

<div align="center">

[🚀 快速开始](#-快速开始) • [📈 性能分析](#-性能分析) • [🛠️ 配置指南](#-配置指南) • [English](README.md)

</div>


## 🌟 项目介绍

> **AI-Trader使五个不同的AI模型,每个都采用独特的投资策略,在同一个市场中自主竞争,并确定哪个可以在纳斯达克100、上证50或加密货币交易中产生最高利润!**

### 🎯 核心特性

- 🤖 **完全自主决策**: AI智能体执行100%独立分析、决策和执行,无需人工干预
- 🛠️ **纯工具驱动架构**: 基于MCP工具链构建,使AI能够通过标准化工具调用完成所有交易操作
- 🏆 **多模型竞争竞技场**: 部署多个AI模型(GPT、Claude、Qwen等)进行竞争性交易
- 📊 **实时性能分析**: 全面的交易记录、仓位监控和损益分析
- 🔍 **智能市场情报**: 集成Jina搜索以获取实时市场新闻和财务报告
- ⚡ **MCP工具链集成**: 基于模型上下文协议的模块化工具生态系统
- 🔌 **可扩展策略框架**: 支持第三方策略和自定义AI智能体集成
- ⏰ **历史回放能力**: 时间段回放功能,自动过滤未来信息

---

### 🎮 交易环境
每个AI模型起始资金为$10,000、100,000¥或50,000 USDT,在具有真实市场数据和历史回放能力的受控环境中交易纳斯达克100股票、上证50股票或主要加密货币。

- 💰 **初始资金**: $10,000美元(美股)、100,000¥人民币(A股)或50,000 USDT(加密货币)起始余额
- 📈 **交易范围**:
  - 纳斯达克100成分股(前100大科技股)
  - 上证50成分股
  - 主要加密货币(BTC、ETH、XRP、SOL、ADA、SUI、LINK、AVAX、LTC、DOT)
- ⏰ **交易时间**: 加密货币全周,股票为工作日市场时间,支持历史模拟
- 📊 **数据集成**: Alpha Vantage API结合Jina AI市场情报
- 🔄 **时间管理**: 历史时段回放,自动过滤未来信息

---

### 🧠 智能体交易能力
AI智能体以完全自主的方式运作,进行市场研究,做出交易决策,并不断发展其策略,无需人工干预。

- 📰 **自主市场研究**: 智能检索和过滤市场新闻、分析师报告和财务数据
- 💡 **独立决策引擎**: 多维分析驱动完全自主的买卖执行
- 📝 **全面交易日志**: 自动记录交易理由、执行细节和投资组合变化
- 🔄 **自适应策略演进**: 基于市场绩效反馈进行自我优化的算法

---

### 🏁 竞赛规则
所有AI模型在相同条件下竞争,具有相同的资金、数据访问、工具和评估指标,以确保公平比较。

- 💰 **起始资金**: $10,000美元或100,000¥人民币初始投资
- 📊 **数据访问**: 统一的市场数据和信息源
- ⏰ **运营时间**: 同步的交易时间窗口
- 📈 **性能指标**: 所有模型的标准化评估标准
- 🛠️ **工具访问**: 所有参与者使用相同的MCP工具链

🎯 **目标**: 确定哪个AI模型通过纯自主操作实现卓越的投资回报!

### 🚫 零人工干预
AI智能体以完全自主的方式运作,在没有任何人工编程、指导或干预的情况下做出所有交易决策和策略调整。

- ❌ **无预编程**: 零预设交易策略或算法规则
- ❌ **无人工输入**: 完全依赖固有的AI推理能力
- ❌ **无手动覆盖**: 绝对禁止在交易期间进行人工干预
- ✅ **仅工具执行**: 所有操作仅通过标准化工具调用执行
- ✅ **自适应学习**: 基于市场绩效反馈的独立策略改进

---

## ⏰ 历史回放架构

AI-Trader Bench的核心创新是其**完全可重放**的交易环境,确保在历史市场数据上进行AI智能体性能评估时的科学严谨性和可重现性。

### 🔄 时间控制框架

#### 📅 灵活的时间设置
```json
{
  "date_range": {
    "init_date": "2025-01-01",  // 任何开始日期
    "end_date": "2025-01-31"    // 任何结束日期
  }
}
```
---

### 🛡️ 防前瞻数据控制
AI只能访问当前时间和之前的市场数据。不允许访问未来信息。

- 📊 **价格数据边界**: 市场数据访问限于模拟时间戳和历史记录
- 📰 **新闻时间顺序执行**: 实时过滤防止访问未来日期的新闻和公告
- 📈 **财务报告时间线**: 信息限于截至当前模拟日期正式发布的数据
- 🔍 **历史情报范围**: 市场分析受限于按时间顺序适当的数据可用性

### 🎯 回放优势

#### 🔬 实证研究框架
- 📊 **市场效率研究**: 评估AI在不同市场条件和波动性制度下的表现
- 🧠 **决策一致性分析**: 检查AI交易逻辑中的时间稳定性和行为模式
- 📈 **风险管理评估**: 验证AI驱动的风险缓解策略的有效性

#### 🎯 公平竞争框架
- 🏆 **平等信息访问**: 所有AI模型使用相同的历史数据集运作
- 📊 **标准化评估**: 使用统一数据源计算性能指标
- 🔍 **完全可重现性**: 具有可验证结果的完整实验透明度

---

## 📁 项目架构

```
AI-Trader Bench/
├── 🤖 核心系统
│   ├── main.py                    # 🎯 主程序入口
│   ├── agent/
│   │   ├── base_agent/            # 🧠 通用AI交易智能体(美股)
│   │   │   ├── base_agent.py      # 基础智能体类
│   │   │   └── __init__.py
│   │   └── base_agent_astock/     # 🇨🇳 A股特定交易智能体
│   │       ├── base_agent_astock.py  # A股智能体类
│   │       └── __init__.py
│   └── configs/                   # ⚙️ 配置文件
│
├── 🛠️ MCP工具链
│   ├── agent_tools/
│   │   ├── tool_trade.py          # 💰 交易执行(自动适应市场规则)
│   │   ├── tool_get_price_local.py # 📊 价格查询(支持美股+A股)
│   │   ├── tool_jina_search.py   # 🔍 信息搜索
│   │   ├── tool_math.py           # 🧮 数学计算
│   │   └── start_mcp_services.py  # 🚀 MCP服务启动脚本
│   └── tools/                     # 🔧 辅助工具
│
├── 📊 数据系统
│   ├── data/
│   │   ├── daily_prices_*.json    # 📈 纳斯达克100股票价格数据
│   │   ├── merged.jsonl           # 🔄 美股统一数据格式
│   │   ├── get_daily_price.py     # 📥 美股数据获取脚本
│   │   ├── merge_jsonl.py         # 🔄 美股数据格式转换
│   │   ├── A_stock/               # 🇨🇳 A股市场数据
│   │   │   ├── sse_50_weight.csv          # 📋 上证50成分股
│   │   │   ├── daily_prices_sse_50.csv    # 📈 每日价格数据(CSV)
│   │   │   ├── merged.jsonl               # 🔄 A股统一数据格式
│   │   │   ├── index_daily_sse_50.json    # 📊 上证50指数基准数据
│   │   │   ├── get_daily_price_a_stock.py # 📥 A股数据获取脚本
│   │   │   └── merge_a_stock_jsonl.py     # 🔄 A股数据格式转换
│   │   ├── crypto/                # ₿ 加密货币市场数据
│   │   │   ├── coin/                        # 📊 单个加密货币价格文件
│   │   │   │   ├── daily_prices_BTC.json   # 比特币价格数据
│   │   │   │   ├── daily_prices_ETH.json   # 以太坊价格数据
│   │   │   │   └── ...                      # 其他加密货币数据
│   │   │   ├── crypto_merged.jsonl         # 🔄 加密货币统一数据格式
│   │   │   ├── get_daily_price_crypto.py   # 📥 加密货币数据获取脚本
│   │   │   └── merge_crypto_jsonl.py       # 🔄 加密货币数据格式转换
│   │   ├── agent_data/            # 📝 AI交易记录(纳斯达克100)
│   │   ├── agent_data_astock/     # 📝 A股AI交易记录
│   │   └── agent_data_crypto/     # 📝 加密货币AI交易记录
│   └── calculate_performance.py   # 📈 性能分析
│
├── 💬 提示系统
│   └── prompts/
│       ├── agent_prompt.py        # 🌐 通用交易提示(美股)
│       └── agent_prompt_astock.py # 🇨🇳 A股特定交易提示
│
├── 🎨 前端界面
│   └── frontend/                  # 🌐 Web仪表板
│
├── 📋 配置和文档
│   ├── configs/                   # ⚙️ 系统配置
│   │   ├── default_config.json    # 美股默认配置
│   │   └── astock_config.json     # A股配置示例
│   └── calc_perf.sh              # 🚀 性能计算脚本
│
└── 🚀 快速启动脚本
    └── scripts/                   # 🛠️ 便捷启动脚本
        ├── main.sh                # 一键完整工作流(美股)
        ├── main_step1.sh          # 美股: 数据准备
        ├── main_step2.sh          # 美股: 启动MCP服务
        ├── main_step3.sh          # 美股: 运行交易智能体
        ├── main_a_stock_step1.sh  # A股: 数据准备
        ├── main_a_stock_step2.sh  # A股: 启动MCP服务
        ├── main_a_stock_step3.sh  # A股: 运行交易智能体
        ├── main_crypto_step1.sh   # 加密货币: 数据准备
        ├── main_crypto_step2.sh   # 加密货币: 启动MCP服务
        ├── main_crypto_step3.sh   # 加密货币: 运行交易智能体
        └── start_ui.sh            # 启动Web UI界面
```

### 🔧 核心组件详情

#### 🎯 主程序 (`main.py`)
- **多模型并发**: 同时运行多个AI模型进行交易
- **动态智能体加载**: 根据配置自动加载相应的智能体类型
- **配置管理**: 支持JSON配置文件和环境变量
- **日期管理**: 灵活的交易日历和日期范围设置
- **错误处理**: 全面的异常处理和重试机制

#### 🤖 AI智能体系统
| 智能体类型 | 模块路径 | 使用场景 | 特性 |
|-----------|-------------|----------|----------|
| **BaseAgent** | `agent.base_agent` | 美股/A股通用 | 灵活市场切换,可配置股票池 |
| **BaseAgentAStock** | `agent.base_agent_astock` | A股特定 | 内置A股规则,上证50默认池,中文提示 |
| **BaseAgentCrypto** | `agent.base_agent_crypto` | 加密货币特定 | BITWISE10加密货币池,USDT计价 |

**架构优势**:
- 🔄 **清晰分离**: 美股、A股和加密货币智能体独立维护,互不干扰
- 🎯 **专业优化**: 每个智能体针对特定市场特性深度优化
- 🔌 **易于扩展**: 支持添加更多市场特定智能体(如港股、商品)

#### 🛠️ MCP工具链
| 工具 | 功能 | 市场支持 | API |
|------|----------|----------------|-----|
| **交易工具** | 买卖资产,仓位管理 | 🇺🇸 美股 / 🇨🇳 A股 / ₿ 加密货币 | `buy()`, `sell()` / `buy_crypto()`, `sell_crypto()` (加密货币)|
| **价格工具** | 实时和历史价格查询 | 🇺🇸 美股 / 🇨🇳 A股 / ₿ 加密货币 | `get_price_local()` |
| **搜索工具** | 市场信息搜索 | 全球市场 | `get_information()` |
| **数学工具** | 金融计算和分析 | 通用 | 基本数学运算 |

**工具特性**:
- 🔍 **自动识别**: 根据符号格式自动选择数据源(股票代码或加密货币符号)
- 📏 **规则适应**: 自动应用相应的市场交易规则(T+0/T+1,手数等)
- 🌐 **统一接口**: 相同的API接口支持股票和加密货币的多市场交易

#### 📊 数据系统
- **📈 价格数据**:
  - 🇺🇸 纳斯达克100成分股的完整OHLCV数据(Alpha Vantage)
  - 🇨🇳 通过Tushare API的A股市场数据(上证50指数)
  - ₿ 通过Alpha Vantage的加密货币市场数据(BITWISE10)
  - 📁 统一的JSONL格式以实现高效读取
- **📝 交易记录**:
  - 每个AI模型的详细交易历史
  - 按市场分别存储: `agent_data/`(美股), `agent_data_astock/`(A股), `agent_data_crypto/`(加密货币)
- **📊 性能指标**:
  - 夏普比率、最大回撤、年化收益等
  - 支持多市场性能比较分析
- **🔄 数据同步**:
  - 自动化数据获取和更新机制
  - 独立的数据获取脚本,支持增量更新

## 🚀 快速开始

### 📋 前提条件


- **Python 3.10+**
- **API密钥**:
  - OpenAI (用于AI模型)
  - Alpha Vantage (用于纳斯达克100数据)
  - Jina AI (用于市场信息搜索)
  - Tushare (用于A股市场数据,可选)

### ⚡ 一键安装

```bash
# 1. 克隆项目
git clone https://github.com/HKUDS/AI-Trader.git
cd AI-Trader

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置环境变量
cp .env.example .env
# 编辑.env文件并填入您的API密钥
```

### 🔑 环境配置

创建`.env`文件并配置以下变量:

```bash
# 🤖 AI模型API配置
OPENAI_API_BASE=https://your-openai-proxy.com/v1
OPENAI_API_KEY=your_openai_key

# 📊 数据源配置
ALPHAADVANTAGE_API_KEY=your_alpha_vantage_key  # 用于纳斯达克100数据
JINA_API_KEY=your_jina_api_key
TUSHARE_TOKEN=your_tushare_token               # 用于A股数据

# ⚙️ 系统配置
RUNTIME_ENV_PATH=./runtime_env.json # 建议使用绝对路径

# 🌐 服务端口配置
MATH_HTTP_PORT=8000
SEARCH_HTTP_PORT=8001
TRADE_HTTP_PORT=8002
GETPRICE_HTTP_PORT=8003
# 🧠 AI智能体配置
AGENT_MAX_STEP=30             # 最大推理步数
```

### 📦 依赖项

```bash
# 安装生产依赖
pip install -r requirements.txt

# 或手动安装核心依赖
pip install langchain langchain-openai langchain-mcp-adapters fastmcp python-dotenv requests numpy pandas tushare
```

## 🎮 运行指南

### 🚀 使用脚本快速启动

我们在`scripts/`目录中提供了方便的shell脚本以便快速启动:

#### 🇺🇸 美国市场(纳斯达克100)
```bash
# 一键启动(完整工作流)
bash scripts/main.sh

# 或逐步运行:
bash scripts/main_step1.sh  # 步骤1: 准备数据
bash scripts/main_step2.sh  # 步骤2: 启动MCP服务
bash scripts/main_step3.sh  # 步骤3: 运行交易智能体
```

#### 🇨🇳 A股市场(上证50)
```bash
# 逐步运行:
bash scripts/main_a_stock_step1.sh  # 步骤1: 准备A股数据
bash scripts/main_a_stock_step2.sh  # 步骤2: 启动MCP服务
bash scripts/main_a_stock_step3.sh  # 步骤3: 运行A股交易智能体
```

#### ₿ 加密货币市场(BITWISE10)
```bash
# 逐步运行:
bash scripts/main_crypto_step1.sh  # 步骤1: 准备加密货币数据
bash scripts/main_crypto_step2.sh  # 步骤2: 启动MCP服务
bash scripts/main_crypto_step3.sh  # 步骤3: 运行加密货币交易智能体
```

#### 🌐 Web UI
```bash
# 启动Web界面
bash scripts/start_ui.sh
# 访问: http://localhost:8888
```

---

### 📋 手动设置指南

如果您更喜欢手动运行命令,请按照以下步骤操作:

### 📊 步骤1: 数据准备

#### 🇺🇸 纳斯达克100数据

```bash
# 📈 获取纳斯达克100股票数据
cd data
python get_daily_price.py

# 🔄 将数据合并为统一格式
python merge_jsonl.py
```

#### 🇨🇳 A股市场数据(上证50)

```bash
# 📈 获取中国A股市场数据(上证50指数)
cd data/A_stock
python get_daily_price_a_stock.py

# 🔄 转换为JSONL格式(交易所需)
python merge_a_stock_jsonl.py

# 📊 数据将保存到: data/A_stock/merged.jsonl
```


### 🛠️ 步骤2: 启动MCP服务

```bash
cd ./agent_tools
python start_mcp_services.py
```

### 🚀 步骤3: 启动AI竞技场

#### 美股(纳斯达克100):
```bash
# 🎯 使用默认配置运行
python main.py

# 🎯 或指定美股配置
python main.py configs/default_config.json
```

#### A股(上证50):
```bash
# 🎯 运行A股交易
python main.py configs/astock_config.json
```

#### 加密货币(BITWISE10):
```bash
# 🎯 运行加密货币交易
python main.py configs/default_crypto_config.json
```

### ⏰ 时间设置示例

#### 📅 美股配置示例(使用BaseAgent)
```json
{
  "agent_type": "BaseAgent",
  "market": "us",              // 市场类型: "us"表示美股
  "date_range": {
    "init_date": "2024-01-01",  // 回测开始日期
    "end_date": "2024-03-31"     // 回测结束日期
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
    "initial_cash": 10000.0    // 初始资金: $10,000
  }
}
```

#### 📅 A股配置示例(使用BaseAgentAStock)
```json
{
  "agent_type": "BaseAgentAStock",  // A股特定智能体
  "market": "cn",                   // 市场类型: "cn"表示A股(可选,将被忽略,始终使用cn)
  "date_range": {
    "init_date": "2025-10-09",      // 回测开始日期
    "end_date": "2025-10-31"         // 回测结束日期
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
    "initial_cash": 100000.0        // 初始资金: ¥100,000
  }
}
```

> 💡 **提示**: 使用`BaseAgentAStock`时,`market`参数会自动设置为`"cn"`,无需手动指定。

#### 📅 加密货币配置示例(使用BaseAgentCrypto)
```json
{
  "agent_type": "BaseAgentCrypto",  // 加密货币特定智能体
  "market": "crypto",               // 市场类型: "crypto"表示加密货币
  "date_range": {
    "init_date": "2025-10-20",      // 回测开始日期
    "end_date": "2025-10-31"         // 回测结束日期
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
    "initial_cash": 50000.0        // 初始资金: 50,000 USDT
  }
}
```

### 📈 启动Web界面

```bash
cd docs
python3 -m http.server 8000
# 访问 http://localhost:8000
```

## 📈 性能分析

### 🏆 竞赛规则

| 规则项 | 美股 | A股(中国) | 加密货币 |
|-----------|-----------|------------------|------------------|
| **💰 初始资金** | $10,000 | ¥100,000 | 50,000 USDT |
| **📈 交易目标** | 纳斯达克100 | 上证50 | BITWISE10顶级加密货币 |
| **🌍 市场** | 美国股市 | 中国A股市场 | 全球加密市场 |
| **⏰ 交易时间** | 工作日 | 工作日 | 全周 |
| **💲 价格基准** | 开盘价 | 开盘价 | 开盘价 |
| **📝 记录方法** | JSONL格式 | JSONL格式 | JSONL格式 |

## ⚙️ 配置指南

### 📋 配置文件结构

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

### 🔧 配置参数

| 参数 | 描述 | 选项 | 默认值 |
|-----------|-------------|---------|---------------|
| `agent_type` | AI智能体类型 | "BaseAgent"(通用)<br>"BaseAgentAStock"(A股特定) | "BaseAgent" |
| `market` | 市场类型 | "us"(美股)<br>"cn"(A股)<br>"crypto"(加密货币)<br>注意: 使用BaseAgentAStock时自动设置为"cn",使用BaseAgentCrypto时自动设置为"crypto" | "us" |
| `max_steps` | 最大推理步数 | 正整数 | 30 |
| `max_retries` | 最大重试次数 | 正整数 | 3 |
| `base_delay` | 操作延迟(秒) | 浮点数 | 1.0 |
| `initial_cash` | 初始资金 | 浮点数 | $10,000(美股)<br>¥100,000(A股) <br> 50,000-USDT(加密货币) |

#### 📋 智能体类型详情

| 智能体类型 | 适用市场 | 特性 |
|-----------|-------------------|----------|
| **BaseAgent** | 美股 / A股 | • 通用交易智能体<br>• 通过`market`参数切换市场<br>• 灵活的股票池配置 |
| **BaseAgentAStock** | A股特定 | • 针对A股优化<br>• 内置A股交易规则(100股手,T+1)<br>• 默认上证50股票池<br>• 人民币定价 |
| **BaseAgentCrypto** | 加密货币特定 | • 默认BITWISE 10<br>• USDT定价 |

### 📊 数据格式

#### 💰 持仓记录(position.jsonl)
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

#### 📈 价格数据(merged.jsonl)
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

### 📁 文件结构

```
data/agent_data/
├── claude-3.7-sonnet/
│   ├── position/
│   │   └── position.jsonl      # 📝 持仓记录
│   └── log/
│       └── 2025-01-20/
│           └── log.jsonl       # 📊 交易日志
├── gpt-4o/
│   └── ...
└── qwen3-max/
    └── ...
```

## 🔌 第三方策略集成

AI-Trader Bench采用模块化设计,支持轻松集成第三方策略和自定义AI智能体。

### 🛠️ 集成方法

#### 1. 自定义AI智能体
```python
# 创建新的AI智能体类
class CustomAgent(BaseAgent):
    def __init__(self, model_name, **kwargs):
        super().__init__(model_name, **kwargs)
        # 添加自定义逻辑
```

#### 2. 注册新智能体
```python
# 在main.py中注册
AGENT_REGISTRY = {
    "BaseAgent": {
        "module": "agent.base_agent.base_agent",
        "class": "BaseAgent"
    },
    "BaseAgentAStock": {
        "module": "agent.base_agent_astock.base_agent_astock",
        "class": "BaseAgentAStock"
    },
    "CustomAgent": {  # 新的自定义智能体
        "module": "agent.custom.custom_agent",
        "class": "CustomAgent"
    },
}
```

#### 3. 配置文件设置
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

### 🔧 扩展工具链

#### 添加自定义工具
```python
# 创建新的MCP工具
@mcp.tools()
class CustomTool:
    def __init__(self):
        self.name = "custom_tool"

    def execute(self, params):
        # 实现自定义工具逻辑
        return result
```

## 🚀 路线图

### 🌟 未来计划
- [x] **🇨🇳 A股支持** - ✅ 上证50指数数据集成已完成
- [x] **₿ 加密货币** - ✅ BITWISE10数字货币交易支持已完成
- [ ] **📊 盘后统计** - 自动利润分析
- [ ] **🔌 策略市场** - 添加第三方策略共享平台
- [ ] **🎨 酷炫前端界面** - 现代化Web仪表板
- [ ] **📈 更多策略** - 技术分析,量化策略
- [ ] **⏰ 高级回放** - 支持分钟级时间精度和实时回放
- [ ] **🔍 智能过滤** - 更精确的未来信息检测和过滤


## 📞 支持与社区

- **💬 讨论**: [GitHub Discussions](https://github.com/HKUDS/AI-Trader/discussions)
- **🐛 问题**: [GitHub Issues](https://github.com/HKUDS/AI-Trader/issues)

## 📄 许可证

本项目根据[MIT许可证](LICENSE)授权。

## 🙏 致谢

感谢以下开源项目和服务:
- [LangChain](https://github.com/langchain-ai/langchain) - AI应用开发框架
- [MCP](https://github.com/modelcontextprotocol) - 模型上下文协议
- [Alpha Vantage](https://www.alphavantage.co/) - 美股金融数据API
- [Tushare](https://tushare.pro/) - 中国A股市场数据API
- [Jina AI](https://jina.ai/) - 信息搜索服务

## 👥 管理员

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

## 🤝 贡献

<div align="center">
  我们感谢所有贡献者的宝贵贡献。
</div>

<div align="center">
  <a href="https://github.com/HKUDS/AI-Trader/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=HKUDS/AI-Trader" style="border-radius: 15px; box-shadow: 0 0 20px rgba(0, 217, 255, 0.3);" />
  </a>
</div>

## 免责声明

AI-Trader项目提供的材料仅用于研究目的,不构成任何投资建议。投资者在做出任何投资决策之前应寻求独立的专业建议。如有任何过往表现,不应将其作为未来结果的指标。您应注意投资价值可能上涨也可能下跌,并且不保证回报。AI-Trader项目的所有内容仅用于研究目的,不构成投资任何提及的证券或板块的建议。投资有风险。如有需要,请寻求专业建议。

---

<div align="center">

**🌟 如果这个项目对您有帮助,请给我们一个Star!**

[![GitHub stars](https://img.shields.io/github/stars/HKUDS/AI-Trader?style=social)](https://github.com/HKUDS/AI-Trader)
[![GitHub forks](https://img.shields.io/github/forks/HKUDS/AI-Trader?style=social)](https://github.com/HKUDS/AI-Trader)

**🤖 通过完全自主决策体验AI在金融市场的全部潜力!**
**🛠️ 纯工具驱动执行,零人工干预——真正的AI交易竞技场!** 🚀

</div>

---

## ⭐ Star历史

*社区增长轨迹*

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
  <em> ❤️ 感谢访问 ✨ AI-Trader!</em><br><br>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.AI-Trader&style=for-the-badge&color=00d4ff" alt="Views">
</p>
