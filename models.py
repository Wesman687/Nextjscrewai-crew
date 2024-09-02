from pydantic import BaseModel
from typing import List

class NamedUrls(BaseModel):
    name: str
    url: str

class PositionInfo(BaseModel):
    company: str
    position: str
    name: str
    blog_articles_urls: List[str]
    youtube_interview_urls: List[NamedUrls]
    
class PositionInfoList(BaseModel):
    positions: List[PositionInfo]