from loguru import logger

from app.primos import generar_primos

def main() -> None:
    primos = generar_primos(100)
    logger.info('READY!')
    logger.info(f'Lista de primos: {primos}')

main()