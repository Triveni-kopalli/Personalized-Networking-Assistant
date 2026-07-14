import wikipedia
from pydantic import BaseModel
import logging

logger = logging.getLogger(__name__)

class FactCheckResult(BaseModel):
    summary: str
    source_url: str | None = None
    error: str | None = None

def get_fact_check(query: str) -> FactCheckResult:
    """
    Search Wikipedia for the query and return a short summary (2-3 sentences)
    along with the source URL. Handles errors gracefully.
    """
    try:
        # Search for the most relevant page
        search_results = wikipedia.search(query, results=1)
        if not search_results:
            return FactCheckResult(
                summary="No relevant information found for this query.",
                error="Page not found"
            )
        
        page_title = search_results[0]
        
        # Get the page summary (2-3 sentences)
        page = wikipedia.page(title=page_title, auto_suggest=False)
        summary = wikipedia.summary(title=page_title, sentences=3, auto_suggest=False)
        
        return FactCheckResult(
            summary=summary,
            source_url=page.url
        )
        
    except wikipedia.exceptions.DisambiguationError as e:
        logger.warning(f"Disambiguation error for query '{query}': {e.options}")
        return FactCheckResult(
            summary=f"The topic '{query}' is too broad. It could refer to: {', '.join(e.options[:3])}...",
            error="Disambiguation error"
        )
    except wikipedia.exceptions.PageError:
        logger.warning(f"Page not found for query '{query}'")
        return FactCheckResult(
            summary="Sorry, no Wikipedia page was found for this query.",
            error="Page not found"
        )
    except Exception as e:
        logger.error(f"Unexpected error during fact check: {e}")
        return FactCheckResult(
            summary="An unexpected error occurred while fact-checking.",
            error=str(e)
        )
