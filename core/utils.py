from starlette.requests import Request


def get_db(request: Request): # возвращает state который записывается в middleware request.state.db = SessionLocal()
  return request.state.db
