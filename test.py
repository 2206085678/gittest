# @Crate_Time  : 2021/7/6 10:29 
# @Author      : 孙北晨 
"""
    Introduction:
    
"""
from pycallgraph import PyCallGraph, Config, GlobbingFilter
from pycallgraph.output import GraphvizOutput


def main():
    print(1)


if __name__ == "__main__":
    config = Config()
    # 关系图中包括(include)哪些函数名。
    # 如果是某一类的函数，例如类gobang，则可以直接写'gobang.*'，表示以gobang.开头的所有函数。（利用正则表达式）。
    config.trace_filter = GlobbingFilter(include=[
        'main',
        'draw_chessboard',
        'draw_chessman',
        'draw_chessboard_with_chessman',
        'choose_save',
        'choose_turn',
        'choose_mode',
        'choose_button',
        'save_chess',
        'load_chess',
        'play_chess',
        'pop_window',
        'tip',
        'get_score',
        'max_score',
        'win',
        'key_control'
    ])
    # 该段作用是关系图中不包括(exclude)哪些函数。(正则表达式规则)
    # config.trace_filter = GlobbingFilter(exclude=[
    #     'pycallgraph.*',
    #     '*.secret_function',
    #     'FileFinder.*',
    #     'ModuleLockManager.*',
    #     'SourceFilLoader.*'
    # ])
    graphviz = GraphvizOutput()
    graphviz.output_file = 'graph.png'
    with PyCallGraph(output=graphviz, config=config):
        main()

from pycallgraph import PyCallGraph, Config, GlobbingFilter
from pycallgraph.output import GraphvizOutput


def main():
    print(1)


if __name__ == "__main__":
    config = Config()
    # 关系图中包括(include)哪些函数名。
    # 如果是某一类的函数，例如类gobang，则可以直接写'gobang.*'，表示以gobang.开头的所有函数。（利用正则表达式）。
    config.trace_filter = GlobbingFilter(include=[
        'main',
        'draw_chessboard',
        'draw_chessman',
        'draw_chessboard_with_chessman',
        'choose_save',
        'choose_turn',
        'choose_mode',
        'choose_button',
        'save_chess',
        'load_chess',
        'play_chess',
        'pop_window',
        'tip',
        'get_score',
        'max_score',
        'win',
        'key_control'
    ])
    # 该段作用是关系图中不包括(exclude)哪些函数。(正则表达式规则)
    # config.trace_filter = GlobbingFilter(exclude=[
    #     'pycallgraph.*',
    #     '*.secret_function',
    #     'FileFinder.*',
    #     'ModuleLockManager.*',
    #     'SourceFilLoader.*'
    # ])
    graphviz = GraphvizOutput()
    graphviz.output_file = 'graph.png'
    with PyCallGraph(output=graphviz, config=config):
        main()