from pyecharts.charts import Bar, Liquid
from pyecharts import options as opts
from pyecharts.globals import SymbolType
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(["handbag", "coat", "shirt", "jeans", "shoes", "socks"])
bar.add_yaxis("Hermes", [5, 20, 36, 10, 75, 90])
bar.add_yaxis("LV", [15, 8, 32, 20, 36, 70])
# render 会生成本地 HTML 文件，默认会在当前目录生成 pyChart.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render("pyChart.html")


liquid = Liquid().add("lq", [0.3, 0.7], is_outline_show=False, shape=SymbolType.DIAMOND).set_global_opts(title_opts=opts.TitleOpts(title="Diamond")).render("diamond.html")
