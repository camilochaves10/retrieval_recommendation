from typing import Optional, Union
from pydantic import BaseModel, Field




class RAGRequest(BaseModel):
    query: str = Field(..., description="The query to be used in the RAG pipeline")
    thread_id: str = Field(..., description="The thread ID")

class RAGUsedContext(BaseModel):
    image_url: str = Field(..., description="The URL of the image of the item")
    price: Optional[float] = Field(None, description="The price of the item")
    description: str = Field(..., description="The description of the item")

class RAGResponse(BaseModel):
    request_id: str = Field(..., description="The request ID")
    answer: str = Field(..., description="The answer to the query")
    used_context: list[RAGUsedContext] = Field(..., description="Information about the items used to answer the query")
    trace_id: str = Field(..., description="The trace ID")

class FeedbackRequest(BaseModel):
    feeback_score: Union[int, None] = Field(..., description= "1 if the feedback is positive, 0 if feedback is negative")
    feedback_text: str = Field(..., description="The feedback text")
    trace_id: str = Field(..., description="The trace ID")
    thread_id: str = Field(..., description= "The thread ID")
    feedback_source_type: str = Field(..., description="The type of feedback, Human or API")

class FeedbackResponse(BaseModel):
    request_id: str = Field(..., description="The request ID")
    status: str = Field(..., description="The status of the feedback submission")