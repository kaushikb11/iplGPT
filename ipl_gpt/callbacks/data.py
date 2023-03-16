from contextlib import contextmanager
from typing import Any, Dict, Generator, List, Optional, Union

from langchain.callbacks import get_callback_manager
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentAction, AgentFinish, LLMResult


class DataCallbackHandler(BaseCallbackHandler):

    data = None
    outputs = None

    @property
    def always_verbose(self) -> bool:
        """Whether to call verbose callbacks even if verbose is False."""
        return True

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        """Print out the prompts."""
        pass

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Do nothing."""
        pass

    def on_llm_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        """Do nothing."""
        pass

    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> None:
        """Print out that we are entering a chain."""
        pass

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
        """Print out that we finished a chain."""
        pass

    def on_chain_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        """Do nothing."""
        pass

    def on_tool_start(
        self,
        serialized: Dict[str, Any],
        action: AgentAction,
        color: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """Print out the log in specified color."""
        self.data = action

    def on_tool_end(
        self,
        output: str,
        color: Optional[str] = None,
        observation_prefix: Optional[str] = None,
        llm_prefix: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """If not the final action, print out observation."""
        # pass
        self.data = output
        # import pdb; pdb.set_trace()
        # print(f"Observation prefix: {observation_prefix}")

    def on_tool_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        """Do nothing."""
        pass

    def on_text(
        self,
        text: str,
        color: Optional[str] = None,
        end: str = "",
        **kwargs: Optional[str],
    ) -> None:
        """Run when agent ends."""
        pass

    def on_agent_finish(
        self, finish: AgentFinish, color: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Run on agent end."""
        # self.outputs = finish.return_values["output"]
        self.outputs = finish.return_values["output"]

    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        pass

    def on_llm_new_token(self, token: str, **kwargs: Any) -> Any:
        pass


@contextmanager
def get_data_callback() -> Generator[DataCallbackHandler, None, None]:
    handler = DataCallbackHandler()
    manager = get_callback_manager()
    manager.add_handler(handler)
    yield handler
    manager.remove_handler(handler)
