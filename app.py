import js2py

# 定义 JavaScript 函数并调用
js_code = """
function add(a, b) {
    return a + b;
}
add(2, 3);
"""
result = js2py.eval_js(js_code)
print(result)  # 输出: 5