import logging

logging.basicConfig(level=logging.INFO)


def logging_decorator(func):
    def wrapper_logging(*args, **kwargs):
        logging.info('开始执行{}() ...'.format(func.__name__))
        func(*args, **kwargs)
        logging.info('{} 执行完成! '.format(func.__name__))

    return wrapper_logging


def show_info(*args, **kwargs):
    print('这是一个测试函数，参数：', args, kwargs)


# logging_decorator 表示用logging_decorator 装饰器来修饰how_min 函数
@logging_decorator
def show_min(a, b):
    print('{}、{} 中的最小值是：{}'.format(a, b, min(a, b)))


decorated_show_info = logging_decorator(show_info)
decorated_show_info('arg1', 'arg2', kwarg1=1, kwarg2=2)

# decorated_show_min = logging_decorator(show_min)
# decorated_show_min(2,3)
show_min(2, 3)
