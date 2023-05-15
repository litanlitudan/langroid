from llmagent.agent.base import Agent
from tests.configs import CustomAgentConfig
from llmagent.language_models.base import StreamingIfAllowed, LLMConfig
from llmagent.cachedb.redis_cachedb import RedisCacheConfig


def test_agent():
    """
    Test whether the combined configs work as expected.
    """
    agent_config = CustomAgentConfig(
        llm = LLMConfig(
            type="openai",
            cache_config=RedisCacheConfig(fake=True),
        )
    )
    agent = Agent(agent_config)
    response = agent.respond("what is the capital of France?")  # direct LLM question
    assert "Paris" in response.content

    with StreamingIfAllowed(agent.llm, False):
        response = agent.respond("what is the capital of France?")
    assert "Paris" in response.content
