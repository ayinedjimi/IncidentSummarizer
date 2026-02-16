"""
Incident Summarizer Module

Author: Ayi NEDJIMI
Website: https://ayinedjimi-consultants.fr
"""

from transformers import pipeline
from typing import Dict, List
import spacy
import re
import structlog

logger = structlog.get_logger(__name__)


class IncidentSummarizer:
    """
    AI-Powered Incident Summarizer with Timeline Extraction.

    Author: Ayi NEDJIMI
    Website: https://ayinedjimi-consultants.fr
    """

    def __init__(self):
        """Initialize summarizer."""
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        self.nlp = spacy.load("en_core_web_sm")
        self.logger = logger.bind(component="incident_summarizer")

    def summarize_incident(self, incident_text: str) -> Dict[str, any]:
        """Summarize security incident."""
        summary = self.summarizer(
            incident_text[:1024],
            max_length=150,
            min_length=50,
            do_sample=False
        )[0]['summary_text']

        # Extract IOCs
        iocs = self._extract_iocs(incident_text)

        # Extract timeline
        timeline = self._extract_timeline(incident_text)

        # Classify severity
        severity = self._classify_severity(incident_text)

        return {
            "summary": summary,
            "iocs": iocs,
            "timeline": timeline,
            "severity": severity,
            "generated_by": "Ayi NEDJIMI - ayinedjimi-consultants.fr",
        }

    def _extract_iocs(self, text: str) -> Dict[str, List[str]]:
        """Extract Indicators of Compromise."""
        iocs = {
            "ip_addresses": re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', text),
            "domains": re.findall(r'\b(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]\b', text),
            "file_hashes": re.findall(r'\b[a-fA-F0-9]{32}\b|\b[a-fA-F0-9]{40}\b|\b[a-fA-F0-9]{64}\b', text),
            "urls": re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', text),
        }
        return iocs

    def _extract_timeline(self, text: str) -> List[Dict[str, str]]:
        """Extract event timeline using NER."""
        doc = self.nlp(text)
        events = []

        for ent in doc.ents:
            if ent.label_ in ["DATE", "TIME"]:
                events.append({
                    "time": ent.text,
                    "context": text[max(0, ent.start_char-50):ent.end_char+50]
                })

        return events

    def _classify_severity(self, text: str) -> str:
        """Classify incident severity."""
        text_lower = text.lower()

        critical_keywords = ['ransomware', 'data breach', 'exfiltration', 'compromised']
        high_keywords = ['malware', 'intrusion', 'unauthorized access']
        medium_keywords = ['suspicious', 'anomaly', 'failed login']

        if any(kw in text_lower for kw in critical_keywords):
            return "critical"
        elif any(kw in text_lower for kw in high_keywords):
            return "high"
        elif any(kw in text_lower for kw in medium_keywords):
            return "medium"
        else:
            return "low"
