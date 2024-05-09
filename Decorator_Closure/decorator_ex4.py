import functools

# 전략 인터페이스 역할의 데커레이터
def render_strategy(func):
    @functools.wraps(func)
    def wrapper(text):
        return func(text)
    return wrapper

# 구체적인 전략 1: HTML 렌더링
@render_strategy
def render_html(text):
    return f"<html><body>{text}</body></html>"

# 구체적인 전략 2: Markdown 렌더링
@render_strategy
def render_markdown(text):
    return f"**{text}**"

# 문맥을 정의하는 클래스
class TextRenderer:
    def __init__(self, render_func):
        self.render_func = render_func

    def render(self, text):
        return self.render_func(text)

# 사용 예
renderer = TextRenderer(render_html)
print(renderer.render("Hello World"))
# <html><body>Hello World</body></html>

renderer = TextRenderer(render_markdown)
print(renderer.render("Hello World"))
# **Hello World**