from transformers import pipeline
import logging

logger = logging.getLogger(__name__)

class EventAnalyzer:
    def __init__(self):
        logger.info("Loading DistilBERT zero-shot-classification pipeline...")
        # Using a distilbert-based model for zero-shot classification as requested
        self.classifier = pipeline(
            "zero-shot-classification", 
            model="typeform/distilbert-base-uncased-mnli"
        )
        # Default broad candidate themes
        self.candidate_labels = [
            "AI & Machine Learning",
            "Sustainability & Environment",
            "Healthcare & Biotech",
            "Finance & FinTech",
            "Marketing & Sales",
            "Entrepreneurship & Startups",
            "Technology & Software",
            "Leadership & Management",
            "Education & EdTech",
            "Arts & Entertainment"
        ]

    def analyze(self, text: str, top_k: int = 3) -> list[str]:
        """
        Analyzes the event description and extracts key themes.
        Returns a list of strings representing the top themes.
        """
        if not text.strip():
            return []

        result = self.classifier(text, self.candidate_labels, multi_label=True)
        
        labels = result['labels']
        # Return the top_k themes
        top_themes = labels[:top_k]
        return top_themes

# Singleton instance to avoid reloading the model
event_analyzer = EventAnalyzer()
