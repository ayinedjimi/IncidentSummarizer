# IncidentSummarizer 🚨

**AI-Powered Security Incident Summarizer**

Author: **Ayi NEDJIMI**
Website: [ayinedjimi-consultants.fr](https://ayinedjimi-consultants.fr)

## Features
- BART-based incident summarization
- IOC extraction (IPs, domains, hashes, URLs)
- Timeline extraction with NER
- Automatic severity classification

## Usage
```python
from incidentsummarizer import IncidentSummarizer

summarizer = IncidentSummarizer()
result = summarizer.summarize_incident(incident_text)

print(result['summary'])
print(result['iocs'])
print(result['severity'])
```

## License
MIT - Copyright (c) 2024 Ayi NEDJIMI

---
Made with ❤️ by Ayi NEDJIMI | [ayinedjimi-consultants.fr](https://ayinedjimi-consultants.fr)
