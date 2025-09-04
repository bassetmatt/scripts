import matplotlib
import matplotlib.pyplot as plt
from cycler import cycler

#############
### Fonts ###
#############

BIG_FONT = True


def setMplFont():
    matplotlib.rcParams["font.family"] = "serif"
    matplotlib.rcParams["font.serif"] = "CMU Serif"
    matplotlib.rcParams["font.monospace"] = "Hack"
    if BIG_FONT:
        matplotlib.rcParams["figure.figsize"] = (20, 10)
        matplotlib.rcParams["font.size"] = 22
        matplotlib.rcParams["legend.handlelength"] = 2
        matplotlib.rcParams["lines.linewidth"] = 3


#####################
#####          #####
#####  Colors  #####
#####          #####
#####################


# KDE default
class kde:
    GREY = "#292f34"
    GREY2 = "#31363b"
    BORDER = "#75797c"


# Terminal
class term:
    GREY = "#1e2229"
    GREY2 = "#7f8c8d"
    RED = "#ed1515"
    RED2 = "#c0392b"
    GREEN = "#44853a"
    GREEN2 = "#55a649"
    ORANGE = "#f67400"
    ORANGE2 = "#fdbc4b"
    BLUE = "#1d99f3"
    BLUE2 = "#3daee9"
    PURPLE = "#9b59b6"
    PURPLE2 = "#8e44ad"
    CYAN = "#1abc9c"
    CYAN2 = "#16a085"
    WHITE = "#fcfcfc"
    WHITE2 = "#ffffff"


# VS Code Synthwave 84 theme
class code:
    MAIN_BG = "#262335"
    CODE_BG = "#241b2f"
    BORDER = "#433360"
    BLUE = "#36f9f6"
    RED = "#fe4450"
    PURPLE = "#ff7ec0"
    YELLOW = "#fede5d"
    SALMON = "#f97e72"
    ORANGE = "#ff8b39"
    GREEN = "#72f1b8"
    GREY = "#848bbd"


# Default matplotlib colors
class default_colors:
    BLUE = "#1f77b4"
    ORANGE = "#ff7f0e"
    GREEN = "#2ca02c"
    RED = "#d62728"
    PURPLE = "#9467bd"
    BROWN = "#8c564b"
    ROSE = "#e377c2"
    GREY = "#7f7f7f"
    YELLOW = "#bcbd22"
    BLUE2 = "#17becf"
    WHITE = "#ffffff"
    WHITE2 = "#F7F3F0"
    WHITE3 = "#FAF9F6"
    WHITE4 = "#FBF9F7"
    GREY2 = "#242526"
    BLACK = "#000000"


def mpSetParamStyle(style: str, latex: bool = True, mono: bool = False):
    """Sets the parameters for matplotlib to have a nice graph with fancy colors

    Args:
        style (str): must be "code" or "kde", different styles
        latex (bool, optional): LaTeX support. Defaults to True.
        mono (bool, optional): Monospace font, incompatible w/ LaTeX. Defaults to False.
    """
    params = {}
    # Fonts config
    params["font.serif"] = "CMU Serif"
    params["font.monospace"] = "Hack"
    # LaTeX support
    if latex:
        params["text.usetex"] = "true"
    else:
        params["text.usetex"] = "false"
    # Monospace font
    if mono:
        params["font.family"] = "monospace"
    else:
        params["font.family"] = "serif"

    # Global graph options :
    params["figure.figsize"] = (40, 20)
    params["font.size"] = 22
    params["legend.handlelength"] = 2
    params["lines.linewidth"] = 2

    # Global color style
    params["legend.framealpha"] = 0.7
    match style:
        case "code":
            # Background
            params["figure.facecolor"] = code.MAIN_BG
            params["axes.facecolor"] = code.MAIN_BG
            params["legend.facecolor"] = code.CODE_BG
            params["legend.edgecolor"] = code.BORDER

            # Axis
            params["axes.edgecolor"] = code.BORDER

            # Text
            params["text.color"] = code.ORANGE
            params["axes.labelcolor"] = code.PURPLE
            params["xtick.color"] = code.SALMON
            params["ytick.color"] = code.SALMON

            # lines colors :
            params["axes.prop_cycle"] = cycler(
                "color",
                [
                    code.BLUE,
                    code.RED,
                    code.YELLOW,
                    code.GREEN,
                    code.GREY,
                    term.CYAN,
                    term.PURPLE,
                    term.CYAN2,
                    term.WHITE,
                    default_colors.GREY,
                ],
            )

        case "kde":
            # Background
            params["figure.facecolor"] = kde.GREY
            params["axes.facecolor"] = term.GREY
            params["legend.facecolor"] = kde.GREY2
            params["legend.edgecolor"] = term.GREY2

            # Axis
            params["axes.edgecolor"] = kde.BORDER

            # Text
            params["text.color"] = term.GREEN2
            params["axes.labelcolor"] = term.CYAN2
            params["xtick.color"] = term.WHITE
            params["ytick.color"] = term.WHITE

            # lines colors :
            params["axes.prop_cycle"] = cycler(
                "color",
                [
                    term.BLUE,
                    term.RED,
                    term.ORANGE,
                    term.PURPLE2,
                    term.RED2,
                    term.GREEN,
                    term.BLUE2,
                    term.WHITE2,
                    default_colors.BROWN,
                    code.GREEN,
                ],
            )
        case "default":
            # Background
            params["figure.facecolor"] = default_colors.WHITE
            params["axes.facecolor"] = default_colors.WHITE4
            params["legend.facecolor"] = default_colors.WHITE2
            params["legend.edgecolor"] = default_colors.GREY2

            # Axis
            params["axes.edgecolor"] = default_colors.BLACK

            # Text
            params["text.color"] = default_colors.BLACK
            params["axes.labelcolor"] = default_colors.BLACK
            params["xtick.color"] = default_colors.BLACK
            params["ytick.color"] = default_colors.BLACK

            # lines colors :
            params["axes.prop_cycle"] = cycler(
                "color",
                [
                    default_colors.BLUE,
                    default_colors.RED,
                    default_colors.YELLOW,
                    default_colors.GREEN,
                    default_colors.GREY,
                    default_colors.PURPLE,
                    default_colors.GREY2,
                ],
            )
    plt.rcParams.update(params)


def plTest():
    import numpy as np

    fig = plt.figure()
    fig.suptitle("Matplotlib test")
    plt.xlabel(r"Label for $x_i$")
    plt.ylabel(r"Label for $y_i$")
    X = np.linspace(0, 10, 1000)

    matplotlib.rcParams["legend.loc"] = "upper left"
    plt.xlim((0, 10))

    # Multiple plots
    plt.plot(X, np.power(X, 2), label=r"$x^2$")
    plt.plot(X, 80 - 5 * X, label=r"$80-5x$")
    plt.plot(X, 50 * np.log(X + 1), label=r"$50 \ln(x+1)$")
    plt.plot(X, np.exp(0.5 * X), label=r"$e^{x/2}$")
    plt.plot(X, 100 / np.sqrt(X + 1), label=r"$\frac{100}{\sqrt{x+1}}$")
    plt.plot(X, np.power(X, 3) / 8, label=r"$x^3/8$")
    plt.plot(X, 15 * np.sqrt(X), label=r"$15\sqrt{x}$")
    plt.plot(X, 150 - X**2, label=r"$150-x^2$")
    plt.plot(X, np.floor(10 * X + 3.5), label=r"$\lfloor 10x + 3.5 \rfloor$")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    mpSetParamStyle("kde")

    plTest()
