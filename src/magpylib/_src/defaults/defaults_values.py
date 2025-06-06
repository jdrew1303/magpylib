"""Package level config defaults"""

from __future__ import annotations

DEFAULTS = {
    "display": {
        "autosizefactor": 10,
        "animation": {
            "fps": 20,
            "maxfps": 30,
            "maxframes": 200,
            "time": 5,
            "slider": True,
            "output": None,
        },
        "backend": "auto",
        "colorsequence": (
            "#2E91E5",
            "#E15F99",
            "#1CA71C",
            "#FB0D0D",
            "#DA16FF",
            "#B68100",
            "#750D86",
            "#EB663B",
            "#511CFB",
            "#00A08B",
            "#FB00D1",
            "#FC0080",
            "#B2828D",
            "#6C7C32",
            "#778AAE",
            "#862A16",
            "#A777F1",
            "#620042",
            "#1616A7",
            "#DA60CA",
            "#6C4516",
            "#0D2A63",
            "#AF0038",
            "#222A2A",
        ),
        "style": {
            "base": {
                "path": {
                    "line": {"width": 1, "style": "solid", "color": None},
                    "marker": {"size": 3, "symbol": "o", "color": None},
                    "show": True,
                    "frames": None,
                    "numbering": False,
                },
                "description": {"show": True, "text": None},
                "legend": {"show": True, "text": None},
                "opacity": 1,
                "model3d": {"showdefault": True, "data": []},
                "color": None,
            },
            "magnet": {
                "magnetization": {
                    "show": True,
                    "arrow": {
                        "show": True,
                        "size": 1,
                        "sizemode": "scaled",
                        "offset": 1,
                        "width": 2,
                        "style": "solid",
                        "color": None,
                    },
                    "color": {
                        "north": "#E71111",
                        "middle": "#DDDDDD",
                        "south": "#00B050",
                        "transition": 0.2,
                        "mode": "tricolor",
                    },
                    "mode": "auto",
                }
            },
            "current": {
                "arrow": {
                    "show": True,
                    "size": 1,
                    "sizemode": "scaled",
                    "offset": 0.5,
                    "width": 1,
                    "style": "solid",
                    "color": None,
                },
                "line": {"show": True, "width": 2, "style": "solid", "color": None},
            },
            "sensor": {
                "size": 1,
                "sizemode": "scaled",
                "pixel": {
                    "size": 1,
                    "sizemode": "scaled",
                    "color": None,
                    "symbol": "o",
                },
                "arrows": {
                    "x": {"color": "red"},
                    "y": {"color": "green"},
                    "z": {"color": "blue"},
                },
            },
            "dipole": {"size": 1, "sizemode": "scaled", "pivot": "middle"},
            "triangle": {
                "magnetization": {
                    "show": True,
                    "arrow": {
                        "show": True,
                        "size": 1,
                        "sizemode": "scaled",
                        "offset": 1,
                        "width": 2,
                        "style": "solid",
                        "color": None,
                    },
                    "color": {
                        "north": "#E71111",
                        "middle": "#DDDDDD",
                        "south": "#00B050",
                        "transition": 0.2,
                        "mode": "tricolor",
                    },
                    "mode": "auto",
                },
                "orientation": {
                    "show": True,
                    "size": 1,
                    "color": "grey",
                    "offset": 0.9,
                    "symbol": "arrow3d",
                },
            },
            "triangularmesh": {
                "orientation": {
                    "show": False,
                    "size": 1,
                    "color": "grey",
                    "offset": 0.9,
                    "symbol": "arrow3d",
                },
                "mesh": {
                    "grid": {
                        "show": False,
                        "line": {"width": 2, "style": "solid", "color": "black"},
                        "marker": {"size": 1, "symbol": "o", "color": "black"},
                    },
                    "open": {
                        "show": False,
                        "line": {"width": 2, "style": "solid", "color": "cyan"},
                        "marker": {"size": 1, "symbol": "o", "color": "black"},
                    },
                    "disconnected": {
                        "show": False,
                        "line": {"width": 2, "style": "solid", "color": "black"},
                        "marker": {"size": 5, "symbol": "o", "color": "black"},
                        "colorsequence": (
                            "red",
                            "blue",
                            "green",
                            "cyan",
                            "magenta",
                            "yellow",
                        ),
                    },
                    "selfintersecting": {
                        "show": False,
                        "line": {"width": 2, "style": "solid", "color": "magenta"},
                        "marker": {"size": 1, "symbol": "o", "color": "black"},
                    },
                },
            },
            "markers": {"marker": {"size": 2, "color": "grey", "symbol": "x"}},
        },
    },
}
