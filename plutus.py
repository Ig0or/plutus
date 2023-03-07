# Third Party
import uvicorn

# Local
from src.routers.base.base_router import BaseRouter

app = BaseRouter.register_routers()


if __name__ == "__main__":
    uvicorn.run(app=app)
