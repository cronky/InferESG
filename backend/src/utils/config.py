import os
from dotenv import load_dotenv

default_frontend_url = "http://localhost:8650"
default_neo4j_uri = "bolt://localhost:7687"
default_redis_host = "localhost"


class Config(object):
    def __init__(self):
        self.frontend_url = default_frontend_url
        self.mistral_url = None
        self.mistral_key = None
        self.mistral_model = None
        self.openai_key = None
        self.neo4j_uri = default_neo4j_uri
        self.neo4j_user = None
        self.neo4j_password = None
        self.answer_agent_llm = None
        self.intent_agent_llm = None
        self.report_agent_llm = None
        self.materiality_agent_llm = None
        self.validator_agent_llm = None
        self.datastore_agent_llm = None
        self.web_agent_llm = None
        self.chart_generator_llm = None
        self.router_llm = None
        self.suggestions_llm = None
        self.dynamic_knowledge_graph_llm = None
        self.ollama_url = None
        self.validator_agent_model = None
        self.intent_agent_model = None
        self.answer_agent_model = None
        self.report_agent_model = None
        self.materiality_agent_model = None
        self.datastore_agent_model = None
        self.chart_generator_model = None
        self.web_agent_model = None
        self.router_model = None
        self.file_agent_llm = None
        self.redis_host = default_redis_host
        self.suggestions_model = None
        self.dynamic_knowledge_graph_model = None
        self.load_env()

    def load_env(self):
        """
        Load environment variables from .env file.
        """
        load_dotenv()
        try:
            self.frontend_url = os.getenv("FRONTEND_URL", default_frontend_url)
            self.mistral_url = os.getenv("MISTRAL_URL")
            self.mistral_key = os.getenv("MISTRAL_KEY")
            self.mistral_model = os.getenv("MODEL")
            self.openai_key = os.getenv("OPENAI_KEY")
            self.ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434")
            self.neo4j_uri = os.getenv("NEO4J_URI", default_neo4j_uri)
            self.neo4j_user = os.getenv("NEO4J_USERNAME")
            self.neo4j_password = os.getenv("NEO4J_PASSWORD")
            self.answer_agent_llm = os.getenv("ANSWER_AGENT_LLM")
            self.intent_agent_llm = os.getenv("INTENT_AGENT_LLM")
            self.report_agent_llm = os.getenv("REPORT_AGENT_LLM")
            self.materiality_agent_llm = os.getenv("MATERIALITY_AGENT_LLM")
            self.validator_agent_llm = os.getenv("VALIDATOR_AGENT_LLM")
            self.datastore_agent_llm = os.getenv("DATASTORE_AGENT_LLM")
            self.chart_generator_llm = os.getenv("CHART_GENERATOR_LLM")
            self.web_agent_llm = os.getenv("WEB_AGENT_LLM")
            self.router_llm = os.getenv("ROUTER_LLM")
            self.suggestions_llm = os.getenv("SUGGESTIONS_LLM")
            self.dynamic_knowledge_graph_llm = os.getenv("DYNAMIC_KNOWLEDGE_GRAPH_LLM")
            self.file_agent_llm = os.getenv("FILE_AGENT_LLM")
            self.answer_agent_model = os.getenv("ANSWER_AGENT_MODEL")
            self.intent_agent_model = os.getenv("INTENT_AGENT_MODEL")
            self.report_agent_model = os.getenv("REPORT_AGENT_MODEL")
            self.materiality_agent_model = os.getenv("MATERIALITY_AGENT_MODEL")
            self.validator_agent_model = os.getenv("VALIDATOR_AGENT_MODEL")
            self.datastore_agent_model = os.getenv("DATASTORE_AGENT_MODEL")
            self.web_agent_model = os.getenv("WEB_AGENT_MODEL")
            self.chart_generator_model = os.getenv("CHART_GENERATOR_MODEL")
            self.router_model = os.getenv("ROUTER_MODEL")
            self.redis_host = os.getenv("REDIS_HOST", default_redis_host)
            self.suggestions_model = os.getenv("SUGGESTIONS_MODEL")
            self.dynamic_knowledge_graph_model = os.getenv("DYNAMIC_KNOWLEDGE_GRAPH_MODEL")
            self.file_agent_model = os.getenv("FILE_AGENT_MODEL")
        except FileNotFoundError:
            raise FileNotFoundError("Please provide a .env file. See the Getting Started guide on the README.md")
        except Exception:
            raise Exception("Missing .env file property. See the Getting Started guide on the README.md")
