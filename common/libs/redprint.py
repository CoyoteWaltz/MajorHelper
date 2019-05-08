class Redprint():
    # 模仿蓝图的功能，关键是route这个装饰器
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        
        def decorator(f):
            # blueprint 里面就是用了add_url_rule这个方法，但是需要blueprint
            # 在这里把这些信息都存起来 mound里面
            self.mound.append((f, rule, options)) #用元组作为列表的元素
            return f
        return decorator

    def register(self, bp, url_prefix=None):
        #　这里可以拿到蓝图！
        if url_prefix is None:
            url_prefix = ''.join(('/', self.name))
        for f, rule, options in self.mound:
            endpoint = options.pop("endpoint", f.__name__)  # 字典pop，如果没有endpoint，就去默认值：f.__name__
            bp.add_url_rule(''.join((url_prefix, rule)), endpoint, f, **options)
        


