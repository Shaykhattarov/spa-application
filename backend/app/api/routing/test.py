from fastapi import APIRouter



router: APIRouter = APIRouter(prefix='/test', tags=['test'])


@router.get('/')
def test_response():
    return {"message": "Тестовый запрос. Проверка роутинга"}