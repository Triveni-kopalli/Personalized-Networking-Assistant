from transformers import pipeline, set_seed
import logging
import re

logger = logging.getLogger(__name__)

class TopicGenerator:
    def __init__(self):
        logger.info("Loading GPT-2 text generation pipeline...")
        self.generator = pipeline("text-generation", model="gpt2")
        set_seed(42)

    def generate_starters(self, themes: list[str], interests: list[str], num_starters: int = 3) -> list[str]:
        """
        Combine extracted themes + user interests into a prompt template, 
        then use GPT-2 to produce conversation starters.
        """
        interests_str = ", ".join(interests) if interests else "professional networking"
        themes_str = ", ".join(themes) if themes else "various topics"
        
        # Craft a prompt that encourages generating a question or opening sentence
        prompt = (
            f"Event themes: {themes_str}. My interests: {interests_str}. "
            f"A natural, polite, and engaging conversation starter question for a professional at this event: \""
        )

        # Generate multiple sequences
        results = self.generator(
            prompt,
            max_new_tokens=25,
            num_return_sequences=num_starters,
            do_sample=True,
            top_k=50,
            top_p=0.92,
            temperature=0.7,
            pad_token_id=50256, # GPT-2 EOS token
            truncation=True
        )
        
        starters = []
        for res in results:
            generated = res['generated_text'][len(prompt):]
            
            # Post-process output to clean up GPT-2 artifacts
            # Remove any trailing quotes
            cleaned = generated.strip()
            
            # Keep only until the first end-of-sentence punctuation (. ? !)
            match = re.search(r'([.?!])', cleaned)
            if match:
                end_idx = match.start() + 1
                cleaned = cleaned[:end_idx]
            else:
                # If no sentence ending punctuation is found, just add a period at the end
                # but only take a sensible chunk to avoid run-on sentences
                words = cleaned.split()
                if len(words) > 15:
                    cleaned = " ".join(words[:15]) + "..."
                else:
                    cleaned += "."
                    
            # Remove leading quotes or weird characters
            cleaned = re.sub(r'^["\'-]+', '', cleaned).strip()

            if cleaned and cleaned not in starters:
                starters.append(cleaned)
                
        # Fill in generic fallbacks if generation failed to produce enough unique items
        fallbacks = [
            f"How are you finding the event so far?",
            f"What brings you to an event focused on {themes[0] if themes else 'these topics'}?",
            f"Are you currently working on anything related to {interests[0] if interests else 'this field'}?"
        ]
        
        while len(starters) < num_starters:
            starters.append(fallbacks.pop(0))

        return starters[:num_starters]

# Singleton instance to avoid reloading the model
topic_generator = TopicGenerator()
