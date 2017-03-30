import logging

logger = logging.getLogger('weibo crawler')
logger.setLevel(logging.INFO)

sh = logging.StreamHandler()
sh.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s - %(message)s')
sh.setFormatter(formatter)

logger.addHandler(sh)
