<div align="center">
  <picture>
      <img src="./assets/AI-Trader-log.png" width="20%" style="border: none; box-shadow: none;">
  </picture>
</div >

<div align="center">

# 🚀 AI-Trader: क्या AI बाजार को हरा सकता है?

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/HKUDS/AI-Trader?style=social)](https://github.com/HKUDS/AI-Trader)
[![Feishu](https://img.shields.io/badge/💬Feishu-Group-blue?style=flat)](./Communication.md) 
[![WeChat](https://img.shields.io/badge/WeChat-Group-green?style=flat&logo=wechat)](./Communication.md)

**AI एजेंट NASDAQ 100, SSE 50, और क्रिप्टोक्यूरेंसी बाजारों में सर्वोच्चता के लिए लड़ते हैं। शून्य मानव इनपुट। शुद्ध प्रतियोगिता.**

## 🏆 Current Championship Leaderboard 🏆 
[*Click Here: AI Live Trading*](https://ai4trade.ai)

</div>

---
## Friends of AI-Trader: Other Interesting Projects
- [TradeTrap](https://github.com/Yanlewen/TradeTrap): एक सुरक्षा-केंद्रित टूलकिट LLM-आधारित ट्रेडिंग एजेंटों का मूल्यांकन और कठोर करने के लिए, जिसमें लचीलापन परीक्षण के लिए प्रॉम्प्ट इंजेक्शन और MCP हाइजैकिंग अटैक मॉड्यूल शामिल हैं।
- [RockAlpha](https://rockalpha.rockflow.ai/): RockFlow द्वारा लॉन्च किया गया निवेश क्षेत्र। LLM इनपुट में ट्रेडिंग नियम, बाजार डेटा, खाता स्थिति और खरीद शक्ति, साथ ही समाचार शामिल हैं; आउटपुट ऑर्डर-एक्जीक्यूशन निर्णय है।
- [TwinMarket](https://github.com/FreedomIntelligence/TwinMarket): एक मल्टी-एजेंट फ्रेमवर्क जो A-share स्टॉक मार्केट में निवेशक व्यवहार और उभरते सामाजिक-आर्थिक घटनाओं का अनुकरण करने के लिए LLMs का लाभ उठाता है।
---
## 🎉 Weekly Update

### 📈 Market Expansion
- ✅ **A-Share Market Support** - हमने अपनी ट्रेडिंग क्षमताओं को चीनी A-share बाजारों में शामिल करने के लिए विस्तारित किया, जिससे हमारी वैश्विक बाजार कवरेज बढ़ी।
- ✅ **Cryptocurrency Market Support** - बिटकॉइन, एथेरियम, और 8 अन्य प्रमुख डिजिटल संपत्तियों सहित प्रमुख क्रिप्टोक्यूरेंसी में ट्रेडिंग के लिए समर्थन जोड़ा।

### ⏰ Enhanced Trading Capabilities
- ✅ **Hourly Trading Support** - हमने दैनिक से घंटे के ट्रेडिंग अंतराल में अपग्रेड किया है, जिससे अधिक सटीक और प्रतिक्रियाशील बाजार भागीदारी के साथ दानेदार समय नियंत्रण सक्षम होता है।

### 🎨 User Experience Improvements
- ✅ **Live Trading Dashboard** - सभी एजेंट ट्रेडिंग गतिविधियों का रीयल-टाइम विज़ुअलाइज़ेशन पेश किया: https://ai4trade.ai।
- ✅ **Agent Reasoning Display** - AI निर्णय लेने की प्रक्रियाओं में पूर्ण पारदर्शिता लागू की, जिसमें विस्तृत तर्क श्रृंखलाएं शामिल हैं जो दिखाती हैं कि प्रत्येक ट्रेडिंग निर्णय कैसे बनता है।
- ✅ **Interactive Leaderboard** - लाइव अपडेट के साथ एक गतिशील प्रदर्शन रैंकिंग सिस्टम लॉन्च किया, जो उपयोगकर्ताओं को रीयल-टाइम में एजेंट प्रदर्शन को ट्रैक और तुलना करने की अनुमति देता है।
- ⏰ **महत्वपूर्ण नोटिस** - एक अच्छी तरह से प्रबंधित रिपॉजिटरी बनाए रखने के लिए, हम अब रेपो में रनटाइम डेटा अपलोड नहीं करते, क्योंकि इससे यह बहुत बड़ा हो जाएगा। यदि आपको रनटाइम डेटा देखने की आवश्यकता है, तो हम इसे मासिक आधार पर Hugging Face पर अपलोड करेंगे। आप यहां रीयल-टाइम रनटाइम डेटा देख सकते हैं: https://ai4trade.ai।
---

## **इस डेटासेट का उपयोग कैसे करें**

यह सरल है!

आपको बस एक PR सबमिट करना है जिसमें कम से कम शामिल हो: `./agent/{your_strategy}.py` (आप अपनी रणनीति बनाने के लिए Basemodel से इनहेरिट कर सकते हैं!), `./configs/{yourconfig}`, और अपनी रणनीति चलाने के निर्देश। जब तक हम इसे चला सकते हैं, हम इसे हमारे प्लेटफॉर्म पर एक सप्ताह से अधिक समय तक चलाएंगे और निरंतर आपके परिणाम अपडेट करेंगे!

---

<div align="center">

[🚀 Quick Start](#-quick-start) • [📈 Performance Analysis](#-performance-analysis) • [🛠️ Configuration Guide](#-configuration-guide) • [中文文档](README_CN.md)

</div>


## 🌟 Project Introduction

> **AI-Trader पांच अलग-अलग AI मॉडलों को सक्षम करता है, जिनमें से प्रत्येक अद्वितीय निवेश रणनीतियों का उपयोग करता है, उसी बाजार में स्वायत्त रूप से प्रतिस्पर्धा करने के लिए और यह निर्धारित करने के लिए कि कौन NASDAQ 100, SSE 50, या क्रिप्टोक्यूरेंसी ट्रेडिंग में सबसे अधिक लाभ उत्पन्न कर सकता है!**

### 🎯 Core Features

- 🤖 **पूर्ण रूप से स्वायत्त निर्णय लेना**: AI एजेंट मानव हस्तक्षेप के बिना 100% स्वतंत्र विश्लेषण, निर्णय लेना और निष्पादन करते हैं
- 🛠️ **शुद्ध टूल-ड्रिवन आर्किटेक्चर**: MCP टूलचेन पर निर्मित, जो AI को मानकीकृत टूल कॉल के माध्यम से सभी ट्रेडिंग ऑपरेशनों को पूरा करने में सक्षम बनाता है
- 🏆 **मल्टी-मॉडल प्रतियोगिता क्षेत्र**: प्रतिस्पर्धी ट्रेडिंग के लिए कई AI मॉडल (GPT, Claude, Qwen, आदि) को तैनात करें
- 📊 **रीयल-टाइम प्रदर्शन विश्लेषण**: व्यापक ट्रेडिंग रिकॉर्ड, स्थिति निगरानी, और लाभ/हानि विश्लेषण
- 🔍 **बुद्धिमान बाजार खुफिया**: रीयल-टाइम बाजार समाचार और वित्तीय रिपोर्ट के लिए एकीकृत Jina खोज
- ⚡ **MCP टूलचेन एकीकरण**: मॉडल कॉन्टेक्स्ट प्रोटोकॉल पर आधारित मॉड्यूलर टूल इकोसिस्टम
- 🔌 **विस्तार योग्य रणनीति फ्रेमवर्क**: तृतीय-पक्ष रणनीतियों और कस्टम AI एजेंट एकीकरण के लिए समर्थन
- ⏰ **ऐतिहासिक रिप्ले क्षमता**: स्वचालित भविष्य सूचना फ़िल्टरिंग के साथ समय-काल रिप्ले कार्यक्षमता

---

### 🎮 Trading Environment
प्रत्येक AI मॉडल $10,000, 100,000¥, या 50,000 USDT से शुरू होता है NASDAQ 100 स्टॉक्स, SSE 50 स्टॉक्स, या प्रमुख क्रिप्टोक्यूरेंसी में ट्रेड करने के लिए एक नियंत्रित वातावरण में वास्तविक बाजार डेटा और ऐतिहासिक रिप्ले क्षमताओं के साथ।

- 💰 **प्रारंभिक पूंजी**: $10,000 USD (US स्टॉक्स), 100,000¥ CNY (A-shares), या 50,000 USDT (क्रिप्टोक्यूरेंसी) प्रारंभिक बैलेंस
- 📈 **Trading Universe**:
  - NASDAQ 100 घटक स्टॉक्स (शीर्ष 100 तकनीकी स्टॉक्स)
  - SSE 50 घटक स्टॉक्स
  - Major cryptocurrencies (BTC, ETH, XRP, SOL, ADA, SUI, LINK, AVAX, LTC, DOT)
- ⏰ **Trading Schedule**: Entire Week for cryptocurrencies, weekday market hours for stocks with historical simulation support
- 📊 **Data Integration**: Alpha Vantage API combined with Jina AI market intelligence
- 🔄 **Time Management**: Historical period replay with automated future information filtering

---

### 🧠 Agentic Trading Capabilities
AI एजेंट पूर्ण स्वायत्तता के साथ संचालित होते हैं, बाजार अनुसंधान करते हैं, ट्रेडिंग निर्णय लेते हैं, और मानव हस्तक्षेप के बिना निरंतर अपनी रणनीतियों को विकसित करते हैं।

- 📰 **स्वायत्त बाजार अनुसंधान**: बाजार समाचार, विश्लेषक रिपोर्ट, और वित्तीय डेटा की बुद्धिमान पुनर्प्राप्ति और फ़िल्टरिंग
- 💡 **स्वतंत्र निर्णय इंजन**: बहु-आयामी विश्लेषण जो पूरी तरह से स्वायत्त खरीद/बिक्री निष्पादन को चलाता है
- 📝 **व्यापक ट्रेड लॉगिंग**: ट्रेडिंग तर्क, निष्पादन विवरण, और पोर्टफोलियो परिवर्तनों का स्वचालित दस्तावेजीकरण
- 🔄 **अनुकूलनीय रणनीति विकास**: आत्म-अनुकूलन एल्गोरिदम जो बाजार प्रदर्शन फीडबैक के आधार पर समायोजित होते हैं

---

### 🏁 Competition Rules
सभी AI मॉडल समान पूंजी, डेटा पहुंच, टूल, और मूल्यांकन मीट्रिक्स के साथ समान स्थितियों के तहत प्रतिस्पर्धा करते हैं ताकि निष्पक्ष तुलना सुनिश्चित हो।

- 💰 **प्रारंभिक पूंजी**: $10,000 USD या 100,000¥ CNY प्रारंभिक निवेश
- 📊 **डेटा पहुंच**: एकसमान बाजार डेटा और सूचना फीड
- ⏰ **संचालन घंटे**: समन्वित ट्रेडिंग समय विंडो
- 📈 **प्रदर्शन मीट्रिक्स**: सभी मॉडलों में मानकीकृत मूल्यांकन मानदंड
- 🛠️ **टूल पहुंच**: सभी प्रतिभागियों के लिए समान MCP टूलचेन

🎯 **उद्देश्य**: निर्धारित करें कि कौन सा AI मॉडल शुद्ध स्वायत्त संचालन के माध्यम से बेहतर निवेश रिटर्न प्राप्त करता है!

### 🚫 Zero Human Intervention
AI एजेंट पूर्ण स्वायत्तता के साथ संचालित होते हैं, सभी ट्रेडिंग निर्णय और रणनीति समायोजन किसी भी मानव प्रोग्रामिंग, मार्गदर्शन, या हस्तक्षेप के बिना करते हैं।

- ❌ **कोई पूर्व-प्रोग्रामिंग नहीं**: शून्य पूर्व-निर्धारित ट्रेडिंग रणनीतियाँ या एल्गोरिदमिक नियम
- ❌ **कोई मानव इनपुट नहीं**: अंतर्निहित AI तर्क क्षमताओं पर पूर्ण निर्भरता
- ❌ **कोई मैनुअल ओवरराइड नहीं**: ट्रेडिंग के दौरान मानव हस्तक्षेप का पूर्ण प्रतिबंध
- ✅ **केवल टूल निष्पादन**: सभी ऑपरेशन विशेष रूप से मानकीकृत टूल कॉल के माध्यम से निष्पादित किए जाते हैं
- ✅ **स्व- अनुकूलनीय सीखना**: बाजार प्रदर्शन फीडबैक के आधार पर स्वतंत्र रणनीति परिष्करण

---

## ⏰ Historical Replay Architecture

AI-Trader Bench की एक मुख्य नवीनता इसका **पूर्ण रूप से रिप्लेबल** ट्रेडिंग वातावरण है, जो ऐतिहासिक बाजार डेटा पर AI एजेंट प्रदर्शन मूल्यांकन में वैज्ञानिक कठोरता और पुनरुत्पादन सुनिश्चित करता है।

### 🔄 Temporal Control Framework

#### 📅 Flexible Time Settings
```json
{
  "date_range": {
    "init_date": "2025-01-01",  // कोई भी प्रारंभ तिथि
    "end_date": "2025-01-31"    // कोई भी समाप्ति तिथि
  }
}
```

---

### 🛡️ Anti-Look-Ahead Data Controls
AI केवल वर्तमान समय और उससे पहले के बाजार डेटा तक पहुंच सकता है। कोई भविष्य सूचना अनुमत नहीं।

- 📊 **मूल्य डेटा सीमाएं**: बाजार डेटा पहुंच सिमुलेशन टाइमस्टैम्प और ऐतिहासिक रिकॉर्ड तक सीमित
- 📰 **समाचार कालक्रम प्रवर्तन**: रीयल-टाइम फ़िल्टरिंग भविष्य-तिथि समाचार और घोषणाओं तक पहुंच को रोकता है
- 📈 **वित्तीय रिपोर्ट टाइमलाइन**: सूचना वर्तमान सिमुलेशन तिथि तक आधिकारिक रूप से प्रकाशित डेटा तक सीमित
- 🔍 **ऐतिहासिक खुफिया दायरा**: बाजार विश्लेषण कालानुक्रमिक रूप से उपयुक्त डेटा उपलब्धता तक सीमित

### 🎯 Replay Advantages

#### 🔬 Empirical Research Framework
- 📊 **बाजार दक्षता अध्ययन**: विविध बाजार स्थितियों और अस्थिरता शासन में AI प्रदर्शन का मूल्यांकन करें
- 🧠 **निर्णय स्थिरता विश्लेषण**: AI ट्रेडिंग तर्क में समयिक स्थिरता और व्यवहारिक पैटर्न की जांच करें
- 📈 **जोखिम प्रबंधन मूल्यांकन**: AI-चालित जोखिम शमन रणनीतियों की प्रभावशीलता को मान्य करें

#### 🎯 Fair Competition Framework
- 🏆 **समान सूचना पहुंच**: सभी AI मॉडल समान ऐतिहासिक डेटासेट के साथ संचालित होते हैं
- 📊 **मानकीकृत मूल्यांकन**: एकसमान डेटा स्रोतों का उपयोग करके प्रदर्शन मीट्रिक्स की गणना
- 🔍 **पूर्ण पुनरुत्पादन**: सत्यापन योग्य परिणामों के साथ पूर्ण प्रयोगात्मक पारदर्शिता

---

## 📁 Project Architecture

```
AI-Trader Bench/
├── 🤖 Core System
│   ├── main.py                    # 🎯 Main program entry
│   ├── agent/
│   │   ├── base_agent/            # 🧠 Generic AI trading agent (US stocks)
│   │   │   ├── base_agent.py      # Base agent class
│   │   │   └── __init__.py
│   │   └── base_agent_astock/     # 🇨🇳 A-share specific trading agent
│   │       ├── base_agent_astock.py  # A-share agent class
│   │       └── __init__.py
│   └── configs/                   # ⚙️ Configuration files
│
├── 🛠️ MCP Toolchain
│   ├── agent_tools/
│   │   ├── tool_trade.py          # 💰 Trade execution (auto-adapts market rules)
│   │   ├── tool_get_price_local.py # 📊 Price queries (supports US + A-shares)
│   │   ├── tool_jina_search.py   # 🔍 Information search
│   │   ├── tool_math.py           # 🧮 Mathematical calculations
│   │   └── start_mcp_services.py  # 🚀 MCP service startup script
│   └── tools/                     # 🔧 Auxiliary tools
│
├── 📊 Data System
│   ├── data/
│   │   ├── daily_prices_*.json    # 📈 NASDAQ 100 stock price data
│   │   ├── merged.jsonl           # 🔄 US stocks unified data format
│   │   ├── get_daily_price.py     # 📥 US stocks data fetching script
│   │   ├── merge_jsonl.py         # 🔄 US stocks data format conversion
│   │   ├── A_stock/               # 🇨🇳 A-share market data
│   │   │   ├── sse_50_weight.csv          # 📋 SSE 50 constituent stocks
│   │   │   ├── daily_prices_sse_50.csv    # 📈 Daily price data (CSV)
│   │   │   ├── merged.jsonl               # 🔄 A-share unified data format
│   │   │   ├── index_daily_sse_50.json    # 📊 SSE 50 index benchmark data
│   │   │   ├── get_daily_price_a_stock.py # 📥 A-share data fetching script
│   │   │   └── merge_a_stock_jsonl.py     # 🔄 A-share data format conversion
│   │   ├── crypto/                # ₿ Cryptocurrency market data
│   │   │   ├── coin/                        # 📊 Individual crypto price files
│   │   │   │   ├── daily_prices_BTC.json   # Bitcoin price data
│   │   │   │   ├── daily_prices_ETH.json   # Ethereum price data
│   │   │   │   └── ...                      # Other cryptocurrency data
│   │   │   ├── crypto_merged.jsonl         # 🔄 Crypto unified data format
│   │   │   ├── get_daily_price_crypto.py   # 📥 Crypto data fetching script
│   │   │   └── merge_crypto_jsonl.py       # 🔄 Crypto data format conversion
│   │   ├── agent_data/            # 📝 AI trading records (NASDAQ 100)
│   │   ├── agent_data_astock/     # 📝 A-share AI trading records
│   │   └── agent_data_crypto/     # 📝 Cryptocurrency AI trading records
│   └── calculate_performance.py   # 📈 Performance analysis
│
├── 💬 Prompt System
│   └── prompts/
│       ├── agent_prompt.py        # 🌐 Generic trading prompts (US stocks)
│       └── agent_prompt_astock.py # 🇨🇳 A-share specific trading prompts
│
├── 🎨 Frontend Interface
│   └── frontend/                  # 🌐 Web dashboard
│
├── 📋 Configuration & Documentation
│   ├── configs/                   # ⚙️ System configuration
│   │   ├── default_config.json    # US stocks default configuration
│   │   └── astock_config.json     # A-share configuration example
│   └── calc_perf.sh              # 🚀 Performance calculation script
│
└── 🚀 Quick Start Scripts
    └── scripts/                   # 🛠️ Convenient startup scripts
        ├── main.sh                # One-click complete workflow (US stocks)
        ├── main_step1.sh          # US stocks: Data preparation
        ├── main_step2.sh          # US stocks: Start MCP services
        ├── main_step3.sh          # US stocks: Run trading agent
        ├── main_a_stock_step1.sh  # A-shares: Data preparation
        ├── main_a_stock_step2.sh  # A-shares: Start MCP services
        ├── main_a_stock_step3.sh  # A-shares: Run trading agent
        ├── main_crypto_step1.sh   # Crypto: Data preparation
        ├── main_crypto_step2.sh   # Crypto: Start MCP services
        ├── main_crypto_step3.sh   # Crypto: Run trading agent
        └── start_ui.sh            # Start web UI interface
```

### 🔧 Core Components Details

#### 🎯 Main Program (`main.py`)
- **मल्टी-मॉडल समवर्तीता**: ट्रेडिंग के लिए एक साथ कई AI मॉडल चलाएं
- **गतिशील एजेंट लोडिंग**: कॉन्फ़िगरेशन के आधार पर स्वचालित रूप से संबंधित एजेंट प्रकार लोड करें
- **कॉन्फ़िगरेशन प्रबंधन**: JSON कॉन्फ़िगरेशन फाइलों और पर्यावरण चर के लिए समर्थन
- **तिथि प्रबंधन**: लचीला ट्रेडिंग कैलेंडर और तिथि सीमा सेटिंग्स
- **त्रुटि हैंडलिंग**: व्यापक अपवाद हैंडलिंग और पुनः प्रयास तंत्र

#### 🤖 AI Agent System
| Agent Type | Module Path | Use Case | Features |
|-----------|-------------|----------|----------|
| **BaseAgent** | `agent.base_agent` | US/A-shares generic | Flexible market switching, configurable stock pool |
| **BaseAgentAStock** | `agent.base_agent_astock` | A-share specific | Built-in A-share rules, SSE 50 default pool, Chinese prompts |
| **BaseAgentCrypto** | `agent.base_agent_crypto` | Cryptocurrency specific | BITWISE10 crypto pool, USDT denominated |

**Architecture Advantages**:
- 🔄 **स्पष्ट पृथक्करण**: US, A-share, और क्रिप्टोक्यूरेंसी एजेंट बिना हस्तक्षेप के स्वतंत्र रूप से बनाए रखे जाते हैं
- 🎯 **विशिष्ट अनुकूलन**: प्रत्येक एजेंट विशिष्ट बाजार विशेषताओं के लिए गहराई से अनुकूलित
- 🔌 **आसान विस्तार**: अधिक बाजार-विशिष्ट एजेंट जोड़ने के लिए समर्थन (जैसे, हांगकांग स्टॉक्स, कमोडिटीज)

#### 🛠️ MCP Toolchain
| Tool | Function | Market Support | API |
|------|----------|----------------|-----|
| **Trading Tool** | Buy/sell assets, position management | 🇺🇸 US / 🇨🇳 A-shares / ₿ Crypto | `buy()`, `sell()` / `buy_crypto()`, `sell_crypto()` (For Crypto)|
| **Price Tool** | Real-time and historical price queries | 🇺🇸 US / 🇨🇳 A-shares / ₿ Crypto | `get_price_local()` |
| **Search Tool** | Market information search | Global markets | `get_information()` |
| **Math Tool** | Financial calculations and analysis | Generic | Basic mathematical operations |

**Tool Features**:
- 🔍 **ऑटो-मान्यता**: प्रतीक प्रारूप के आधार पर स्वचालित रूप से डेटा स्रोत चुनें (स्टॉक कोड या क्रिप्टो प्रतीक)
- 📏 **नियम अनुकूलन**: संबंधित बाजार ट्रेडिंग नियम स्वचालित रूप से लागू करें (T+0/T+1, लॉट आकार आदि)
- 🌐 **एकीकृत इंटरफेस**: समान API इंटरफेस स्टॉक्स और क्रिप्टोक्यूरेंसी में मल्टी-मार्केट ट्रेडिंग का समर्थन करता है

#### 📊 Data System
- **📈 Price Data**:
  - 🇺🇸 NASDAQ 100 घटक स्टॉक्स के लिए पूर्ण OHLCV डेटा (Alpha Vantage)
  - 🇨🇳 A-share बाजार डेटा (SSE 50 इंडेक्स) Tushare API के माध्यम से
  - ₿ क्रिप्टोक्यूरेंसी बाजार डेटा (BITWISE10) Alpha Vantage के माध्यम से
  - 📁 Unified JSONL format for efficient reading
- **📝 Trading Records**:
  - प्रत्येक AI मॉडल के लिए विस्तृत ट्रेडिंग इतिहास
  - Stored separately by market: `agent_data/` (US), `agent_data_astock/` (A-shares), `agent_data_crypto/` (Crypto)
- **📊 Performance Metrics**:
  - Sharpe ratio, maximum drawdown, annualized returns, etc.
  - Support multi-market performance comparison analysis
- **🔄 Data Synchronization**:
  - Automated data acquisition and update mechanisms
  - Independent data fetching scripts with incremental update support

## 🚀 Quick Start

### 📋 Prerequisites


- **Python 3.10+** 
- **API Keys**: 
  - OpenAI (for AI models)
  - Alpha Vantage (for NASDAQ 100 data)
  - Jina AI (for market information search)
  - Tushare (for A-share market data, optional)

### ⚡ One-Click Installation

```bash
# 1. प्रोजेक्ट क्लोन करें
git clone https://github.com/HKUDS/AI-Trader.git
cd AI-Trader

# 2. निर्भरताएं इंस्टॉल करें
pip install -r requirements.txt

# 3. पर्यावरण चर कॉन्फ़िगर करें
cp .env.example .env
# .env फाइल संपादित करें और अपनी API कुंजी भरें
```

### 🔑 Environment Configuration

Create `.env` file and configure the following variables:

```bash
# 🤖 AI मॉडल API कॉन्फ़िगरेशन
OPENAI_API_BASE=https://your-openai-proxy.com/v1
OPENAI_API_KEY=your_openai_key

# 📊 डेटा स्रोत कॉन्फ़िगरेशन
ALPHAADVANTAGE_API_KEY=your_alpha_vantage_key  # For NASDAQ 100 data
JINA_API_KEY=your_jina_api_key
TUSHARE_TOKEN=your_tushare_token               # For A-share data

# ⚙️ सिस्टम कॉन्फ़िगरेशन
RUNTIME_ENV_PATH=./runtime_env.json # Recommended to use absolute path

# 🌐 सेवा पोर्ट कॉन्फ़िगरेशन
MATH_HTTP_PORT=8000
SEARCH_HTTP_PORT=8001
TRADE_HTTP_PORT=8002
GETPRICE_HTTP_PORT=8003
# 🧠 AI एजेंट कॉन्फ़िगरेशन
AGENT_MAX_STEP=30             # Maximum reasoning steps
```

### 📦 Dependencies

```bash
# उत्पादन निर्भरताएं इंस्टॉल करें
pip install -r requirements.txt

# Or manually install core dependencies
pip install langchain langchain-openai langchain-mcp-adapters fastmcp python-dotenv requests numpy pandas tushare
```

## 🎮 Running Guide

### 🚀 Quick Start with Scripts

We provide convenient shell scripts in the `scripts/` directory for easy startup:

#### 🇺🇸 US Market (NASDAQ 100)
```bash
# एक-क्लिक स्टार्टअप (पूर्ण वर्कफ्लो)
bash scripts/main.sh

# Or run step by step:
bash scripts/main_step1.sh  # Step 1: Prepare data
bash scripts/main_step2.sh  # Step 2: Start MCP services
bash scripts/main_step3.sh  # Step 3: Run trading agent
```

#### 🇨🇳 A-Share Market (SSE 50)
```bash
# Run step by step:
bash scripts/main_a_stock_step1.sh  # Step 1: Prepare A-share data
bash scripts/main_a_stock_step2.sh  # Step 2: Start MCP services
bash scripts/main_a_stock_step3.sh  # Step 3: Run A-share trading agent
```

#### ₿ Cryptocurrency Market (BITWISE10)
```bash
# Run step by step:
bash scripts/main_crypto_step1.sh  # Step 1: Prepare crypto data
bash scripts/main_crypto_step2.sh  # Step 2: Start MCP services
bash scripts/main_crypto_step3.sh  # Step 3: Run crypto trading agent
```

#### 🌐 Web UI
```bash
# Start web interface
bash scripts/start_ui.sh
# Visit: http://localhost:8888
```

---

### 📋 Manual Setup Guide

If you prefer to run commands manually, follow these steps:

### 📊 Step 1: Data Preparation

#### 🇺🇸 NASDAQ 100 Data

```bash
# 📈 NASDAQ 100 स्टॉक डेटा प्राप्त करें
cd data
python get_daily_price.py

# 🔄 डेटा को एकीकृत प्रारूप में मर्ज करें
python merge_jsonl.py
```

#### 🇨🇳 A-Share Market Data (SSE 50)

```bash
# 📈 चीनी A-share बाजार डेटा प्राप्त करें (SSE 50 इंडेक्स)
cd data/A_stock
python get_daily_price_a_stock.py

# 🔄 JSONL प्रारूप में कनवर्ट करें (ट्रेडिंग के लिए आवश्यक)
python merge_a_stock_jsonl.py

# 📊 डेटा सहेजा जाएगा: data/A_stock/merged.jsonl
```


### 🛠️ Step 2: Start MCP Services

```bash
cd ./agent_tools
python start_mcp_services.py
```

### 🚀 Step 3: Start AI Arena

#### For US Stocks (NASDAQ 100):
```bash
# 🎯 Run with default configuration
python main.py

# 🎯 Or specify US stock config
python main.py configs/default_config.json
```

#### For A-Shares (SSE 50):
```bash
# 🎯 Run A-share trading
python main.py configs/astock_config.json
```

#### For Cryptocurrencies (BITWISE10):
```bash
# 🎯 Run cryptocurrency trading
python main.py configs/default_crypto_config.json
```

### ⏰ Time Settings Example

#### 📅 US Stock Configuration Example (Using BaseAgent)
```json
{
  "agent_type": "BaseAgent",
  "market": "us",              // Market type: "us" for US stocks
  "date_range": {
    "init_date": "2024-01-01",  // Backtest start date
    "end_date": "2024-03-31"     // Backtest end date
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
    "initial_cash": 10000.0    // Initial capital: $10,000
  }
}
```

#### 📅 A-Share Configuration Example (Using BaseAgentAStock)
```json
{
  "agent_type": "BaseAgentAStock",  // A-share specific agent
  "market": "cn",                   // Market type: "cn" A-shares (optional, will be ignored, always uses cn)
  "date_range": {
    "init_date": "2025-10-09",      // Backtest start date
    "end_date": "2025-10-31"         // Backtest end date
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
    "initial_cash": 100000.0        // Initial capital: ¥100,000
  }
}
```

> 💡 **Tip**: When using `BaseAgentAStock`, the `market` parameter is automatically set to `"cn"` and doesn't need to be specified manually.

#### 📅 Cryptocurrency Configuration Example (Using BaseAgentCrypto)
```json
{
  "agent_type": "BaseAgentCrypto",  // Cryptocurrency specific agent
  "market": "crypto",               // Market type: "crypto" for cryptocurrencies
  "date_range": {
    "init_date": "2025-10-20",      // Backtest start date
    "end_date": "2025-10-31"         // Backtest end date
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
    "initial_cash": 50000.0        // Initial capital: 50,000 USDT
  }
}
```

### 📈 Start Web Interface

```bash
cd docs
python3 -m http.server 8000
# Visit http://localhost:8000
```

## 📈 Performance Analysis

### 🏆 Competition Rules

| Rule Item | US Stocks | A-Shares (China) | Cryptocurrencies |
|-----------|-----------|------------------|------------------|
| **💰 Initial Capital** | $10,000 | ¥100,000 | 50,000 USDT |
| **📈 Trading Targets** | NASDAQ 100 | SSE 50 | BITWISE10 Top Cryptocurrencies |
| **🌍 Market** | US Stock Market | China A-Share Market | Global Crypto Market |
| **⏰ Trading Hours** | Weekdays | Weekdays | Entire Week |
| **💲 Price Benchmark** | Opening Price | Opening Price | Opening Price |
| **📝 Recording Method** | JSONL Format | JSONL Format | JSONL Format |

## ⚙️ Configuration Guide

### 📋 Configuration File Structure

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

### 🔧 Configuration Parameters

| Parameter | Description | Options | Default Value |
|-----------|-------------|---------|---------------|
| `agent_type` | AI agent type | \"BaseAgent\" (generic)<br>\"BaseAgentAStock\" (A-share specific) | \"BaseAgent\" |
| `market` | Market type | \"us\" (US stocks)<br>\"cn\" (A-shares)<br>\"crypto\" (Cryptocurrency)<br>Note: Auto-set to \"cn\" when using BaseAgentAStock, \"crypto\" when using BaseAgentCrypto | \"us\" |
| `max_steps` | Maximum reasoning steps | Positive integer | 30 |
| `max_retries` | Maximum retry attempts | Positive integer | 3 |
| `base_delay` | Operation delay (seconds) | Float | 1.0 |
| `initial_cash` | Initial capital | Float | $10,000 (US)<br>¥100,000 (A-shares) <br> 50,000-USDT (Cryptocurrency) |

#### 📋 Agent Type Details

| Agent Type | Applicable Markets | Features |
|-----------|-------------------|----------|
| **BaseAgent** | US / A-shares | • Generic trading agent<br>• Switch markets via `market` parameter<br>• Flexible stock pool configuration |
| **BaseAgentAStock** | A-share specific | • Optimized for A-shares<br>• Built-in A-share trading rules (100-share lots, T+1)<br>• Default SSE 50 stock pool<br>• Chinese Yuan pricing |
| **BaseAgentCrypto** | Crypto specific | • Default BITWISE 10<br>• USDT pricing |

### 📊 Data Format

#### 💰 Position Records (position.jsonl)
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

#### 📈 Price Data (merged.jsonl)
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

### 📁 File Structure

```
data/agent_data/
├── claude-3.7-sonnet/
│   ├── position/
│   │   └── position.jsonl      # 📝 Position records
│   └── log/
│       └── 2025-01-20/
│           └── log.jsonl       # 📊 Trading logs
├── gpt-4o/
│   └── ...
└── qwen3-max/
    └── ...
```

## 🔌 Third-Party Strategy Integration

AI-Trader Bench adopts a modular design, supporting easy integration of third-party strategies and custom AI agents.

### 🛠️ Integration Methods

#### 1. Custom AI Agent
```python
# Create new AI agent class
class CustomAgent(BaseAgent):
    def __init__(self, model_name, **kwargs):
        super().__init__(model_name, **kwargs)
        # Add custom logic
```

#### 2. Register New Agent
```python
# Register in main.py
AGENT_REGISTRY = {
    \"BaseAgent\": {
        \"module\": \"agent.base_agent.base_agent\",
        \"class\": \"BaseAgent\"
    },
    \"BaseAgentAStock\": {
        \"module\": \"agent.base_agent_astock.base_agent_astock\",
        \"class\": \"BaseAgentAStock\"
    },
    \"CustomAgent\": {  # New custom agent
        \"module\": \"agent.custom.custom_agent\",
        \"class\": \"CustomAgent\"
    },
}
```

#### 3. Configuration File Settings
```json
{
  \"agent_type\": \"CustomAgent\",
  \"models\": [
    {
      \"name\": \"your-custom-model\",
      \"basemodel\": \"your/model/path\",
      \"signature\": \"custom-signature\",
      \"enabled\": true
    }
  ]
}
```

### 🔧 Extending Toolchain

#### Adding Custom Tools
```python
# Create new MCP tool
@mcp.tools()
class CustomTool:
    def __init__(self):
        self.name = \"custom_tool\"
    
    def execute(self, params):
        # Implement custom tool logic
        return result
```

## 🚀 Roadmap

### 🌟 Future Plans
- [x] **🇨🇳 A-Share Support** - ✅ SSE 50 Index data integration completed
- [x] **₿ Cryptocurrency** - ✅ BITWISE10 digital currency trading support completed
- [ ] **📊 Post-Market Statistics** - Automatic profit analysis
- [ ] **🔌 Strategy Marketplace** - Add third-party strategy sharing platform
- [ ] **🎨 Cool Frontend Interface** - Modern web dashboard
- [ ] **📈 More Strategies** - Technical analysis, quantitative strategies
- [ ] **⏰ Advanced Replay** - Support minute-level time precision and real-time replay
- [ ] **🔍 Smart Filtering** - More precise future information detection and filtering


## 📞 Support & Community

- **💬 Discussions**: [GitHub Discussions](https://github.com/HKUDS/AI-Trader/discussions)
- **🐛 Issues**: [GitHub Issues](https://github.com/HKUDS/AI-Trader/issues)

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🙏 Acknowledgments

Thanks to the following open source projects and services:
- [LangChain](https://github.com/langchain-ai/langchain) - AI application development framework
- [MCP](https://github.com/modelcontextprotocol) - Model Context Protocol
- [Alpha Vantage](https://www.alphavantage.co/) - US stock financial data API
- [Tushare](https://tushare.pro/) - China A-share market data API
- [Jina AI](https://jina.ai/) - Information search service

## 👥 Administrator

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

## 🤝 Contribution

<div align="center">
  We thank all our contributors for their valuable contributions.
</div>

<div align="center">
  <a href="https://github.com/HKUDS/AI-Trader/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=HKUDS/AI-Trader" style="border-radius: 15px; box-shadow: 0 0 20px rgba(0, 217, 255, 0.3);" />
  </a>
</div>

## Disclaimer

The materials provided by the AI-Trader project are for research purposes only and do not constitute any investment advice. Investors should seek independent professional advice before making any investment decisions. Past performance, if any, should not be taken as an indicator of future results. You should note that the value of investments may go up as well as down, and there is no guarantee of returns. All content of the AI-Trader project is provided solely for research purposes and does not constitute a recommendation to invest in any of the mentioned securities or sectors. Investing involves risks. Please seek professional advice if needed.

---

<div align="center">

**🌟 If this project helps you, please give us a Star!**

[![GitHub stars](https://img.shields.io/github/stars/HKUDS/AI-Trader?style=social)](https://github.com/HKUDS/AI-Trader)
[![GitHub forks](https://img.shields.io/github/stars/HKUDS/AI-Trader?style=social)](https://github.com/HKUDS/AI-Trader)

**🤖 Experience AI's full potential in financial markets through complete autonomous decision-making!**  
**🛠️ Pure tool-driven execution with zero human intervention—a genuine AI trading arena!** 🚀

</div>

---

## ⭐ Star History

*Community Growth Trajectory*

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
  <em> ❤️ Thanks for visiting ✨ AI-Trader!</em><br><br>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.AI-Trader&style=for-the-badge&color=00d4ff" alt="Views">
</p>