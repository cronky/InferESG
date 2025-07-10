import logging
from fastapi import HTTPException
from ollama import AsyncClient
from src.utils import Config
from src.llm.llm import LLM, LLMFile
from src.session.file_uploads import get_file_content_for_filename, set_file_content_for_filename
from src.utils.file_utils import extract_text

logger = logging.getLogger(__name__)
config = Config()


class Ollama(LLM):
    def __init__(self):
        # ollama.AsyncClient expects the server host via the ``host`` argument
        # and internally forwards it as ``base_url`` to ``httpx.AsyncClient``.
        # Passing ``base_url`` here leads to ``httpx`` receiving two values for
        # that keyword, so use ``host`` instead.
        self.client = AsyncClient(host=config.ollama_url or "http://localhost:11434")

    async def chat(self, model: str, system_prompt: str, user_prompt: str, return_json: bool = False) -> str:
        try:
            response = await self.client.chat(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
            )
            return response["message"]["content"]
        except Exception as e:  # pragma: no cover - network errors
            logger.exception(f"Error calling Ollama model: {e}")
            return "An error occurred while processing the request."

    async def chat_with_file(
        self,
        model: str,
        system_prompt: str,
        user_prompt: str,
        files: list[LLMFile],
        return_json: bool = False,
    ) -> str:
        try:
            for file in files:
                extracted_content = get_file_content_for_filename(file.filename)
                if not extracted_content:
                    extracted_content = extract_text(file)
                    set_file_content_for_filename(file.filename, extracted_content)
                user_prompt += f"\n\nDocument:\n{extracted_content}"
            return await self.chat(model, system_prompt, user_prompt, return_json)
        except Exception as file_error:  # pragma: no cover - simple wrapper
            logger.exception(file_error)
            raise HTTPException(status_code=500, detail=f"Failed to process files: {file_error}") from file_error
