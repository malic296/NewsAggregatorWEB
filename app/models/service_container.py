from dataclasses import dataclass
from app.services import ArticlesService, ChannelsService, ConsumersService, LikesService

@dataclass
class ServiceContainer:
    articles: ArticlesService
    channels: ChannelsService
    consumers: ConsumersService
    likes: LikesService
