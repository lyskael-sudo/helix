from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import config
import prompts

class HelixAgent:
    def __init__(self, model="mistral"):
        """Initialize Helix AI Agent"""
        self.model_name = model
        try:
            self.llm = Ollama(
                base_url=config.OLLAMA_BASE_URL,
                model=model,
                temperature=0.3
            )
        except Exception as e:
            print(f"Error initializing Ollama: {e}")
            print(f"Make sure Ollama is running at {config.OLLAMA_BASE_URL}")
            raise
    
    def switch_model(self, model):
        """Switch to a different model"""
        if model not in config.AVAILABLE_MODELS:
            return f"❌ Model '{model}' not available. Choose from: {', '.join(config.AVAILABLE_MODELS)}"
        
        self.model_name = model
        self.llm = Ollama(
            base_url=config.OLLAMA_BASE_URL,
            model=model,
            temperature=0.3
        )
        return f"✅ Switched to model: {model}"
    
    def generate_code(self, language, request):
        """Generate code based on request"""
        prompt_template = PromptTemplate(
            input_variables=["language", "request"],
            template=prompts.GENERATE_PROMPT
        )
        chain = LLMChain(llm=self.llm, prompt=prompt_template)
        result = chain.run(language=language, request=request)
        return result
    
    def explain_code(self, language, code):
        """Explain given code"""
        prompt_template = PromptTemplate(
            input_variables=["language", "code"],
            template=prompts.EXPLAIN_PROMPT
        )
        chain = LLMChain(llm=self.llm, prompt=prompt_template)
        result = chain.run(language=language, code=code)
        return result
    
    def optimize_code(self, language, code):
        """Optimize code"""
        prompt_template = PromptTemplate(
            input_variables=["language", "code"],
            template=prompts.OPTIMIZE_PROMPT
        )
        chain = LLMChain(llm=self.llm, prompt=prompt_template)
        result = chain.run(language=language, code=code)
        return result
    
    def fix_code(self, language, code, issue):
        """Fix bugs in code"""
        prompt_template = PromptTemplate(
            input_variables=["language", "code", "issue"],
            template=prompts.FIX_PROMPT
        )
        chain = LLMChain(llm=self.llm, prompt=prompt_template)
        result = chain.run(language=language, code=code, issue=issue)
        return result
    
    def convert_code(self, from_lang, to_lang, code):
        """Convert code from one language to another"""
        prompt_template = PromptTemplate(
            input_variables=["from_lang", "to_lang", "code"],
            template=prompts.CONVERT_PROMPT
        )
        chain = LLMChain(llm=self.llm, prompt=prompt_template)
        result = chain.run(from_lang=from_lang, to_lang=to_lang, code=code)
        return result
