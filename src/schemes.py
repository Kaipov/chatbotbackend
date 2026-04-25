from typing import Literal

from openai.types.chat import (
    ChatCompletionAssistantMessageParam,
    ChatCompletionUserMessageParam,
)
from pydantic import BaseModel, ConfigDict, Field


class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str

    def to_openai_message(
        self,
    ) -> ChatCompletionUserMessageParam | ChatCompletionAssistantMessageParam:
        if self.role == "user":
            return {"role": "user", "content": self.content}
        return {"role": "assistant", "content": self.content}


class ChatRequest(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "query": "Привет! Как дела?",
                    "history": [],
                }
            ]
        }
    )

    query: str
    history: list[ChatMessage] = Field(default_factory=list)
