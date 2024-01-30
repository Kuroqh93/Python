import logging
logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="a", format="%(asctime)s %(levelname)s - %(message)s")
def div(a,b)
try:
    print(10/0)
except Exception:
    logging.exception(Exception)
div()