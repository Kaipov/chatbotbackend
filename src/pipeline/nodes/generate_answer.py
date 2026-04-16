from src.clients.llm import get_chat_completion
from src.pipeline.abc_base_node import BaseNode
from src.pipeline.context import Context


class LLMAnswer(BaseNode):
    name = "llm_answer"

    async def _execute(self, context: Context) -> Context:
        prompt = (
            "Answer the user query based on the provided documents. "
            "If the documents do not contain enough information, say so."
        )

        formatted_documents = [
            f"Document {i}: {document}"
            for i, document in enumerate(context.documents or [], start=1)
        ]

        response = await get_chat_completion(
            user_query=context.query
            + "\n\nDocuments:\n"
            + "\n\n".join(formatted_documents),
            system_message=prompt,
            history=context.history,
            settings=context.settings,
        )
        context.output = response
        return context
