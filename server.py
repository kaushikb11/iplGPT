import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ipl_gpt.agents import default_sql_agent

# ------------------ Models ------------------


class IPLSearchResults(BaseModel):
    search_query: str
    result: str
    data: str


# ------------------- API -------------------


class IPLSearchAPI:
    def __init__(self) -> None:
        self.router = APIRouter()

        self.router.add_api_route("/ping", self.ping, methods=["GET"])
        self.router.add_api_route("/search", self.search, methods=["POST"])

        self.agent = default_sql_agent("sqlite:///ipl.sqlite")

    def ping(self) -> str:
        return "ping"

    def search(self, search_query: str) -> IPLSearchResults:

        response = self.agent.run(search_query)
        return IPLSearchResults(
            search_query=search_query, result=str(response), data="check"
        )


if __name__ == "__main__":

    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # startup tasks
    @app.on_event("startup")
    async def init_db() -> None:
        """Initializes database connection."""
        pass

    # shutdown tasks
    @app.on_event("shutdown")
    async def close_process() -> None:
        """Activities to perform on server shut-down."""
        pass

    app.include_router(IPLSearchAPI().router)

    uvicorn.run(app, host="0.0.0.0", port=8000)
